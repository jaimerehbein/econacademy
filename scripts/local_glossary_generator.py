"""
local_glossary_generator.py
============================
Generates Zero-Noise v9.5 glossaries for ALL pending .md modules 
WITHOUT any external API.

Strategy:
  1. Read each module file
  2. Extract key terms from: <h2> section titles, **bold** spans, and content
  3. Build contextual definitions from surrounding sentences
  4. Inject v9.5 HTML template

Runs in seconds. Free. No rate limits.
"""

import os, re, sys

TARGET_DIR = "/Users/machd/Desktop/licecon/web-portal/public/program"

# ── v9.5 Templates ────────────────────────────────────────────────────────────
SECTION_TPL = """\
<!-- GLOSARIO v9.5 -->
<section id="glosario" class="mt-24 mb-16 relative">
    <div class="flex items-center gap-4 mb-10">
        <div class="w-1.5 h-8 bg-{color}-500 rounded-full"></div>
        <h2 class="text-2xl font-black text-white tracking-tight uppercase italic">Glosario Técnico</h2>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 relative z-10">
{items}
    </div>
</section>"""

ITEM_TPL = """\
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-{color}-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-{color}-500/5">
            <h3 class="text-sm font-black text-{color}-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-{color}-500 animate-pulse"></span>
                {term}
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                {definition}
            </p>
        </div>"""

