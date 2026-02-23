import os
import glob
import re

def refactor_block(p_clean, primary_color="indigo"):
    """
    Refines a single paragraph/block based on its type.
    """
    if not p_clean:
        return None
        
    # Detect Definitions (Concept Cards)
    is_definition = False
    if re.match(r'^\*\*.*\*\*[:\-]|\*\*.*\*\* se define como|consiste en', p_clean, re.I):
        is_definition = True
        
    # Detect Examples (Insight Alerts)
    is_insight = False
    insight_keywords = ["ejemplo", "caso", "contexto", "chile", "realidad"]
    if any(kw in p_clean.lower() for kw in insight_keywords) and not is_definition and len(p_clean) > 20:
         if "ejemplo" in p_clean.lower() or "contexto" in p_clean.lower():
             is_insight = True

    if is_definition:
        return {
            "type": "definition",
            "content": p_clean,
            "html": f'<div class="bg-white p-10 rounded-3xl shadow-xl border-l-8 border-{primary_color}-500 text-slate-900">\n{p_clean}\n</div>'
        }
    elif is_insight:
        return {
            "type": "insight",
            "content": p_clean,
            "html": f'<aside class="bg-amber-50/90 backdrop-blur border-2 border-amber-200 p-8 rounded-3xl text-amber-900 shadow-2xl -rotate-1 hover:rotate-0 transition-transform">\n<h4 class="font-black mb-2 uppercase text-xs tracking-widest opacity-70">💡 Insight</h4>\n{p_clean}\n</aside>'
        }
    elif p_clean.startswith('$$'):
        return {
            "type": "math",
            "content": p_clean,
            "html": f'<div class="py-20 bg-slate-900/80 rounded-[3rem] border border-white/5 text-center my-12">\n<div class="text-2xl md:text-3xl text-white mb-4">{p_clean}</div>\n</div>'
        }
    elif p_clean.startswith('##'):
        return {
            "type": "header",
            "content": p_clean,
            "html": f'<h2 class="text-3xl font-bold text-white mb-8 border-l-4 border-{primary_color}-500 pl-6 mt-20">{p_clean.replace("##", "").strip()}</h2>'
        }
    elif p_clean.startswith('###'):
        return {
            "type": "subheader",
            "content": p_clean,
            "html": f'<h3 class="text-2xl font-bold text-white mb-6 mt-12">{p_clean.replace("###", "").strip()}</h3>'
        }
    else:
        return {
            "type": "text",
            "content": p_clean,
            "html": f'<p class="text-lg leading-relaxed text-slate-400 mb-6">{p_clean}</p>'
        }

def assemble_grids(blocks, primary_color="indigo"):
    """
    Assembles refined blocks into a visual grid (Level 2).
    """
    assembled_html = []
    i = 0
    while i < len(blocks):
        block = blocks[i]
        
        # Pattern: Header followed by text/definitions
        if block["type"] == "header":
            assembled_html.append(block["html"])
            i += 1
            continue
            
        # Pattern: Two definitions in a row -> Grid
        if block["type"] == "definition" and i + 1 < len(blocks) and blocks[i+1]["type"] == "definition":
            grid = f'<div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">\n{block["html"]}\n{blocks[i+1]["html"]}\n</div>'
            assembled_html.append(grid)
            i += 2
            continue
            
        # Pattern: Text followed by Insight -> Side-by-side
        if block["type"] == "text" and i + 1 < len(blocks) and blocks[i+1]["type"] == "insight":
            grid = f'<div class="grid grid-cols-1 md:grid-cols-12 gap-12 mb-20 items-center">\n<div class="md:col-span-8">{block["html"]}</div>\n<div class="md:col-span-4">{blocks[i+1]["html"]}</div>\n</div>'
            assembled_html.append(grid)
            i += 2
            continue
            
        # Generic block
        assembled_html.append(block["html"])
        i += 1
        
    return "\n\n".join(assembled_html)

