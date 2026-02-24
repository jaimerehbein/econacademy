import os
import re

VISUALS = {
    "a1": {
        "title": "Estructura Organizacional y Cadena de Valor",
        "diagram": """
```mermaid
graph TD
    %% Estructura Organizacional
    subgraph Jerarquía Corporativa
        CEO[Dirección General / CEO] --> DIR_FIN[Dir. Finanzas]
        CEO --> DIR_OP[Dir. Operaciones]
        CEO --> DIR_MKT[Dir. Marketing]
        DIR_FIN --> CONT[Contabilidad]
        DIR_FIN --> TES[Tesorería]
        DIR_OP --> PROD[Producción]
        DIR_OP --> LOG[Logística]
        DIR_MKT --> VTAS[Ventas]
        DIR_MKT --> PUB[Publicidad]
    end

    %% Flujo de Cadena de Valor de Porter Simplificada
    subgraph Cadena de Valor
        INFRA[Infraestructura] --> LOG_IN
        RRHH[Recursos Humanos] --> LOG_IN
        DES[Desarrollo Tecnológico] --> LOG_IN
        COMPRAS[Compras] --> LOG_IN

        LOG_IN[Logística de Entrada] --> OP[Operaciones]
        OP --> LOG_OUT[Logística de Salida]
        LOG_OUT --> MKT_VTAS[Marketing y Ventas]
        MKT_VTAS --> SERV[Servicios Post-Venta]
        
        SERV -.-> MARGEN((MARGEN DE<br>GANANCIA))
    end
    
    classDef default fill:#1e1e2f,stroke:#10b981,stroke-width:1px,color:#d1d5db
    classDef main fill:#064e3b,stroke:#10b981,stroke-width:2px,color:#fff
    classDef accent fill:#8b5cf6,stroke:#a78bfa,stroke-width:2px,color:#fff,font-weight:bold
    class CEO,MARGEN accent
    class DIR_FIN,DIR_OP,DIR_MKT main
```
"""
    },
    "a2": {
        "title": "Estratificación y Movilidad Social",
        "diagram": """
```mermaid
mindmap
  root((Sociedad))
    Estratificación
      Clase Alta
        Capital Económico
        Capital Cultural
        Élites de Poder
      Clase Media
        Profesionales
        Burocracia
      Clase Trabajadora
        Proletariado Industrial
        Servicios Básicos
      Marginación
        Lumpenproletariado
        Exclusión Sistémica
    Dimensiones Analíticas
      Marxismo
        Propiedad de Medios
        Lucha de Clases
      Weberianismo
        Prestigio (Estatus)
        Poder Político (Partido)
        Clase Económica
    Dinámicas
      Movilidad Social
        Ascendente
        Descendente
        Horizontal
      Alienación
      Anomia (Durkheim)
```
"""
    },
    "a3": {
        "title": "Frontera de Posibilidades de Producción y Flujo Circular",
        "diagram": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-8 my-12">
    <div class="bg-gray-900/50 p-6 rounded-2xl border border-gray-700/50">
        <h4 class="text-emerald-400 font-bold mb-4">Frontera de Posibilidades de Producción (FPP)</h4>
        <div class="text-gray-300 text-sm mb-4">
            Muestra las cantidades máximas de producción que puede obtener una economía, dados sus conocimientos tecnológicos y la cantidad de inputs disponibles.
        </div>
```mermaid
xychart-beta
    title "FPP: Trade-off entre dos bienes"
    x-axis "Bienes de Consumo (X)" [0, 10, 20, 30, 40, 50]
    y-axis "Bienes de Capital (Y)" 0 --> 50
    line [50, 48, 42, 32, 18, 0]
```
        <p class="text-xs text-gray-500 mt-2 italic">A lo largo de la curva: Eficiencia. Por dentro: Ineficiencia. Por fuera: Inalcanzable.</p>
    </div>
    <div class="bg-gray-900/50 p-6 rounded-2xl border border-gray-700/50">
        <h4 class="text-emerald-400 font-bold mb-4">Flujo Circular de la Renta</h4>
```mermaid
flowchart LR
    HOG[Hogares] <-->|Gasto en Consumo| M_BS[Mercado de Bienes<br>y Servicios]
    M_BS <-->|Ingresos| EMP[Empresas]
    EMP <-->|Salarios, Rentas, Bº| M_FP[Mercado de Factores<br>de Producción]
    M_FP <-->|Rentas (Ingreso)| HOG

    HOG -.->|Trabajo, Tierra, Capital| M_FP
    M_FP -.->|Factores productivos| EMP
    EMP -.->|Bienes y Servicios| M_BS
    M_BS -.->|Bienes comprados| HOG
    
    classDef default fill:#1e1e2f,stroke:#3b82f6,stroke-width:1px,color:#d1d5db
    classDef market fill:#1e3a8a,stroke:#60a5fa,stroke-width:2px,color:#fff
    class M_BS,M_FP market
```
    </div>
</div>
"""
    },
    "a4": {
        "title": "Jerarquía de las Normas (Pirámide de Kelsen)",
        "diagram": """
```mermaid
graph TD
    classDef level1 fill:#4c1d95,stroke:#a78bfa,stroke-width:2px,color:#fff,font-weight:bold
    classDef level2 fill:#312e81,stroke:#818cf8,stroke-width:1px,color:#e2e8f0
    classDef level3 fill:#1e3a8a,stroke:#60a5fa,stroke-width:1px,color:#cbd5e1
    classDef level4 fill:#1e1b4b,stroke:#4f46e5,stroke-width:1px,color:#94a3b8

    CONST[I. Constitución Política / Bloque de Constitucionalidad]
    CONST --> LEY[II. Leyes Normativas]
    
    subgraph Leyes
        D_LEGISLATIVOS[Decretos Legislativos]
        L_ORGANICAS[Leyes Orgánicas]
        L_ORDINARIAS[Leyes Ordinarias]
    end
    LEY --> Leyes
    
    Leyes --> REG[III. Decretos y Reglamentos]
    
    subgraph Actos Administrativos
        RES_SUP[Resoluciones Supremas]
        RES_MIN[Resoluciones Ministeriales]
        RES_DIR[Resoluciones Directorales]
    end
    REG --> Actos Administrativos
    
    Actos Administrativos --> SENT[IV. Sentencias, Contratos y Actos Jurídicos Individualizados]

    class CONST level1
    class LEY,D_LEGISLATIVOS,L_ORGANICAS,L_ORDINARIAS level2
    class REG,RES_SUP,RES_MIN,RES_DIR level3
    class SENT level4
```
"""
    },
    "a5": {
        "title": "Fundamentos Analíticos: Límites, Derivadas e Integrales",
        "diagram": """
<div class="my-10 bg-gray-900/60 p-8 rounded-3xl border border-blue-500/20">
    <h3 class="text-blue-400 font-bold text-xl mb-6">El Triunvirato del Cálculo Infinitesimal</h3>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        <div class="p-5 bg-black/40 rounded-xl border border-gray-800">
            <h4 class="text-white font-semibold mb-3">1. Límite (Tendencia)</h4>
            <div class="font-mono text-sm text-center py-4 bg-black/50 rounded-lg mb-3">
                $$\lim_{x \to a} f(x) = L$$
            </div>
            <p class="text-slate-400 text-xs text-justify">El comportamiento asintótico hacia donde converge inexorablemente una función cuando su variable independiente se acorrala infinitesimalmente cerca de un umbral.</p>
        </div>

        <div class="p-5 bg-black/40 rounded-xl border border-gray-800">
            <h4 class="text-white font-semibold mb-3">2. Derivada (Velocidad)</h4>
            <div class="font-mono text-sm text-center py-4 bg-black/50 rounded-lg mb-3">
                $$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$
            </div>
            <p class="text-slate-400 text-xs text-justify">La tasa de variación instantánea. Gráficamente, es el sismógrafo que dicta la pendiente (aceleración métrica) de la recta tangente en un punto exacto de la curva empírica.</p>
        </div>

        <div class="p-5 bg-black/40 rounded-xl border border-gray-800">
            <h4 class="text-white font-semibold mb-3">3. Integral (Acumulación)</h4>
            <div class="font-mono text-sm text-center py-4 bg-black/50 rounded-lg mb-3">
                $$\int_{a}^{b} f(x) dx = F(b) - F(a)$$
            </div>
            <p class="text-slate-400 text-xs text-justify">El acaparador macro. La sumatoria de infinitésimos de Riemann que halla el área confinada topográficamente bajo el trazo de la función, revelando acervos acumulados.</p>
        </div>
    </div>
</div>
"""
    }
}

# Add dummy text for remaining a6-a10
for i in range(6, 11):
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
            # inject before glossary if it exists, else before footer
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