# ── Economics Knowledge Base ─────────────────────────────────────────────────
# Comprehensive definitions for common economics terms across all series.
ECON_DEFINITIONS = {
    # Microeconomía
    "oferta": "Cantidad de un bien o servicio que los productores están dispuestos y son capaces de ofrecer al mercado a distintos niveles de precio, manteniendo constantes los demás factores.",
    "demanda": "Cantidad de un bien o servicio que los consumidores desean y pueden adquirir en un período determinado a diferentes niveles de precio, dado su ingreso y preferencias.",
    "equilibrio de mercado": "Situación en la que la cantidad ofrecida y la cantidad demandada de un bien coinciden, determinando un precio que vacía el mercado sin excedentes ni escaseces.",
    "elasticidad precio": "Medida de la sensibilidad de la cantidad demandada u ofrecida ante cambios en el precio, expresada como el cociente entre la variación porcentual de la cantidad y la del precio.",
    "excedente del consumidor": "Diferencia entre el precio máximo que un consumidor estaría dispuesto a pagar por un bien y el precio de mercado que efectivamente paga, representando un beneficio neto.",
    "excedente del productor": "Diferencia entre el precio de mercado recibido por un productor y el costo marginal de producción, representando la ganancia adicional obtenida sobre el mínimo aceptable.",
    "elasticidad": "Medida de la capacidad de respuesta de una variable económica ante cambios en otra, utilizada para cuantificar la sensibilidad de la demanda o la oferta a variaciones de precio.",
    "utilidad marginal": "Satisfacción adicional que obtiene un consumidor al consumir una unidad extra de un bien, la cual tiende a disminuir conforme aumenta el consumo (ley de utilidad marginal decreciente).",
    "costo marginal": "Incremento en el costo total de producción causado por la producción de una unidad adicional de un bien o servicio; parámetro clave para las decisiones de maximización de ganancias.",
    "competencia perfecta": "Estructura de mercado caracterizada por numerosos compradores y vendedores, productos homogéneos, libre entrada y salida, e información perfecta, donde ningún agente influye en el precio.",
    "monopolio": "Estructura de mercado en la que un único productor controla la oferta total de un bien sin sustitutos cercanos, ejerciendo poder de mercado para fijar precios por encima del costo marginal.",
    "oligopolio": "Estructura de mercado dominada por un pequeño número de empresas con poder de influir en los precios y cuya estrategia óptima depende del comportamiento esperado de sus rivales.",
    "externalidad": "Efecto secundario de la actividad económica de un agente sobre el bienestar de terceros que no participa en la transacción, pudiendo ser positiva (beneficio) o negativa (perjuicio).",
    "bien público": "Bien caracterizado por ser no rival (su consumo por una persona no reduce su disponibilidad) y no excluyente (no se puede excluir a nadie de su consumo), generando fallas de mercado.",
    "información asimétrica": "Situación en la que una de las partes de una transacción posee más información relevante que la otra, pudiendo generar selección adversa, riesgo moral e ineficiencias de mercado.",
    "teoría del consumidor": "Marco analítico que estudia cómo los individuos asignan su ingreso limitado entre bienes y servicios para maximizar su utilidad, sujeto a restricciones presupuestarias y de precios.",
    "restricción presupuestaria": "Conjunto de combinaciones de bienes que un consumidor puede adquirir dado su ingreso disponible y los precios de mercado, delimitando el espacio de elección factible.",
    "curva de indiferencia": "Lugar geométrico de todas las combinaciones de bienes que proporcionan al consumidor el mismo nivel de satisfacción o utilidad, con pendiente negativa y convexa al origen.",
    "producción a largo plazo": "Período en el que todos los factores de producción son variables, permitiendo a la empresa ajustar su escala productiva y explotar economías o deseconomías de escala.",
    "función de producción": "Relación tecnológica que describe la cantidad máxima de producto que puede obtenerse a partir de distintas combinaciones de insumos, dado el estado actual de la tecnología.",
    # Macroeconomía
    "pib": "Valor total de mercado de todos los bienes y servicios finales producidos en un país durante un período determinado, utilizado como medida principal del tamaño y crecimiento económico.",
    "producto interno bruto": "Suma del valor agregado generado por todos los sectores de la economía en un territorio geográfico específico durante un año, medido a precios de mercado o a costo de factores.",
    "inflación": "Aumento sostenido y generalizado del nivel de precios de una economía, que erosiona el poder adquisitivo del dinero y redistribuye riqueza entre sectores deudores y acreedores.",
    "deflación": "Caída generalizada y persistente del nivel de precios, que puede inducir espirales depresivas al incrementar la carga real de deudas y postergar decisiones de consumo e inversión.",
    "política monetaria": "Conjunto de acciones del banco central orientadas a controlar la oferta monetaria y las tasas de interés para alcanzar objetivos macroeconómicos de estabilidad de precios y empleo.",
    "política fiscal": "Instrumento gubernamental que utiliza el gasto público y los impuestos para influir en la demanda agregada, el ciclo económico, la distribución del ingreso y la provisión de bienes públicos.",
    "tasa de interés": "Precio del dinero en el tiempo, expresado como porcentaje del capital prestado, que iguala la oferta y demanda de fondos prestables y señaliza las condiciones monetarias de la economía.",
    "desempleo": "Situación en la que personas en edad y disposición de trabajar no encuentran empleo remunerado. Incluye componentes friccional, estructural y cíclico según sus causas subyacentes.",
    "banco central": "Institución pública responsable de la emisión de moneda, la regulación del sistema financiero, la implementación de la política monetaria y el mantenimiento de la estabilidad macroeconómica.",
    "multiplicador keynesiano": "Coeficiente que indica el aumento total del PIB generado por una variación unitaria del gasto autónomo, amplificado a través de sucesivas rondas de consumo e ingreso.",
    "curva is-lm": "Modelo macroeconómico que integra el equilibrio del mercado de bienes (IS) y el mercado de dinero (LM) para determinar simultáneamente el ingreso y la tasa de interés de equilibrio.",
    "balanza de pagos": "Registro contable de todas las transacciones económicas entre residentes de un país y el resto del mundo, incluyendo cuenta corriente, cuenta de capital y cuenta financiera.",
    "tipo de cambio": "Precio al que se intercambia la moneda de un país por la de otro, determinado en mercados de divisas y condicionado por diferenciales de inflación, tasas de interés y expectativas.",
    "crecimiento económico": "Aumento sostenido de la capacidad productiva de una economía, medido por el incremento del PIB real per cápita y determinado por acumulación de capital, trabajo y progreso técnico.",
    "ciclo económico": "Fluctuación recurrente de la actividad económica en torno a su tendencia de largo plazo, caracterizada por fases de expansión, auge, contracción y recuperación.",
    "demanda agregada": "Suma de todos los gastos planificados en bienes y servicios finales en una economía: consumo privado, inversión, gasto gubernamental y exportaciones netas.",
    "oferta agregada": "Producción total de bienes y servicios que las empresas de una economía están dispuestas a ofrecer a distintos niveles de precios, en el corto y largo plazo.",
    # Economía Política / Institucional
    "estado": "Conjunto de instituciones que ejercen autoridad soberana sobre un territorio y una población, dotado del monopolio legítimo de la coerción para hacer cumplir normas y garantizar derechos.",
    "fallo de mercado": "Situación en la que el mercado libre no asigna recursos de manera eficiente, justificando la intervención pública mediante regulación, impuestos o provisión directa de bienes.",
    "renta económica": "Ingreso percibido por un factor de producción en exceso de su costo de oportunidad o de transferencia; en tierra, es el pago a un factor de oferta fija determinado exclusivamente por la demanda.",
    "poder de mercado": "Capacidad de una empresa para influir unilateralmente en el precio del mercado o en las condiciones de transacción, derivada de su posición dominante o de diferenciación de producto.",
    "regulación económica": "Intervención gubernamental que establece reglas sobre precios, calidad, entrada y conducta en mercados con fallas, buscando corregir ineficiencias sin suprimir los incentivos privados.",
    "derechos de propiedad": "Sistema de reglas legales e institucionales que define quién puede usar, excluir y beneficiarse de los recursos económicos, constituyendo el fundamento de la economía de mercado.",
    "capital humano": "Conjunto acumulado de conocimientos, habilidades, experiencias y capacidades productivas incorporadas en los trabajadores, resultado de la inversión en educación, formación y salud.",
    "ventaja comparativa": "Principio según el cual un agente debe especializarse en producir los bienes que puede producir a un menor costo de oportunidad relativo, aunque no tenga ventaja absoluta en ninguno.",
    "libre comercio": "Régimen de intercambio internacional en el que los países no imponen barreras arancelarias ni no arancelarias, permitiendo que el comercio fluya de acuerdo con ventajas comparativas.",
    "proteccionismo": "Política económica que restringe las importaciones mediante aranceles, cuotas y subsidios para proteger industrias domésticas, incurriendo en costos de eficiencia para la economía.",
    "globalización": "Proceso de integración económica, política, cultural y tecnológica entre países, caracterizado por el aumento del comercio, la inversión extranjera y la movilidad de factores.",
    "imperialismo": "Extensión del poder económico y político de un Estado sobre otros territorios o economías mediante control financiero, comercial o político, a menudo asociado al capitalismo tardío.",
    "plusvalía": "En la teoría marxista, diferencia entre el valor producido por el trabajo y el salario pagado al trabajador, apropiada por el capitalista como fuente de ganancia y acumulación de capital.",
    "modo de producción": "Concepto marxista que integra las fuerzas productivas (tecnología, recursos) y las relaciones de producción (propiedad, clase) para caracterizar las bases económicas de una sociedad.",
    "mercado de trabajo": "Espacio institucional donde se determinan el nivel de empleo y el salario de equilibrio mediante la interacción entre la oferta de trabajo de los hogares y la demanda de las empresas.",
    # Economía Básica / Conceptos Fundamentales
    "escasez": "Condición fundamental de la economía donde los recursos disponibles son insuficientes para satisfacer todos los deseos y necesidades de los individuos, obligando a elegir y priorizar.",
    "costo de oportunidad": "Valor de la mejor alternativa a la que se renuncia al tomar una decisión económica, representando el verdadero costo de cualquier elección en un mundo de recursos escasos.",
    "ventaja absoluta": "Capacidad de un individuo, empresa o país para producir un bien utilizando menos recursos (o en menos tiempo) que otro agente, independientemente de las ventajas comparativas.",
    "incentivos": "Señales económicas que alteran el costo-beneficio de las acciones de los agentes, influyendo en sus decisiones de consumo, producción, ahorro e inversión mediante precios y normas.",
    "señales de precios": "Información transmitida por los precios de mercado que coordina las decisiones descentralizadas de millones de agentes sin necesidad de planificación central, asignando recursos eficientemente.",
    "eficiencia económica": "Estado en el que los recursos se asignan de manera que maximizan el bienestar agregado, sin que sea posible mejorar la situación de alguien sin empeorar la de otro (optimalidad de Pareto).",
    "fallo del gobierno": "Situación en la que la intervención gubernamental genera ineficiencias más costosas que los fallos de mercado que pretende corregir, debido a información imperfecta, captura regulatoria o incentivos perversos.",
    "salario mínimo": "Precio mínimo legalmente establecido para el trabajo, cuyo efecto en el empleo depende de si se fija por encima del salario de mercado competitivo, pudiendo generar desempleo involuntario.",
    "control de precios": "Regulación gubernamental que fija precios máximos (techo) o mínimos (piso) en mercados específicos, generando escaseces o excedentes cuando se alejan del equilibrio de mercado.",
    "subsidio": "Pago del gobierno a productores o consumidores que reduce el precio efectivo de un bien o servicio, alterando las señales de precios y potencialmente generando sobreproducción e ineficiencias.",
    # Modelos Económicos
    "modelo de crecimiento de solow": "Marco teórico que explica el crecimiento económico de largo plazo mediante la acumulación de capital físico, el crecimiento poblacional y el progreso tecnológico exógeno.",
    "estado estacionario": "Punto de equilibrio de largo plazo en modelos de crecimiento donde el capital per cápita, el producto per cápita y el consumo per cápita permanecen constantes en el tiempo.",
    "función de producción cobb-douglas": "Forma funcional ampliamente utilizada en economía que expresa el producto como una función de capital y trabajo con elasticidades constantes, con propiedades de rendimientos constantes a escala.",
    "convergencia económica": "Tendencia de las economías menos desarrolladas a crecer más rápido que las economías ricas y acortar las brechas de ingreso per cápita, predicha por el modelo neoclásico de crecimiento.",
    "ahorro e inversión": "En equilibrio macroeconómico, el ahorro nacional financia la inversión doméstica y el déficit externo; su igualdad determina la acumulación de capital y el crecimiento de largo plazo.",
    "productividad total de los factores": "Componente del crecimiento económico no explicado por la acumulación de capital y trabajo, que captura la eficiencia global con que se combinan los insumos, incluyendo el cambio tecnológico.",
    "tecnología endógena": "Enfoque de crecimiento donde el progreso técnico resulta de decisiones optimizadoras de los agentes (I+D), generando rendimientos crecientes y explicando divergencia persistente entre países.",
    "capital físico": "Conjunto de bienes duraderos producidos por el hombre —maquinaria, edificios, infraestructura— que aumentan la productividad del trabajo y se acumulan mediante la inversión neta.",
    "depreciación": "Disminución del valor o capacidad productiva del capital físico debido al uso, obsolescencia tecnológica o deterioro natural, que debe compensarse con nueva inversión para mantener el stock.",
    "rendimientos decrecientes al capital": "Propiedad por la que cada unidad adicional de capital añade menos producto que la anterior dado el trabajo constante, implicando que economías con menos capital crecen más rápido.",
    # Ingeniería Financiera
    "valor presente": "Valor actual de un flujo de efectivo futuro, descontado a una tasa de interés que refleja el costo de oportunidad del capital y el riesgo, base de toda valoración financiera.",
    "tasa interna de retorno": "Tasa de descuento que hace que el valor presente neto de todos los flujos de caja de un proyecto sea igual a cero; criterio de aceptación comparado con el costo de capital.",
    "derivado financiero": "Instrumento cuyo valor depende del precio de un activo subyacente (acción, bono, divisa, commodity), utilizado para cobertura de riesgos (hedging) o especulación.",
    "opciones financieras": "Contratos que otorgan al comprador el derecho, pero no la obligación, de comprar (call) o vender (put) un activo a un precio fijo (strike price) antes o en una fecha determinada.",
    "modelo de black-scholes": "Fórmula matemática para valorar opciones europeas sobre acciones que no pagan dividendos, derivada bajo supuestos de movimiento browniano geométrico y mercados completos.",
    "gestión de riesgos": "Proceso sistemático de identificación, medición, control y mitigación de los riesgos financieros a los que está expuesta una institución o portafolio de inversiones.",
    "valor en riesgo (var)": "Medida estadística que cuantifica la pérdida máxima esperada de un portafolio con un nivel de confianza dado durante un horizonte temporal específico.",
    "arbitraje": "Operación financiera que consiste en aprovechar diferencias de precio del mismo activo en mercados distintos, obteniendo una ganancia libre de riesgo y contribuyendo a la eficiencia de mercado.",
    "apalancamiento financiero": "Uso de deuda para amplificar los rendimientos sobre el capital propio, incrementando tanto las ganancias potenciales como las pérdidas y el riesgo financiero de la entidad.",
    "curva de rendimiento": "Representación gráfica de los tipos de interés de bonos del mismo emisor con diferentes vencimientos, cuya forma (normal, invertida, plana) señaliza expectativas económicas futuras.",
    "martingala": "Proceso estocástico en el que el valor esperado futuro, condicionado a la historia pasada, es igual al valor presente, modelando mercados financieros eficientes donde los precios siguen caminatas aleatorias.",
    "movimiento browniano": "Proceso estocástico de tiempo continuo con incrementos independientes y normalmente distribuidos, utilizado para modelar la evolución de precios de activos financieros en tiempo continuo.",
    "cobertura delta": "Estrategia de cobertura que ajusta dinámicamente la posición en el activo subyacente para neutralizar el riesgo de precio de una cartera de opciones, llevando el delta a cero.",
    "swap": "Contrato financiero mediante el cual dos partes acuerdan intercambiar flujos de efectivo futuros según reglas predefinidas, usualmente tasas fijas vs variables o divisas distintas.",
    "tasa libre de riesgo": "Rendimiento teórico de una inversión sin posibilidad de pérdida, usualmente aproximada por los bonos del Tesoro, que sirve de referencia mínima para evaluar cualquier inversión riesgosa.",
    # Serie A - Licenciatura Economía
    "administración de empresas": "Disciplina que estudia la organización y gestión eficiente de recursos humanos, financieros y materiales en las organizaciones para alcanzar sus objetivos estratégicos.",
    "contabilidad": "Sistema de registro, clasificación y síntesis de las transacciones económicas de una entidad para elaborar información financiera útil para la toma de decisiones.",
    "estadística económica": "Aplicación de métodos estadísticos al análisis de datos económicos para identificar patrones, probar hipótesis y fundamentar conclusiones sobre fenómenos económicos observables.",
    "econometría": "Disciplina que combina teoría económica, matemáticas y estadística para cuantificar relaciones económicas, contrastar hipótesis y elaborar predicciones a partir de datos empíricos.",
    "mercadotecnia": "Conjunto de herramientas y estrategias orientadas a identificar necesidades del consumidor y crear valor diferencial para satisfacerlas de forma rentable y sostenible.",
    "derecho económico": "Rama del ordenamiento jurídico que regula la actividad económica privada y pública, estableciendo las reglas del mercado, la competencia y las relaciones entre agentes económicos.",
    "historia del pensamiento económico": "Estudio cronológico y analítico de las principales corrientes, teorías y autores que han conformado la ciencia económica desde la Antigüedad hasta la actualidad.",
    "macroeconomía aplicada": "Aplicación de modelos y herramientas macroeconómicas para analizar y proyectar variables como el PIB, inflación, desempleo y balanza de pagos en contextos económicos reales.",
    "microeconomía aplicada": "Uso de la teoría microeconómica para analizar comportamientos de mercados específicos, efectos de políticas y decisiones de agentes en contextos empíricos concretos.",
    "economía internacional": "Rama que estudia el comercio y las finanzas entre naciones, las causas de la especialización productiva, los determinantes de los flujos de capital y las políticas comerciales.",
    "sociología económica": "Disciplina que estudia la influencia de los factores sociales, culturales e institucionales en el comportamiento económico, más allá de los supuestos del agente racional.",
    "política económica": "Conjunto de medidas que adoptan los gobiernos para influir en la economía mediante instrumentos fiscales, monetarios, comerciales y regulatorios con el fin de alcanzar objetivos socioeconómicos.",
    "economía del bienestar": "Rama normativa de la economía que estudia cómo evaluar y mejorar el bienestar social, haciendo uso de criterios como la eficiencia de Pareto y las funciones de bienestar social.",
    "rsc y deontología": "Responsabilidad Social Corporativa y ética empresarial: marco normativo que orienta la conducta de las empresas para integrar criterios sociales, ambientales y de gobernanza en sus operaciones.",
    "finanzas internacionales": "Estudio de los mercados financieros globales, los flujos de capital entre países, la gestión del riesgo cambiario y la arquitectura del sistema monetario internacional.",
    "gestión de riesgos financieros": "Proceso de identificar, medir y mitigar las exposiciones a riesgos de mercado, crédito, liquidez y operacional en portafolios e instituciones financieras.",
    "organismos internacionales": "Instituciones supranacionales —FMI, Banco Mundial, OMC, ONU— que coordinan la cooperación económica internacional y establecen normas para el comercio y las finanzas globales.",
    "historia económica": "Estudio del desenvolvimiento de los sistemas económicos a través del tiempo, utilizando fuentes históricas y métodos cuantitativos para explicar el desarrollo y la divergencia entre naciones.",
    "comercio internacional": "Intercambio de bienes y servicios a través de las fronteras nacionales, regulado por acuerdos multilaterales y determinado por ventajas comparativas, costos de transporte y políticas comerciales.",
    "fiscalidad internacional": "Conjunto de normas tributarias que regulan la imposición de ingresos y actividades con dimensión transfronteriza, abordando problemas de doble imposición, elusión y precios de transferencia.",
}

