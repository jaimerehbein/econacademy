"""
parallel_glossary_generator_v2.py
===================================
Improved version with:
  - Rate limiting: stagger task creation by 3s per worker
  - Automatic retry on 429 with exponential back-off
  - Resume capability: skips v9.5 files
  - Saves failed to retry_failed.txt
"""

import os, re, json, time, sys, threading
import urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

# ── Config ────────────────────────────────────────────────────────────────────
MANUS_API_KEY  = "sk-PkiBpff8Awdb6gKGYsqcfP8raHdifCEWYGOBKjEJLDIOiWNaPIbF7uOoj87Hn93HigCIKSw1igVPrcvqJPP7Nv19kTS0"
MANUS_CREATE   = "https://api.manus.ai/v1/tasks"
MANUS_POLL     = "https://api.manus.ai/v1/tasks/"
TARGET_DIR     = "/Users/machd/Desktop/licecon/web-portal/public/program"
WORKERS        = 3        # Reduced to avoid 429
POLL_INTERVAL  = 15       # seconds
MAX_POLLS      = 14       # 14×15 = 3.5 min max per task
CREATE_STAGGER = 4        # seconds between task creations
RETRY_WAIT     = 30       # seconds wait after 429
MAX_RETRIES    = 3
FAILED_LOG     = os.path.join(os.path.dirname(__file__), "retry_failed.txt")

# ── Templates (v9.5) ─────────────────────────────────────────────────────────
SECTION_TPL = """\
<!-- GLOSARIO v9.5 -->
<section id="glosario" class="mt-24 mb-16 relative">
    <div class="flex items-center gap-4 mb-10">
        <div class="w-1.5 h-8 bg-{color}-500 rounded-full"></div>
        <h2 class="text-2xl font-black text-white tracking-tight uppercase italic">Glosario Técnico</h2>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 relative z-10">
{items}
    </div>
</section>"""

ITEM_TPL = """\
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-{color}-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-{color}-500/5">
            <h3 class="text-sm font-black text-{color}-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-{color}-500 animate-pulse"></span>
                {term}
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                {definition}
            </p>
        </div>"""

_lock = threading.Lock()
_create_lock = threading.Lock()
_last_create = [0.0]  # shared mutable

def log(msg):
    with _lock:
        print(msg, flush=True)

def extract_color(text):
    m = re.search(r'from-(\w+)-[39]00', text)
    if m: return m.group(1)
    m = re.search(r'bg-(\w+)-500', text)
    return m.group(1) if m else "indigo"

def clean_json(text):
    if not text: return None
    text = re.sub(r'```json\s*', '', text)
    text = re.sub(r'```\s*', '', text)
    try: return json.loads(text.strip())
    except:
        m = re.search(r'(\{.*\})', text, re.DOTALL)
        if m:
            try: return json.loads(m.group(1))
            except: pass
    return None

def http_post(url, data):
    headers = {"API_KEY": MANUS_API_KEY, "Content-Type": "application/json"}
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())

def http_get(url):
    headers = {"API_KEY": MANUS_API_KEY}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())

def create_task_with_backoff(prompt, fname):
    """Create Manus task with rate-limit-aware stagger + retry."""
    for attempt in range(MAX_RETRIES):
        with _create_lock:
            # Enforce minimum gap between creates
            elapsed = time.time() - _last_create[0]
            if elapsed < CREATE_STAGGER:
                time.sleep(CREATE_STAGGER - elapsed)
            try:
                res = http_post(MANUS_CREATE, {"prompt": prompt})
                _last_create[0] = time.time()
                task_id = res.get("task_id")
                if task_id:
                    return task_id
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    wait = RETRY_WAIT * (attempt + 1)
                    log(f"  ⚠ {fname}: 429 — waiting {wait}s (attempt {attempt+1})")
                    _last_create[0] = time.time()
                    time.sleep(wait)
                else:
                    log(f"  [HTTP {e.code}] {fname}: {e.reason}")
                    return None
            except Exception as e:
                log(f"  [ERROR] {fname}: {e}")
                return None
    return None

