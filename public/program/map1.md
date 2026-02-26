<section class="max-w-6xl mx-auto space-y-16 pb-20">

<!-- Hero Section -->
<div class="relative overflow-hidden rounded-[2.5rem] border border-white/10 bg-gradient-to-br from-slate-900 to-black p-8 lg:p-16 shadow-2xl">
    <div class="absolute inset-0 bg-[linear-gradient(to_right,#e2e8f00a_1px,transparent_1px),linear-gradient(to_bottom,#e2e8f00a_1px,transparent_1px)] bg-[size:48px_48px]"></div>

    <div class="absolute top-0 right-0 w-[800px] h-[800px] bg-slate-500/10 rounded-full blur-[120px] -translate-y-1/2 translate-x-1/3 pointer-events-none"></div>

    <div class="relative z-10 space-y-8">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 text-white/70 text-sm font-medium">
            <span class="w-2 h-2 rounded-full bg-blue-500 animate-pulse"></span>
            Modeloteca
        </div>
        
        <div class="space-y-4">
            <h1 class="text-5xl lg:text-7xl font-bold tracking-tight text-white">
                Atlas de <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-emerald-400">Modelos Mentales</span>
            </h1>
            <p class="text-lg text-slate-400 max-w-2xl leading-relaxed">
                Cartografía visual de hiper-densidad teórica que condensa siglos de progreso económico y matrices analíticas en ocho ecosistemas conceptuales interactivos.
            </p>
        </div>
    </div>
</div>

<div class="space-y-12">

    <!-- Ecosistema Keynesiano (Corto Plazo) -->
    <div class="bg-slate-900/80 border border-white/5 rounded-3xl p-8 shadow-xl mt-8">
        <h3 class="text-2xl font-bold text-blue-400 mb-2">Ecosistema Keynesiano (Corto Plazo)</h3>
        <p class="text-slate-400 text-sm mb-8">El paradigma de la intervención estatal y la demanda agregada como motor de la producción bajo precios rígidos.</p>
        
        <div class="overflow-hidden rounded-xl border border-white/5 bg-slate-950/50 p-6 flex justify-center">
            <pre class="mermaid w-full flex justify-center">
flowchart LR
A["KEYNESIANISMO (Corto Plazo)"]

    A --> B["Demanda Agregada"]
    B --> B1["Consumo (C)"]
    B --> B2["Inversión (I)"]
    B --> B3["Gasto Público (G)"]

    B1 -.-> B1a["Propensión Marginal"]
    B2 -.-> B2a["Espíritus Animales"]
    B3 -.-> B3a["Multiplicador Keynesiano"]

    A --> C["Modelo IS-LM"]
    C --> C1["Curva IS (Bienes)"]
    C --> C2["Curva LM (Dinero)"]
    C2 -.-> C2a["Trampa de Liquidez"]

    A --> D["Mercado Laboral"]
    D --> D1["Rigidez Salarial"]
    D --> D2["Desempleo Involuntario"]
    D --> D3["Ilusión Monetaria"]

    style A fill:#0f172a,stroke:#3b82f6,stroke-width:2px,color:#eff6ff
    style B fill:#1e293b,stroke:#64748b,stroke-width:1px,color:#e2e8f0
    style B1 fill:#020617,stroke:#3f3f46,stroke-dasharray:3 3,color:#a1a1aa
    style B2 fill:#020617,stroke:#3f3f46,stroke-dasharray:3 3,color:#a1a1aa
    style B3 fill:#0ea5e9,stroke:#bae6fd,stroke-width:1px,color:#fff
    style B1a fill:#020617,stroke:#3f3f46,stroke-dasharray:3 3,color:#a1a1aa
    style B2a fill:#020617,stroke:#3f3f46,stroke-dasharray:3 3,color:#a1a1aa
    style B3a fill:#0ea5e9,stroke:#bae6fd,stroke-width:1px,color:#fff
    style C fill:#1e293b,stroke:#64748b,stroke-width:1px,color:#e2e8f0
    style C1 fill:#020617,stroke:#3f3f46,stroke-dasharray:3 3,color:#a1a1aa
    style C2 fill:#020617,stroke:#3f3f46,stroke-dasharray:3 3,color:#a1a1aa
    style C2a fill:#be185d,stroke:#fbcfe8,stroke-width:1px,color:#fff
    style D fill:#1e293b,stroke:#64748b,stroke-width:1px,color:#e2e8f0
    style D1 fill:#020617,stroke:#3f3f46,stroke-dasharray:3 3,color:#a1a1aa
    style D2 fill:#be185d,stroke:#fbcfe8,stroke-width:1px,color:#fff
    style D3 fill:#020617,stroke:#3f3f46,stroke-dasharray:3 3,color:#a1a1aa
            </pre>
        </div>
    </div>

    <!-- Crecimiento Neoclásico (Largo Plazo) -->
    <div class="bg-slate-900/80 border border-white/5 rounded-3xl p-8 shadow-xl mt-8">
        <h3 class="text-2xl font-bold text-emerald-400 mb-2">Crecimiento Neoclásico (Largo Plazo)</h3>
        <p class="text-slate-400 text-sm mb-8">La dinámica de acumulación de factores y el salto tecnológico infinito.</p>
        
        <div class="overflow-hidden rounded-xl border border-white/5 bg-slate-950/50 p-6 flex justify-center">
            <pre class="mermaid w-full flex justify-center">