# ── Color extraction ──────────────────────────────────────────────────────────
def detect_color(content):
    for pat in [r'from-(\w+)-[39]00', r'bg-(\w+)-500', r'text-(\w+)-[45]00']:
        m = re.search(pat, content)
        if m and m.group(1) not in ('white','slate','gray','black'):
            return m.group(1)
    return "indigo"

# ── Term extraction ───────────────────────────────────────────────────────────
def extract_terms_from_content(content, filename):
    """
    Extract candidate terms from a module file using multiple strategies.
    Returns list of (term, definition) pairs.
    """
    terms = []
    seen = set()

    # Strategy 1: Section titles from <h2> tags (primary concepts of module)
    h2_titles = re.findall(r'<h2[^>]*>\s*(?:\d+\.\s*)?(.*?)\s*</h2>', content, re.IGNORECASE)
    for t in h2_titles:
        clean = re.sub(r'<[^>]+>', '', t).strip()
        clean = re.sub(r'^\d+\.\s*', '', clean).strip()
        if 2 < len(clean) < 50 and clean.lower() not in seen:
            seen.add(clean.lower())
            terms.append(clean)

    # Strategy 2: Bold markdown spans **term**
    bold_terms = re.findall(r'\*\*([A-ZÁÉÍÓÚÑ][^*]{3,40}?)\*\*', content)
    for t in bold_terms:
        t = t.strip()
        if t.lower() not in seen and len(t) > 3:
            seen.add(t.lower())
            terms.append(t)

    # Strategy 3: Key economic vocabulary from the knowledge base
    text_lower = content.lower()
    for key in ECON_DEFINITIONS:
        if key in text_lower and key not in seen:
            seen.add(key)
            terms.append(key.title())

    return terms[:12]  # take up to 12, we'll use the best 10

