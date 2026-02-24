import os
import re

VISUALS = {
    "a11": {
        "title": "Estructura del Sistema Tributario",
        "diagram": """
```mermaid
mindmap
  root((Tributos))
    Impuestos
      Directos
        Renta (IRPF / IS)
        Patrimonio
      Indirectos
        IVA / IGV
        Tasas Específicas
    Tasas
      Uso de Dominio Público
      Servicios Administrativos
    Contribuciones Especiales
      Mejoras de Infraestructura
      Seguridad Social
    Elementos Contractuales
      Sujeto Activo (Estado)
      Sujeto Pasivo (Contribuyente)
      Base Imponible
      Hecho Imponible
      Alicuota (Tasa %)
```
"""
    },
    "a13": {
        "title": "Distribución Normal Estadística",
        "diagram": """
<div class="my-10 bg-gray-900/60 p-8 rounded-3xl border border-blue-500/20">
    <h3 class="text-blue-400 font-bold text-xl mb-6">La Campana de Gauss (Distribución Normal)</h3>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
        <div>
            <div class="font-mono text-sm text-center py-4 bg-black/50 rounded-lg mb-4">
                $$f(x) = \\frac{1}{\\sigma \sqrt{2\pi}} e^{-\\frac{1}{2}(\\frac{x-\\mu}{\\sigma})^2}$$
            </div>
            <p class="text-gray-300 text-sm mb-4">
                El pilar paramétrico de la inferencia estadística cuantitativa. Su simetría absoluta dictamina probabilísticamente dónde orbita la manada muestral respecto a su centro de gravedad ($\mu$) y su esquizofrenia volátil ($\sigma$).
            </p>
        </div>
        <div class="bg-black/40 rounded-xl p-4 border border-gray-700">
            <h4 class="text-blue-300 font-bold text-sm mb-3">Postulados de Dispersión Empírica:</h4>
            <ul class="space-y-2 text-sm text-gray-400 font-mono">
                <li><span class="text-purple-400">[\u03bc \u00b1 1\u03c3]</span> \u2192 Aglutina \u2248 68.2% del acervo.</li>
                <li><span class="text-purple-500">[\u03bc \u00b1 2\u03c3]</span> \u2192 Aglutina \u2248 95.4% del acervo.</li>
                <li><span class="text-purple-600">[\u03bc \u00b1 3\u03c3]</span> \u2192 Aglutina \u2248 99.7% del acervo.</li>
            </ul>
        </div>
    </div>
</div>
"""
    },
    "a15": {
        "title": "Equilibrio IS-LM y Demanda Agregada",
        "diagram": """
```mermaid
graph TD
    %% Modelo IS-LM Simplificado
    subgraph El Laberinto Macroeconómico
        IS[Curva IS: Sector Real] --> EQ((Equilibrio<br>Simbiótico P, Y))
        LM[Curva LM: Sector Monetario] --> EQ
        
        EQ --> DA[Demanda Agregada]
        OA[Oferta Agregada] --> EQ2{Equilibrio General}
        DA --> EQ2
        
        EQ2 --> Y[PIB / Renta]
        EQ2 --> INFL[Nivel de Precios]
    end
    
    classDef default fill:#111827,stroke:#3b82f6,stroke-width:1px,color:#d1d5db
    classDef curve fill:#1e3a8a,stroke:#60a5fa,stroke-width:2px,color:#fff
    classDef eq fill:#1e40af,stroke:#93c5fd,stroke-width:2px,color:#fff,font-weight:bold
    class IS,LM,DA,OA curve
    class EQ,EQ2 eq
```
"""
    }
}

# Add dummy text for remaining
for i in range(11, 21):
    if f"a{i}" not in VISUALS:
        VISUALS[f"a{i}"] = {
            "title": f"Esquema Conceptual Módulo A{i}",
            "diagram": f"""
```mermaid
graph LR
    A[Concepto Base] --> B(Aplicación Empírica)
    B --> C{{Resolución Analítica}}
    C -->|Óptimo| D[Equilibrio]
    C -->|Falla| E[Intervención]
    
    classDef default fill:#111827,stroke:#3b82f6,stroke-width:1px,color:#d1d5db
    classDef decision fill:#1e3a8a,stroke:#60a5fa,stroke-width:2px,color:#fff
    class C decision
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