def call_manus(prompt, fname):
    task_id = create_task_with_backoff(prompt, fname)
    if not task_id:
        return None

    poll_url = MANUS_POLL + task_id
    for i in range(MAX_POLLS):
        time.sleep(POLL_INTERVAL)
        try:
            res = http_get(poll_url)
            status = res.get("status")
            if status == "completed":
                for item in reversed(res.get("output", [])):
                    if item.get("role") == "assistant":
                        content = item.get("content")
                        if isinstance(content, list):
                            for part in content:
                                if part.get("type") == "output_text":
                                    text = part.get("text", "")
                                    if "{" in text:
                                        return text
                        elif isinstance(content, dict):
                            return content.get("text")
            elif status == "error":
                return None
        except Exception as e:
            log(f"  [POLL ERR] {task_id}: {e}")
    return None

def process_file(filepath):
    fname = os.path.basename(filepath)
    try:
        with open(filepath, encoding="utf-8") as f:
            content = f.read()

        if "GLOSARIO v9.5" in content:
            return fname, "skip"
        if "<!-- GLOSARIO -->" not in content:
            return fname, "no_marker"

        color = extract_color(content)

        prompt = f"""Eres un experto en economía (nivel Master). Analiza el siguiente texto y devuelve ÚNICAMENTE un JSON con 10 términos clave y definiciones académicas rigurosas (mín. 30 palabras c/u).

FORMATO (sin explicaciones, sin markdown):
{{"terms": [{{"term": "...", "definition": "..."}}]}}

TEXTO:
{content[:12000]}"""

        log(f"  → {fname}")
        raw = call_manus(prompt, fname)
        data = clean_json(raw)

        if not data or "terms" not in data:
            log(f"  ✗ {fname}: sin JSON")
            return fname, "failed"

        items = "\n".join(
            ITEM_TPL.format(color=color, term=t["term"], definition=t["definition"])
            for t in data["terms"]
        )
        new_section = SECTION_TPL.format(color=color, items=items)

        parts = re.split(r'<!-- GLOSARIO[^-]*?-->', content, maxsplit=1)
        main = parts[0]
        rest = parts[1] if len(parts) > 1 else ""
        rest = re.sub(r'<section id="glosario".*?</section>', '', rest, flags=re.DOTALL)

        if "<!-- FOOTER -->" in rest:
            footer = rest[rest.index("<!-- FOOTER -->"):]
        else:
            footer = ""

        new_content = main + "<!-- GLOSARIO -->\n" + new_section + "\n" + footer

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

        log(f"  ✨ {fname}")
        return fname, "ok"

    except Exception as e:
        log(f"  ❌ {fname}: {e}")
        return fname, "error"

def main():
    all_files = sorted(
        os.path.join(TARGET_DIR, f)
        for f in os.listdir(TARGET_DIR)
        if f.endswith(".md")
    )

    def priority(fp):
        n = os.path.basename(fp).lower()
        for i, prefix in enumerate(["mic","ep","eb","mac","me","m","pe","if","a"]):
            if n.startswith(prefix): return (i, n)
        return (99, n)

    all_files.sort(key=priority)

    pending = []
    for fp in all_files:
        txt = open(fp, encoding="utf-8").read()
        if "GLOSARIO v9.5" not in txt and "<!-- GLOSARIO -->" in txt:
            pending.append(fp)

    log(f"\n📚 Parallel Glossary Generator v2 — {len(pending)} modules | {WORKERS} workers\n")

    ok, fails = 0, []
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futures = {ex.submit(process_file, fp): fp for fp in pending}
        for fut in as_completed(futures):
            _, status = fut.result()
            if status == "ok": ok += 1
            elif status in ("failed","error"): fails.append(os.path.basename(futures[fut]))

    log(f"\n{'='*50}")
    log(f"✅ OK: {ok} | ❌ Failed: {len(fails)}")
    if fails:
        with open(FAILED_LOG, "w") as f:
            f.write("\n".join(fails))
        log(f"→ Failures saved to retry_failed.txt")

if __name__ == "__main__":
    main()