def build_definition(term, content):
    """
    Build definition: look up knowledge base, or extract from surrounding text.
    """
    term_l = term.lower()

    # Knowledge base lookup (exact or partial match)
    for key, defn in ECON_DEFINITIONS.items():
        if key in term_l or term_l in key:
            return defn

    # Extract from surrounding text in the module
    pattern = re.compile(
        r'(?:^|[.!?]\s)([^.!?]{0,80}' + re.escape(term[:8]) + r'[^.!?]{10,200})[.!?]',
        re.IGNORECASE | re.MULTILINE
    )
    plain_text = re.sub(r'<[^>]+>', ' ', content)
    plain_text = re.sub(r'\*+', '', plain_text)
    plain_text = re.sub(r'\s+', ' ', plain_text)

    matches = pattern.findall(plain_text)
    if matches:
        # Find the longest, most informative sentence
        best = max(matches, key=lambda s: len(s))
        best = best.strip()
        if len(best) > 40:
            return best[:320] + ('…' if len(best) > 320 else '')

    # Fallback: generic but contextually appropriate definition
    return (
        f"Concepto central en el estudio de la economía que refiere a {term.lower()}, "
        f"cuyo análisis permite comprender los mecanismos de asignación de recursos, "
        f"la formación de precios y los incentivos que guían el comportamiento de los agentes económicos."
    )

