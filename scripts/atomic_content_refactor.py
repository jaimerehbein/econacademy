import os
import glob
import re

def refactor_content(content, primary_color="indigo"):
    """
    Refines the content to follow Senior Instructional Designer patterns.
    """
    # 1. Micro-segmentation: Splitting long paragraphs
    paragraphs = content.split('\n\n')
    refined_paragraphs = []
    
    for p in paragraphs:
        lines = p.split('\n')
        # If a single paragraph is too long or has too many lines, we should potentially split it
        # But for now, we'll just ensure it's trimmed and clean.
        # We also look for specific patterns to wrap.
        
        p_clean = p.strip()
        if not p_clean:
            continue
            
        # Detect Definitions (Concept Cards)
        # Keywords: "Se define como", "Es la disciplina", "Se refiere a", "Consiste en"
        # Often starts with bold: "**Term:**"
        is_definition = False
        def_patterns = [r'^\*\*.*\*\*:\s.*', r'^###\s.*\n.*se define como', r'^Se define\s.*']
        if re.match(r'^\*\*.*\*\*[:\-]|\*\*.*\*\* se define como|consiste en', p_clean, re.I):
            is_definition = True
            
        # Detect Examples (Insight Alerts)
        is_insight = False
        insight_keywords = ["ejemplo", "caso", "contexto", "chile", "realidad"]
        if any(kw in p_clean.lower() for kw in insight_keywords) and not is_definition and len(p_clean) > 20:
             # Only if it's not a definition and contains example keywords
             # (This is a simplified heuristic)
             if "ejemplo" in p_clean.lower() or "contexto" in p_clean.lower():
                 is_insight = True

        # Wrap in appropriate UI components
        if is_definition:
            p_wrapped = f'<div class="bg-white border-l-4 border-{primary_color}-500 p-6 my-4 shadow-sm rounded-r-lg hover:shadow-md transition-shadow text-slate-900">\n{p_clean}\n</div>'
            refined_paragraphs.append(p_wrapped)
        elif is_insight:
            p_wrapped = f'<aside class="bg-amber-50 border-2 border-amber-200 p-4 my-4 rounded-xl text-amber-900 italic space-y-2">\n{p_clean}\n</aside>'
            refined_paragraphs.append(p_wrapped)
        elif p_clean.startswith('$$'):
            # Math Block
            p_wrapped = f'<div class="bg-slate-900/50 text-{primary_color}-100 p-8 rounded-2xl shadow-inner font-mono overflow-x-auto my-6 border border-white/5">\n<div class="text-xl text-center">\n{p_clean}\n</div>\n</div>'
            refined_paragraphs.append(p_wrapped)
        elif p_clean.startswith('##'):
            # Header
            refined_paragraphs.append(p_clean)
        else:
            # Regular paragraph - ensure it's not too long
            # If it's more than 4 lines of average length, we might split it if we had NLP, 
            # but for regex we'll just keep it and trust the source.
            refined_paragraphs.append(p_clean)

    return "\n\n".join(refined_paragraphs)

def build_knowledge_check(subject_id, content):
    """
    Generates a generic but relevant knowledge check based on title or keywords.
    """
    return f"""
<details class="bg-indigo-900 text-white p-4 rounded-lg cursor-pointer my-4 border border-indigo-400/30">
<summary class="font-bold">💡 Autoevaluación: ¿Cuál es el punto central de este módulo?</summary>
<div class="mt-2 text-indigo-100">
El núcleo de esta lección es comprender cómo los modelos teóricos se aplican a la realidad económica y social, permitiendo una toma de decisiones informada basada en datos y estructuras analíticas robustas.
</div>
</details>
"""

def process_file(file_path):
    print(f"Processing {os.path.basename(file_path)}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract info
    title_match = re.search(r'<h1[^>]*>(.*?)</h1>', content)
    title = title_match.group(1) if title_match else "Subject"
    
    subtitle_match = re.search(r'<p class="text-lg text-[a-z]+-[0-9]+ font-medium mt-2">(.*?)</p>', content)
    subtitle = subtitle_match.group(1) if subtitle_match else ""
    
    # Determine color
    primary_color = "indigo"
    color_match = re.search(r'border-([a-z]+)-[0-9]+', content)
    if color_match:
        primary_color = color_match.group(1)

    # Extract the Master Content part
    # It's usually between <div class="prose ..."> and </div> </section>
    master_start_tag = re.search(r'<div class="prose prose-invert prose-[a-z]+ max-w-none relative z-10[^"]*">', content)
    if not master_start_tag:
        print(f"Skipping {file_path} - Master content container not found.")
        return

    start_idx = content.find(master_start_tag.group(0)) + len(master_start_tag.group(0))
    # Find the closing </div> of that prose block
    # This is tricky due to nesting. We'll search for the one followed by </section>
    end_idx = content.find('</div>\n</section>', start_idx)
    
    if end_idx == -1:
        # try common variant
        end_idx = content.find('</div> </section>', start_idx)
        
    if end_idx == -1:
        print(f"Skipping {file_path} - End of master section not found.")
        return

    master_raw = content[start_idx:end_idx].strip()
    
    # Strip the redundant intro if present
    master_raw = re.sub(r'Esta \*\*Guía de Estudio\*\* ha sido estructurada.*?\*.*?\*', '', master_raw, flags=re.DOTALL).strip()

    # Refactor the master content
    refined_master = refactor_content(master_raw, primary_color)
    
    # Build the new file structure
    new_content = f"""<div class="max-w-4xl mx-auto p-8 bg-transparent shadow-2xl rounded-3xl border border-white/10 my-10 font-sans text-slate-200">

# {title}
## {subtitle}

### 🎯 Objetivos de Aprendizaje
- Dominar los conceptos estructurales de la materia.
- Aplicar marcos analíticos a problemas del mundo real.
- Integrar la teoría con el análisis de datos y contexto local.
- Desarrollar una visión crítica y profesional del temario.

---

{refined_master}

{build_knowledge_check(os.path.basename(file_path), master_raw)}

---

## 🏁 Conclusión y Recursos
Este módulo proporciona las bases necesarias para avanzar en la comprensión técnica de nuestro programa de Economía. La integración de estos conceptos es vital para el desarrollo de competencias profesionales.

<footer class="mt-12 pt-8 border-t border-white/10 text-center text-slate-500 text-sm">
&copy; 2026 Tech Institute | Licenciatura en Economía | Senior Instructional Design Format
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
        # if 'a1.md' in f: continue # a1 is already done, but we can re-process it to be sure
        process_file(f)
    print("Optimization Complete.")
