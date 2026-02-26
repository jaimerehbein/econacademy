import os

colors = {
    "blue": {"base": "blue-500", "light": "blue-400", "dark": "blue-950", "bg": "blue-500/10", "bg_hover": "blue-500/15", "border": "blue-500/20", "text": "blue-300", "gradient": "from-blue-300 to-indigo-400"},
    "emerald": {"base": "emerald-500", "light": "emerald-400", "dark": "emerald-950", "bg": "emerald-500/10", "bg_hover": "emerald-500/15", "border": "emerald-500/20", "text": "emerald-300", "gradient": "from-emerald-300 to-teal-400"},
    "amber": {"base": "amber-500", "light": "amber-400", "dark": "amber-950", "bg": "amber-500/10", "bg_hover": "amber-500/15", "border": "amber-500/20", "text": "amber-300", "gradient": "from-amber-300 to-orange-400"},
    "rose": {"base": "rose-500", "light": "rose-400", "dark": "rose-950", "bg": "rose-500/10", "bg_hover": "rose-500/15", "border": "rose-500/20", "text": "rose-300", "gradient": "from-rose-300 to-pink-400"},
    "teal": {"base": "teal-500", "light": "teal-400", "dark": "teal-950", "bg": "teal-500/10", "bg_hover": "teal-500/15", "border": "teal-500/20", "text": "teal-300", "gradient": "from-teal-300 to-cyan-400"},
    "fuchsia": {"base": "fuchsia-500", "light": "fuchsia-400", "dark": "fuchsia-950", "bg": "fuchsia-500/10", "bg_hover": "fuchsia-500/15", "border": "fuchsia-500/20", "text": "fuchsia-300", "gradient": "from-fuchsia-300 to-purple-400"},
    "cyan": {"base": "cyan-500", "light": "cyan-400", "dark": "cyan-950", "bg": "cyan-500/10", "bg_hover": "cyan-500/15", "border": "cyan-500/20", "text": "cyan-300", "gradient": "from-cyan-300 to-blue-400"},
}

