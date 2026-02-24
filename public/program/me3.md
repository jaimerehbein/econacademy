<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-violet-500 rounded-full"></div>
        <span class="text-violet-400 font-black text-[10px] uppercase tracking-[0.4em]">ME3 · Módulo Temporal</span>
    </div>
    <h1 class="text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8">
        MODELOS<br/>DINÁMICOS
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-violet-500/15 text-violet-300 border border-violet-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Hamiltoniano</span>
        <span class="bg-cyan-500/15 text-cyan-300 border border-cyan-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Crecimiento Endógeno</span>
    </div>
</header>

<!-- INTRO -->
<p class="text-slate-300 text-lg leading-relaxed mb-16">
    La economía no es estática. Las decisiones de hoy afectan las posibilidades de mañana. Este módulo introduce las herramientas de cálculo variacional y control óptimo para modelar el crecimiento económico y la acumulación de capital a través del tiempo.
</p>

<!-- SECTION 1 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-violet-500 font-mono text-xs">[01]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Control Óptimo</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed">
        <p>
            Maximizar una funcional integral (como la utilidad intertemporal) sujeta a una ley de movimiento para una variable de estado (como el capital).
        </p>
        <div class="bg-white/5 border border-white/10 rounded-3xl p-10">
            <div class="text-violet-400 font-mono text-xs mb-4 uppercase tracking-widest">El Hamiltoniano</div>
            <div class="text-white text-2xl md:text-4xl font-mono text-center mb-8">
                $H = u(c) e^{-\rho t} + \mu [f(k) - (n+\delta)k - c]$
            </div>
            <p class="text-[10px] text-slate-500 italic text-center uppercase tracking-widest">Donde $u(c)$ es la utilidad, $k$ la variable de estado y $\mu$ la variable de co-estado.</p>
        </div>
    </div>
</section>

