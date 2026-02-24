import os
import re

GLOSSARIES = {
    "a21": {
        "color": "blue",
        "title": "Glosario: Módulo A21",
        "concepts": [
            ("Econometría", "Telescopio matemático y balanza estadística para medir colisiones asimétricas económicas."),
            ("Heterocedasticidad", "Falla oracular donde la varianza del error disloca y muta asintóticamente."),
            ("Autocorrelación", "Infección de serie temporal donde el error de hoy abraza y arrastra al de ayer."),
            ("Multicolinealidad", "Enredo asfixiante donde vectores explicativos colisionan y se solapan inorgánicamente."),
            ("Mínimos Cuadrados (MCO)", "Método alquímico para trazar la recta purificadora que aniquile errores verticales."),
            ("Variable Instrumental", "Muleta estadística asimétrica para purgar estimaciones de endogeneidades tóxicas."),
            ("Endogeneidad", "Circulo vicioso donde el error subyacente interactúa y contamina al vector causal."),
            ("Significancia Estadística", "Umbral probabilista y dictamen de oro que avala inquebrantable una inferencia."),
            ("R-cuadrado", "Termómetro numérico que acusa qué proporción del abismo fáctico es explicado."),
            ("Prueba de Hipótesis", "Juicio inquisitivo para condenar o absolver premoniciones sobre parámetros asintóticos.")
        ]
    }
}

# Generating dummy concepts for A22-A30.
for i in range(22, 31):
    GLOSSARIES[f"a{i}"] = {
        "color": "blue",
        "title": f"Glosario: Módulo A{i}",
        "concepts": [
            ("Desarrollo Económico", "Metamorfosis colosal que transmuta a la nación de subsistente a excedentaria."),
            ("Crecimiento Endógeno", "Motor interno e inagotable (ej. capital humano) que tracciona la arcadia futura."),
            ("Curva de Kuznets", "Arco parabólico dictaminando que la inequidad primero exuda y luego converge."),
            ("Dependencia", "Vasallaje estructural y grillete periférico ligado a colosos centrales hegemónicos."),
            ("Bienes de Capital", "Sustratos inorgánicos y forjas primigenias pre-destinadas a alumbrar consumo."),
            ("Fuga de Capitales", "Hemorragia patrimonial y diáspora de rentabilidades ante pánicos inescrutables."),
            ("Estado de Bienestar", "Escudo protector y asimilador coercitivo que blinda a la plebe con salud y seguro."),
            ("Sustitución de Importaciones", "Muralla aduanera e incubadora artificial para forjar industria infante endógena."),
            ("Trampa de Pobreza", "Pozo gravitacional y foso circular donde la miseria arrastra ineludible perenne."),
            ("Excedente del Consumidor", "Goce pecuniario, alivio inmaterial asimétrico y premio utilitario de compra barata.")
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