modules = [
    {
        "id": "me1",
        "title": "Modelos Macroeconómicos",
        "code": "ME1",
        "color": "blue",
        "intro": "Los modelos macroeconómicos operan como laboratorios matemáticos donde ecuaciones simultáneas determinan estados estacionarios o dinámicos para el conjunto de una economía. El núcleo lógico divide la resolución del sistema dependiendo de la velocidad de ajuste de precios frente a las rigideces del mercado.",
        "diagram": """flowchart LR
    A["Macroeconomía"] --> B["Corto Plazo (Keynes)"]
    A --> C["Largo Plazo (Clásico)"]
    B --> B1["IS-LM"]
    B --> B2["OA-DA Dinámico"]
    C --> C1["Pleno Empleo"]
    C --> C2["Neutralidad Monetaria"]
    
    style A fill:#0f172a,stroke:#3b82f6,stroke-width:2px,color:#eff6ff
    style B fill:#1e293b,stroke:#64748b,stroke-width:1px,color:#e2e8f0
    style C fill:#1e293b,stroke:#64748b,stroke-width:1px,color:#e2e8f0""",
        "sections": [
            {
                "title": "El Paradigma Clásico y la Oferta",
                "text": "La piedra angular clásica postula que los mercados siempre vacían instantáneamente (precios perfectamente flexibles). La producción real ($Y$) está fijada exógenamente en el largo plazo por la función de producción y el trabajo ($L$) de pleno empleo: $Y = F(K, \\bar{L})$.",
                "math": "$$ M \\times V = P \\times Y \\implies P = \\frac{M \\cdot V}{\\bar{Y}} $$",
                "bubbles": [
                    "**Flexibilidad de precios:** El mecanismo de precios garantiza el vaciado instantáneo de todos los mercados.",
                    "**Neutralidad del dinero:** Las políticas monetarias solo afectan el nivel de precios nominales, no la producción real."
                ]
            },
            {
                "title": "Modelos Keynesianos y Rigideces (IS-LM)",
                "text": "John Maynard Keynes revolucionó el modelado al introducir fricciones nominales y rigideces salariales: los precios 'no observan' instantáneamente la cantidad de dinero. La ecuación fundamental de Demanda Agregada dicta la producción a corto plazo.",
                "math": "$$ Y = C(Y-T) + I(r) + G + NX $$",
                "bubbles": [
                    "**Curva IS (Bienes):** Representa el equilibrio donde la inversión planeada iguala al ahorro.",
                    "**Curva LM (Dinero):** Representa la preferencia por la liquidez frente a la oferta monetaria fija del banco central."
                ]
            }
        ],
        "key_points": [
            "La macroeconomía modela el agregado sistémico mediante ecuaciones de equilibrio general simplificadas.",
            "El modelo IS-LM explica las fluctuaciones de corto plazo mediante rigideces nominales.",
            "La síntesis neoclásica integra expectativas racionales y el retorno al pleno empleo."
        ]
    },
    {
        "id": "me2",
        "title": "Modelos Microeconómicos",
        "code": "ME2",
        "color": "emerald",
        "intro": "La Microeconomía modela el comportamiento individual de los agentes optimizadores (consumidores y empresas) sometidos a restricciones tangibles. Se centra en el mecanismo de fijación de precios y la asignación eficiente de recursos limitados mediante cálculo marginal.",
        "diagram": """flowchart LR
    A["Microeconomía"] --> B["Producción"]
    A --> C["Consumo"]
    B --> B1["Cobb-Douglas"]
    B --> B2["Leontief"]
    C --> C1["Maximización Utilidad"]
    C --> C2["Restricción Presupuestaria"]
    
    style A fill:#064e3b,stroke:#10b981,stroke-width:2px,color:#ecfdf5
    style B fill:#064e3b,stroke:#059669,stroke-width:1px,color:#d1fae5
    style C fill:#064e3b,stroke:#059669,stroke-width:1px,color:#d1fae5""",
        "sections": [
            {
                "title": "Topologías de la Función de Producción",
                "text": "La función de producción abstracta abstrae cómo la tecnología combina inputs físicos (Capital $K$, Trabajo $L$) para generar valor económico. El modelo de Cobb-Douglas es la especificación más utilizada debido a sus propiedades algebraicas de elasticidad de sustitución constante.",
                "math": "$$ Q = A \\cdot K^\\alpha L^\\beta $$",
                "bubbles": [
                    "**Rendimientos a Escala:** Si $\\alpha + \\beta = 1$, la firma exhibe rendimientos constantes a escala.",
                    "**Coeficientes Fijos (Leontief):** $Q = \\min (K/a, L/b)$ para procesos industriales sin sustitución."
                ]
            },
            {
                "title": "Estructuras de Fallo: Monopolio",
                "text": "La firma controla monopólicamente la variable precio reconociendo la demanda agregada inversa del mercado $P(Q)$. Esto genera una brecha ineficiente entre el precio y el costo marginal.",
                "math": "$$ \\frac{P - CMg}{P} = \\frac{1}{|\\epsilon_d|} $$",
                "bubbles": [
                    "**Índice de Lerner:** Mide el poder de mercado como el margen sobre el costo marginal.",
                    "**Pérdida de Bienestar:** El monopolio reduce el excedente total de la sociedad comparado con la competencia perfecta."
                ]
            }
        ],
        "key_points": [
            "La optimización restringida es el núcleo de las decisiones del agente representativo.",
            "Bajo competencia perfecta, los teoremas del bienestar garantizan asignaciones Pareto-eficientes.",
            "El monopolio desvía el equilibrio competitivo, forzando la intervención normativa."
        ]
    },
    {
        "id": "me3",
        "title": "Modelos de Crecimiento Económico",
        "code": "ME3",
        "color": "amber",
        "intro": "A diferencia de la Macroeconomía de fluctuaciones, los Modelos de Crecimiento trazan la expansión fundamental del nivel de producción tendencial ($Y_t$). Desplazan el horizonte temporal hacia las décadas, cuantificando la acumulación demográfica de factores físicos y el milagro del salto tecnológico.",
        "diagram": """flowchart TD
    A["Crecimiento"] --> B["Exógeno (Solow)"]
    A --> C["Endógeno (Romer/Lucas)"]
    B --> B1["Estado Estacionario"]
    B --> B2["Progreso Técnico Exógeno"]
    C --> C1["Capital Humano"]
    C --> C2["I+D y Conocimiento"]
    
    style A fill:#451a03,stroke:#f59e0b,stroke-width:2px,color:#fffbeb
    style B fill:#451a03,stroke:#d97706,stroke-width:1px,color:#fef3c7
    style C fill:#451a03,stroke:#d97706,stroke-width:1px,color:#fef3c7""",
        "sections": [
            {
                "title": "Evolución Exógena: Modelo de Solow-Swan",
                "text": "Robert Solow estructuró la primera calibración matemática del crecimiento convergente. Demostró que por culpa de los rendimientos marginales decrecientes del capital, toda acumulación física choca asintóticamente contra un muro de depreciación.",
                "math": "$$ \\dot{k} = s f(k) - (n + g + \\delta)k $$",
                "bubbles": [
                    "**Ahorro y Depreciación:** El motor temporal del crecimiento físico lucha contra la obsolescencia de las máquinas.",
                    "**Estado Estacionario:** Punto de gravedad donde $\\dot{k} = 0$, requiriendo tecnología externa para crecer."
                ]
            },
            {
                "title": "Segunda Generación: Crecimiento Endógeno",
                "text": "La Revolución Endógena de 1990 transmutó el milagro inexplicable de Solow convirtiéndolo en un producto interno voluntario. Modelaron la mente humana y las externalidades como motores inagotables.",
                "math": "$$ \\dot{H} = H_t \\cdot \\delta(1 - u) $$",
                "bubbles": [
                    "**Capital Humano:** La educación es un factor que no padece rendimientos decrecientes.",
                    "**Conocimiento:** Las ideas son bienes no rivales que permiten crecimiento perpetuo."
                ]
            }
        ],
        "key_points": [
            "Solow demostró los límites de la acumulación bruta de infraestructura física.",
            "Romer y Lucas elevaron el crecimiento al ámbito de las ideas y la educación.",
            "El crecimiento de largo plazo depende de la capacidad de innovación tecnológica."
        ]
    },
    {
        "id": "me4",
        "title": "Modelos de Desarrollo Económico",
        "code": "ME4",
        "color": "rose",
        "intro": "El desarrollo no es la simple aceleración numérica del PBI. Constituye el estudio de la maduración morfológica y la mutación estructural severa de toda la geometría productiva interna de una nación ante su integración a un mercado planetario asimétrico.",
        "diagram": """flowchart LR
    A["Desarrollo"] --> B["Estructuralismo (Prebisch)"]
    A --> C["Institucionalismo (Acemoglu)"]
    B --> B1["ISI (Proteccionismo)"]
    B --> B2["Deterioro Intercambio"]
    C --> C1["Derechos Propiedad"]
    C --> C2["Instituciones Inclusivas"]
    
    style A fill:#4c0519,stroke:#f43f5e,stroke-width:2px,color:#fff1f2
    style B fill:#4c0519,stroke:#e11d48,stroke-width:1px,color:#fff1f2
    style C fill:#4c0519,stroke:#e11d48,stroke-width:1px,color:#fff1f2""",
        "sections": [
            {
                "title": "Modelo Agroexportador y Deterioro de Intercambio",
                "text": "El modelo Centro-Periferia de Prebisch-Singer modela matemáticamente los riesgos de insertarse al mercado mundial anclado exclusivamente en materias primas.",
                "math": "$$ RTI = \\frac{P_{\\text{agro}}}{P_{\\text{industrial}}} \\rightarrow 0 $$",
                "bubbles": [
                    "**Ley de Engel:** La demanda de alimentos no crece al ritmo del ingreso mundial.",
                    "**Asimetría Tecnológica:** Los países centrales retienen las ganancias de productividad industrial."
                ]
            },
            {
                "title": "Industrialización por Sustitución (ISI)",
                "text": "La ISI buscó crear un bloque manufacturero interno mediante aranceles y subsidios. Sin embargo, chocó contra la restricción externa de escasez de divisas.",
                "math": "$$ CC = X_p - M_k \\implies \\Delta R < 0 $$",
                "bubbles": [
                    "**Estrangulamiento Externo:** Necesidad de dólares para importar bienes de capital requeridos por la propia industria.",
                    "**Eficiencia Artificial:** Industrias protegidas que no logran competir globalmente sin subsidios."
                ]
            }
        ],
        "key_points": [
            "El subdesarrollo es una falla sistémica de articulación matricial.",
            "La ISI fue el intento latinoamericano por romper la dependencia primaria.",
            "El desarrollo avanzado requiere marcos institucionales inclusivos y estables."
        ]
    },
    {
        "id": "me5",
        "title": "Modelos Estadísticos",
        "code": "ME5",
        "color": "teal",
        "intro": "Incluso la matriz teórica más sofisticada es meramente una hipótesis si no sobrevive a la colisión empírica. Los Modelos Estadísticos dotan a la economía de validación algorítmica y control sistemático paramétrico.",
        "diagram": """flowchart TD
    A["Estadística"] --> B["Regresión (MCO)"]
    A --> C["Series Temporales"]
    B --> B1["Inferencia Lineal"]
    B --> B2["Modelos Logit/Probit"]
    C --> C1["Procesos Estocásticos"]
    C --> C2["VAR y Volatilidad"]
    
    style A fill:#042f2e,stroke:#14b8a6,stroke-width:2px,color:#f0fdfa
    style B fill:#042f2e,stroke:#0d9488,stroke-width:1px,color:#ccfbf1
    style C fill:#042f2e,stroke:#0d9488,stroke-width:1px,color:#ccfbf1""",
        "sections": [
            {
                "title": "Fundamentos de Inferencia Lineal (MCO)",
                "text": "La Regresión Múltiple extrae el peso gravimétrico aislado de múltiples variables simultáneamente, permitiendo filtrar el ruido ambiental.",
                "math": "$$ \\hat{\\beta}_{MCO} = (X^T X)^{-1} X^T Y $$",
                "bubbles": [
                    "**MELI (BLUE):** Bajo ciertos axiomas, MCO es el mejor estimador lineal insesgado.",
                    "**Significancia Estadística:** Evaluación probabilística de si el efecto hallado es real o producto del azar."
                ]
            },
            {
                "title": "Estimación Discreta y Series Temporales",
                "text": "Modelamos decisiones dicotómicas (Logit) y el eco histórico de los datos temporales (Series Temporales) para predecir fluctuaciones bursátiles o sociales.",
                "math": "$$ \\sigma_t^2 = \\alpha_0 + \\alpha_1 \\varepsilon_{t-1}^2 + \\gamma \\sigma_{t-1}^2 $$",
                "bubbles": [
                    "**Arquitectura Logit:** Confinamiento de predicciones en el rango [0,1].",
                    "**GARCH:** Modelado de la volatilidad arracimada en mercados financieros."
                ]
            }
        ],
        "key_points": [
            "La econometría diferencia lo anecdótico de lo causal irrefutable.",
            "Los modelos discretos capturan la esencia de las decisiones binarias humanas.",
            "Las series temporales son el nervio central del trading algorítmico moderno."
        ]
    },
    {
        "id": "me6",
        "title": "Modelos Informáticos de Optimización",
        "code": "ME6",
        "color": "cyan",
        "intro": "Los modelos de Optimización computan normativamente el protocolo definitivo máximo matemático a seguir imperativamente por una entidad logística bajo escasez fatal de recursos.",
        "diagram": """flowchart LR
    A["Optimización"] --> B["Programación Lineal"]
    A --> C["Gestión de Inventarios"]
    B --> B1["Simplex de Dantzig"]
    B --> B2["Modelos de Transporte"]
    C --> C1["Lote Económico (EOQ)"]
    C --> C2["Just-In-Time"]
    
    style A fill:#083344,stroke:#06b6d4,stroke-width:2px,color:#ecfeff
    style B fill:#083344,stroke:#0891b2,stroke-width:1px,color:#cffafe
    style C fill:#083344,stroke:#0891b2,stroke-width:1px,color:#cffafe""",
        "sections": [
            {
                "title": "Programación Lineal y Simplex",
                "text": "Asignación de recursos (capital, horas, materiales) para maximizar beneficios o minimizar costos dentro de un polítopo de restricciones.",
                "math": "$$ \\max Z = C^T X \\quad \\text{s.t.} \\quad A X \\leq B $$",
                "bubbles": [
                    "**Frontera Viable:** El conjunto de todas las soluciones que cumplen las restricciones.",
                    "**Vértices Óptimos:** El Simplex recorre los vértices del poliedro para hallar el máximo."
                ]
            },
            {
                "title": "Modelo de Transporte e Inventarios",
                "text": "Optimización del flujo logístico desde orígenes a destinos y cálculo del lote óptimo de pedido para minimizar costos de almacenamiento.",
                "math": "$$ Q^* = \\sqrt{\\frac{2 \\cdot D \\cdot C_p}{C_h}} $$",
                "bubbles": [
                    "**Minimización de Flete:** Distribución que reduce el costo total de envío trans-fronterizo.",
                    "**Wilson (EOQ):** Equilibrio perfecto entre el costo de pedir y el costo de guardar."
                ]
            }
        ],
        "key_points": [
            "La programación lineal guía los megaproyectos logísticos mundiales.",
            "El algoritmo EOQ es el pilar de la eficiencia industrial SAP ERP.",
            "La optimización es la ventaja competitiva final en un mundo de recursos finitos."
        ]
    }
]

