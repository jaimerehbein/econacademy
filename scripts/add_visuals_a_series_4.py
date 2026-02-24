import os
import re

VISUALS = {
    "a31": {
        "title": "Balanza de Pagos y Tipo de Cambio",
        "diagram": """
```mermaid
graph TD
    classDef default fill:#111827,stroke:#3b82f6,stroke-width:1px,color:#d1d5db
    classDef acc fill:#1e3a8a,stroke:#60a5fa,stroke-width:2px,color:#fff
    classDef def fill:#7f1d1d,stroke:#f87171,stroke-width:2px,color:#fff
    classDef sur fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#fff

    BP[Balanza de Pagos Nacional] --> CC[Cuenta Corriente]
    BP --> CF[Cuenta Financiera y de Capital]
    BP --> ER[Errores y Omisiones]
    
    CC --> X[Exportaciones (Bienes y Servicios)]
    CC --> M[Importaciones (Bienes y Servicios)]
    CC --> R_P[Rentas Primarias y Secundarias]
    
    CF --> IED[Inversión Extranjera Directa]
    CF --> ICP[Inversión de Cartera]
    CF --> OTR[Otras Inversiones]
    CF --> RES[Variación de Reservas Internacionales]
    
    X --> SURG(Superávit)
    IED --> SURG
    
    M --> DEF(Déficit)
    
    class CC,CF acc
    class SURG sur
    class DEF def
```
"""
    },
    "a32": {
        "title": "Fallas del Mercado e Intervención Pública",
        "diagram": """
<div class="my-10 bg-gray-900/60 p-8 rounded-3xl border border-blue-500/20">
    <h3 class="text-blue-400 font-bold text-xl mb-6">Taxonomía de las Fallas Arquitectónicas del Mercado</h3>
    
    <div class="space-y-6">
        <div class="p-5 bg-black/40 rounded-xl border border-gray-700">
            <h4 class="text-red-400 font-bold mb-2 flex items-center gap-2">
                <span class="bg-red-500/20 px-2 py-0.5 rounded text-xs">1</span> 
                Externalidades
            </h4>
            <p class="text-gray-300 text-sm">
                Colisiones asimétricas no internalizadas en los precios. 
                <span class="text-gray-400 italic">Ej: Contaminación exuda costos sociales marginales mayores al costo privado, forzando la inyección de **impuestos pigouvianos**.</span>
            </p>
        </div>
        
        <div class="p-5 bg-black/40 rounded-xl border border-gray-700">
            <h4 class="text-yellow-400 font-bold mb-2 flex items-center gap-2">
                <span class="bg-yellow-500/20 px-2 py-0.5 rounded text-xs">2</span> 
                Bienes Públicos
            </h4>
            <p class="text-gray-300 text-sm">
                Condenados por la **no-exclusión** y la **no-rivalidad**. El mercado libre falla letalmente por el incentivo parásito (free-rider), exigiendo la provisión asimiladora del Estado.
            </p>
        </div>
        
        <div class="p-5 bg-black/40 rounded-xl border border-gray-700">
            <h4 class="text-purple-400 font-bold mb-2 flex items-center gap-2">
                <span class="bg-purple-500/20 px-2 py-0.5 rounded text-xs">3</span> 
                Información Asimétrica
            </h4>
            <p class="text-gray-300 text-sm">
                Ceguera y opacidad fútil donde una parte ostenta presciencia sobre la otra. Detona **Selección Adversa** ex-ante y **Riesgo Moral** ex-post en mercados securitizadores o crediticios.
            </p>
        </div>
        
        <div class="p-5 bg-black/40 rounded-xl border border-gray-700">
            <h4 class="text-cyan-400 font-bold mb-2 flex items-center gap-2">
                <span class="bg-cyan-500/20 px-2 py-0.5 rounded text-xs">4</span> 
                Poder de Mercado (Monopolios)
            </h4>
            <p class="text-gray-300 text-sm">
                La tiranía del precio dictaminado. Destruye el excedente del consumidor asintóticamente al comprimir las cantidades (Q) por debajo del óptimo paretiano dictado en la alquimia de la Competencia Perfecta.
            </p>
        </div>
    </div>
</div>
"""
    }
}

# Dummy generation
for i in range(31, 41):
    if f"a{i}" not in VISUALS:
        VISUALS[f"a{i}"] = {
            "title": f"Modelo Analítico de la Asignatura A{i}",
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