flowchart LR
A["CRECIMIENTO NEOCLÁSICO"]

    A --> B["Modelo Solow-Swan"]
    B --> B1["Acumulación de Capital"]
    B --> B2["Crecimiento Poblacional (n)"]
    B1 -.-> B1a["Tasa Ahorro (s)"]
    B1 -.-> B1b["Depreciación (δ)"]
    B --> B3["Estado Estacionario"]
    B3 -.-> B3a["Regla de Oro"]

    A --> C["Modelo Ramsey"]
    C --> C1["Optimización Intertemporal"]
    C --> C2["Ecuación de Euler"]

    A --> D["Progeso Tecnológico (A)"]
    D --> D1["Exógeno (Solow)"]
    D --> D2["Endógeno (Romer)"]
    D2 -.-> D2a["I+D y Externalidades"]

    style A fill:#064e3b,stroke:#10b981,stroke-width:2px,color:#ecfdf5
    style B fill:#065f46,stroke:#34d399,stroke-width:1px,color:#d1fae5
    style B1 fill:#022c22,stroke:#047857,stroke-dasharray:3 3,color:#a7f3d0
    style B2 fill:#022c22,stroke:#047857,stroke-dasharray:3 3,color:#a7f3d0
    style B1a fill:#022c22,stroke:#047857,stroke-dasharray:3 3,color:#a7f3d0
    style B1b fill:#022c22,stroke:#047857,stroke-dasharray:3 3,color:#a7f3d0
    style B3 fill:#fbbf24,stroke:#fef3c7,stroke-width:1px,color:#78350f
    style B3a fill:#fbbf24,stroke:#fef3c7,stroke-width:1px,color:#78350f
    style C fill:#065f46,stroke:#34d399,stroke-width:1px,color:#d1fae5
    style C1 fill:#022c22,stroke:#047857,stroke-dasharray:3 3,color:#a7f3d0
    style C2 fill:#fbbf24,stroke:#fef3c7,stroke-width:1px,color:#78350f
    style D fill:#065f46,stroke:#34d399,stroke-width:1px,color:#d1fae5
    style D1 fill:#022c22,stroke:#047857,stroke-dasharray:3 3,color:#a7f3d0
    style D2 fill:#fbbf24,stroke:#fef3c7,stroke-width:1px,color:#78350f
    style D2a fill:#022c22,stroke:#047857,stroke-dasharray:3 3,color:#a7f3d0
            </pre>
        </div>
    </div>

    <!-- Microeconomía Estructural -->
    <div class="bg-slate-900/80 border border-white/5 rounded-3xl p-8 shadow-xl mt-8">
        <h3 class="text-2xl font-bold text-amber-500 mb-2">Microeconomía Estructural</h3>
        <p class="text-slate-400 text-sm mb-8">Los cimientos de la decisión y eficiencia en la asignación de recursos microeconómicos limitados.</p>
        
        <div class="overflow-hidden rounded-xl border border-white/5 bg-slate-950/50 p-6 flex justify-center">
            <pre class="mermaid w-full flex justify-center">
