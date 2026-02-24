"""
reformat_glossaries_v95.py
==========================
Re-styles ALL existing <section id="glosario"> blocks in every .md file
from the old v9.4 light-mode 3-column layout to the new v9.5 dark-mode
2-column layout, WITHOUT calling any external API.

Strategy:
  1. Scan every .md in public/program/
  2. Find the <section id="glosario"> ... </section> block
  3. Extract each term (h3) + definition (p) pair
  4. Re-emit with the new v9.5 HTML template
  5. Overwrite the file in-place
"""

import os
import re
import sys

TARGET_DIR = "/Users/machd/Desktop/licecon/web-portal/public/program"

# ── v9.5 Design Templates ──────────────────────────────────────────────────────

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


def extract_color(content: str) -> str:
    """Pick the dominant Tailwind colour from the file (e.g. 'indigo', 'amber')."""
    # Prefer a colour from the section header gradient
    m = re.search(r'from-(\w+)-[39]00', content)
    if m:
        return m.group(1)
    # Fallback: first bg-X-500 found
    m = re.search(r'bg-(\w+)-500', content)
    return m.group(1) if m else "indigo"


def reformat_glossary(file_content: str) -> tuple[str, bool]:
    """
    Finds the existing glosario block, extracts term/definition pairs,
    and replaces it with the v9.5 template.
    Returns (new_content, was_changed).
    """
    # Already v9.5?
    if "<!-- GLOSARIO v9.5 -->" in file_content:
        return file_content, False

    # Locate the glosario section
    section_pat = re.compile(
        r'<!-- GLOSARIO[^-]*?-->\s*(<section id="glosario".*?</section>)',
        re.DOTALL
    )
    m = section_pat.search(file_content)
    if not m:
        # Nothing to reformat
        return file_content, False

    old_block = m.group(0)   # Full match including the comment
    section_html = m.group(1)

    color = extract_color(file_content)

    # Extract (term, definition) pairs
    # Old cards have <h3 ...>{term}</h3> and <p ...>{definition}</p>
    card_pat = re.compile(
        r'<h3[^>]*>\s*(.*?)\s*</h3>\s*<p[^>]*>\s*(.*?)\s*</p>',
        re.DOTALL
    )
    pairs = card_pat.findall(section_html)

    if not pairs:
        return file_content, False

    # Build v9.5 items
    items_html = "\n".join(
        ITEM_TPL.format(
            color=color,
            term=t.strip(),
            definition=d.strip()
        )
        for t, d in pairs
    )

    new_section = SECTION_TPL.format(color=color, items=items_html)

    new_content = file_content.replace(old_block, "<!-- GLOSARIO -->\n" + new_section, 1)
    return new_content, True


def main():
    files = sorted(os.listdir(TARGET_DIR))
    updated = 0
    skipped = 0
    errors = 0

    for fname in files:
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(TARGET_DIR, fname)
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                original = f.read()

            new_content, changed = reformat_glossary(original)

            if changed:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"  ✨ {fname} → v9.5")
                updated += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"  ❌ Error en {fname}: {e}", file=sys.stderr)
            errors += 1

    print(f"\nDone. Updated: {updated} | Skipped (already v9.5 or no glosario): {skipped} | Errors: {errors}")


if __name__ == "__main__":
    main()
