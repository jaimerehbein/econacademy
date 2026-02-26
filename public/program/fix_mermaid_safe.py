import re

with open('/Users/machd/Desktop/licecon/web-portal/public/program/map1.md', 'r') as f:
    text = f.read()

# Define the safe classDefs for each model
class_defs = {
    'KEYNESIANISMO': '''classDef root fill:#0f172a,stroke:#3b82f6,stroke-width:2px,color:#eff6ff;
    classDef main fill:#1e293b,stroke:#64748b,stroke-width:1px,color:#e2e8f0;
    classDef sub fill:#020617,stroke:#3f3f46,stroke-dasharray: 3 3,color:#a1a1aa;
    classDef alert fill:#be185d,stroke:#fbcfe8,stroke-width:1px,color:#fff;
    classDef bright fill:#0ea5e9,stroke:#bae6fd,stroke-width:1px,color:#fff;''',
    
    'CRECIMIENTO NEOCLÁSICO': '''classDef root fill:#064e3b,stroke:#10b981,stroke-width:2px,color:#ecfdf5;
    classDef main fill:#065f46,stroke:#34d399,stroke-width:1px,color:#d1fae5;
    classDef sub fill:#022c22,stroke:#047857,stroke-dasharray: 3 3,color:#a7f3d0;
    classDef highlight fill:#fbbf24,stroke:#fef3c7,stroke-width:1px,color:#78350f;''',
    
    'MICROECONOMÍA ESTRUCTURAL': '''classDef root fill:#78350f,stroke:#f59e0b,stroke-width:2px,color:#fffbeb;
    classDef main fill:#92400e,stroke:#fbbf24,stroke-width:1px,color:#fef3c7;
    classDef sub fill:#451a03,stroke:#b45309,stroke-dasharray: 3 3,color:#fde68a;
    classDef alert fill:#b91c1c,stroke:#fca5a5,stroke-width:1px,color:#fff;''',
    
    'MARXISMO': '''classDef mRoot fill:#881337,stroke:#e11d48,stroke-width:2px,color:#fff1f2;
    classDef mMain fill:#9f1239,stroke:#f43f5e,stroke-width:1px,color:#ffe4e6;
    classDef mSub fill:#4c0519,stroke:#be185d,stroke-dasharray: 3 3,color:#fecdd3;
    classDef mAlert fill:#020617,stroke:#fb7185,stroke-width:1px,color:#fff;''',
    
    'INSTITUCIONALISMO': '''classDef iRoot fill:#134e4a,stroke:#14b8a6,stroke-width:2px,color:#f0fdfa;
    classDef iMain fill:#0f766e,stroke:#2dd4bf,stroke-width:1px,color:#ccfbf1;
    classDef iSub fill:#042f2e,stroke:#0d9488,stroke-dasharray: 3 3,color:#99f6e4;
    classDef iAlert fill:#7f1d1d,stroke:#fca5a5,stroke-width:1px,color:#fff;''',
    
    'TEORÍA DE JUEGOS': '''classDef gRoot fill:#4a044e,stroke:#d946ef,stroke-width:2px,color:#fdf4ff;
    classDef gMain fill:#701a75,stroke:#e879f9,stroke-width:1px,color:#fae8ff;
    classDef gSub fill:#2e1065,stroke:#a21caf,stroke-dasharray: 3 3,color:#f5d0fe;
    classDef gBright fill:#be185d,stroke:#fbcfe8,stroke-width:1px,color:#fff;''',
    
    'LEONTIEF INPUT-OUTPUT': '''classDef lRoot fill:#1e3a8a,stroke:#3b82f6,stroke-width:2px,color:#eff6ff;
    classDef lMain fill:#1d4ed8,stroke:#60a5fa,stroke-width:1px,color:#dbeafe;
    classDef lSub fill:#172554,stroke:#2563eb,stroke-dasharray: 3 3,color:#bfdbfe;
    classDef lBright fill:#0369a1,stroke:#7dd3fc,stroke-width:1px,color:#fff;''',
    
    'HISTORIA DEL PENSAMIENTO': '''classDef hRoot fill:#7c2d12,stroke:#f97316,stroke-width:2px,color:#fff7ed;
    classDef hMain fill:#9a3412,stroke:#fb923c,stroke-width:1px,color:#ffedd5;
    classDef hSub fill:#431407,stroke:#ea580c,stroke-dasharray: 3 3,color:#fed7aa;
    classDef hHigh fill:#b45309,stroke:#fcd34d,stroke-width:1px,color:#fff;'''
}

graphs = {
    'KEYNESIANISMO': '''
    A["KEYNESIANISMO (Corto Plazo)"] :::root

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
    D --> D3["Ilusión Monetaria"] :::sub''',

    'CRECIMIENTO NEOCLÁSICO': '''
    A["CRECIMIENTO NEOCLÁSICO"] :::root

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
    D2 -.-> D2a["I+D y Externalidades"] :::sub''',

    'MICROECONOMÍA ESTRUCTURAL': '''
    A["MICROECONOMÍA ESTRUCTURAL"] :::root

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
    D --> D3["Oligopolio (Cournot)"] :::sub''',

    'MARXISMO': '''
    A["MARXISMO"] :::mRoot

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
    E --> E2["Dictadura Proletariado"] :::mAlert''',

    'INSTITUCIONALISMO': '''
    A["INSTITUCIONALISMO"] :::iRoot

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
    D --> D3["Asimetrías Información"] :::iSub''',

    'TEORÍA DE JUEGOS': '''
    A["TEORÍA DE JUEGOS"] :::gRoot

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
    D2 -.-> D2a["Árboles de Decisión"] :::gSub''',

    'LEONTIEF INPUT-OUTPUT': '''
    A["LEONTIEF INPUT-OUTPUT"] :::lRoot

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
    E1 -.-> E1a["Impactos Indir. Infinitos"] :::lSub''',

    'HISTORIA DEL PENSAMIENTO': '''
    A["HISTORIA DEL PENSAMIENTO"] :::hRoot

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
    E2 -.-> E2a["Expectativas Racionales"] :::hSub'''
}

for key, new_graph in graphs.items():
    # Find the current flowchart LR block for this key
    # It starts with flowchart LR and ends with </pre>
    pattern = r'(flowchart LR\n).*?(A\["' + key + r'".*?)(</pre>)'
    
    def replacer(match):
        header = match.group(1)
        # inject classDefs
        c_defs = class_defs[key]
        full_graph = header + '    ' + c_defs + '\n' + new_graph + '\n            ' + match.group(3)
        return full_graph
    
    text = re.sub(pattern, replacer, text, flags=re.DOTALL)

with open('/Users/machd/Desktop/licecon/web-portal/public/program/map1.md', 'w') as f:
    f.write(text)