flowchart LR
A["MICROECONOMÍA ESTRUCTURAL"]

    A --> B["Teoría del Consumidor"]
    B --> B1["Curvas de Indiferencia"]
    B --> B2["Restricción Presupuestaria"]
    B1 -.-> B1a["Axiomas & RMS"]
    B --> B3["Efectos en Renta"]
    B3 -.-> B3a["Efecto Sustitución"]
    B3 -.-> B3b["Efecto Renta"]

    A --> C["Teoría del Productor"]
    C --> C1["Función Producción"]
    C1 -.-> C1a["Isocuantas"]
    C --> C2["Minimización Costes"]
    C2 -.-> C2a["Costo Marginal"]

    A --> D["Estructuras de Mercado"]
    D --> D1["Competencia Perfecta"]
    D1 -.-> D1a["P = CMg"]
    D --> D2["Monopolio"]
    D2 -.-> D2a["Pérdida Irrecuperable"]
    D --> D3["Oligopolio (Cournot)"]

    style A fill:#78350f,stroke:#f59e0b,stroke-width:2px,color:#fffbeb
    style B fill:#92400e,stroke:#fbbf24,stroke-width:1px,color:#fef3c7
    style B1 fill:#451a03,stroke:#b45309,stroke-dasharray:3 3,color:#fde68a
    style B2 fill:#451a03,stroke:#b45309,stroke-dasharray:3 3,color:#fde68a
    style B1a fill:#451a03,stroke:#b45309,stroke-dasharray:3 3,color:#fde68a
    style B3 fill:#92400e,stroke:#fbbf24,stroke-width:1px,color:#fef3c7
    style B3a fill:#451a03,stroke:#b45309,stroke-dasharray:3 3,color:#fde68a
    style B3b fill:#451a03,stroke:#b45309,stroke-dasharray:3 3,color:#fde68a
    style C fill:#92400e,stroke:#fbbf24,stroke-width:1px,color:#fef3c7
    style C1 fill:#451a03,stroke:#b45309,stroke-dasharray:3 3,color:#fde68a
    style C1a fill:#451a03,stroke:#b45309,stroke-dasharray:3 3,color:#fde68a
    style C2 fill:#92400e,stroke:#fbbf24,stroke-width:1px,color:#fef3c7
    style C2a fill:#451a03,stroke:#b45309,stroke-dasharray:3 3,color:#fde68a
    style D fill:#92400e,stroke:#fbbf24,stroke-width:1px,color:#fef3c7
    style D1 fill:#451a03,stroke:#b45309,stroke-dasharray:3 3,color:#fde68a
    style D1a fill:#451a03,stroke:#b45309,stroke-dasharray:3 3,color:#fde68a
    style D2 fill:#b91c1c,stroke:#fca5a5,stroke-width:1px,color:#fff
    style D2a fill:#b91c1c,stroke:#fca5a5,stroke-width:1px,color:#fff
    style D3 fill:#451a03,stroke:#b45309,stroke-dasharray:3 3,color:#fde68a
            </pre>
        </div>
    </div>

    <!-- Marxismo y Economía Política -->
    <div class="bg-slate-900/80 border border-white/5 rounded-3xl p-8 shadow-xl mt-8">
        <h3 class="text-2xl font-bold text-rose-500 mb-2">Marxismo y Economía Política</h3>
        <p class="text-slate-400 text-sm mb-8">La visión del capital como sistema de explotación, lucha de clases y crisis cíclicas inherentes.</p>
        
        <div class="overflow-hidden rounded-xl border border-white/5 bg-slate-950/50 p-6 flex justify-center">
            <pre class="mermaid w-full flex justify-center">