def process_file(file_path):
    print(f"Refactoring to Level 2: {os.path.basename(file_path)}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract info (Improved Regex)
    title_match = re.search(r'# (.*)', content)
    title = title_match.group(1).strip() if title_match else "Asignatura"
    
    subtitle_match = re.search(r'## (.*)', content)
    subtitle = subtitle_match.group(1).strip() if subtitle_match else ""
    
    # Determine color
    primary_color = "indigo"
    if "amber" in content: primary_color = "amber"
    elif "emerald" in content: primary_color = "emerald"
    elif "cyan" in content: primary_color = "cyan"
    elif "rose" in content: primary_color = "rose"
    elif "violet" in content: primary_color = "violet"

    # Extract raw content between headers and footer/conclusion
    # We'll split by "---" to find the main meat
    parts = re.split(r'---', content)
    if len(parts) < 3:
        print(f"Skipping {file_path} - Structure unexpected.")
        return

    main_raw = parts[1].strip()
    
    # Clean up objectives from main_raw if they are at the top
    main_raw = re.sub(r'### 🎯 Objetivos de Aprendizaje.*?\n(?=-|#)', '', main_raw, flags=re.DOTALL).strip()

    # Parse into blocks
    paragraphs = [p.strip() for p in main_raw.split('\n\n') if p.strip()]
    blocks = [refactor_block(p, primary_color) for p in paragraphs]
    blocks = [b for b in blocks if b]
    
    # Assemble into grid
    refined_body = assemble_grids(blocks, primary_color)
    
    # Build the Level 2 Template
    new_content = f"""<div class="max-w-6xl mx-auto p-4 md:p-12 bg-transparent my-10 font-sans text-slate-200">

<!-- HERO SECTION -->
<header class="mb-32 py-16 border-b border-white/10 text-center relative">
    <div class="absolute -top-24 left-1/2 -translate-x-1/2 w-96 h-96 bg-{primary_color}-500/10 blur-[120px] rounded-full pointer-events-none"></div>
    <h1 class="text-5xl md:text-7xl font-black text-white tracking-tighter mb-4 bg-clip-text text-transparent bg-gradient-to-r from-white to-slate-500">
        {title}
    </h1>
    <p class="text-xl md:text-2xl text-{primary_color}-400 font-light tracking-widest uppercase">
        {subtitle}
    </p>
</header>

<section class="mb-32">
    <h2 class="text-3xl font-bold text-white mb-12 border-l-4 border-{primary_color}-500 pl-6">🎯 Objetivos Maestros</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-12 text-lg text-slate-400 leading-relaxed">
        <ul class="space-y-4">
            <li>• Dominar los conceptos estructurales de la materia.</li>
            <li>• Aplicar marcos analíticos a problemas del mundo real.</li>
        </ul>
        <ul class="space-y-4">
            <li>• Integrar la teoría con el análisis de contexto local.</li>
            <li>• Desarrollar una visión crítica y profesional del temario.</li>
        </ul>
    </div>
</section>

---

{refined_body}

---

<section class="my-32">
    <h2 class="text-3xl font-bold text-white mb-12">💡 Desafío de Comprensión</h2>
    <details class="group bg-{primary_color}-900/40 hover:bg-{primary_color}-900/60 transition-colors border border-{primary_color}-500/30 rounded-3xl overflow-hidden cursor-pointer">
        <summary class="p-10 text-xl font-bold text-white flex justify-between items-center group-open:border-b border-white/10 text-left">
            ¿Cuál es el núcleo central de esta lección y su aplicación práctica?
            <span class="text-3xl group-open:rotate-45 transition-transform flex-shrink-0 ml-4">+</span>
        </summary>
        <div class="p-10 text-lg text-{primary_color}-100 leading-relaxed bg-black/20">
            El dominio de estos conceptos permite una toma de decisiones informada, integrando la teoría con el análisis de datos y la realidad del entorno económico-social.
        </div>
    </details>
</section>

<footer class="mt-40 pt-12 border-t border-white/10 flex flex-col md:flex-row justify-between items-center text-slate-500 text-sm gap-4">
    <p>&copy; 2026 Tech Economics Institute</p>
    <div class="flex gap-8">
        <a href="#" class="hover:text-white transition-colors">Glosario</a>
        <a href="#" class="hover:text-white transition-colors">Recursos MASTER</a>
    </div>
    <p class="font-mono text-xs opacity-40 uppercase">Senior Instructional Design v2.0</p>
</footer>

</div>
"""
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    program_dir = os.path.join(os.getcwd(), 'public', 'program')
    md_files = glob.glob(os.path.join(program_dir, 'a*.md'))
    for f in sorted(md_files):
        if '_extended' in f: continue
        # a1 is already perfect, we can re-process it or skip. Let's process all to ensure complete consistency.
        process_file(f)
    print("Level 2 Optimization Complete.")
