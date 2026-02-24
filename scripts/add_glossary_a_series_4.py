import os
import re

GLOSSARIES = {
    # Generating dummy concepts for A31-A40 
}
for i in range(31, 41):
    GLOSSARIES[f"a{i}"] = {
        "color": "blue",
        "title": f"Glosario: Módulo A{i}",
        "concepts": [
            ("Política Monetaria", "Timón oracular del Banco Central para encauzar el torrente fáctico transaccional."),
            ("Política Fiscal", "Bisturí de gasto e impuestos del Estado para amputar depresiones asimétricas."),
            ("Ventaja Comparativa", "Ley ricardiana de especialización asimétrica ineluctable según costes de oportunidad relativos."),
            ("Economías de Escala", "Abatimiento asintótico de costos unitarios frente a la expansión colosal del acervo productivo."),
            ("Rendimientos Decrecientes", "Dogma malthusiano donde la inyección estéril marginal aporrea y frena la eclosión productiva."),
            ("Deflación", "Letargo de precios en caída libre, pánico de diferimiento asfixiante arrastrado y parálisis de consumos."),
            ("Barreras de Entrada", "Fosos defensivos, aranceles o colosos fácticos que amurallan el mercado bloqueando a competidores fútiles."),
            ("Competencia Perfecta", "Arcadia utópica inmaculada paramétrica con multitudes atomizadas y poder de mercado irrisoriamente nulo."),
            ("Bienes Giffen", "Anomalías fácticas y acertijos consumistas donde la carestía y alza del precio exuda una compra inusitadamente mayor."),
            ("Equidad vs Eficiencia", "Dicotomía trágica y pugna distributiva donde igualar la porción asimétrica erosiona el total fáctico del horneado.")
        ]
    }

def inject_glossaries():
    for mod, data in GLOSSARIES.items():
        base_path = f"/Users/machd/Desktop/licecon/web-portal/public/program/{mod}"
        filepaths_to_try = [f"{base_path}.md", f"{base_path}_extended.md"]
        
        injected = False
        for filepath in filepaths_to_try:
            if not os.path.exists(filepath):
                continue
                
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            if "<!-- GLOSARIO -->" in content:
                print(f"Glossary already exists in {filepath}")
                continue

            color = data["color"]
            
            # Build HTML
            html = f'<!-- GLOSARIO -->\n<section class="mb-24">\n    <div class="flex items-center gap-3 mb-10">\n        <span class="text-{color}-500 font-mono text-xs">[GL]</span>\n        <h2 class="text-white font-black text-2xl uppercase tracking-tighter">{data["title"]}</h2>\n    </div>\n    <div class="space-y-3">\n'
            
            for term, desc in data["concepts"]:
                term_esc = term.replace('\\', '\\\\')
                desc_esc = desc.replace('\\', '\\\\')
                html += f'''        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-{color}-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">{term_esc}</span>
            <p class="text-slate-400 text-sm leading-relaxed">{desc_esc}</p>
        </div>\n'''
            
            html += '    </div>\n</section>\n\n'

            target = "<!-- FOOTER -->"
            if target in content:
                content = content.replace(target, html + target)
            else:
                content = re.sub(r'(</div>\s*</div>\s*)$', html + r'\1', content)
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"Injected glossary into {filepath}")
            injected = True
            
        if not injected:
            print(f"File not found or already injected: {mod}")

if __name__ == "__main__":
    inject_glossaries()
