import os
import glob
import re

THEMES = {
    "if": {"color": "emerald", "hex": "#10b981", "bg": "#064e3b"},
    "ep": {"color": "rose", "hex": "#f43f5e", "bg": "#881337"},
    "eb": {"color": "amber", "hex": "#f59e0b", "bg": "#78350f"},
    "mac": {"color": "cyan", "hex": "#06b6d4", "bg": "#164e63"},
    "mic": {"color": "fuchsia", "hex": "#d946ef", "bg": "#701a75"},
    "me": {"color": "lime", "hex": "#84cc16", "bg": "#3f6212"},
    "m": {"color": "teal", "hex": "#14b8a6", "bg": "#134e4a"},
}

def get_theme(filename):
    # Extracts the series name, e.g., 'if' from 'if1_extended.md'
    match = re.match(r'([a-zA-Z]+)\d+', filename)
    if match:
        series = match.group(1).lower()
        if series in THEMES:
            return THEMES[series]
    
    # Special exact matches or fallbacks
    for key in THEMES:
        if filename.startswith(key):
            return THEMES[key]
            
    return {"color": "blue", "hex": "#3b82f6", "bg": "#1e3a8a"}  # Default

def generate_visual_html(mod_name, theme):
    color = theme["color"]
    hex_color = theme["hex"]
    bg_color = theme["bg"]
    title = f"Esquema Conceptual Módulo {mod_name.upper()}"
    
    diagram = f"""
        <pre class="mermaid bg-transparent flex justify-center">
graph LR
    A[Fundamentos Teóricos] --> B(Aplicación Práctica)
    B --> C{{Análisis Crítico}}
    C -->|Evaluación| D[Validación Empírica]
    C -->|Revisión| E[Ajuste de Modelo]
    
    classDef default fill:#111827,stroke:{hex_color},stroke-width:1px,color:#d1d5db
    classDef decision fill:{bg_color},stroke:{hex_color},stroke-width:2px,color:#fff
    class C decision
        </pre>
"""

    return f'''
<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-{color}-500 font-mono text-xs">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-xl">{title}</h3>
    </div>
    <div class="bg-black/30 p-2 md:p-6 rounded-2xl border border-white/5 overflow-x-auto">
        {diagram}
    </div>
</div>
'''

def inject_visuals():
    files = glob.glob("/Users/machd/Desktop/licecon/web-portal/public/program/*.md")
    
    count = 0
    for filepath in files:
        filename = os.path.basename(filepath)
        
        # Skip 'a' series as they are already done
        if re.match(r'^a\d+', filename) or filename.startswith('eb_') or filename.startswith('ep_') or filename.startswith('if_'):
            continue
            
        # Parse module name (e.g., 'mac3')
        mod_match = re.match(r'^([a-zA-Z]+\d+)', filename)
        if not mod_match:
            continue
        mod_name = mod_match.group(1)

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if "<!-- VISUAL_ENRICHMENT -->" in content:
            # print(f"Visuals already exist in {filename}")
            continue

        theme = get_theme(filename)
        html = generate_visual_html(mod_name, theme)

        # Inject logic
        if "<!-- GLOSARIO -->" in content:
            target = "<!-- GLOSARIO -->"
            content = content.replace(target, html + "\n" + target)
        elif "<!-- FOOTER -->" in content:
            target = "<!-- FOOTER -->"
            content = content.replace(target, html + "\n" + target)
        else:
            content += html
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Injected visual enrichment into {filename}")
        count += 1
        
    print(f"Total files enriched: {count}")

if __name__ == "__main__":
    inject_visuals()