flowchart LR
A["MARXISMO"]

    A --> B["Estructura Base"]
    B --> B1["Modo de Producción"]
    B --> B2["Fuerzas Productivas"]
    B2 -.-> B2a["Tecnología y Materia"]
    B --> B3["Relaciones Producción"]
    B3 -.-> B3a["Propiedad Privada"]

    A --> C["Superestructura"]
    C --> C1["Estado y Leyes"]
    C --> C2["Religión y Cultura"]

    A --> D["Mecanismos del Capitalismo"]
    D --> D1["Teoría Valor Trabajo"]
    D --> D2["Plusvalía"]
    D2 -.-> D2a["Absoluta / Relativa"]
    D --> D3["Crisis Cíclicas"]

    A --> E["Agencia (Lucha Clases)"]
    E --> E1["Conciencia de Clase"]
    E --> E2["Dictadura Proletariado"]

    style A fill:#881337,stroke:#e11d48,stroke-width:2px,color:#fff1f2
    style B fill:#9f1239,stroke:#f43f5e,stroke-width:1px,color:#ffe4e6
    style B1 fill:#4c0519,stroke:#be185d,stroke-dasharray:3 3,color:#fecdd3
    style B2 fill:#4c0519,stroke:#be185d,stroke-dasharray:3 3,color:#fecdd3
    style B2a fill:#4c0519,stroke:#be185d,stroke-dasharray:3 3,color:#fecdd3
    style B3 fill:#020617,stroke:#fb7185,stroke-width:1px,color:#fff
    style B3a fill:#020617,stroke:#fb7185,stroke-width:1px,color:#fff
    style C fill:#9f1239,stroke:#f43f5e,stroke-width:1px,color:#ffe4e6
    style C1 fill:#4c0519,stroke:#be185d,stroke-dasharray:3 3,color:#fecdd3
    style C2 fill:#4c0519,stroke:#be185d,stroke-dasharray:3 3,color:#fecdd3
    style D fill:#9f1239,stroke:#f43f5e,stroke-width:1px,color:#ffe4e6
    style D1 fill:#4c0519,stroke:#be185d,stroke-dasharray:3 3,color:#fecdd3
    style D2 fill:#020617,stroke:#fb7185,stroke-width:1px,color:#fff
    style D2a fill:#020617,stroke:#fb7185,stroke-width:1px,color:#fff
    style D3 fill:#4c0519,stroke:#be185d,stroke-dasharray:3 3,color:#fecdd3
    style E fill:#9f1239,stroke:#f43f5e,stroke-width:1px,color:#ffe4e6
    style E1 fill:#4c0519,stroke:#be185d,stroke-dasharray:3 3,color:#fecdd3
    style E2 fill:#020617,stroke:#fb7185,stroke-width:1px,color:#fff
            </pre>
        </div>
    </div>

    <!-- Economía Institucional -->
    <div class="bg-slate-900/80 border border-white/5 rounded-3xl p-8 shadow-xl mt-8">
        <h3 class="text-2xl font-bold text-teal-400 mb-2">Economía Institucional</h3>
        <p class="text-slate-400 text-sm mb-8">El imperio soberano de las reglas, derechos de propiedad y asimetrías de información.</p>
        
        <div class="overflow-hidden rounded-xl border border-white/5 bg-slate-950/50 p-6 flex justify-center">
            <pre class="mermaid w-full flex justify-center">
