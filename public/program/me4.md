<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-violet-500 rounded-full"></div>
        <span class="text-violet-400 font-black text-[10px] uppercase tracking-[0.4em]">ME4 · Módulo Estratégico</span>
    </div>
    <h1 class="text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8">
        TEORÍA DE<br/>JUEGOS
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-violet-500/15 text-violet-300 border border-violet-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Nash Equilibrium</span>
        <span class="bg-cyan-500/15 text-cyan-300 border border-cyan-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Mecanismos</span>
    </div>
</header>

<!-- INTRO -->
<p class="text-slate-300 text-lg leading-relaxed mb-16">
    La economía moderna es el estudio de la interacción estratégica. Este módulo formaliza cómo los individuos toman decisiones cuando sus resultados dependen de las acciones de los demás, desde juegos estáticos simples hasta el diseño de mecanismos complejos bajo información asimétrica.
</p>

<!-- SECTION 1 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-violet-500 font-mono text-xs">[01]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Equilibrio de Nash</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed">
        <p>
            Una situación donde ningún jugador tiene incentivos para desviarse unilateralmente de su estrategia, dada la estrategia de los demás.
        </p>
        <div class="bg-white/5 border border-white/10 rounded-3xl p-10 font-mono text-white text-center text-xl md:text-2xl italic">
            $a^*_i \in \arg \max_{a_i \in A_i} u_i(a_i, a^*_{-i}) \quad \forall i$
        </div>
        <p class="text-xs text-slate-500 uppercase tracking-widest text-center mt-4">Punto Fijo de la Función de Mejor Respuesta</p>
    </div>
</section>

<!-- SECTION 2 (ENRICHMENT) -->
<section class="mb-24 grid grid-cols-1 md:grid-cols-2 gap-8">
    <div class="p-8 border border-white/10 rounded-3xl bg-violet-900/10">
        <h4 class="text-violet-400 font-black text-[9px] uppercase tracking-widest mb-4">Competencia de Bertrand</h4>
        <p class="text-white text-xs leading-relaxed">
            Las empresas compiten en <strong>precios</strong> en lugar de cantidades. En el equilibrio básico, el precio colapsa al coste marginal ($P = MC$), resultando en beneficios nulos.
        </p>
    </div>
    <div class="p-8 border border-white/10 rounded-3xl bg-cyan-900/10">
        <h4 class="text-cyan-400 font-black text-[9px] uppercase tracking-widest mb-4">Modelo de Stackelberg</h4>
        <p class="text-white text-xs leading-relaxed">
            Juego secuencial donde una empresa es la <strong>líder</strong> y otra la seguidora. La ventaja del líder radica en comprometerse con una cantidad antes que su competidor.
        </p>
    </div>
</section>

<!-- SECTION 3 (DYNAMICS) -->
<section class="mb-24 p-12 bg-violet-600/5 border border-violet-500/10 rounded-[3rem]">
    <h4 class="text-violet-500 font-black text-[10px] uppercase tracking-[0.4em] mb-8 text-center uppercase">Juegos Dinámicos y Repetidos</h4>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-10">
        <div>
            <h5 class="text-white font-bold mb-4">Inducción Hacia Atrás</h5>
            <p class="text-xs text-slate-400 leading-relaxed">Resolución de juegos de información perfecta desde el último periodo hacia el inicio para encontrar el Equilibrio Perfecto en Subjuegos (SPNE).</p>
        </div>
        <div>
            <h5 class="text-white font-bold mb-4">Teoremas Populares</h5>
            <p class="text-xs text-slate-400 leading-relaxed">En juegos repetidos infinitamente, cualquier asignación individualmente racional puede sostenerse como equilibrio mediante estrategias de castigo (Grit-Trigger).</p>
        </div>
    </div>
</section>