template = '''---
titulo: "{title}"
modulo: "{code}"
---

<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-{bg_base} rounded-full"></div>
        <span class="text-{text_color} font-black text-[10px] uppercase tracking-[0.4em]">Master en Modelos Económicos</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
        {code}
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-{bg_color} text-{text_color} border border-{border_color} px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Zero-Noise UX</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">v9.5 · {title}</span>
    </div>
</header>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">{intro}</p>

<!-- DIAGRAMA INICIAL -->
<div class="bg-slate-900/50 border border-white/5 rounded-3xl p-8 my-12 shadow-2xl relative overflow-hidden group">
    <div class="absolute top-0 right-0 p-4 opacity-20 group-hover:opacity-40 transition-opacity">
        <span class="text-4xl">📊</span>
    </div>
    <h3 class="text-xl font-bold text-white mb-6 flex items-center gap-3">
        Archivonomía Visual del Modelo
    </h3>
    <div class="overflow-hidden rounded-xl border border-white/5 bg-slate-950/50 p-6 flex justify-center">
        <pre class="mermaid w-full flex justify-center">
{diagram}
        </pre>
    </div>
</div>

{sections_html}

<div class="bg-gradient-to-br from-slate-900/90 to-black border border-{border_color} p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-{text_color} text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave del Módulo
        </h5>
        <ul class="space-y-4">
{key_points_html}
        </ul>
    </div>
</div>

</div>
'''