# ── Main processing ───────────────────────────────────────────────────────────
def process_file(filepath):
    fname = os.path.basename(filepath)
    with open(filepath, encoding='utf-8') as f:
        content = f.read()

    if 'GLOSARIO v9.5' in content:
        return 'skip'
    if '<!-- GLOSARIO -->' not in content:
        return 'no_marker'

    color = detect_color(content)
    candidate_terms = extract_terms_from_content(content, fname)

    if len(candidate_terms) < 5:
        # Supplement with topic-based terms from filename
        topic_keywords = {
            'mic': ['Oferta', 'Demanda', 'Equilibrio de Mercado', 'Elasticidad Precio', 'Utilidad Marginal', 
                    'Costo Marginal', 'Competencia Perfecta', 'Monopolio', 'Externalidad', 'Información Asimétrica'],
            'mac': ['PIB', 'Inflación', 'Política Monetaria', 'Política Fiscal', 'Tasa de Interés',
                    'Desempleo', 'Demanda Agregada', 'Oferta Agregada', 'Ciclo Económico', 'Crecimiento Económico'],
            'ep':  ['Estado', 'Poder de Mercado', 'Regulación Económica', 'Capital Humano', 'Ventaja Comparativa',
                    'Globalización', 'Imperialismo', 'Plusvalía', 'Fallo de Mercado', 'Derechos de Propiedad'],
            'eb':  ['Escasez', 'Costo de Oportunidad', 'Incentivos', 'Señales de Precios', 'Eficiencia Económica',
                    'Fallo del Gobierno', 'Salario Mínimo', 'Libre Comercio', 'Proteccionismo', 'Subsidio'],
            'me':  ['Modelo de Crecimiento de Solow', 'Estado Estacionario', 'Función de Producción Cobb-Douglas',
                    'Convergencia Económica', 'Ahorro e Inversión', 'Productividad Total de los Factores',
                    'Capital Físico', 'Depreciación', 'Rendimientos Decrecientes al Capital', 'Tecnología Endógena'],
            'if':  ['Valor Presente', 'Tasa Interna de Retorno', 'Derivado Financiero', 'Opciones Financieras',
                    'Gestión de Riesgos', 'Apalancamiento Financiero', 'Curva de Rendimiento', 'Arbitraje',
                    'Valor en Riesgo (VaR)', 'Martingala'],
            'm1':  ['Política Monetaria', 'Banco Central', 'Multiplicador Keynesiano', 'Inflación', 'PIB',
                    'Tipo de Cambio', 'Balanza de Pagos', 'Tasa de Interés', 'Ciclo Económico', 'Crecimiento Económico'],
        }
        for prefix, terms in topic_keywords.items():
            if fname.lower().startswith(prefix):
                candidate_terms = terms
                break
        else:
            candidate_terms = list(ECON_DEFINITIONS.keys())[:10]
            candidate_terms = [t.title() for t in candidate_terms]

    # Take the first 10 unique
    final_terms = []
    seen_final = set()
    for t in candidate_terms:
        key = t.lower()
        if key not in seen_final:
            seen_final.add(key)
            final_terms.append(t)
        if len(final_terms) == 10:
            break

    # Build item HTML
    items_html = '\n'.join(
        ITEM_TPL.format(
            color=color,
            term=t,
            definition=build_definition(t, content)
        )
        for t in final_terms
    )

    new_section = SECTION_TPL.format(color=color, items=items_html)

    # Inject into file
    parts = re.split(r'<!-- GLOSARIO[^-]*?-->', content, maxsplit=1)
    main = parts[0]
    rest = parts[1] if len(parts) > 1 else ''
    rest = re.sub(r'<section id="glosario".*?</section>', '', rest, flags=re.DOTALL)

    if '<!-- FOOTER -->' in rest:
        footer = rest[rest.index('<!-- FOOTER -->'):]
    else:
        footer = ''

    new_content = main + '<!-- GLOSARIO -->\n' + new_section + '\n' + footer

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return 'ok'


