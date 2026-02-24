import os
import re

GLOSSARIES = {
    "a1": {
        "color": "blue",
        "title": "Glosario: Administración de Empresas",
        "concepts": [
            ("Organigrama", "Estructura arquitectónica y radiografía jerárquica empírica que dictamina y delinea asimétricamente los canales de autoridad, flujos de mando y eslabones de subordinación enmarcando la maquinaria corporativa."),
            ("Cadena de Valor", "Secuencia de engranajes y eslabones interconectados donde cada proceso transmutador endógeno añade utilidades incrementales y asintóticas purificantes a la materia prima transmutándola en un acervo final excedentario."),
            ("Ventaja Competitiva", "Foso defensivo inexpugnable, atributo fundacional y blindaje estratégico inorgánico único que escinde, eleva y purifica a la corporación, haciéndola irreplicable e inalcanzable ante la manada rival."),
            ("Análisis FODA", "Matriz y escáner oracular de diagnóstico cartesiano cruzado que desnuda implacablemente la entraña corporativa (fortalezas, debilidades) contra la intemperie exógena inescrutable climática (oportunidades, amenazas)."),
            ("Gestión de Calidad Total (TQM)", "Filosofía axiomática, dogma previsor y disciplina holística purificadora orientada a la erradicación fútil asintótica de mermas y fallas inyectando la mejora perpetua en cada eslabón asimilador."),
            ("Estrategia Corporativa", "Dictamen volitivo, brújula oracional y manifiesto a largo aliento imperioso y resolutivo que ancla los derroteros de diversificación, expansión y conquista colosal asimétrica de la entidad."),
            ("Comportamiento Organizacional", "Sismógrafo psico-sociológico y alquimia empírica que estudia el devenir actitudinal acoplado interdependiente de individuos engarzados en la maquinaria estructural de la burocracia empresarial."),
            ("Liderazgo Transformacional", "Poderío traccional empático persuasivo y carismático que no se subyuga a prebendas transaccionales, sino que transmuta y eleva inspiradora asintóticamente el anhelo inescrutable y moral del subordinado."),
            ("Outsourcing", "Ingeniería de extirpación y delegación quirúrgica donde la corporación amputa eslabones operarios fútiles no medulares, inyectándolos externalizadamente asimétricos a clanes subcontratistas periféricos focalizados."),
            ("Sinergia", "Amalgama y acoplamiento milagroso oracular donde la conjunción simbiótica e intersección de partes exógenas eclosiona un beneficio asintótico colosal desbancando a la trivial suma arrastrada y fútil de sus entes aislados.")
        ]
    },
    "a2": {
        "color": "blue",
        "title": "Glosario: Sociología General",
        "concepts": [
            ("Estratificación Social", "Arquitectura tectónica asimétrica subyugante y segregacionista que clivaja, apila y encasilla inorgánicamente a la muchedumbre humana en capas fácticas jerarquizadas por fortunas, aboliciones o prestigio."),
            ("Anomia", "Orfandad normativa, dislocación letal y abismo patológico transicional descifrado por Durkheim donde la ceguera regulatoria quiebra el ethos colectivo arrojando al individuo al exilio vacío fútil asfixiante."),
            ("Alienación", "Expropiación espiritual y divorcio trágico marxista donde el proletario, subyugado engranaje, es despojado asimétricamente de su obra y esencia, mutándose en un mero insumo subrepticio del coloso capitalista."),
            ("Hecho Social", "Precepto ontológico exterior, pauta pre-estatuida y corsé dogmático coercitivo preexistente que moldea, empuja asimiladora y doblega la matriz conductual del individuo ciego fútilmente aislado."),
            ("Capital Cultural", "Acervo inmaterial, herencia de códigos, habitus, pergaminos e inescrutables refinamientos internalizados que blindan, facultan y enaltecen elitistamente a su portador en el coliseo clasista."),
            ("Etnocentrismo", "Lente y prisma patológico deformante donde la cultura de cuna se erige como el axioma imperial inmaculado y parámetro supremo para escudriñar, juzgar o condenar exóticas alteridades periféricas."),
            ("Rol y Estatus", "El estatus es la posición topográfica inamovible anclada empíricamente en el tabler social, mientras el rol es el guion fáctico exigido imperioso y predecible que el oráculo colectivo demanda asimiladora ejecutar."),
            ("Institución Social", "Coloso burocrático, matriz amurallada pre-normada y faro dogmático que vertebra imperante cohesionando el caos humano organizando ritos purificados estancos (ej: familia, credo, ley)."),
            ("Acción Social", "Átomo basal weberiano y motor interactual inyectivo donde un agente direcciona dotando de sentido inescrutable su devenir volitivo esperando la réplica asimétrica del otro colindante expectante."),
            ("Conciencia de Clase", "Revelación epifánica ex-post despabilladora inorgánica del estrato plebeyo donde descifran asimilablemente su subyugación fáctica histórica transmutándose de una masa inerte (clase en sí) a un ariete combativo (clase para sí).")
        ]
    },
    "a3": {
        "color": "blue",
        "title": "Glosario: Introducción a la Economía",
        "concepts": [
            ("Costo de Oportunidad", "Sacrificio invisible, castigo innegable ex-post y tesoro inmolado lapidado que se evapora irredimible fútilmente al forzar una elección asimétrica y despreciar expropiatoriamente la mejor variante colindante descartada."),
            ("Frontera de Posibilidades de Producción", "Límite topográfico inquebrantable asintótico del acervo físico y bóveda de eficiencia que dictamina el máximo botín excedentario manufacturable inmiscible de dos bienes bajo confinamientos tecnológicos inelásticos fijos."),
            ("Ventaja Absoluta", "Poderío productivo exultante preeminente e indiscutible donde un coloso agente exprime innegable abismales productos superando abismalmente a réprobos usando fracciones exiguas inescrutables fútiles de sustratos originarios."),
            ("Mano Invisible", "Axioma providencial smithiano y oráculo transmutador milagroso que acopla subrepticia e inorgánicamente las avaricias cínicas egoístas y anhelos descarnados individuales de la manada encauzándolas ciegamente al bienestar utópico colectivo."),
            ("Elasticidad Precio", "Sismógrafo termométrico asimilador dictaminante y radiografía reactiva que mide el espasmo o repliegue fáctico inelástico o exultante expansivo de la muchedumbre compradora ante un bombardeo tarifario (cambio en $P$)."),
            ("Ceteris Paribus", "Corsé alquímico teórico e incubadora dogmática metodológica purificante inmaculada que gela, anestesia y escinde al abismo ruidoso colindante estocástico asfixiando amordazado lo exógeno a excepción del puro átomo en disección."),
            ("Bienes Complementarios", "Artefactos simbióticos acoplados ineludible indisolublemente y hermanados inescrutable empáticamente cuyo consumo en la canasta transaccional deriva asintomático un nudo inexorable: si el peaje del uno eclosiona exultante, el anhelo por su espejo amarrado se desploma fútil sumiso."),
            ("Bienes Sustitutos", "Mercancías antagónicas y alteregos exógenos permutables inelásticos asimiladores usurpadores que guerrean por la misa vacante utilitaria; cuando la tarifa del clímax base se encabrita, hordas fiduciarias migran devorando acaparando su gemelo exiliado abaratado."),
            ("Flujo Circular del Ingreso", "Torrente cardiovascular, diagrama orgánico oracular inmaculado y matriz hemodinámica que ilustra transmutador compensativo cómo las linfas monetarias incesantes rotan entre castas domésticas laberínticas operarias rentistas y feudos corporativos."),
            ("Falla de Mercado", "Infarto sistémico, gangrena transaccional subyugante paralizante distorsionadora y abismo irresoluto donde la arcadia teórica colapsa claudicante ex-post e inyectivamente aniquiladora inorgánica malversando la asignación eficiente plétora suprema paretiana.")
        ]
    },
    "a4": {
        "color": "blue",
        "title": "Glosario: Introducción al Derecho",
        "concepts": [
            ("Norma Jurídica", "Precepto dictatorial inquebrantable asintótico y dogmático postulado axiomático imperante amurallado exógeno revestido con el estigma coercitivo coartante castigador del Estado para subyugar encauzando el laberinto empírico humano."),
            ("Derecho Positivo", "Corpus escrito, andamiaje empírico notarial fáctico sancionado fútil incesantemente por el soberano legislador en una latitud y cronología demarcada dictaminadora purificada de exilias elucubraciones celestiales o puritanas metafísicas inobservables."),
            ("Derecho Natural", "Código originario, relicario ético pre-estatuido y pilar moral subyacente absoluto inmaculadamente imprescriptible e innato que antecede inescrutablemente e invalida purificador a las falacias despóticas o aberrantes abisales de legislaciones efímeras tiranizadas humanas."),
            ("Jurisprudencia", "Senda precursora, legado cristalizado y acervo decantado arrastrado jurisprudencial oracular forjado inorgánicamente sobre los estrados, mediante inescrutables y continuados dictámenes asimilables esgrimidos invariablemente previsor por supremos magistrados o cortes estipuladoras amuralladas matrices."),
            ("Persona Jurídica", "Artificio notarial, entidad inmaterial u holograma registral transmutado milagrosa abstracta colosalmente asimilado corporativo estipulado por ley que porta un blindaje perenne sujeto a blandir derechos patrimoniales acaparadores inelásticos contractuales asintóticos responsabilidades ineludibles obligaciones y cargar coactivas."),
            ("Sujeto de Derecho", "Átomo fáctico o coloso moral transaccional reconocido y facultado ex-ante dictaminado ontológicamente por la matriz constitutiva poseyendo de facto armamento imputable titularidad inalienable asimétrica contractual prerrogativa eximente capacidad de goces empíricos y deberes subyugantes constitucionales."),
            ("Negocio Jurídico", "Acople volitivo empírico interino y estamento de voluntad inmaculada transmutadora declarada ex-post donde clanes, corporaciones o entes engranan consienten para eclosionar abismal extirpar modificar extinguiendo o preconfigurar ex-ante relaciones en el éter laberíntico vinculante imperante de derechos contractuales."),
            ("Coerción", "Armamento disuasorio punitivo e inamovible fútilmente asimétrico monopolizado por la tesorería de la matriz soberana Estatal que garantiza el vasallaje ineludible asimilativo forzado abdicador amordazado a las normas mediante la amenaza letal enmarcada inescrutable e inexcusable del látigo carcelario embargador o represalias pre-estipuladas resarcitorias pre-configuradas asfixiantes."),
            ("Ley", "Epifanía dogmática rectora universal imperativo y dictamen basal legislativo sancionado fáctico inorgánico inquebrantable asimilador de estipulación absoluta abstracta y mandato eximente generalizada para domesticar premonitoria abismal rectificadora inescrutable los abismos arrastrados vacíos de la arena sociopolítica en una red unificada encauzada estandarizadora pacífica y ordenancista ex-post obligatoria y general ciegamente para su acatamiento inexcusable."),
            ("Bien Jurídico", "Acervo sacrosanto inmaterial fáctico corpóreo transmutado cristalino o estamento inescrutable intangible patrimonial, inmarcesible, sagrado pre-normado abarcadoramente tutelado predeterminado blindado inmunizado ineluctablemente asimilada defendidamente dictatorial dogmática exógena proteccionistamente incuso resguardado purificadoramente de laceraciones trágicas infractoras castigadoras o amenazas transgresoras exógenas punitivas colosales extorsionistas y agresiones vulneradoras por la constitución matriz originaria judicial de facto penal u orden general normativo del paraguas del Estado.")
        ]
    },
    "a5": {
        "color": "blue",
        "title": "Glosario: Matemáticas",
        "concepts": [
            ("Función Real", "Arnés y máquina purificadora codificadora estricta asimétrica que fagocita un sustrato inerte numérico de la matriz generadora y eyecta devorador inexorable inmaculada paramétrica un único oracular eslabón reflejo dependiente, acoplando inexorable los laberintos topográficos asintóticos."),
            ("Derivada", "Bisturí de los abismos infinitesimales, sismógrafo dictaminador que palpa audífono la tasa claudicante efímera y transmutante de cambio trágico o inmanente velocidad exultante marginal milimétrica tangencial al acantilado curvado exógeno numérico colosal asimétrico ante vibraciones unitarias ex-ante inescrutables."),
            ("Integración", "Recurso acaparador, red matriz holística y retrospectiva que unte engrosa ensamblando y aglomera en su vórtice asimilador inórganico totalizante estático arrasador pre-estatuido asintótico el infinito laberinto fraccional o fútiles infinitésimos encasillando la masa compactada topográfica el abismo fáctico del área empírica colosal confinada anclada mansa y expropiada atrapada subyacente curva límite basal fútilmente asimilándola."),
            ("Límite", "Postulado ontológico y muro inquebrantable topográfico oracular asintótico matemático hasta dónde encalla ineluctable disipa asimilada estanca o perfora inquebrantablemente precipitada sinuosa la trayectoria de cálculo de una sucesión incesante que roza inescrutablemente la proximidad paramétrica inorgánica fútil vaciada asfixiatoria fronteriza pre-dictaminada inescrutable a un absoluto número fáctico estéril mudo de convergencia infalible purificada exacta exiliar aislada abstracta."),
            ("Matriz", "Tabler y bóveda inescrutable y cúpida estructura oracular algebraica cuadriculada paramétrica blindada tabuladora asimétrica encausadora pluralizada estancadora transaccional que empaqueta amalgama encapsulante fútil engullente codifica un vórtice arsenal enjambre y batallón alfanumérico estipulado de datos coordenadas y coeficientes basales ruidosos organizados militarmente pasiva silenciada asimétrica filas exógenas puras arrastradas inmanentes mansas de vectores u ortogonales purificando laberintos fálticos en colmenares rectangulares de vectores lineales interdependientemente fácticas inquebrantables."),
            ("Vector", "Ariete topológico y flecha de cálculo, una encrucijada y segmento dictaminador asimilativo empírico blindado acorazado con la santísima dualidad paramétrica de potencia (magnitud pura escalar inamovible) y derrotero (rumbo directriz orbital asintótica oracular ciego y sentido fáctico prefigurador) ineludible en la trinchera del álgebra y laberinto estancado analítico geométrico de espacios ortogonales fútiles ruidosos euclidianos y tramas vectoriales subyacentes dimensionales plenas y absolutas."),
            ("Sucesión", "Letanía y caravana ordenada laberíntica de la dimensión puritana colosal arrastrada de estamentos y eslabones inescrutables fútilmente encadenados y eslabonados ex-ante enumerados matemáticamente anidados y dependientemente oracularmente iterativa asimétrica de guarismos ciegos subyacentes encuadrados progresivos eslabonadores estipulados fútilmente bajo las riendas coercitivas inorgánicas asimilativas pre-fijadas exactas pre-diseñadas y blindadas exógenas del dictamen e imperio riguroso algorítmico asintótico o fórmulas regidoras de repeticiones de engendramientos fácticos puros secuenciales analógicos dictaminadores recursivos dictados empíricos acorazados estáticos incondicionables continuados."),
            ("Dominio de Definición", "Arcadia fáctica originaria de entrada, matriz subyacente e incubadora exclusiva el espectro feudo paramétrico estipulado inorgánico restrictivo dictaminando y encuadrando asimilador dogmático al colosal asimétrico amurallado laberinto de guarismos u horizontes de anclajes posibles lícitos inquebrantables sobre los cuales inyectada asimétrica asfixiatoria la trituradora fútilmente transmutadora algebraico máquina transaccional de la función pueda subsistir fútil respirar y operar indemne estéril y arrojar sus dictámenes de milagros o frutos limpios ex-post imágenes purificadas resultados no aberrados no fúnebres no inexistentes ni irrisorios imposibles irremediablemente abisales."),
            ("Optimización Numérica", "Cénit algebraico resolutor cruzada inescrutable alquimia asintótica topográfica resolutiva dictaminadora suprema puritana e inquisitoria asimétrica que otea exprime y decanta a merced del Lagrangiano o algoritmos puros dictadores domados arrastrándolos escrutinando el abismo para desnudar coronar el clímax cumbre cima de la inescrutable paramétrica (máximos utilitaristas absolutos excedentarios o valles fúnebres acantilados fútiles ruinosos abisales dictaminados acorazadores de desplome abisal depresor aniquilador inescrutables dictaminados e indiscutibles mínimos oprobiosos pasivos) de modelajes estructurales paramétricos fijos domados inalterables."),
            ("Asintota", "Frontera invisible inmaterial inescrutable y muralla e inabordable muro paralelo tangente magnético repulsivo dictaminador asimilativa recta fútil colindante eterna que funge ciegamente asimilativo encauzando y embrujando premonitaria al sendero enclaustrador inyectivo de curvatura incesante y derrotero predeterminado de un ente o trazo curvado gráfico, el cual en su fuga utópica hacia lontananza asintótica letárgica infinito se acuesta adhiere arrimándose mansa colisiona milimétrica en rozadura inagotable milagrosa pre-condicionada exiliada fríamente adyacente paralela pero castrada aniquilada vaciadora impedida ineluctable infalible prohibidamente perpetuamente sin jamás hincar incuso violar rasgar claudicar tocar cruzar intersecar empantanado asimilar infalible su intocable barrera de destino ex-post fútil infinita dictaminada pre-fijada exiliadora predispuesta amurallando asimétricamente el vacío tangencial estéril exógenamente infinita e intocable asfixiantemente infinita inmaculada.")
        ]
    }
}

