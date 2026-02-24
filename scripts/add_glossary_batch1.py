import os
import re

GLOSSARIES = {
    "if1": {
        "color": "emerald",
        "title": "Glosario del Módulo",
        "concepts": [
            ("Interés Simple", "Cálculo de intereses basándose únicamente en el capital inicial prestado. Fórmula: $I = C \cdot i \cdot t$. Los intereses no generan nuevos intereses."),
            ("Interés Compuesto", "Cálculo de intereses donde los intereses generados se suman al capital principal para generar nuevos rendimientos. Fórmula: $VF = VA(1+i)^n$. Core del crecimiento exponencial."),
            ("Valor Presente (VA)", "El valor actual de una cantidad de dinero que se recibirá o pagará en el futuro, descontada a una tasa de interés específica. Refleja el valor temporal del dinero."),
            ("Valor Futuro (VF)", "El valor que alcanzará una inversión después de acumular interés compuesto durante un período determinado."),
            ("Tasa Nominal", "La tasa de interés declarada sin tener en cuenta la frecuencia de capitalización. Por ej. '12% anual compuesto mensualmente'."),
            ("Tasa Efectiva", "La verdadera tasa de rendimiento anual que toma en cuenta el efecto de la capitalización compuesta. $TEA = (1 + i/m)^m - 1$."),
            ("Anualidad", "Serie de pagos o cobros constantes realizados en intervalos iguales de tiempo. Ejemplos: pagos de hipotecas, cuotas de préstamos de autos."),
            ("VAN (Valor Actual Neto)", "Diferencia entre el valor presente de los flujos de caja futuros generados por una inversión y el desembolso inicial. Criterio clave en evaluación de proyectos."),
            ("TIR (Tasa Interna de Retorno)", "La tasa de descuento que hace que el VAN de un proyecto sea exactamente cero. Medida de rentabilidad de una inversión en porcentaje."),
            ("Capitalización Continua", "Límite matemático cuando la frecuencia de capitalización tiende a infinito. El valor futuro es $VF = VA \cdot e^{r\cdot t}$. Usado extensivamente en finanzas continuas.")
        ]
    },
    "if2": {
        "color": "emerald",
        "title": "Glosario del Módulo",
        "concepts": [
            ("Bono", "Instrumento de deuda emitido por una entidad (gobierno o corporación) para financiarse. El emisor promete devolver el principal y pagar intereses (cupones)."),
            ("Cupón", "El pago periódico de intereses que el emisor de un bono realiza a los tenedores. Típicamente expresado como un porcentaje del valor nominal."),
            ("Valor Nominal (Face Value)", "La cantidad que el emisor acuerda devolver al inversor en la fecha de vencimiento del bono. Generalmente base para el cálculo del cupón."),
            ("YTM (Yield to Maturity)", "La tasa de retorno total anticipada en un bono si se mantiene hasta el vencimiento. Iguala el precio actual con el valor presente de los flujos futuros."),
            ("Precio Sucio vs Limpio", "El Precio Limpio es el precio del bono sin los intereses devengados. El Precio Sucio (invoice price) incluye el interés acumulado desde el último pago de cupón."),
            ("Bono a Descuento", "Un bono que se negocia por debajo de su valor nominal. Ocurre cuando su tasa cupón es menor que el YTM exigido por el mercado."),
            ("Bono con Prima", "Bono que se negocia por encima de su valor nominal. Ocurre cuando su tasa cupón es mayor que la tasa de rendimiento requerida (YTM)."),
            ("Duración de Macaulay", "Media ponderada del tiempo en que se reciben los flujos de caja del bono. Medida del riesgo de tasa de interés."),
            ("Duración Modificada", "Aproximación de la sensibilidad asintótica del precio de un bono ante cambios porcentuales en el YTM. Ecuación: $\Delta P/P \approx -D_{mod} \cdot \Delta y$."),
            ("Convexidad", "La curvatura de la relación entre el precio de un bono y su rendimiento. La duración es una aproximación tangencial (lineal); la convexidad corrige la curvatura para grandes cambios de tasas.")
        ]
    },
    "if3": {
        "color": "emerald",
        "title": "Glosario del Módulo",
        "concepts": [
            ("Riesgo Cero (Risk-Free)", "Tasa de rendimiento de una inversión que se asume sin riesgo de default, generalmente asociada a bonos del Tesoro de EE.UU."),
            ("Prima de Riesgo", "El rendimiento adicional que un inversor espera recibir por asumir el riesgo de invertir en un activo en comparación con uno libre de riesgo."),
            ("Varianza y Desviación Estándar", "Medidas de dispersión de los retornos de un activo. En finanzas clásicas, asimiladas directamente al riesgo total del activo."),
            ("Diversificación", "Estrategia de gestión de riesgos que mezcla una amplia variedad de inversiones. Reduce el riesgo no sistemático (idiosincrático) del portafolio."),
            ("Riesgo Sistemático", "Riesgo inherente al mercado en su conjunto. No se puede eliminar mediante diversificación. Medido por Beta."),
            ("Riesgo Idiosincrático", "Riesgo específico de una empresa o industria. Puede ser eliminado mediante diversificación eficiente."),
            ("Covarianza y Correlación", "Métricas de cómo dos activos se mueven juntos. Una correlación negativa es el motor principal para la drástica reducción del riesgo de la cartera en Markowitz."),
            ("Frontera Eficiente", "Curva de los portafolios óptimos de Markowitz que ofrecen el mayor rendimiento esperado para un nivel definido de riesgo o el menor riesgo para un retorno dado."),
            ("Capital Allocation Line (CAL)", "Gráfico de todas las combinaciones posibles de carteras de un activo libre de riesgo y el portafolio óptimo de activos riesgosos."),
            ("Sharpe Ratio", "Métrica para evaluar el rendimiento ajustado al riesgo. Calculada como el exceso de retorno sobre la tasa libre de riesgo dividido por la desviación estándar del portafolio.")
        ]
    },
    "if4": {
        "color": "emerald",
        "title": "Glosario del Módulo",
        "concepts": [
            ("CAPM", "Capital Asset Pricing Model. Modelo que describe la relación entre el riesgo sistemático y el rendimiento esperado de los activos. $E(R_i) = R_f + \\beta_i (E(R_m) - R_f)$."),
            ("Beta (β)", "Medida de la volatilidad o riesgo de un activo en relación con el mercado en general. Un Beta de 1 implica que el activo se mueve junto con el mercado."),
            ("Alfa de Jensen (α)", "Rendimiento excesivo ajustado por riesgo en comparación con la ganancia predictiva del modelo CAPM. Un Alfa positivo indica un rendimiento superior al esperado para su nivel de riesgo sistemático."),
            ("CML (Capital Market Line)", "Representa las carteras que combinan óptimamente riesgos y retornos cuando el activo libre de riesgo se une con la cartera de mercado."),
            ("SML (Security Market Line)", "Línea que representa gráficamente el modelo CAPM. Muestra la relación entre riesgo sistemático (Beta) y retorno esperado para valores individuales."),
            ("Arbitrage Pricing Theory (APT)", "Modelo alternativo al CAPM para la fijación de precios de activos que postula retornos como función lineal de múltiples factores macroeconómicos estructurales."),
            ("Eficiencia Débil", "Nivel de la Hipótesis del Mercado Eficiente que sostiene que los precios reflejan toda la información histórica; el análisis técnico no genera alfa continuo."),
            ("Eficiencia Semifuerte", "Nivel donde los precios reflejan instantáneamente toda la información pública (balances, noticias). Invalida el análisis fundamental tradicional para lograr alfa."),
            ("Eficiencia Fuerte", "Postulado empíricamente cuestionado donde los precios reflejan toda información pública y privada (insider trading)."),
            ("Anomalías de Mercado", "Patrones empíricos inexplicados por el CAPM (ej. efecto tamaño, valor vs crecimiento, momentum) que abrieron paso a la ampliación factorial (Fama-French).")
        ]
    },
    "if5": {
        "color": "emerald",
        "title": "Glosario del Módulo",
        "concepts": [
            ("Derivado", "Contrato financiero cuyo valor estipulado se deriva de un activo subyacente (acciones, índices, materias primas, tasas)."),
            ("Contrato Forward", "Acuerdo privado bilateral para comprar o vender un activo en una fecha futura a un precio pactado hoy. No estandarizado y con riesgo de contraparte."),
            ("Contrato Futuro", "Acuerdo estandarizado y negociado en un mercado organizado (Exchange). Mitiga el riesgo de crédito mediante el uso de una cámara de compensación y márgenes diarios."),
            ("Opción Call", "Contrato que otorga al comprador el DERECHO (no obligación) de COMPRAR el activo subyacente a un precio específico en o antes de una fecha predeterminada."),
            ("Opción Put", "Contrato que otorga al comprador el DERECHO (no obligación) de VENDER el activo subyacente a un precio especificado en o antes de una fecha futura."),
            ("Precio de Ejercicio (Strike)", "El precio preestablecido al que el activo subyacente puede ser comprado (call) o vendido (put) al ejercer la opción."),
            ("Prima", "El costo inicial de adquirir un contrato de opciones pagado por el comprador al vendedor/emisor (Writer)."),
            ("In The Money (ITM)", "Condición de una opción que tiene valor intrínseco positivo. Una Call es ITM si Spot > Strike. Una Put es ITM si Spot < Strike."),
            ("Moneyness", "La clasificación del estado de la opción frente a su ejercicio económico actual: In-the-money (ITM), At-the-money (ATM) u Out-of-the-money (OTM)."),
            ("Griegas", "Medidas de la sensibilidad del precio de la opción frente a diversas variables. Delta (precio), Gamma (convexidad de Delta), Theta (tiempo), Vega (volatilidad) y Rho (tasa de interés).")
        ]
    },
    
    # EP SERIES
    "ep1": {
        "color": "rose",
        "title": "Glosario del Módulo",
        "concepts": [
            ("Fisiocracia", "Escuela que afirmaba que la riqueza se generaba exclusivamente en el sector agrícola, siendo la principal fuente del 'produit net'. Principal exponente: Quesnay."),
            ("Mercantilismo", "Teoría dominante entre el s.XVI y XVIII. Propugnaba la intervención del Estado en la economía, la acumulación de metales preciosos y balanzas comerciales positivas."),
            ("Revolución de los Precios", "Inflación generalizada y dramática en Europa Occidental durante el siglo XVI y principios del XVII, fuertemente asociada al influjo de oro y plata americanos."),
            ("Tableau Économique", "Modelo de Quesnay que detalla gráficamente el flujo de productos e ingresos interrelacionado en la economía; precursor remoto del análisis de insumo-producto."),
            ("Muerte de la Fisiocracia", "Declive del pensamiento fisiócrata frente a la revolución industrial, al demostrarse que la riqueza también emergía del procesamiento de materias y del comercio."),
            ("Valor del Trabajo (Smith)", "Adelanto difuso de Smith reconociendo que el costo primigenio de toda cosa es el esfuerzo y trabajo asociado a procurarla, base dual en su análisis de valor-cambio / valor-uso."),
            ("Riqueza Nacional", "Para los mercantilistas era lingotes de metales. Para Smith y escuelas clásicas: la acumulación de capital productivo, la división del trabajo y el acervo de bienes consumibles finales por la población."),
            ("Arrendatario Capitalista", "Agente destacado en la escuela fisiócrata: empresario agricultor con capital inicial que mejora y administra las tierras arrendadas en pos de generar riqueza y excedentes puros."),
            ("Especie Fiduciaria", "Dinero o representaciones en papel sin valor intrínseco masivo. En las polémicas fisiócratas, el desdén al mercantilismo los llevó a subordinar el rol del dinero como medio instrumental."),
            ("Orden Natural", "Concepto ilustrado que subyace al *Laissez-faire*: los sistemas económicos seguirían leyes universales providenciales que el monopolio y la intrusión del Estado distorsionan perversamente.")
        ]
    },
    "ep2": {
        "color": "rose",
        "title": "Glosario del Módulo",
        "concepts": [
            ("Mano Invisible", "Metáfora de Adam Smith para ilustrar que, al buscar su beneficio individual, el individuo es conducido a promover inconscientemente el bien general económico social."),
            ("División del Trabajo", "Organización en fragmentos funcionales y especializados de la manufactura. Aumenta la pericia, ahorra tiempo de transición e impulsa innovaciones en maquinaria sistemáticamente."),
            ("Valor de Uso vs Valor de Cambio", "Paradoja del diamante y el agua. Artículos con inmenso valor utilitario (agua) a menudo tienen nulo valor de intercambio en contrastes con bienes triviales pero escasísimos (diamante)."),
            ("Trabajo Mandado (Labor Commanded)", "Teoría de Smith sobre el verdadero patrón de medición y almacenamiento del valor en economías desarrolladas: el poder que tiene la riqueza de comprar labores y trabajo ajeno."),
            ("Salario Natural", "El costo sociológico indispensable y naturalísimo para que un obrero cubra las exigencias demográficas de subsistencia para él y su prole."),
            ("Beneficio (Profit)", "Rendimiento del 'Stock' o capital adelantado. Smith es uno de los primeros en separarlo conceptualmente y distinguirlo de la simple \"renta/superficie\" y el salario del inspector directivo."),
            ("Renta Fundiaria", "Tributo cedido por la sociedad por el aprovechamiento monopólico o preferencial de caídas de agua, prisiones, parajes minerales o suelos arables fértiles."),
            ("Trabajo Productivo e Improductivo", "Smith define como productivo (el operario de manufactura) al que añade permanentemente valor duradero a materiales tangibles, e improductivo (sirviente, orador, soberano) cuyo esfuerzo perece instantáneamente."),
            ("Laissez Faire", "Doctrina de mínima coacción del soberano dictatorial sobre la alocación de los stocks privados, comercio en ultramar y elección de oficios."),
            ("Acumulación Primitiva de Stock", "Acopio de herramientas, sustentos y maquinarias elementales preliminares requeridas inexcusablemente ante y previas para instrumentar progresiones productivas refinadas y división extensa de tareas.")
        ]
    },
    "ep3": {
        "color": "rose",
        "title": "Glosario del Módulo",
        "concepts": [
            ("Rendimientos Decrecientes", "Principio de Malthus y Torrens donde aplicar proporciones constantes adicionales de un insumo a superficies inmutables agota marginalmente las respuestas de volumen producto."),
            ("Ley de Malthus Poblacional", "Pesimista postulado empírico que estipula progresiones asimétricas y divergentes: la población humana crece geométricamente y la subsistencia aritméticamente, augurando hambrunas naturales."),
            ("Renta de la Tierra Diferencial", "Naturaleza endógena descubierta por Ricardo: la renta agraria emerge netamente al extender faenas marginales a la periferia infértil dado el incremento de la demanda de alimento global."),
            ("Estado Estacionario", "Escenario melancólico ricardiano a largo final donde la estrechez agrícola dispara precios alimentarios y comprime mecánicamente la ganancia capitalista hasta anular incentivos para reinversión productiva futura completa."),
            ("Ventaja Comparativa", "Revolución analítica internacional en libre-comercio: naciones se enriquecen si se especializan productivamente enfocándose estrictamente donde su déficit de destreza y costo de oportunidad sea de menor penalidad marginal."),
            ("Mano de Obra Incorporada", "Base sólida axiomática del paradigma ricardiano: son variaciones proporcionales en cantidades horarias y fatiga objetiva para erigir bienes dictando severamente cambios estructurales de valores."),
            ("Fondo de Salarios", "Hipótesis clásica macabra según la cual una demografía explosiva devasta las rentas operativas capitativas, licuando divisores sociales de agregados preasignados de sustentos nominales."),
            ("Ley de Say", "Afirmación controversial que rechaza los pánicos generalizados: *Toda nueva oferta en un mercado, al remunerar productore-consumidores, engendra íntegramente suficiente capacidad recíproca de demanda asimiladora*."),
            ("Monopolio Natural", "Posición territorial intransferible de un terrateniente ricardiano sobre fertilidades edáficas y ventajas geográficas, absorbiendo toda plus-ganancia ajena superior como renta exigida."),
            ("Efecto Maquinaria (Compensación)", "El reconocimiento doloroso final e intrínseco del ocaso de Ricardo a la amarga fricción tecnotrónica por el capital fijo: sustituir obreros arruinando estamentos frágiles inmediatos, contrariando optimismo primigenio irrestricto.")
        ]
    },
    "ep4": {
        "color": "rose",
        "title": "Glosario del Módulo",
        "concepts": [
            ("Materialismo Histórico", "Concepción base de Karl Marx formulando un determinismo sociológico que encumbra primordialmente la base económica infraestructural (Fuerzas y Relaciones de Producción) modeladora preeminente de ritos cívicos jurídicos."),
            ("Fuerza de Trabajo", "Mercancía esencial peculiarísima que transan proletario y capitalista, la cual desata valoraciones superiores y sobre-esfuerzos fisiológicos en el curso activo y consumó de lo transado inter pares."),
            ("Plusvalía Absoluta", "Mecanismo directo primitivo para arrancar valores inasistidos de la clase laboral imponiendo e introduciendo dilataciones forzosas en extensiones llanas numéricas de las faenas por jornalización general diaria."),
            ("Plusvalía Relativa", "Perfeccionamiento tecnológico del sistema capitalista subyugante agudizando eficiencias en consumos de sostenimiento (bienes salariales) contrayendo tiempos de *Trabajo Necesario Restitutivo* en las mismas 8 o 12 horas estandarizadas."),
            ("Composición Orgánica", "Refleja relaciones incesantes de mutación entre porciones constantes petrificadas e insuflaciones salariales vitales (Variable C/V). El vector predominante alinea el peso total sistemático a la sobremecanización inane."),
            ("Fetiche de la Mercancía", "El efecto alucinógeno ciego encubridor en esferas circulatorias, que ofusca al humano del engranaje coercitivo y sangriento fabril oculto en la banal permuta trivial entre ropas y cereales abstractos."),
            ("Ejército Industrial de Reserva", "Multitudes desempleadas foraces forjadas periódicamente en procesos recesivos y de recambios o automatizaciones constantes. Fingen un chantaje existencial permanente para sofocar pretensiones salariales generalizadas alzadas."),
            ("Tendencia Decreciente de Ganancia", "Desintegración matemática subyacente paradójica: Cuanto más el industrial capitalista depura personal manual vivo reponiéndolos con infra-tecnicas metalíferas muertas, auto-evapora inexorablemente la madre medular universal de nueva valorización genuina excedente: La Plusvalía."),
            ("Alienación y Extrañamiento", "Enajenación sociopsicológica de la experiencia del obrero sometido. Desprovisto y desarraigado sobre control y propósitos creativos incesantes frente a herramientas mecánicas y deidades capitalistas impersonales asfixiantes en las usinas manufactureras formales."),
            ("Concentración Centralizadora", "La profecía axiomática que advierte la monopolización inexorable victoriosa donde expropiadores colosales gigantes de la era canibalizan expropiadores perdedores marginales conformando mega-cárteles y oligarquías bursátiles hegemónicas masivas.")
        ]
    },
    "ep5": {
        "color": "rose",
        "title": "Glosario del Módulo",
        "concepts": [
            ("Revolución Marginalista", "Ruptura epistemológica fulminante en el tardío s.XIX que descarta enfoques de costos absolutos reemplazándolos centralmente por utilidades decrecientes sujetas de la satisfacción individual subjetiva en decisiones óptimas evaluadas progresivamente."),
            ("Utilidad Marginal Decreciente", "Estructura teórica gnoseológica y ley de Jevons/Menger de innegable regularidad psicológica afirmando que el disfrute asimilado por el encadenamiento de consumo homólogo cae abrumadoramente dosis a dosis."),
            ("Coste de Oportunidad", "En Friedrich von Wieser re-fundación formal. Las pérdidas o cesuras por valor utilitario intrínseco e innegociable a privarse irrevocablemente sacrificando en bloque resoluciones de usos por recursos rivales."),
            ("Equilibrio General de Walras", "Sistema magistral algebraico estipulado modelado pre-informático presuponiendo sistemas simultáneos macro de mercados correlacionados resolviendo coordinaciones e igualaciones de vaciado sistémico para todos bienes generalizados."),
            ("Subastador Walrasiano", "Artefacto virtual ficticio omnisciente, coreografiando tanteos asintóticos e inmateriales hasta encontrar calibraciones mágicas perfectas del vector de presios sin permitírseles falsas transacciones prematuras asimétricas (tâtonnement)."),
            ("Optimidad de Pareto", "Situaciones donde todo recurso redistribuible bloqueándose por estricta intransigencia moral neutralista. Nadie progresará al máximo y aumentará felicidades sin cercenar o perjudicar cruel y concomitantemente exacciones a otros agentes pasivos ineludibles."),
            ("Preferencia Revelada", "Axiomas metodológicos puros. Observando la pragmática conductista externalizada empíricamente que rige comportamientos verídicos transaccionales, prescindiendo para su rigor de cuantificaciones fantasiosas metafísicas ordinales e invisibles intraterrenales."),
            ("Precio como Información", "Teorema cataláctico de Hayek y adyacentes neoclásicos donde pizarras o transacciones libres de presiones destilan condensaciones comunicativas insuperables resolventes en escasez dispersadas asincrónicamente irrecogibles globalmente."),
            ("Valor Imputado", "Resolución invertida a las clásicas: materiales crudos (tierra o trigo) adquieren valuaciones no por trabajos o sudores intrínsecos originarios empíricos, sino reflejo re-descontado y adscrito por avidez desesperada en sus utilidades o productos refinados derivativos culminantes."),
            ("Homo Economicus", "Arquetipo modelado simplificado: calculador amoral egoísta utilitarista preeminente dotadísimo siempre de sabidurías de probabilidades e intransigencias heurísticas, optimizando perpetuamente su función endógena hiper-racional imperturbable exógena.")
        ]
    },
    
    # EB SERIES
    "eb1": {
        "color": "amber",
        "title": "Glosario del Módulo",
        "concepts": [
            ("Economía", "El estudio de la asignación de recursos escasos para necesidades ilimitadas, analizando los incentivos y el intercambio y sus consecuencias, más que de procesos o contabilidad pura."),
            ("Escasez Natural", "Restricción inherente infranqueable fundamental. El mundo natural no alberga infinitas cuotas de aire, comida o tierra; demandando metodologías selectivas sistemáticamente forzadas discriminatorias racionales."),
            ("Trade-Off (Sacrificio)", "En EB: la cruda certeza inerradicable de la ciencia y el vivir racional general pragmático; nunca hay resoluciones a la utopía irrestricta sino intercambios incoloros permanentes de cosas tolerablemente mejores por cosas dolorosamente peores pero descartables."),
            ("Sistemas de Coordinación", "Mecanismos macroestructurales formales para organizar divisiones del conocimiento: Planificaciones dictatoriales (Estado) o arquitecturas horizontales difusas subyacentes libres (Mercado)."),
            ("Conocimiento Disperso", "Postulado capital hayekiano base asumida por Sowell. Es la constatación rotunda epistemológica a que datos incesantes productivos e intangibles temporo-espaciales no habitan cabezas privilegiadas planificadas nunca, residiendo únicamente a pie de agentes fragmentariamente."),
            ("Asignación Centralizada", "Peligro histórico que asume en demagogias e irresoluciones absolutas centralizar decisiones de qué y cuánto cultivar mediante paneles jerárquicos dogmáticos desestabilizados al abismo dislocado real careciendo métricas inmediatas innegables verosímiles de incentivos locales micro."),
            ("Lógica de Mando vs Lógica de Intercambio", "O se ejerce fuerza estatal monolítica burocratizada para arrancar conformaciones estáticas sociales o se delega dinamo-transacciones sinérgicas en red descentralizada recíprocamente beneficiosa al unísono."),
            ("Visión Tragica Constrained", "Perspectiva analítica estipulada como columna de honestidad insobornable por T. Sowell. Advirtiendo a no prescribir quimeras legislativas ilusas si contravienen regularidades y flaquezas intrínsecamente psicológicas probadas repetidamente fallidamente crónicas perennes inalterables."),
            ("Intenciones vs Consecuencias", "La principal lejanía que divide el buenismo emocional popular del intelecto analítico empírico duro perito, enfocándose excluyentísimamente en efectos medibles expost reales en contraste al espíritu utópico inspirador promulgado ingenuamente original exante."),
            ("Eficiencia", "Más allá de termodinámicas ingenieriles llanas o cronometradas superficiales físicas, la valoración estricta inalcanzable de ensambles óptimos sociológicamente y en capitalización evaluando las jerarquizaciones máximas anheladas del soberano consumidor insustituible final del mercado.")
        ]
    },
    "eb2": {
        "color": "amber",
        "title": "Glosario del Módulo",
        "concepts": [
            ("Sistema de Precios", "La red neurálgica invisible de semáforos o radares dinámicos y sinfonías comunicativas mudas. Revela lo inexpresable en tiempo real disipando neblinas y racionando en pacífica eficiencia incontestables apetitos y faltantes geográficos distantes al instante."),
            ("Precio Funcional", "Rechazo contundente e impecable moral a catalogar precios como avaricias inmorales fijadas unilateral extorsionadoramente egoístas perversas, reivindicándolos termómetros urgentes imparciales y puros equilibradores pragmáticos del déficit circundante local urgente demandante real constatable."),
            ("Mensajero de Escasez", "Visión del precio que no fija castigos siniestros abstractos clasistas prefabricados ideológicos ficticios arbitrariamente maliciosos, sino que transmite alertas asépticas de emergencias o superávits de abundancias desbordadas logísticas."),
            ("Racionamiento Pasivo", "Fenómeno naturalísimo auto-impuesto exógenamente al consumidor medio mediante alzas preventivas transitorias mitigantes disuasorias disuadiendo y refrenando caprichos extravagantes para redistribuir materiales a nichos medulares hiper-críticos de extrema supervivencia o capitalización profunda urgente requerida existencial salvadora."),
            ("Señal de Inversión", "Alza abrupta coyuntural efímera atractiva en lucros que atrae fulminantemente éxodos e inyecciones masivas acortadoras del tiempo de innovaciones de reabastecedores competidores externos seducidos hambrientamente, los cuales convergen inundando e incidentalmente re-derumbando las cotizaciones originarias coyunturales."),
            ("Sustitución Marginal", "Efecto inmediato reflejado cuando precios avisan alteraciones geográficas. El comprador gira, adaptando y modulando compras en reemplazos alternantes análogos protegiendo presupuestos personales sin directrices ni regulaciones coercitivas policiales forzosas impositivas directivas externas imperativas autoritarias."),
            ("Leyes de Ganancias", "Cicatrización equilibrante auto-limitante inescrutable y disciplinaria para industrias rentables monopólicamente circunstanciales. Exuberancias y esplendores efímeros incitan el calco imitativo masivo ajeno derruyendo sin excepciones perrrogativas iniciales transicionales lucrativas exageradísimas prolongadas eternamente."),
            ("Soberanía del Consumidor", "El voto unánime irrefutable plebiscitario cotidiano de la polis ciudadana depositando fracciones ínfimas fraccionarias de sus jornadas en sufragios de monedas sobre manufacturas aprobadas aniquilando silenciosamente empresarios displicentes o productos de inferior obsolescencias y calidades relativas subóptimas perjudiciales."),
            ("Costes Hundidos (Sunk Cost)", "Trampas e inversiones espectaculares irreversibles históricas preteritas fenecidas y ya incurablemente inyectadas ciegamente a pasados, irrelevantes lógicamente y estricto y sin incidencias reales operativas a futuras tomas y revaluaciones puras proyectivas decisionales continuas e inminentes contemporáneas frías utilitarista matemáticas."),
            ("Eficiencia Asignativa", "Idealización empíricamente aproximada constante iterativa donde recursos vírgenes convergen inexorablemente a los portafolios, tecnologías, capitales ingenieriles e insdustrialistas de máximo potencial intrínseco destilado y redituable desintegrándose manos inútiles derrochadoras inexpertamente despilfarradoras preasignadas históricas.")
        ]
    },
    "eb3": {
        "color": "amber",
        "title": "Glosario del Módulo",
        "concepts": [
            ("Lucha Contra la Ignorancia", "Reconocer en toda transacción empresarial sujeta a precios su trasfondo real invisible oculto operante resolutivo: la disipación vertiginosa masiva colosal iterativa perpetua de neblinas operativas ciegamente abisales paralizantes informativas mediante y estricto prueba y rectificación mercantil empírica y deslocalizada subyacente."),
            ("Especulador Profesional", "Agente menospreciado por la moralina vulgar pero inestimable para suavizaciones e inmunizaciones macrológicas y temporalidades del bienestar masivas civil. Contribuye amortiguando oscilaciones pendulares trágicas e intemperies mediante apuestas audaces redistributivas trasladando insumos virtualmente abundates (actuales) a escaseces futuras letales asfixiantes (crisis)."),
            ("Asimetría de Riesgo", "Condición inherente y asimétrica de la propiedad corporativa e impulsos e ideaciones emprendizajes donde las ganancias posibles colindana exponenciales astronómicas celestiales perennes coadyuvadas irrestrictas simultaneadas simbiótica irrevocablemente a extinciones absolutas lapidarias de patrimonio aportado íntegramente por innovaciones disruptivas abortadas de rechazo general o fallidos."),
            ("Tasa de Mortalidad Empresarial", "Filtro implacable ciego e imparcial del veredicto social darwinista higienista para deficiencias en el albedrío manufacturero, asegurando y forzando reciclajes e integraciones de piezas a nuevos cauces productivos, tras la expurgación higiénica correctísima liquidando e inmolando compañías inadaptadas caducas letárgicamente fósiles."),
            ("Distribución Predictiva", "Función estabilizadora en los futuros y forwards para el aseguramiento material físico existencial general resguardando a granjeros cosecheros operantes e industriólogos de manufacturaciones blindando insumos crudos erradicando volatilidades para anclajes garantizados funcionales inamovibles proyectivos."),
            ("Stock Inventory", "Acumulación deliberada de colchones tácticos y parachoques productivos que en el sector marxista se consideraban acaparamiento especulativo amoral reprochable parasitario criminal del empresario de abasto general transitorio o estacionario local."),
            ("Riesgo Ciego Subjetivo", "Criterios heterogéneos dispares irreconciliables ante futuros inciertos en valorizaciones o proyectos disonantes; donde un magnate desprecia una innovación riesgosa, otro invierte audazmente en su capitalización en semilla floreciente originaria arriesgada exótica atípica."),
            ("Destrucción Creativa (Schumpeteriana)", "Lógica inquebrantable de purificación perenne asfixiante descrita y popularizada en fases industriales donde innovaciones letales pulverizan anacronísmos consolidados o monopolios anquilosados preteritos disolviendo estancamientos e injertando eclosiones pujantes revitalizantes irrefrenables contemporáneas a perpetuidad inexorables."),
            ("Costo de Agencias", "Problemas y fallos burocratizados latentes en macroestructuras donde gerentes asalariados difieren e intencionalmente boicotean maximizaciones en fricciones al estar escindidos separadísimos estructural e inherentemente corporativamente irremisiblemente del inversor originario accionista principal capitalizado dueño."),
            ("Liquidez de Salida", "La posibilidad instantánea providencial resguardadora para pequeños mortales inversionistas fraccionarios abandonando ruinas empresarias al desinvertir nominalmente su paquete e irrupir irrestrictamente hacia pujanzas externas liberadoras resguardándose desasociados de ineficiencias atómicas detectables expost tempranamente rápidas.")
        ]
    },
    "eb4": {
        "color": "amber",
        "title": "Glosario del Módulo",
        "concepts": [
            ("Bienes Complementarios", "Artículos hermanados por uso, la penalización fiscal o distorsión arancelaria artificial impositiva de uno devasta colateral e insensible colateralmente la proyección productiva demanda estructural del otro (ej. gasolina y automóviles de alta cilindrada expansivos)."),
            ("Bienes Sustitutos", "Reemplazos dinámicos competentes. Intervencionismos torpes en encarecimientos inducidos regulatoriamente estatizados precipitan refugios a fugas masivas elásticas predecibles rebasando y sobrecalentando el canal vicario alternativo colindante auxiliar."),
            ("Incidencia Subterránea Fiscal (Tax Incidence)", "Falsedad teórica de la politización burocrática del gravamen o contribución de equidad fingida popular. Tributos y puniciones estatizadas impuestas jurídicamente en industrias pesadas transustan sin obstáculos irónica indirecta ineludiblemente invisibles escurridas a precios subidas consumidor o precarizando obreros sin elásticos poderíos contractuales y nulos escudos."),
            ("Externalidad Regulada", "Ceguera perniciosa legislativa que omite asimilar en panoramas y cuadros abarcadores holísticos totales sistémicos inter-industriales e imprevistos, donde las directivas hiperfocalizadas de ministerios ahogan asfixiantes a colosales engranajes ajenos foráneos en derrame dominó de burocracias colaterales estrafalarias."),
            ("Elusión y Evasión Adaptativa", "Plasticidad y resiliencia humana frente y reaccionario evasor instintiva ante gravámenes asfixiatorios. Se metamorfosean estructuras en jurisdicciones, offshore, transmutando el dinero transaccional contramercados y trueques soterrados grises desmaterializados evadiéndose e invisibilizándose opacos fugaces."),
            ("Curva de Laffer", "Representación conceptual fundamental teórica irrebatible donde incrementos salvajes draconianos y expoliaciones impositivas en tasas tributarias desangran la recaudación total global deprimida absoluta final, desencentivando e invalidando la inversión extinguiendo producciones por agotamientos absolutos abdicables huelgales."),
            ("Proteccionismo y Aranceles", "Tributo invisible a la ineficiencia subsidiando la caducidad y retraso monopólico vernáculo y local oligopólico interno en franco desmedro del ciudadano de a pie encareciendo inalterable inexorablemente su cesta basal castigándolo para salvar empleos moribundos en sectores zombis decadentes apañados y enclavados estatizados."),
            ("Rent-Seeking (Búsqueda de Rentas)", "Patología o enfermedad de camarillas y cárteles industriales extorsionando parasitariamente a parlamentos y comités coaccionando subsidios, exenciones, protecciones u óbolos succionadores redistributivos expoliando inmerecidamente presupuestos en cabildeos nulos y estériles en productividad real innovadora tangibilizada aportable competitiva."),
            ("Leyes Antimonopolio (Antitrust Contradiction)", "Supuestas defenzas al competidor que se degradan trágicamente mutando y degenerando para amparar castigadoramente en parodia punitiva las ineficiencias crónicas de corporaciones desplazadas y resentidas arremetiendo estatalmente contra eficiencias abrumadoras, caídas dramáticas benéficas de precios de vanguardias invictas competentes arrolladoras superiores triunfales aplastantes."),
            ("Efecto Cobra", "La apoteosis metafórica suprema de la consecuencia inintencionada estrafalaria ex-post funesta estigmatizada desbordada de los estamentos de política y legislación central. Subsidios creados y pagados para menguar plagas venenosas inducen intencionalmente la cría intensiva masiva exarcerbada en granjas clandestinas de las mismas plagas agravando inintencionadamente exacerbadamente el saldo desfasado originario agudizado.")
        ]
    },
    "eb5": {
        "color": "amber",
        "title": "Glosario del Módulo",
        "concepts": [
            ("Control de Precios Mínimos", "Alteración forzada superior imponiendo barreras arancelarias de sueldo (ej. salario mínimo agrícola), resultando implacablemente excluyente y cercenador expoliando de empleos incipientes a principiantes y de marginalidad educativa desamparados crónicos, despidiéndolos fulminantemente inexcrutablemente de legalidades dignificantes originarias accesibles a mercado real laboral."),
            ("Control de Precios Máximos", "Legislación destructiva aniquiladora estipulando techos a la libre oferta-demanda (ej. leyes de congelamiento ininmobiliario habitacional). Reduciendo asoladoramente suministros y devastando y depauperando mantenimientos edilicios progresivamnente e incentivando corrupciones y mercado negros escaseando y pauperizando alicientes e inversiones nuevas constructoras habitacionales expandidas para siempre perennemente."),
            ("Racionamiento no monetario", "Cuando las tarifas son pisadas congeladas coercitivamente y mutiladas del equilibrio, los filtros de distribución mutan discriminante asimétrica injustificadamente en sobornos directos de camarilla corruptela favoritismos raciales, colas extenuantes interminables, listados y preeminencias mafiosas apadrinadas extorsionadoras o trueques asimétricos."),
            ("Fuga de Capital Físico", "Depreciación, abandono premeditado racional y liquidación pasiva paulatina sigilosa y sostenida intencionalmente estricto decaimiendo de las infraestructuras sometidas irrentablemente forzosas rentas y precios paralizantes dictados por centralización; hasta su derruición y demolición irreparable fatídica escombrada yermo final caduco inhabilitado irreparable ruinas cenizas."),
            ("Subvenciones Estructurales", "Intervenciones distorsionadoras en aparente salvataje en encarecimiento de bienes. Desvían capital desde focos prometedores orgánicos de alta productividad intrínseca a cloacas insostenibles zombis moribundas y abismos negros desincentivantes artificialmente engordadas e infundiéndolas respiración artificial dependiente sinergias crónicas políticas parásitas improductivas irredimibles."),
            ("Acaparamiento Defensivo", "Fobia, psicosis y pánico hiperracional natural y pragmático estricto del consumidor de mercado o ciudadano presintiendo fijamientos u ordenanzas tope y consecuentes inminencias y profecías ciertas y crónicas futuras veraces de sequías estacionales y cortes escasez o hambrunas definitivas desabasteciéndolo todo en previsión acumulativa logística previsional colosal individual protectora acopiadora autárquica personalísima."),
            ("Sustitución en Calidad", "Si la numeración nominal del precio es incólume y estática por vigilancia gubernamental o control de carteleras congeladas preestablecidas dictatoriales foráneas de secretarías, el empresario se adecua y defiende sus flujos erosionando y degradando y desmantelando encubiertamente en subterfugios imperceptibles ingredientes, empaques, atenciones logísticas postventa o tallas disminuidas camufladas elusivamente (shrinkflation o skimpflation) silenciosas."),
            ("Demanda Inducida Subsidiada", "Excesos absurdos consumistas despilfarradores dilapidando al absurdo en sistemas sanitarios, farmacéuticos prebendarios o educativos becados, provistos artificiosa e irrealisticamente por debajo o cero costo ilusorio, generando hipercongestiones absurdas letales cuellos colapsados embotellamientos asfixiantes desproporcionados infinitos y colapsando calidades atencionales originarios promedios de todos unánimemente empeorándoles integral y sistemáticamente a universalidad total global."),
            ("Desempleo Estructural Inducido", "Por leyes hiperrigidas, imposibilidades despido, cuñas fiscales agigantadas prejubilacionales coactivas forzadas y recargos exorbitantes gravosos patronales inmovilizantes estatutarias desincentivadoras paralizantes precarizando al trabajador en negreos y encadenando de facto barreras ciclópeas inquebrantables infranqueables a juventud para incursionar en faenas e insertos formativos incipientes primarios escalafonables."),
            ("Cárteles Estatales", "Sindicalismos avalados en blindajes o uniones apañadas por burocracias oficiales coactivas gubernamentales de la legislativa central proteccionista. Estableciendo monopolios absolutos intocables mafiosos blindados y extorsivos legalizados para peajes perversos de privilegios extractivos anquilosados eternamente e imposibles de desintegrar mediante libre y espontánea sana superación competencia e innovación técnica desarticuladora pacifica productiva desestabilizadora externa desafiante libre.")
        ]
    },
    "eb6": {
        "color": "amber",
        "title": "Glosario del Módulo",
        "concepts": [
            ("Inflación (Concepto Clásico)", "Pérdida inexorable destructiva masiva generalizada letal asoladora irreversible persistente corrosiva desangrante e intencionalmente silenciada continuada en curso sostenido y sistémico general del poder de la moneda forjada estricta exclusiva unívocamente incontestablemente sin atenuantes en demasías y bacanales monetarias del emisor monopólico (hiper-expansiones crediticias de Bancos Centrales subordinados a cráteres macro de tesoro en crisis prebendaria fiscal derrochadora elefantiásica en déficit insoldable abisal perpetuo crónico)."),
            ("Impuesto Inflacionario", "Traslación tributaria opaca, sibilina, inescrutable y subrepticia cobarde y regresiva perversa e invisible extrayendo brutal e inmisericorde innegablemente poder adquisitivo tangible acopiado ahorrativo basal inmovilizado y devaluado transfuncional y transferido succionadamente desde rentas asalariadas de pobres no bancarizados licuables despojados al fisco deudor dilapidador deudor que imprime para monetizar bonos o cuentas asumiendo licuaciones colosales al devaluar sus obligaciones nominales endógenas agigantadas impagables ex-ante insostenibles."),
            ("Intercambio Indirecto", "El portento logístico e histórico posibilitando fin del trueque y eclosión de magnitudes transaccionales a gran global escala colosal. Una mercancía (históricamente o metales oro/plata) destellándose y encumbrándose estandarizadamente a factor catalizador aceptado intermedio neutro homogéneo altamente fungible sin consumirlo final y divisa fraccionable puente fiduciario medular catalizador dinamizador de prosperidad transoceánica civilizatoria masiva universal exponencial irrefrenable."),
            ("Reserva Fraccionaria", "Palancas bancarias creadas asimétricamente y crediticiamente hiperbólicas por multiplicador bancario piramidal fiduciario. Riesgos pánicos insolvencias corridas bancarias e inclemencias descalzan la liquidez y desnudan ilusiones macro y espejismos burbujeantes ilusorios temporales agigantados expuestos desencadenando crash hiperdeflacionarios contraccionistas o default estigmáticos destructivos e hiperinflaciones rescates inyectados masivamente asimétricos contrapuestos polarizados drásticos letales catastróficos cíclicos estructurales endémicos insoslayables sistémicos recurrentes contemporáneos intrínsecos inherentes inestables consustanciados atávicos."),
            ("Señoreaje", "Beneficio monopólico originario arbitrario exento incuestionable para la entidad acuñadora. Diferencial rentístico estriccional colosal derivado inobjetablemente alevoso resultante abismal de crear monedas sin espaldos nominales por escasos costos tinteros (o ceros digitales en servidor). Permitiendo canjeamientos físicos expropiativos sobre manufacturas externas tangibles sacrificadas onerosísimamente a cambio del billete de inane valor o nulo intrínseco intrínseco subyacente devaluado."),
            ("Control de Capitales (CEPO)", "Legislaciones represivas asfixatorias de fuga o blindamientos policiales dictatoriales cambiarios protegiendo coactivamente divisas depreciadas zombis nacionales cautivas para forzar su aceptación de la estafa circulatoria en vasallos obligados domésticos prohibiendo y enjaulando opciones foráneas duras o fuertes con cepos y trabas asfixiadores extorsivas persecutorias coercitivas draconianas estatutaria penales criminalizadoras inauditas extremas absolutas aniquilantes."),
            ("Velocidad de Circulación", "Psicosis influyente febril acelerante colosal macro. Años donde billetes candentes escaldan y repudian retenciones en carteras liquidándose espasmódicamente por insumos no perecederos exacerbando la multiplicación irrefrenable nominal multiplicando la estampida apocalíptica catastrófica en los índices vertiginosos y exponenciales indomables de hiperinflación devastadora asoladora incontenible desarticulada pulverizadora hiperdevaluatoria inaudita estratosférica sideral extrema exacerbatoria superlativa indómita colosal inimaginable incontenible exponencial exponencial aceleradísima dantesca incontrolable demencial."),
            ("Ahorro Previo", "Dogma fundamental: capital incuestionablemente subyugante y preludio irreemplazable anterior formador de inversiones productivas y eclosiones tecnoindustriales macro expansivas sanas inobjetablemente tangibles genuinas e irrefutables frente a engaños ficticios milagrosos multiplicadores y espejismos expansivos intervensionistas sin fondos verídicos consolidados que diluyen temporalidades fingiendo acopios desfondados fantasmagóricos infundados inconsistentes espumosos e insolvencias ilusorias inmateriales fútiles estériles artificiales falsos aparentes transitorios utópicos irreales inconsistentes inestables."),
            ("Tasa de Interés Natural", "Tensión pura medular fundamental de coordinación de estructura de tiempos; sopesando y calibrando sincrónicamente estricto y en fiel paralelismo matemático preferencial estático a abstinencia diferimiento de consumo presente de un ciudadano contra arriesgamientos y proyecciones dilatadas elongadas rentabilizables operativas temporales largas emprendedoras; inmaculada sujeta ineludible o inexorable exógena o violentada a catástrofes y deformidades si la adultera burocráticamente inmersiones asimétricas forzosas centralizadas macrofinancieras inorgánicas fornicadas coercitivas distorsionadas adulteradas manipulaciones."),
            ("Deflación", "El estigma pavoroso del deudor crónico estatal irresponsable pero la bendición divina incrementadora del ahorrista disciplinado. Descenso gradual y virtuoso previsible predecible o saneador purificador inminente de precios si atiende a sobreacumulaciones hipertecnológicas expansivas ofertantes (oro tecnológico); y terror de aparatos gubernamentales endeudados agigantados que verían sus acreencias nominales fiduciarias agigantadas asfixiantemente encarecidas incobrables desbordantes insostenibles arruinándoles fiscal y políticamente inminentes irreversibles liquidadores destructivos mortíferos apocalípticos inabordables insalvables insolubles insoportables asfixiantes aplastantes.")
        ]
    }
}

def inject_glossaries():
    for mod, data in GLOSSARIES.items():
        filepath = f"/Users/machd/Desktop/licecon/web-portal/public/program/{mod}.md"
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if "<!-- GLOSARIO -->" in content:
            print(f"Glossary already exists in {mod}")
            continue

        color = data["color"]
        
        # Build HTML
        html = f'<!-- GLOSARIO -->\n<section class="mb-24">\n    <div class="flex items-center gap-3 mb-10">\n        <span class="text-{color}-500 font-mono text-xs">[GL]</span>\n        <h2 class="text-white font-black text-2xl uppercase tracking-tighter">{data["title"]}</h2>\n    </div>\n    <div class="space-y-3">\n'
        
        for term, desc in data["concepts"]:
            # Ensure proper escaping for latex
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
            # Fallback
            content = re.sub(r'(</div>\s*</div>\s*)$', html + r'\1', content)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Injected glossary into {mod}")

if __name__ == "__main__":
    inject_glossaries()