section_template = '''<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📌</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r {gradient} bg-clip-text text-transparent break-words leading-tight">{sec_title}</h2>
        <div class="w-10 md:w-14 h-1 bg-{bg_base} rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">{sec_text}</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto text-slate-100 font-mono">
    {sec_math}
</div>

{bubbles_html}
</section>
'''

bubble_template = '''<div class="flex items-start gap-5 p-5 bg-{bg_color} rounded-2xl my-3 border border-{border_color} hover:bg-{bg_hover} transition-all">
    <div class="bg-{bg_base} text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">{index}</div>
    <div class="text-slate-200 text-base leading-snug pt-1">{bubble_text}</div>
</div>'''

def render_module(mod):
    c = colors[mod['color']]
    
    sec_html = ""
    for idx, sec in enumerate(mod['sections']):
        bub_html = ""
        for b_idx, b in enumerate(sec['bubbles']):
            # Remove any double quotes inside bubbles to avoid HTML issues
            safe_text = b.replace('"', "'")
            bub_html += bubble_template.format(
                bg_color=c['bg'], bg_base=c['base'], border_color=c['border'], bg_hover=c['bg_hover'], index=b_idx+1, bubble_text=safe_text
            ) + "\n"
        
        sec_html += section_template.format(
            gradient=c['gradient'], sec_title=sec['title'], bg_base=c['base'], sec_text=sec['text'], sec_math=sec['math'], bubbles_html=bub_html
        )
        
    kp_html = ""
    for kp in mod['key_points']:
        kp_html += f'<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-{c["light"]} flex-shrink-0 mt-0.5 font-black">✦</span><span>{kp}</span></li>\n'
        
    return template.format(
        title=mod['title'], code=mod['code'], bg_base=c['base'], text_color=c['text'], bg_color=c['bg'], border_color=c['border'], intro=mod['intro'], diagram=mod['diagram'], sections_html=sec_html, key_points_html=kp_html
    )

for mod in modules:
    content = render_module(mod)
    with open(f"/Users/machd/Desktop/licecon/web-portal/public/program/{mod['id']}.md", "w", encoding="utf-8") as f:
        f.write(content)

