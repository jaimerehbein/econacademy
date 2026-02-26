"""
sequential_glossary_generator.py
==================================
Sequential generator respecting Manus 1 req/min rate limit.
  - Creates 1 task, waits for completion, then creates the next
  - Explicitly waits 65s between successful creates
  - Resumes automatically (skips v9.5 files)
  - ETA: ~175 modules × 1.5 min avg = ~4.5 hours
"""

import os, re, json, time, sys
import urllib.request, urllib.error

# ── Config ────────────────────────────────────────────────────────────────────
MANUS_API_KEY = "sk-PkiBpff8Awdb6gKGYsqcfP8raHdifCEWYGOBKjEJLDIOiWNaPIbF7uOoj87Hn93HigCIKSw1igVPrcvqJPP7Nv19kTS0"
MANUS_CREATE  = "https://api.manus.ai/v1/tasks"
MANUS_POLL    = "https://api.manus.ai/v1/tasks/"
TARGET_DIR    = "/Users/machd/Desktop/licecon/web-portal/public/program"
POLL_INTERVAL = 15     # seconds between status checks
MAX_POLLS     = 20     # 20 × 15s = 5 min timeout per task
TASK_DELAY    = 65     # seconds to wait after each task creation (rate limit)
FAILED_LOG    = os.path.join(os.path.dirname(__file__), "retry_failed.txt")

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

def log(msg): print(msg, flush=True)

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

def api_post(url, data):
    headers = {"API_KEY": MANUS_API_KEY, "Content-Type": "application/json"}
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())

def api_get(url):
    req = urllib.request.Request(url, headers={"API_KEY": MANUS_API_KEY})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())

def call_manus(prompt, fname):
    """Create task, poll until done. Returns extracted text or None."""
    # Create with retry on 429
    task_id = None
    for attempt in range(5):
        try:
            res = api_post(MANUS_CREATE, {"prompt": prompt})
            task_id = res.get("task_id")
            if task_id: break
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = 60 * (attempt + 1)
                log(f"  ⏳ {fname}: 429 → waiting {wait}s...")
                time.sleep(wait)
            else:
                log(f"  ✗ {fname}: HTTP {e.code}")
                return None
        except Exception as e:
            log(f"  ✗ {fname}: {e}")
            return None

    if not task_id:
        return None

    log(f"  ⏩ {fname}: task {task_id}")
    poll_url = MANUS_POLL + task_id
    for i in range(MAX_POLLS):
        time.sleep(POLL_INTERVAL)
        try:
            res = api_get(poll_url)
            status = res.get("status")
            if status == "completed":
                for item in reversed(res.get("output", [])):
                    if item.get("role") == "assistant":
                        content = item.get("content")
                        if isinstance(content, list):
                            for part in content:
                                if part.get("type") == "output_text":
                                    t = part.get("text", "")
                                    if "{" in t: return t
                        elif isinstance(content, dict):
                            return content.get("text")
            elif status == "error":
                return None
        except Exception as e:
            log(f"    poll error: {e}")
    log(f"  ✗ {fname}: timeout")
    return None

def process(filepath):
    fname = os.path.basename(filepath)
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    if "GLOSARIO v9.5" in content or "<!-- GLOSARIO -->" not in content:
        return "skip"

    color = extract_color(content)
    prompt = f"""Eres un experto en economía (nivel Master). Analiza el siguiente texto y devuelve ÚNICAMENTE un JSON con 10 términos clave y definiciones académicas (mín. 30 palabras c/u).

FORMATO EXACTO:
{{"terms": [{{"term": "...", "definition": "..."}}]}}

TEXTO:
{content[:12000]}"""

    raw = call_manus(prompt, fname)
    data = clean_json(raw)

    if not data or "terms" not in data:
        return "failed"

    items = "\n".join(
        ITEM_TPL.format(color=color, term=t["term"], definition=t["definition"])
        for t in data["terms"]
    )
    new_section = SECTION_TPL.format(color=color, items=items)

    parts = re.split(r'<!-- GLOSARIO[^-]*?-->', content, maxsplit=1)
    main = parts[0]
    rest = parts[1] if len(parts) > 1 else ""
    rest = re.sub(r'<section id="glosario".*?</section>', '', rest, flags=re.DOTALL)
    footer = rest[rest.index("<!-- FOOTER -->"):] if "<!-- FOOTER -->" in rest else ""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(main + "<!-- GLOSARIO -->\n" + new_section + "\n" + footer)

    return "ok"

def main():
    files = sorted(
        os.path.join(TARGET_DIR, f)
        for f in os.listdir(TARGET_DIR) if f.endswith(".md")
    )

    def priority(fp):
        n = os.path.basename(fp).lower()
        for i, p in enumerate(["mic","ep","eb","mac","me","m","pe","if","a"]):
            if n.startswith(p): return (i, n)
        return (99, n)

    files.sort(key=priority)

    pending = [
        fp for fp in files
        if "GLOSARIO v9.5" not in open(fp, encoding="utf-8").read()
        and "<!-- GLOSARIO -->" in open(fp, encoding="utf-8").read()
    ]

    total = len(pending)
    log(f"\n📚 Sequential Glossary Generator — {total} modules\n")

    ok, fails, done = 0, [], 0
    for fp in pending:
        fname = os.path.basename(fp)
        done += 1
        log(f"[{done}/{total}] {fname}")

        status = process(fp)

        if status == "ok":
            ok += 1
            log(f"  ✨ Done. Waiting {TASK_DELAY}s before next task...")
            time.sleep(TASK_DELAY)
        elif status == "failed":
            fails.append(fname)
            log(f"  ⚠  Failed. Continuing in 10s...")
            time.sleep(10)
        elif status == "skip":
            log(f"  ⏭  Skipped (already v9.5)")

    log(f"\n{'='*50}")
    log(f"✅ OK: {ok} | ❌ Failed: {len(fails)} | Total: {total}")
    if fails:
        with open(FAILED_LOG, "w") as f:
            f.write("\n".join(fails))
        log(f"→ Failures saved to retry_failed.txt")

if __name__ == "__main__":
    main()