flowchart LR
A["INSTITUCIONALISMO"]

    A --> B["Instituciones Políticas"]
    B --> B1["Inclusivas"]
    B1 -.-> B1a["Pluralismo / Límites"]
    B --> B2["Extractivas"]
    B2 -.-> B2a["Absolutismo / Elites"]

    A --> C["Instituciones Económicas"]
    C --> C1["Inclusivas"]
    C1 -.-> C1a["Propiedad / Mercados"]
    C --> C2["Extractivas"]
    C2 -.-> C2a["Monopolios / Trabajo"]

    A --> D["Conceptos Transversales"]
    D --> D1["Costos de Transacción"]
    D --> D2["Dependencia Trayectoria"]
    D --> D3["Asimetrías Información"]

    style A fill:#134e4a,stroke:#14b8a6,stroke-width:2px,color:#f0fdfa
    style B fill:#0f766e,stroke:#2dd4bf,stroke-width:1px,color:#ccfbf1
    style B1 fill:#042f2e,stroke:#0d9488,stroke-dasharray:3 3,color:#99f6e4
    style B1a fill:#042f2e,stroke:#0d9488,stroke-dasharray:3 3,color:#99f6e4
    style B2 fill:#7f1d1d,stroke:#fca5a5,stroke-width:1px,color:#fff
    style B2a fill:#7f1d1d,stroke:#fca5a5,stroke-width:1px,color:#fff
    style C fill:#0f766e,stroke:#2dd4bf,stroke-width:1px,color:#ccfbf1
    style C1 fill:#042f2e,stroke:#0d9488,stroke-dasharray:3 3,color:#99f6e4
    style C1a fill:#042f2e,stroke:#0d9488,stroke-dasharray:3 3,color:#99f6e4
    style C2 fill:#7f1d1d,stroke:#fca5a5,stroke-width:1px,color:#fff
    style C2a fill:#7f1d1d,stroke:#fca5a5,stroke-width:1px,color:#fff
    style D fill:#0f766e,stroke:#2dd4bf,stroke-width:1px,color:#ccfbf1
    style D1 fill:#042f2e,stroke:#0d9488,stroke-dasharray:3 3,color:#99f6e4
    style D2 fill:#042f2e,stroke:#0d9488,stroke-dasharray:3 3,color:#99f6e4
    style D3 fill:#042f2e,stroke:#0d9488,stroke-dasharray:3 3,color:#99f6e4
            </pre>
        </div>
    </div>

    <!-- Teoría de Juegos y Decisión Estratégica -->
    <div class="bg-slate-900/80 border border-white/5 rounded-3xl p-8 shadow-xl mt-8">
        <h3 class="text-2xl font-bold text-fuchsia-400 mb-2">Teoría de Juegos y Decisión Estratégica</h3>
        <p class="text-slate-400 text-sm mb-8">La matemática de los incentivos interactivos y los equilibrios no cooperativos.</p>
        
        <div class="overflow-hidden rounded-xl border border-white/5 bg-slate-950/50 p-6 flex justify-center">
            <pre class="mermaid w-full flex justify-center">
