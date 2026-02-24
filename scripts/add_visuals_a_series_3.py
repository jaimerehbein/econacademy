import os
import re

VISUALS = {
    "a21": {
        "title": "Análisis de Regresión Múltiple",
        "diagram": """
<div class="my-10 bg-gray-900/60 p-8 rounded-3xl border border-blue-500/20">
    <h3 class="text-blue-400 font-bold text-xl mb-6">El Motor Econométrico (MCO)</h3>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
        <div>
            <div class="font-mono text-sm text-center py-4 bg-black/50 rounded-lg mb-4">
                $$Y_i = \\beta_0 + \\beta_1 X_{1i} + \\beta_2 X_{2i} + ... + \\beta_k X_{ki} + u_i$$
            </div>
            <p class="text-gray-300 text-sm mb-4">
                La ecuación suprema que desentraña el caos fáctico empírico. $Y_i$ (la variable dictaminada) es diseccionada asimétricamente por vectores de $X$ (los tenientes explicativos), aislando quirúrgicamente el efecto ceteris paribus de cada uno, relegando la ignorancia inescrutable al término de error $u_i$.
            </p>
        </div>
        <div class="bg-black/40 rounded-xl p-4 border border-gray-700">
            <h4 class="text-blue-300 font-bold text-sm mb-3">Supuestos Basales Clásicos:</h4>
            <ul class="space-y-2 text-sm text-gray-400 font-mono">
                <li><span class="text-green-400">[1]</span> Linealidad en parámetros.</li>
                <li><span class="text-green-500">[2]</span> Muestreo aleatorio asombroso.</li>
                <li><span class="text-green-600">[3]</span> Exogeneidad estricta ($E[u|X] = 0$).</li>
                <li><span class="text-teal-400">[4]</span> Homocedasticidad (Varianza inquebrantable pura).</li>
                <li><span class="text-teal-500">[5]</span> No autocorrelación de errores.</li>
            </ul>
        </div>
    </div>
</div>
"""
    },
    "a22": {
        "title": "Diagrama del Crecimiento de Solow-Swan",
        "diagram": """
```mermaid
graph TD
    classDef default fill:#111827,stroke:#3b82f6,stroke-width:1px,color:#d1d5db
    classDef main fill:#1e3a8a,stroke:#60a5fa,stroke-width:2px,color:#fff
    classDef output fill:#1e40af,stroke:#93c5fd,stroke-width:2px,color:#fff,font-weight:bold

    K[Acervo de Capital] --> Y((Producción Total Y))
    L[Fuerza Laboral] --> Y
    A[Progreso Tecnológico] --> Y
    
    Y --> C[Consumo (C)]
    Y --> S{Ahorro = Inversión (S=I)}
    
    S --> DEP[Depreciación]
    S --> GRW[Aumento Poblacional]
    
    S -->|Inyección Neta| K
    
    class K,L,A main
    class Y output
```
"""
    },
    "a24": {
        "title": "Geopolítica y Dependencia",
        "diagram": """
```mermaid
mindmap
  root((Sistema Mundo))
    Centro Hegemónico
      Capitales Tecnológicos
      Financiarización Global
      Monopolios Extractivos
    Periferia (Subyugada)
      Exportador Materias Primas
      Mano de Obra Barata
      Deuda Externa Asfixiante
    Semi-Periferia
      Industrialización Tardía
      Amortiguador Sistémico
    Mecanismos de Transferencia
      Deterioro Términos Intercambio
      Fuga de Ganancias
      Rentabilidad Asimétrica
```
"""
    }
}

# Dummy generation
for i in range(21, 31):
    if f"a{i}" not in VISUALS:
        VISUALS[f"a{i}"] = {
            "title": f"Modelo Conceptual A{i}",
            "diagram": f"""
```mermaid
stateDiagram-v2
    [*] --> Génesis
    Génesis --> Expansión : Inyección Empírica
    Expansión --> Cúspide : Maximización Asintótica
    Cúspide --> Contracción : Fricción Fáctica
    Contracción --> Génesis : Depuración
```
"""
        }

def inject_visuals():
    for mod, data in VISUALS.items():
        base_path = f"/Users/machd/Desktop/licecon/web-portal/public/program/{mod}"
        filepaths_to_try = [f"{base_path}.md", f"{base_path}_extended.md"]
        
        injected = False
        for filepath in filepaths_to_try:
            if not os.path.exists(filepath):
                continue
                
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            if "<!-- VISUAL_ENRICHMENT -->" in content:
                print(f"Visuals already exist in {filepath}")
                continue

            html = f'''
<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-blue-500 font-mono text-xs">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-xl">{data["title"]}</h3>
    </div>
    <div class="bg-black/30 p-2 md:p-6 rounded-2xl border border-white/5 overflow-x-auto">
        {data["diagram"]}
    </div>
</div>
'''
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
                
            print(f"Injected visual enrichment into {filepath}")
            injected = True

if __name__ == "__main__":
    inject_visuals()