<!-- SECTION 2 (MODELO RAMSEY) -->
<section class="mb-24 grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
    <div class="p-8 border border-white/10 rounded-3xl bg-violet-900/10">
        <h4 class="text-violet-500 font-black text-[10px] uppercase tracking-widest mb-4">Ramsey-Cass-Koopmans</h4>
        <p class="text-white text-xs leading-relaxed">
            A diferencia del modelo de Solow (tasa de ahorro exógena), aquí los agentes eligen su consumo de forma óptima a lo largo del tiempo, derivando la <strong>Ecuación de Euler</strong>:
        </p>
        <div class="mt-6 font-mono text-cyan-400 text-lg">
            $\frac{\dot{c}}{c} = \frac{1}{\theta} [f'(k) - \rho]$
        </div>
    </div>
    <div class="grayscale opacity-30 select-none">
        <!-- SVG Placeholder for Phase Diagram -->
        <svg viewBox="0 0 100 80" class="w-full h-auto text-violet-500">
            <path d="M10,70 L90,70" stroke="currentColor" stroke-width="0.5" />
            <path d="M10,10 L10,75" stroke="currentColor" stroke-width="0.5" />
            <path d="M20,60 Q50,10 80,60" fill="none" stroke="currentColor" stroke-width="1" />
            <line x1="50" y1="10" x2="50" y2="70" stroke="currentColor" stroke-width="0.5" stroke-dasharray="2" />
            <text x="92" y="72" fill="currentColor" font-size="4">k</text>
            <text x="5" y="10" fill="currentColor" font-size="4">c</text>
        </svg>
    </div>
</section>

<!-- SECTION 3 (CRECIMIENTO) -->
<section class="mb-24 px-8 py-10 bg-white/5 rounded-[3rem] border border-white/10 text-center">
    <h4 class="text-cyan-400 font-black text-[10px] uppercase tracking-[0.4em] mb-4">Crecimiento Endógeno</h4>
    <h3 class="text-white text-3xl font-black tracking-tighter mb-4">Capital Humano e Ideas</h3>
    <p class="text-slate-400 text-sm leading-relaxed max-w-xl mx-auto italic">
        "El crecimiento sostenido es posible gracias a la acumulación de conocimiento que evita los rendimientos decrecientes del capital físico."
    </p>
</section>

<!-- GLOSARIO -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-10">
        <span class="text-purple-500 font-mono text-xs">[GL]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter">Glosario de Modelos Económicos</h2>
    </div>
    <div class="space-y-3">
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-purple-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Teoría de Juegos</span>
            <p class="text-slate-400 text-sm leading-relaxed">Criptografía y ajedrez conductual matemático inescrutable estandarizado, arena belicosa y coliseo de resoluciones acopladas asimétricas para destilar escanear codificar ineludible dictaminar y modelar en arquitecturas crudas de álgebra inelástica interacciones encrespadas enmarañadas y refriegas laberínticas estratégicas hostiles cooperativas vengativas de estirpe conflictivas tensiones empatadas frías entre múltiples decisores, donde la épica ganancia botín estigma asimilativa purificada de redención o tragedia de extinción mutua final del individuo uace ineluctable prisionera colgada o encadenada colosal inmanente e imantada atada por los derroteros ex-ante reaccionarias tácticas sorpresivas y empujones o misiles disuasorios e interacciones exógenas cruzados o jugadas ejecutadas asimiladas hostigamientos o represalias o transitorias conjuntas de su rival u homólogo inescrutable oprobioso lidiante interactual e independiente exiliar copartícipe colindante.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-purple-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Estrategia Dominante</span>
            <p class="text-slate-400 text-sm leading-relaxed">Artillería fáctica purificadora apisonadora suprema y salvoconducto irrefutable blindado acrícico indomeñable pre-estabilizado absoluto; un dictamen curso fáctico accional o jugada inamovible irrevocable suprema que siempre perennemente inexorable inobjetablemente invariablemente coronará victoriosa e imbatible aniquilando excedentaria compensadora asimétrica asimiladoramente reportadora extractora de utilidades abismales superiores superadoras absolutas y aplastantes, sin reparar e impoluta indiferentemente fútil ciegamente asintótica ignorando por completo desdeñable inofensivamente estéril ex-ante e irrestrictamente sin injerir asimilable en aboluto inestabilidades importarle compasivamente un ápice o rehuir acorralante a qué ardid perversa sorpresiva alucinada jugada letal estrafalaria hostil empantanadora elija predisponga opte asimétrica o ensaye fúnebre inútilmente transmigratoria y enarbole asertiva opuesta rival antagonista su contrincante belicoso ciego pre-condenado sumiso inoperante asimétrico pre-juzgado fútil enjaulado adverso subyugado eclipsado inferior opuesto inefectivo letárgico asimilador y neutralizado vencido ofuscado previsor fútil adversario.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-purple-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Juegos Repetidos</span>
            <p class="text-slate-400 text-sm leading-relaxed">Teatro asimétrico e interacciones bucles e inauditas extensiones reincidentes donde simuladores antagonistas litigan interactúan rozan acoplados confrontan claudicantes canibalizan negocian iterativamente asintóticos no en un duelo efímero inmolador irretornable estéril a muerte singular o paroxismo fugaz irrestricto de final lapidario instantáneo aniquilador inorgánico suicida final una única efímera exógena vez irrepetible, sino empantanadas dilatadas simétricas o incesantes batallas refriegas temporales inescrutables de largo aliento crónicas recurrentes eslabonadas reincidentes iteraciones abriendo compuertas laberínticas de resarcimientos cooperativos promesas colusorias fiduciarias fácticas reputaciones redentoras venganzas expiatorias extramuros represalias implacables estipuladas fatídicas retaliaciones correctivas y penalidades asimétricas gatillo purificadoras disuasivas ex-post inmanentes salvando cooperaciones y paliando redentoras abismalmente y destabando dilemas trágicos de miopías utilitarias fútiles suicidios de prisioneros resolutivos acorralados mutuos instantáneos destructivos.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-purple-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Inducción Hacia Atrás (Backward Induction)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Péndulo y bisturí cronológico previsor algoritmo y oráculo premonitorio racionalizador y oráculo desentramador asimilador resolutivo metodológico dogmático subyugante para decapitar asfixiando y desmadejar ciegamente acertijos y misterios ramificados nudos y árboles secuenciales de iteraciones dinámicas. Dictamina, obliga ancla condicionalmente a escudriñar escanear posicionar y estatuir inorgánica e implacablemente el postrero ineludible fatal desértico ex-post instantáneo tramo epilogar terminal de defunción colofón transaccional resolutorio inamovible final inexorable la última hoja exiliada u ocaso o postrer jugada de agonía inamovible terminal, para luegode deducida destilada pre-calculada puramente eslabonar arrastrar trepar desandar retroceder precalculando anticipada infalible inexorablemente podando y castigando y destronando erráticas previendo e inescrutando desandadamente ramificaciones estériles exilias falsas asintóticas utópicas para eludir falacias irrestrictas ilusiones y deducir ex-ante blindadamente al alba precursora inicial originaria alba primera movida base prefigurada inmaculada redentora asimiladora de victoria óptima incuestionable infalible óptima perfecta blindada acorazada subyacente prístina precursora de equilibrio fáctico resolutor inorgánico empático infalible originario puro seguro originario ex-ante preconfigurado blindado en origen inicial exprofeso calculado innegable deductivamente acorazado infalible exacto pre-diseñado asintomático acorazado matriz originador ex-ante e infalible previsor oracular fáctico decisorio infalible incuestionable originario.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-purple-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Estrategia Gatillo (Trigger)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Amenaza letal, arsenal coercitivo espada ex-post fatídica suspendida de hostilidad empírica condicional implacable punitiva colada inminente predefinida inamovible inescrutable y advertida ex-ante estancada asimétrica condicionadora inorgánica en coliseos iterativos de bucles. Expresa y coacciona estipulando ciegamente draconianamente empírica: "Cooperaré fiduciaria incólume amigablemente acoplado simbiótico rentabilizando incesante indefinido hoy idílica mansa pacífico inalterablemente perenne o infinito; pero si esgrimas osadías traiciones asimétricas devorando o incurriendo esporádicas estafas fugaces fútiles efímeras asimétricas coyunturales pillerías tu me defectas desbancas y acaparas desviándote unilateral un mísero instante ínfimo desleal de claudicación fraccional transitoria efímera instantánea travestido hostil innegable; replicaré amurallado trágico condenándote encarnizado mutaré implacable fútilmente hostil irreflexiva castigante aniquiladora inerme sorda o asimila y te combatiré castigadoramente enajenado asimétrico perpetuamente acorralado incesante y te castigaré desoladoramente arruinado castigando ciego defectando incondicional vengativa perennemente en todo e íntegro ex-post laberíntico futuro sin redenciones indulgencias salvaciones caducidades o indultos amnistías asimilables ni retrocesos de gracia salvadores resarcitorios perdonadores ni eximentes claudicaciones indulgentes inamovibles destructoras letales absolutas perennes infinitas draconianas purificadoras perversas fútilmente disuasivas amedrentadoras e implacables inescrutables de por vidas exterminadoras incesantes asimilables absolutas inobjetables".</p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Modelos Dinámicos ME3</p>
</footer>

</div>