flowchart LR
A["TEORÍA DE JUEGOS"]

    A --> B["Componentes"]
    B --> B1["Jugadores Racionales"]
    B --> B2["Estrategias (Puras/Mixtas)"]
    B --> B3["Pagos (Payoffs)"]

    A --> C["Conceptos de Solución"]
    C --> C1["Equilibrio de Nash"]
    C1 -.-> C1a["Nadie repudia estrategia"]
    C --> C2["Estrategia Dominante/Dominada"]
    C --> C3["Inducción Hacia Atrás"]

    A --> D["Tipologías Clásicas"]
    D --> D1["Juegos Simultáneos"]
    D1 -.-> D1a["Dilema Prisionero / Gallina"]
    D --> D2["Juegos Secuenciales"]
    D2 -.-> D2a["Árboles de Decisión"]

    style A fill:#4a044e,stroke:#d946ef,stroke-width:2px,color:#fdf4ff
    style B fill:#701a75,stroke:#e879f9,stroke-width:1px,color:#fae8ff
    style B1 fill:#2e1065,stroke:#a21caf,stroke-dasharray:3 3,color:#f5d0fe
    style B2 fill:#2e1065,stroke:#a21caf,stroke-dasharray:3 3,color:#f5d0fe
    style B3 fill:#be185d,stroke:#fbcfe8,stroke-width:1px,color:#fff
    style C fill:#701a75,stroke:#e879f9,stroke-width:1px,color:#fae8ff
    style C1 fill:#be185d,stroke:#fbcfe8,stroke-width:1px,color:#fff
    style C1a fill:#2e1065,stroke:#a21caf,stroke-dasharray:3 3,color:#f5d0fe
    style C2 fill:#2e1065,stroke:#a21caf,stroke-dasharray:3 3,color:#f5d0fe
    style C3 fill:#2e1065,stroke:#a21caf,stroke-dasharray:3 3,color:#f5d0fe
    style D fill:#701a75,stroke:#e879f9,stroke-width:1px,color:#fae8ff
    style D1 fill:#2e1065,stroke:#a21caf,stroke-dasharray:3 3,color:#f5d0fe
    style D1a fill:#2e1065,stroke:#a21caf,stroke-dasharray:3 3,color:#f5d0fe
    style D2 fill:#2e1065,stroke:#a21caf,stroke-dasharray:3 3,color:#f5d0fe
    style D2a fill:#2e1065,stroke:#a21caf,stroke-dasharray:3 3,color:#f5d0fe
            </pre>
        </div>
    </div>

    <!-- Modelado Leontief y Dinámica Input-Output -->
    <div class="bg-slate-900/80 border border-white/5 rounded-3xl p-8 shadow-xl mt-8">
        <h3 class="text-2xl font-bold text-sky-400 mb-2">Modelado Leontief y Dinámica Input-Output</h3>
        <p class="text-slate-400 text-sm mb-8">Mapeo total y profundo de la red sistémica general de la producción matricial macro.</p>
        
        <div class="overflow-hidden rounded-xl border border-white/5 bg-slate-950/50 p-6 flex justify-center">
            <pre class="mermaid w-full flex justify-center">
flowchart LR
A["LEONTIEF INPUT-OUTPUT"]

    A --> B["Matriz Transacciones"]
    B --> B1["Sectores Económicos"]
    B --> B2["Flujos Intermedios"]
    B --> B3["Valor Agregado"]

    A --> C["Coeficientes Técnicos (A)"]
    C --> C1["Requerimientos Directos"]
    C --> C2["Proporciones Fijas"]

    A --> D["Ecuación Fundamental"]
    D --> D1["Producción Total (X)"]
    D --> D2["Demanda Final Exógena (D)"]
    D -.-> D3["Eq: X = AX + D"]

    A --> E["Inversa de Leontief"]
    E --> E1["Multiplicador (I-A)⁻¹"]
    E1 -.-> E1a["Impactos Indir. Infinitos"]

    style A fill:#1e3a8a,stroke:#3b82f6,stroke-width:2px,color:#eff6ff
    style B fill:#1d4ed8,stroke:#60a5fa,stroke-width:1px,color:#dbeafe
    style B1 fill:#172554,stroke:#2563eb,stroke-dasharray:3 3,color:#bfdbfe
    style B2 fill:#172554,stroke:#2563eb,stroke-dasharray:3 3,color:#bfdbfe
    style B3 fill:#0369a1,stroke:#7dd3fc,stroke-width:1px,color:#fff
    style C fill:#1d4ed8,stroke:#60a5fa,stroke-width:1px,color:#dbeafe
    style C1 fill:#172554,stroke:#2563eb,stroke-dasharray:3 3,color:#bfdbfe
    style C2 fill:#172554,stroke:#2563eb,stroke-dasharray:3 3,color:#bfdbfe
    style D fill:#1d4ed8,stroke:#60a5fa,stroke-width:1px,color:#dbeafe
    style D1 fill:#172554,stroke:#2563eb,stroke-dasharray:3 3,color:#bfdbfe
    style D2 fill:#0369a1,stroke:#7dd3fc,stroke-width:1px,color:#fff
    style D3 fill:#0369a1,stroke:#7dd3fc,stroke-width:1px,color:#fff
    style E fill:#1d4ed8,stroke:#60a5fa,stroke-width:1px,color:#dbeafe
    style E1 fill:#0369a1,stroke:#7dd3fc,stroke-width:1px,color:#fff
    style E1a fill:#172554,stroke:#2563eb,stroke-dasharray:3 3,color:#bfdbfe
            </pre>
        </div>
    </div>

    <!-- Historia del Pensamiento Económico -->
    <div class="bg-slate-900/80 border border-white/5 rounded-3xl p-8 shadow-xl mt-8">
        <h3 class="text-2xl font-bold text-orange-400 mb-2">Historia del Pensamiento Económico</h3>
        <p class="text-slate-400 text-sm mb-8">La ruta evolutiva y genealógica de todas las corrientes ideológicas de la historia.</p>
        
        <div class="overflow-hidden rounded-xl border border-white/5 bg-slate-950/50 p-6 flex justify-center">
            <pre class="mermaid w-full flex justify-center">
