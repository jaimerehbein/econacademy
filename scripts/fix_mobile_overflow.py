import os
import glob
import re

def fix_mobile_overflow():
    files = glob.glob("/Users/machd/Desktop/licecon/web-portal/public/program/*.md")
    
    count = 0
    for filepath in files:
        filename = os.path.basename(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 1. Update main H1 titles for better mobile wrapping
        # Looking for `text-5xl md:text-7xl` or similar
        content = re.sub(
            r'<h1 class="([^"]*)text-5xl([^"]*)">',
            r'<h1 class="\1text-4xl sm:text-5xl\2 break-words hyphens-auto">',
            content
        )
        
        # 2. Update H2 titles inside sections
        content = re.sub(
            r'<h2 class="([^"]*)text-3xl([^"]*)">',
            r'<h2 class="\1text-2xl sm:text-3xl\2 break-words leading-tight">',
            content
        )
        content = re.sub(
            r'<h2 class="([^"]*)text-4xl([^"]*)">',
            r'<h2 class="\1text-3xl sm:text-4xl\2 break-words leading-tight">',
            content
        )

        # 3. Update diagram headers flex containers
        # From: <div class="flex items-center gap-3 mb-8">
        # To: <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">
        # BUT only for diagram headers where [DIAGRAMA] or [GL] or similar is there. Let's just fix the specific diagram injected block.
        # We know [DIAGRAMA] has a span before it.
        # Actually, let's target the exact string injected by `batch_add_visuals_all_series.py` and `add_visuals_a_series_*.py`
        
        # We can find `<div class="flex items-center gap-3 mb-8">` followed by `<span class="text-` and `[DIAGRAMA]`
        pattern_diagram = r'<div class="flex items-center gap-3 mb-8">\s*<span class="text-([a-z]+)-500 font-mono text-xs">\[DIAGRAMA\]</span>\s*<h3 class="text-white font-bold text-xl">(.*?)</h3>\s*</div>'
        replacement_diagram = r'<div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">\n        <span class="text-\1-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[DIAGRAMA]</span>\n        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">\2</h3>\n    </div>'
        content = re.sub(pattern_diagram, replacement_diagram, content)
        
        # 4. Same for GLOSARIO header which might overflow if flex items-center forces it.
        # <div class="flex items-center gap-3 mb-10"> ... [GL] ... Glosario
        pattern_glosario = r'<div class="flex items-center gap-3 mb-10">\s*<span class="text-([a-z]+)-500 font-mono text-xs">\[GL\]</span>\s*<h2 class="text-white font-black text-2xl uppercase tracking-tighter">(.*?)</h2>\s*</div>'
        replacement_glosario = r'<div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-10">\n        <span class="text-\1-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[GL]</span>\n        <h2 class="text-white font-black text-xl sm:text-2xl uppercase tracking-tighter break-words leading-tight">\2</h2>\n    </div>'
        content = re.sub(pattern_glosario, replacement_glosario, content)

        # 5. Fix extremely long strings in `max-w-4xl mx-auto...` to add `break-words` generally?
        content = content.replace('<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans">', '<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">')

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
            print(f"Fixed overflow in {filename}")

    print(f"Total files fixed: {count}")

if __name__ == "__main__":
    fix_mobile_overflow()
