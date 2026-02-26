import re

with open('/Users/machd/Desktop/licecon/web-portal/public/program/map1.md', 'r') as f:
    text = f.read()

# Dictionary to replace the simple blocks with the full styled blocks
replacements = {
    # 1. Keynesianismo
    """graph LR
    %% Colors

    A((KEYNESIANISMO (Corto Plazo)))

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
    D --> D3["Ilusión Monetaria"]""": """graph LR
    classDef root fill:#0f172a,stroke:#3b82f6,stroke-width:2px,color:#eff6ff,font-weight:bold,rx:10px
    classDef main fill:#1e293b,stroke:#64748b,stroke-width:1px,color:#e2e8f0,rx:5px
    classDef sub fill:#020617,stroke:#3f3f46,stroke-dasharray: 3 3,color:#a1a1aa,rx:3px
    classDef alert fill:#be185d,stroke:#fbcfe8,stroke-width:1px,color:#fff,rx:5px
    classDef bright fill:#0ea5e9,stroke:#bae6fd,stroke-width:1px,color:#fff,rx:5px

    A(["KEYNESIANISMO<br/>(Corto Plazo)"]) :::root

    A --> B["Demanda Agregada"] :::main
    B --> B1["Consumo (C)"] :::sub
    B --> B2["Inversión (I)"] :::sub
    B --> B3["Gasto Público (G)"] :::bright

    B1 -.-> B1a["Propensión Marginal"] :::sub
    B2 -.-> B2a["Espíritus Animales"] :::sub
    B3 -.-> B3a["Multiplicador Keynesiano"] :::bright

    A --> C["Modelo IS-LM"] :::main
    C --> C1["Curva IS (Bienes)"] :::sub
    C --> C2["Curva LM (Dinero)"] :::sub
    C2 -.-> C2a["Trampa de Liquidez"] :::alert

    A --> D["Mercado Laboral"] :::main
    D --> D1["Rigidez Salarial"] :::sub
    D --> D2["Desempleo Involuntario"] :::alert
    D --> D3["Ilusión Monetaria"] :::sub""",
    
    # 2. Neoclasico
    """graph LR

    A((CRECIMIENTO NEOCLÁSICO))

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
    D2 -.-> D2a["I+D y Externalidades"]""": """graph LR
    classDef root fill:#064e3b,stroke:#10b981,stroke-width:2px,color:#ecfdf5,font-weight:bold,rx:10px
    classDef main fill:#065f46,stroke:#34d399,stroke-width:1px,color:#d1fae5,rx:5px
    classDef sub fill:#022c22,stroke:#047857,stroke-dasharray: 3 3,color:#a7f3d0,rx:3px
    classDef highlight fill:#fbbf24,stroke:#fef3c7,stroke-width:1px,color:#78350f,font-weight:bold,rx:5px

    A(["CRECIMIENTO<br/>NEOCLÁSICO"]) :::root

    A --> B["Modelo Solow-Swan"] :::main
    B --> B1["Acumulación de Capital"] :::sub
    B --> B2["Crecimiento Poblacional (n)"] :::sub
    B1 -.-> B1a["Tasa Ahorro (s)"] :::sub
    B1 -.-> B1b["Depreciación (δ)"] :::sub
    B --> B3["Estado Estacionario"] :::highlight
    B3 -.-> B3a["Regla de Oro"] :::highlight

    A --> C["Modelo Ramsey"] :::main
    C --> C1["Optimización Intertemporal"] :::sub
    C --> C2["Ecuación de Euler"] :::highlight

    A --> D["Progeso Tecnológico (A)"] :::main
    D --> D1["Exógeno (Solow)"] :::sub
    D --> D2["Endógeno (Romer)"] :::highlight
    D2 -.-> D2a["I+D y Externalidades"] :::sub""",

    # 3. Microeconomia
    """graph LR

    A((MICROECONOMÍA ESTRUCTURAL))

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
    D --> D3["Oligopolio (Cournot)"]""": """graph LR
    classDef root fill:#78350f,stroke:#f59e0b,stroke-width:2px,color:#fffbeb,font-weight:bold,rx:10px
    classDef main fill:#92400e,stroke:#fbbf24,stroke-width:1px,color:#fef3c7,rx:5px
    classDef sub fill:#451a03,stroke:#b45309,stroke-dasharray: 3 3,color:#fde68a,rx:3px
    classDef alert fill:#b91c1c,stroke:#fca5a5,stroke-width:1px,color:#fff,rx:5px

    A(["MICROECONOMÍA<br/>ESTRUCTURAL"]) :::root

    A --> B["Teoría del Consumidor"] :::main
    B --> B1["Curvas de Indiferencia"] :::sub
    B --> B2["Restricción Presupuestaria"] :::sub
    B1 -.-> B1a["Axiomas & RMS"] :::sub
    B --> B3["Efectos en Renta"] :::main
    B3 -.-> B3a["Efecto Sustitución"] :::sub
    B3 -.-> B3b["Efecto Renta"] :::sub

    A --> C["Teoría del Productor"] :::main
    C --> C1["Función Producción"] :::sub
    C1 -.-> C1a["Isocuantas"] :::sub
    C --> C2["Minimización Costes"] :::main
    C2 -.-> C2a["Costo Marginal"] :::sub

    A --> D["Estructuras de Mercado"] :::main
    D --> D1["Competencia Perfecta"] :::sub
    D1 -.-> D1a["P = CMg"] :::sub
    D --> D2["Monopolio"] :::alert
    D2 -.-> D2a["Pérdida Irrecuperable"] :::alert
    D --> D3["Oligopolio (Cournot)"] :::sub""",
    
    # 4. Marxismo
    """graph LR

    A((MARXISMO))

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
    E --> E2["Dictadura Proletariado"]""": """graph LR
    classDef mRoot fill:#881337,stroke:#e11d48,stroke-width:2px,color:#fff1f2,font-weight:bold,rx:10px
    classDef mMain fill:#9f1239,stroke:#f43f5e,stroke-width:1px,color:#ffe4e6,rx:5px
    classDef mSub fill:#4c0519,stroke:#be185d,stroke-dasharray: 3 3,color:#fecdd3,rx:3px
    classDef mAlert fill:#020617,stroke:#fb7185,stroke-width:1px,color:#fff,rx:5px

    A(["MARXISMO"]) :::mRoot

    A --> B["Estructura Base"] :::mMain
    B --> B1["Modo de Producción"] :::mSub
    B --> B2["Fuerzas Productivas"] :::mSub
    B2 -.-> B2a["Tecnología y Materia"] :::mSub
    B --> B3["Relaciones Producción"] :::mAlert
    B3 -.-> B3a["Propiedad Privada"] :::mAlert

    A --> C["Superestructura"] :::mMain
    C --> C1["Estado y Leyes"] :::mSub
    C --> C2["Religión y Cultura"] :::mSub

    A --> D["Mecanismos del Capitalismo"] :::mMain
    D --> D1["Teoría Valor Trabajo"] :::mSub
    D --> D2["Plusvalía"] :::mAlert
    D2 -.-> D2a["Absoluta / Relativa"] :::mAlert
    D --> D3["Crisis Cíclicas"] :::mSub

    A --> E["Agencia (Lucha Clases)"] :::mMain
    E --> E1["Conciencia de Clase"] :::mSub
    E --> E2["Dictadura Proletariado"] :::mAlert""",
    
    # 5. Institucionalismo
    """graph LR

    A((INSTITUCIONALISMO))

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
    D --> D3["Asimetrías Información"]""": """graph LR
    classDef iRoot fill:#134e4a,stroke:#14b8a6,stroke-width:2px,color:#f0fdfa,font-weight:bold,rx:10px
    classDef iMain fill:#0f766e,stroke:#2dd4bf,stroke-width:1px,color:#ccfbf1,rx:5px
    classDef iSub fill:#042f2e,stroke:#0d9488,stroke-dasharray: 3 3,color:#99f6e4,rx:3px
    classDef iAlert fill:#7f1d1d,stroke:#fca5a5,stroke-width:1px,color:#fff,rx:5px

    A(["INSTITUCIONALISMO"]) :::iRoot

    A --> B["Instituciones Políticas"] :::iMain
    B --> B1["Inclusivas"] :::iSub
    B1 -.-> B1a["Pluralismo / Límites"] :::iSub
    B --> B2["Extractivas"] :::iAlert
    B2 -.-> B2a["Absolutismo / Elites"] :::iAlert

    A --> C["Instituciones Económicas"] :::iMain
    C --> C1["Inclusivas"] :::iSub
    C1 -.-> C1a["Propiedad / Mercados"] :::iSub
    C --> C2["Extractivas"] :::iAlert
    C2 -.-> C2a["Monopolios / Trabajo"] :::iAlert

    A --> D["Conceptos Transversales"] :::iMain
    D --> D1["Costos de Transacción"] :::iSub
    D --> D2["Dependencia Trayectoria"] :::iSub
    D --> D3["Asimetrías Información"] :::iSub""",
    
    # 6. Juegos
    """graph LR

    A((TEORÍA DE JUEGOS))

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
    D2 -.-> D2a["Árboles de Decisión"]""": """graph LR
    classDef gRoot fill:#4a044e,stroke:#d946ef,stroke-width:2px,color:#fdf4ff,font-weight:bold,rx:10px
    classDef gMain fill:#701a75,stroke:#e879f9,stroke-width:1px,color:#fae8ff,rx:5px
    classDef gSub fill:#2e1065,stroke:#a21caf,stroke-dasharray: 3 3,color:#f5d0fe,rx:3px
    classDef gBright fill:#be185d,stroke:#fbcfe8,stroke-width:1px,color:#fff,rx:5px

    A(["TEORÍA DE JUEGOS"]) :::gRoot

    A --> B["Componentes"] :::gMain
    B --> B1["Jugadores Racionales"] :::gSub
    B --> B2["Estrategias (Puras/Mixtas)"] :::gSub
    B --> B3["Pagos (Payoffs)"] :::gBright

    A --> C["Conceptos de Solución"] :::gMain
    C --> C1["Equilibrio de Nash"] :::gBright
    C1 -.-> C1a["Nadie repudia estrategia"] :::gSub
    C --> C2["Estrategia Dominante/Dominada"] :::gSub
    C --> C3["Inducción Hacia Atrás"] :::gSub

    A --> D["Tipologías Clásicas"] :::gMain
    D --> D1["Juegos Simultáneos"] :::gSub
    D1 -.-> D1a["Dilema Prisionero / Gallina"] :::gSub
    D --> D2["Juegos Secuenciales"] :::gSub
    D2 -.-> D2a["Árboles de Decisión"] :::gSub""",

    # 7. Leontief
    """graph LR

    A((LEONTIEF INPUT-OUTPUT))

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
    E1 -.-> E1a["Impactos Indir. Infinitos"]""": """graph LR
    classDef lRoot fill:#1e3a8a,stroke:#3b82f6,stroke-width:2px,color:#eff6ff,font-weight:bold,rx:10px
    classDef lMain fill:#1d4ed8,stroke:#60a5fa,stroke-width:1px,color:#dbeafe,rx:5px
    classDef lSub fill:#172554,stroke:#2563eb,stroke-dasharray: 3 3,color:#bfdbfe,rx:3px
    classDef lBright fill:#0369a1,stroke:#7dd3fc,stroke-width:1px,color:#fff,rx:5px

    A(["LEONTIEF<br/>INPUT-OUTPUT"]) :::lRoot

    A --> B["Matriz Transacciones"] :::lMain
    B --> B1["Sectores Económicos"] :::lSub
    B --> B2["Flujos Intermedios"] :::lSub
    B --> B3["Valor Agregado"] :::lBright

    A --> C["Coeficientes Técnicos (A)"] :::lMain
    C --> C1["Requerimientos Directos"] :::lSub
    C --> C2["Proporciones Fijas"] :::lSub

    A --> D["Ecuación Fundamental"] :::lMain
    D --> D1["Producción Total (X)"] :::lSub
    D --> D2["Demanda Final Exógena (D)"] :::lBright
    D -.-> D3["Eq: X = AX + D"] :::lBright

    A --> E["Inversa de Leontief"] :::lMain
    E --> E1["Multiplicador (I-A)⁻¹"] :::lBright
    E1 -.-> E1a["Impactos Indir. Infinitos"] :::lSub""",

    # 8. Pensamiento
    """graph LR

    A((HISTORIA DEL PENSAMIENTO))

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
    E2 -.-> E2a["Expectativas Racionales"]""": """graph LR
    classDef hRoot fill:#7c2d12,stroke:#f97316,stroke-width:2px,color:#fff7ed,font-weight:bold,rx:10px
    classDef hMain fill:#9a3412,stroke:#fb923c,stroke-width:1px,color:#ffedd5,rx:5px
    classDef hSub fill:#431407,stroke:#ea580c,stroke-dasharray: 3 3,color:#fed7aa,rx:3px
    classDef hHigh fill:#b45309,stroke:#fcd34d,stroke-width:1px,color:#fff,rx:5px

    A(["HISTORIA DEL<br/>PENSAMIENTO"]) :::hRoot

    A --> B["Preclásicos (XVI-XVIII)"] :::hMain
    B --> B1["Mercantilismo"] :::hSub
    B1 -.-> B1a["Suma Cero / Acumulación"] :::hSub
    B --> B2["Fisiocracia"] :::hSub
    B2 -.-> B2a["Laissez-Faire / Quesnay"] :::hHigh

    A --> C["Escuela Clásica"] :::hMain
    C --> C1["Adam Smith (Mano Invisible)"] :::hHigh
    C --> C2["David Ricardo (Ventajas)"] :::hSub
    C --> C3["Thomas Malthus"] :::hSub
    C --> C4["John Stuart Mill"] :::hSub

    A --> D["Rev. Marginalista (1871)"] :::hMain
    D --> D1["Valor Subjetivo (Utilidad)"] :::hHigh
    D --> D2["Jevons / Menger / Walras"] :::hSub

    A --> E["Siglo XX"] :::hMain
    E --> E1["Escuela de Chicago"] :::hHigh
    E1 -.-> E1a["Monetarismo (Friedman)"] :::hSub
    E --> E2["Nueva Macroecon. Clásica"] :::hSub
    E2 -.-> E2a["Expectativas Racionales"] :::hSub"""
}

# Apply all replacements
for search_text, replacement in replacements.items():
    if search_text in text:
        text = text.replace(search_text, replacement)
    else:
        print(f"Warning: Could not find exactly: {search_text[:30]}...")

with open('/Users/machd/Desktop/licecon/web-portal/public/program/map1.md', 'w') as f:
    f.write(text)

print("Done.")