flowchart LR
A["HISTORIA DEL PENSAMIENTO"]

    A --> B["Preclásicos (XVI-XVIII)"]
    B --> B1["Mercantilismo"]
    B1 -.-> B1a["Suma Cero / Acumulación"]
    B --> B2["Fisiocracia"]
    B2 -.-> B2a["Laissez-Faire / Quesnay"]

    A --> C["Escuela Clásica"]
    C --> C1["Adam Smith (Mano Invisible)"]
    C --> C2["David Ricardo (Ventajas)"]
    C --> C3["Thomas Malthus"]
    C --> C4["John Stuart Mill"]

    A --> D["Rev. Marginalista (1871)"]
    D --> D1["Valor Subjetivo (Utilidad)"]
    D --> D2["Jevons / Menger / Walras"]

    A --> E["Siglo XX"]
    E --> E1["Escuela de Chicago"]
    E1 -.-> E1a["Monetarismo (Friedman)"]
    E --> E2["Nueva Macroecon. Clásica"]
    E2 -.-> E2a["Expectativas Racionales"]

    style A fill:#7c2d12,stroke:#f97316,stroke-width:2px,color:#fff7ed
    style B fill:#9a3412,stroke:#fb923c,stroke-width:1px,color:#ffedd5
    style B1 fill:#431407,stroke:#ea580c,stroke-dasharray:3 3,color:#fed7aa
    style B1a fill:#431407,stroke:#ea580c,stroke-dasharray:3 3,color:#fed7aa
    style B2 fill:#431407,stroke:#ea580c,stroke-dasharray:3 3,color:#fed7aa
    style B2a fill:#b45309,stroke:#fcd34d,stroke-width:1px,color:#fff
    style C fill:#9a3412,stroke:#fb923c,stroke-width:1px,color:#ffedd5
    style C1 fill:#b45309,stroke:#fcd34d,stroke-width:1px,color:#fff
    style C2 fill:#431407,stroke:#ea580c,stroke-dasharray:3 3,color:#fed7aa
    style C3 fill:#431407,stroke:#ea580c,stroke-dasharray:3 3,color:#fed7aa
    style C4 fill:#431407,stroke:#ea580c,stroke-dasharray:3 3,color:#fed7aa
    style D fill:#9a3412,stroke:#fb923c,stroke-width:1px,color:#ffedd5
    style D1 fill:#b45309,stroke:#fcd34d,stroke-width:1px,color:#fff
    style D2 fill:#431407,stroke:#ea580c,stroke-dasharray:3 3,color:#fed7aa
    style E fill:#9a3412,stroke:#fb923c,stroke-width:1px,color:#ffedd5
    style E1 fill:#b45309,stroke:#fcd34d,stroke-width:1px,color:#fff
    style E1a fill:#431407,stroke:#ea580c,stroke-dasharray:3 3,color:#fed7aa
    style E2 fill:#431407,stroke:#ea580c,stroke-dasharray:3 3,color:#fed7aa
    style E2a fill:#431407,stroke:#ea580c,stroke-dasharray:3 3,color:#fed7aa
            </pre>
        </div>
    </div>

</div>
</section>