<!-- SECTION 3 (MECHANISM DESIGN) -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-violet-500 font-mono text-xs">[02]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Diseño de Mecanismos</h2>
    </div>
    <div class="bg-white/5 border border-white/10 rounded-3xl p-8 space-y-6">
        <p class="text-slate-400 text-sm leading-relaxed">
            "Ingeniería inversa" de la economía: Dado un objetivo social (ej. eficiencia), ¿qué reglas e incentivos debemos diseñar para que los agentes revelen su verdadera información?
        </p>
        <ul class="space-y-4">
            <li class="flex items-center gap-3 text-white text-xs font-bold uppercase tracking-widest">
                <span class="w-1.5 h-1.5 bg-cyan-400 rounded-full"></span>
                Compatibilidad de Incentivos (IC)
            </li>
            <li class="flex items-center gap-3 text-white text-xs font-bold uppercase tracking-widest">
                <span class="w-1.5 h-1.5 bg-cyan-400 rounded-full"></span>
                Racionalidad Individual (IR)
            </li>
        </ul>
    </div>
</section>

<!-- GLOSARIO -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-10">
        <span class="text-purple-500 font-mono text-xs">[GL]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter">Glosario de Modelos Económicos</h2>
    </div>
    <div class="space-y-3">
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-purple-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Expectativas Racionales</span>
            <p class="text-slate-400 text-sm leading-relaxed">Axioma asfixiante y pre-estatuido oráculo y canon dogmático subyugante y purificador postulado implacable donde muchedumbres estadistas e individuos no son entes miopes ciegos desinformados inermes bobos desprovios aturdidos engañabobos fútiles manipulables. Asimilan devoran decodifican integran y sopesan inórganica eficientes exactas simétricas escudriñando esotéricas en sus cálculos neurales absolutamente toda variable exógena filtración anticipación estadística dato historial fútil patente macro predecible arsenal subyacente o filtrada publicitado o empíricamente inferida modelo disponible pública información asintótica ex-ante, imposibilitando fútil y anulando vaciando castigadora esterilizando inofensivamente nula fútil cualquier estéril ilusión política trampa expansiva coyuntural prebendaria subrepticia sorpresa fiduciaria macro populista ingenieril ex-ante inyectada intencionalmente del emisor para distorsionar empujar espasmos o licuar exprimir abismal y desestabilizar real extorsionadora y macro productiva la senda originaria en inyecciones subrepticias nulas irrelevantes absorbidas estériles inoperantes esterilizadas vaciadas ciegamente neutralizadas por blindajes pre-ajustados defensivos auto-ajustados previstos de anticipados contratos y de corazas paritarias o de precios auto-ajustados previsor anticipables blindados neutralizadores elásticos de indexación ex-ante reajustes paralelos blindadores esterilizantes disolventes nulos esterilizadores inmediatos y de disueltas nulas ilusiones previsoras exactas inmunes blindadas y vaciadas.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-purple-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Múltiples Equilibrios</span>
            <p class="text-slate-400 text-sm leading-relaxed">Pantanos y ciénagas laberínticas fractales de indeterminación topográfica ex-ante y abismales lagunas engranajes de indecisión teórica de modelajes no lineales o circulares de expectativas simbióticas conjuntas asimilativas (profecías auto-cumplidas espirales) en que las corazonadas coordinadas conjuncionales empáticas o manadas inorgánicas acopladas sinérgicas de asambleas actitudinales agentes puros derivan y desembocan canalizan arrastran gravitacional asintóticamente al sistema cíclicamente empantanado o arrojado a encallar colisionando anclando dislocándose estabilizado en diversas heterogéneas divergentes polarizadas plurales mesetas atractoras o clímax estabilizadores estáticos pre-dictaminados (ej: euforias esplendorosas de trances exultantes idílicos optimistas utópicos puros estabilizados o abismos dantescos catastróficos fúnebres de corridas lúgubres depresiones pánicos deflacionistas arrastrados pánicos bancarios caóticos deflativos estancados asfixiantes pánicos de corridas bancarias caóticas o postraciones letárgicas estériles y pánicos masivos paralizantes de corralitos ruinosos catastróficos letales absolutos anquilosadores fijos fútiles depresivos trágicos resolutivos irreversibles finales asintóticos subyacentes destructivos aniquiladores).</p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Teoría de Juegos ME4</p>
</footer>

</div>