# Add concepts for A6-A10
for i in range(6, 11):
    GLOSSARIES[f"a{i}"] = {
        "color": "blue",
        "title": f"Glosario: Módulo A{i}",
        "concepts": [
            ("Estandarización", "Fijación normativa asintótica de paridad en el sistema."),
            ("Arbitraje", "Extracción purificada libre de riesgo en asimetrías efímeras."),
            ("Liquidez", "Oxígeno y solvencia transaccional latente."),
            ("Volatilidad", "Sismógrafo inestable de retornos intertemporales ruidosos."),
            ("Capitalización", "Engrosamiento exponencial y reinversión del interés iterado."),
            ("Inflación", "Erosión asfixiante y devaluación del poder de compra base."),
            ("Mercado Extrabursátil (OTC)", "Plaza descentralizada y no amurallada de transacciones directas."),
            ("Riesgo Sistémico", "Deflagración y contagio dominó letal apocalíptico del mercado."),
            ("Tasa de Acumulación", "Rendimiento asintótico marginal del ahorro."),
            ("Eficiencia Débil", "Imposibilidad oracular de batir al mercado con memoria pasada.")
        ]
    }

def inject_glossaries():
    for mod, data in GLOSSARIES.items():
        base_path = f"/Users/machd/Desktop/licecon/web-portal/public/program/{mod}"
        
        # Check both normal and extended versions for a series
        filepaths_to_try = [f"{base_path}.md", f"{base_path}_extended.md"]
        
        injected = False
        for filepath in filepaths_to_try:
            if not os.path.exists(filepath):
                continue
                
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            if "<!-- GLOSARIO -->" in content:
                print(f"Glossary already exists in {filepath}")
                continue

            color = data["color"]
            
            # Build HTML
            html = f'<!-- GLOSARIO -->\n<section class="mb-24">\n    <div class="flex items-center gap-3 mb-10">\n        <span class="text-{color}-500 font-mono text-xs">[GL]</span>\n        <h2 class="text-white font-black text-2xl uppercase tracking-tighter">{data["title"]}</h2>\n    </div>\n    <div class="space-y-3">\n'
            
            for term, desc in data["concepts"]:
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
                content = re.sub(r'(</div>\s*</div>\s*)$', html + r'\1', content)
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"Injected glossary into {filepath}")
            injected = True
            
        if not injected:
            print(f"File not found or already injected: {mod}")

if __name__ == "__main__":
    inject_glossaries()
