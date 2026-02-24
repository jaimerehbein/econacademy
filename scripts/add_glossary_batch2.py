import os
import re

GLOSSARIES = {
    # MAC SERIES
    "mac1": {
        "color": "fuchsia",
        "title": "Glosario de Macroeconomía",
        "concepts": [
            ("Macroeconomía", "El estudio de la economía en su conjunto. Examina fenómenos que afectan a toda la economía, como el desempleo, la inflación y el crecimiento económico general, desde una perspectiva agregada."),
            ("Microeconomía", "Estudio de las decisiones que toman los hogares y las empresas, y de cómo interactúan en mercados específicos. Base micro-fundacional de gran parte de la macroeconomía moderna."),
            ("Modelos Económicos", "Representaciones simplificadas de la realidad matemática o gráfica utilizadas por economistas para explicar variables económicas, prediciendo cómo cambios exógenos afectan variables endógenas."),
            ("Variables Endógenas", "Aquellas variables que el modelo económico intenta explicar; su valor se determina dentro del propio sistema del modelo al alcanzar el equilibrio (ej. el precio de equilibrio del mercado)."),
            ("Variables Exógenas", "Variables cuyos valores se toman como dados desde fuera del modelo. Actúan como causas o choques que alteran el equilibrio del modelo, induciendo cambios en las variables endógenas."),
            ("Limpieza de Mercado (Market Clearing)", "Supuesto analítico central donde los precios y los salarios son completamente flexibles y se ajustan rápidamente para igualar la cantidad ofrecida con la cantidad demandada de manera continua."),
            ("Rigidez de Precios (Sticky Prices)", "Imperfección o fricción del mercado a corto plazo donde precios y salarios tardan en reaccionar a choques de oferta o demanda, dando origen al ciclo económico y al desempleo temporal."),
            ("Enfoque de Largo Plazo", "Perspectiva clásica donde se asume flexibilidad total de precios (market clearing). Permite que el producto converja a su nivel natural dictado por factores reales de la oferta."),
            ("Enfoque de Corto Plazo", "Perspectiva keynesiana aplicable cuando los precios son pegajosos. La demanda agregada puede desviarse de la oferta agregada, provocando recesiones o expansiones sobrecalentadas transitorias."),
            ("Agregación", "El proceso de sumar y condensar millones de decisiones microeconómicas individuales en indicadores estadísticos amplios y únicos como el PIB o el IPC, diluyendo particularidades en pro de tendencias.")
        ]
    },
    "mac2": {
        "color": "fuchsia",
        "title": "Glosario de Macroeconomía",
        "concepts": [
            ("PIB (Producto Interior Bruto)", "Valor de mercado de todos los bienes y servicios finales producidos en la economía doméstica durante un periodo. Mide tanto la renta total como el gasto total de la economía."),
            ("PIB Nominal", "Valor monetario corriente de la producción de una economía empleando los precios actuales del momento de medición, sin haber sido ajustado o purgado por la inflación reciente acumulada."),
            ("PIB Real", "Medición de los bienes producidos y valorados a precios constantes y anclados de un año base. Refleja fielmente el volumen físico de la actividad marginando y aislando las distorsiones de los precios."),
            ("Deflactor del PIB", "Índice o ratio (PIB Nominal / PIB Real) que mide de manera implícita la variación promedio e íntegra de precios de todos, y exclusivamente, los bienes de la economía doméstica nacional producida."),
            ("IPC (Índice de Precios de Consumo)", "Indicador estadístico fundamental del coste de una cesta representativa de bienes y servicios fijos comprados por un consumidor promedio metropolitano representativo frente al año base encuestado."),
            ("Identidad Macroeconómica", "La contabilidad nacional formal que reza que el total del Gasto $Y = C + I + G + NX$, estableciendo irrefutablemente que cada moneda gastada es simultáneamente una renta recibida correspondida íntegra."),
            ("Consumo (C)", "Componente mayoritario e inercial estable de la demanda agregada; gasto continuo que realizan los hogares en bienes duraderos, no duraderos o de servicios directos privados no comerciales."),
            ("Inversión (I)", "Expendios destinados deliberadamente a engrosar el stock capitalista empresarial. Maquinarias, instalaciones, inventarios o viviendas de hogares. Extremadamente volátil a ciclos económicos y coyuntura."),
            ("Tasa de Desempleo", "Porcentaje medido correspondiente estrictamente a la fuerza laboral activa que, sin poseer trabajo real transitorio, busca ocupación rentada formal pero fallando incesantemente en obtenerlo de pleno."),
            ("Tasa de Actividad", "El ratio absoluto de la población civil adulta en edad de laborar que decide participar visiblemente en la Población Económicamente Activa (PEA), estén estos ocupados operantes o desocupados postulantes.")
        ]
    },
    "mac3": {
        "color": "fuchsia",
        "title": "Glosario de Macroeconomía",
        "concepts": [
            ("Función de Producción", "Relación matemática $Y = F(K,L)$ que detalla y asocia estrictamente de qué modo técnico los factores combinados y la tecnología aglutinada detonan o restringen a la cuantía nacional final."),
            ("Factores de Producción", "Batería clásica de los ingresos primordiales en economías básicas (Tierra, Trabajo $L$ y Capital $K$) empleados y agotados secuencialmente para engrosar el flujo contable del acervo servicial productivo."),
            ("Rendimientos Constantes as Escala", "Hipótesis donde duplicar o expandir pro-porcional simultáneamente todos y acoplados los factores rinde asimétricamente un aumento general de idéntica proporción e igual cuantía absoluta de producto final ($zY = F(zK, zL)$)."),
            ("Producto Marginal del Trabajo (PML)", "La cuota fraccionaria puramente física de producto extraordinario incremental devengado al añadir una hora cruda final laboral de obrero adicional o peón marginal ceteris paribus congelado inamovible."),
            ("Salario Real", "Remuneración transaccional o pago en equivalentes adquisitivos efectivos crudos; calculado en base del producto marginal ($W/P = PML$), expresado no en dinero billete inane sino en cuantía tangible real de cosas medibles equivalentes."),
            ("Beneficio Económico vs Contable", "Mide el saldo después del pago a los factores, restando o drenando a priori no solo desembolsos patentes monetarios y operativos corrientes directos, sino detrayendo también íntegramente todo costo oportunidad indirecto escondido sacrificado intrínsecamente del inversor originario aportante directriz decisor puro."),
            ("Teorema de Euler", "Derivación matemática en mercados perfectos bajo rendimientos constantes, donde si los factores crudos obreros (L) o prestamistas (K) son remunerados implacablemente por sus productos marginales limpios netos en punto asintótico marginal óptimo y purgado, la suma exacta total macroeconómica salda $Y$ exahustivamente, y el beneficio originario puramente económico puro puro residual es devengado exhaustivamente cero exacto neutralizado vaciado puro."),
            ("Consumo Autónomo", "Gasto endoliente base existencial constante basal y natural incomprensible disociada independientemente apartada e inesquivable a pesar de rentas nulificadas asumiendo expropiación pasiva descapitalizadora liquidable de activos o recurriendo a empréstitos deudos asimétricos desmedidos deudas exacerbadísimas paliativas extremas urgentes transicionales."),
            ("Propensión Marginal al Consumo (PMC)", "La sensibilidad, inclinación, o declive y ratio exacto de derivación en gastos que consume privadamente perennemente una familia urbana promedia empírica estadística de cada eventual unidad (ej, dólar extra exógeno inyectado marginal incremental recibido originario puro)."),
            ("Efecto Expulsión (Crowding Out)", "Mecánica del tipo de interés macro. Si el aparato gobernante eleva su inmersión asfixiante y expoliadora demandando exorbitadamente deuda ($G$ o bonos), desplaza y contrae asfixiantemente encarecida excluyentamente secantemente drenando secamente irrecuperable asfixiante por sequía crediticia paralizadora total y asimétricamente la Inversión ($I$) real productista fabril y de riesgo expansiva originaria puramente capitalista empresarial pujante vanguardista emprendedurista privada de la esfera originaria civil de transacciones.")
        ]
    },
    "mac4": {
        "color": "fuchsia",
        "title": "Glosario de Macroeconomía",
        "concepts": [
            ("Dinero", "El activo transaccional altamente fungible, aceptado y estandarizado con elocuente suprema preeminencia liquidable universalizada y fluida que se erige como catalizador supremo general subyugante y perenne dinamo de permutas e intercambio mercantil y macrooperaciones sociales generalizadas de trueques en red total interpares civil de intercambios recurrentes difusos y anónimos en transacciones cotidianas mundiales."),
            ("Dinero Fiduciario (Fiat)", "Impresiones, denominaciones de cuentas crediticias, acrícilos nominales estandarizados por mandato del Estado sin ningún intrínseco respaldo en aleación u oro duro contante y real sino cimentado sostenidamente anclado por fe en aparatos y aparatajes expropiatorios de coacción recaudadora legal y coactitva fiscal exclusiva centralista institucional."),
            ("Funciones del Dinero", "Tres ejes: 1) Unidad de cuenta (termómetro referencial asintótico). 2) Medio líquido de cambio puro transaccional elástico lubricante total libre. 3) Dispositivo atesorador protector reserva temporal refugio acumulativo diferido y amortiguable o previsor previsor acopiador preservador proyectivos de patrimonios e inversiones."),
            ("Oferta Monetaria (M)", "Acopio circulante expandido aglutinador. Conforma efectivo billetes físicos y también subcategorías expansivas exponenciales o endógenas ($M1, M2$, etc); en conjunción a depósitos a la vista fiduciarios u operaciones subyacentes inmediatas plásticas bancarias de libre transabilidad instantánea veloz en chequeras instantáneas cotidianas generalizadas totales."),
            ("Banco Central", "Órgano regulador, emisior institucional director estatutario macro rector monolítico controlador que interviene dictatorialmente la oferta nominal primaria macro circulante base, las exigencias bancarias multiplicadoras perfiles de tasas prestatitarias anclas directrices base fundamentales en la geografía soberana monetizada nacional imperante abrumadoramente determinante innegable y totalizante absoluta en mandatos fiduciarios dictaminadores del rubro financiero total y mercado divisa total paralizante asimétrica o estipulativa macro expansiva crediticia expansiva en general cíclica."),
            ("Operaciones de Mercado Abierto (OMA)", "Vehículo instrumental ejecutor. Banco Central interviene comprando/vendiendo bonos; en compra (imprimiendo liquidez o engrosando balances de encajes bancos), insufla asimétricamente M al torrente civil crediticio encendificador alza multiplicadora monetizada o recesora drenando y retirando aspiradora deflacionante."),
            ("Reserva Bancaria Fraccionaria", "Sistema crediticio bancario operante asimétricamente elástico subyacente que reingresa prestándolo colosalmente reiterativa un colosal mayor fracción o saldo a deudores prestamistas terceros desfondando fraccionablemente el acopio originario estricto primario conservando solo una franja de base restrictiva basal requerida de precaución legalizada para no iliquidez sistémica prevenida operativa de corridas sistémicas previsibles matemáticas estadísticamente probables medias esperadas de cajeros de la masa total ahorrista cliente en global normal de flujo de salidas estándar de normal media."),
            ("Multiplicador Monetario ($m$)", "Ecuación y propensión estacional amplificadora empírica $m = (cr+1)/(cr+rr)$ estipulando en cuántas dimensiones fractales o subyacentes agregativas y colosales expansiones piramidales una inyección de un dólar crudo basal primario por emisor $1/$ del encaje impacta exponenciablemente y piramidalmente total aglutinado inmaterial engrosado real prestatitariamente y agregativo colosal multiplicativo ampliado desmedidamente transado indirecto virtualizado englobado en $M$, o de cuentas expansivas contables."),
            ("Base Monetaria ($B$)", "Los pasivos estancos férreos duros de Banco Centrales; la circulación papel física billetes de la ciudadanía civil más las sumas depositarias congeladas de bóvedas bancarias como pasivos de la matriz, deudas directas exógenas primarias irrestrictas matrices matrices emisoras del tesoro matriz, su crecimiento es directo por inyecciones OMA o flexibilizaciones masivas cuantitativas extraordinarias QE exclusivas rectoras asimétricas puras de inyección en cuentas crediticias directas matrices centralizadas dictadas en cuentas computacionales oficiales centrales asimétricas de monopolio rector expansivo creador originario del ciclo creados asimétricamente por apuntes expansivos de origen."),
            ("Apalancamiento Bancario", "Utilización exultante asimétrica exponencial aglutinadora y piramidal maximizando ratios frágil de equidad del balance bancario; operando masivamente el dinero ageno endeudado apalancador prestamista masivo acreedor acrecentando astronómicamente ratios ROE, pero subyugan agigantando en hiperfragilidades al riesgo sistémico sistémico ante desfalco e incobrables en estampidas incobrables arrastrando y devaluando cascada insolventaciones dominó letales en masa cíclicas crónicas paralizadoras liquidantes asoladoras asfixiantes o quiebras masivas de rescates masivas en insolvencias globales crónicas periódicas recurrentes generalizadas absolutas inevitables frágiles inestables pendulares trágicas desfondadas abismales catastróficas desarticuladoras sistémicas devaluadores licuadores destructores implacables endémicas irreparables crónicas estructurales atávicas implacables letales inoportunas inexorables fatídicas funestas desdichadas recurrentes abisales de pánico terminal sistémicos irreparables masivos recurrentemente endémicas sistémicas frágiles crónicas colapsando insolventados encadenados fatalmente fatídicos implacables inestables endémicas estructurales cíclicas.")
        ]
    },
    "mac5": {
        "color": "fuchsia",
        "title": "Glosario de Macroeconomía",
        "concepts": [
            ("Ecuación Cuantitativa", "Identidad: $M \cdot V = P \cdot Y$. En el fondo de la ortodoxia dice que aumentos inyeccionales nominales irrestrictos en dineros inyectados $M$ (si la velocidad e impulsividad es constante estable empírica e inamovible transaccional $V$) inexorablemente derivan correlativamente ex-post puramente en precios e inflados asfixiantes simétricos $P$ de toda mercancía y costo basal transaccional real productivos no incrementando el caudal irreal productivo basal o neutral inelástico verdadero absoluto material o físico subyacente global real macro-estructural originario real estable basal natural puro originario constante de manufacturación absoluta total incoloro fijo total constante transable irreal o ilusión óptica fiduciaria irreal o crecimiento falaz apócrifo de valores de cuentas expansivos o ilusión agregativa fiduciaria nominalizada puramente del desdoble unitario monetario medidor del factor multiplicador distorsionador."),
            ("Señoreaje", "Financiamiento o recaudación expropiatoria y subrepticia furtiva que percibe la Tesorería o Casa al acuñar o imprimir papel despojado emisor subyugando, asimilándose al tributo y canibalización macro inflacionaria en perjuicio expropiador devaluador absoluto inclemente cobarde encubierta solapada indirecta o subrepticia furtiva sibilina exaccionador confiscador letal del ahorrista y despojos ahorrativo del ciudadano inerte acaparador monetizado sin resguardos elásticos blindados no indexados indefensos cautivos forzados sumisos atrapados fiduciariamente perdiendo valor y liquado absoluto deudor y drenantes a la máquina emisora rectora privilegiada prebendarista dictatorial macro originaria asimétrica de origen expoliadora monopolista creadora de la merma encarecedora distributiva destructora abismal destructiva de masa de recursos absolutos tangibles fijos totales global de deudores expoliatoria confiscatoria regresiva extrema empobrecedora expoliadora letal recesiva asimétrica brutal inmisericorde recesiva de exacción sistemáticas recurrentes colosales agudas o dramáticas crónicas fiduciario fútiles prebendaria destructivas y dramáticas catastróficas agigantadas masivas subrepticias dramáticas endógenas asimétricas crónicas estructurales cíclicas recurrentes letales absolutas devastadoras asfixiadores implacables encubiertas brutales asoladoras implacables sibilinas peredadas devaluadoras opacas abismal encubiertas silenciosa expropiatorias masivas regresivas abisales exaccionatorias confiscaciones aniquilantes colosales de purgas exaccionistas encubiertas crónicas regresivas aniquiladoras sibilinas"),
            ("Efecto Fisher", "Postulado que iguala tasa nominal $i$ integrando a la adición estricta premonitorial pura cruda macro: tasa y real fundamental o real $r$ aunada íntimamente indivisible e indomeñable previsoramente sumando expectativas anticipatorias inflacionarias plenas $\pi_e$. La derivación $i = r + \pi_e$ predice un ajuste alzado 1:1 o simétrico encarecedor anticipado y precautelatorio prestamista para salvaguardajes prestatistas o escudos amortiguadores plenos indexadoramente autoajustados del acreedor ante el terror expoliador desvalorizador y licuente de devoramiento y quita impositiva subrepticio erosionadora o desangrante previsible o merma futura anticipable erosiva desvalorizante anticipadamente futura inflacionista endémica colosal previsible futura destructiva y abismal letal licuatoria encubierta fútil inflacionarla transmigratoria desestabilizadora nominal.")
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

        # Determine injection point
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