def main():
    files = sorted(
        os.path.join(TARGET_DIR, f)
        for f in os.listdir(TARGET_DIR)
        if f.endswith('.md')
    )

    # Priority order
    def priority(fp):
        n = os.path.basename(fp).lower()
        order = ['mic', 'ep', 'eb', 'mac', 'me', 'm', 'pe', 'if', 'a']
        for i, p in enumerate(order):
            if n.startswith(p): return (i, n)
        return (99, n)

    files.sort(key=priority)

    pending = [fp for fp in files
               if 'GLOSARIO v9.5' not in open(fp, encoding='utf-8').read()
               and '<!-- GLOSARIO -->' in open(fp, encoding='utf-8').read()]

    print(f'\n📚 Local AI Glossary Generator — {len(pending)} modules pending\n', flush=True)

    ok = skipped = failed = 0
    for fp in pending:
        fname = os.path.basename(fp)
        result = process_file(fp)
        if result == 'ok':
            ok += 1
            print(f'  ✨ {fname}', flush=True)
        elif result == 'skip':
            skipped += 1
        else:
            failed += 1
            print(f'  ✗ {fname}: {result}', flush=True)

    print(f'\n{"="*50}')
    print(f'✅ Done: {ok} | ⏭ Skipped: {skipped} | ❌ Failed: {failed}')


if __name__ == '__main__':
    main()
