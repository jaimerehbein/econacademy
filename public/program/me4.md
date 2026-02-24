<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-violet-500 rounded-full"></div>
        <span class="text-violet-400 font-black text-[10px] uppercase tracking-[0.4em]">ME4 · Módulo Estratégico</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
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


<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">
        <span class="text-lime-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo ME4</h3>
    </div>
    <div class="bg-black/30 p-2 md:p-6 rounded-2xl border border-white/5 overflow-x-auto">
        
        <pre class="mermaid bg-transparent flex justify-center">
graph LR
    A[Fundamentos Teóricos] --> B(Aplicación Práctica)
    B --> C{Análisis Crítico}
    C -->|Evaluación| D[Validación Empírica]
    C -->|Revisión| E[Ajuste de Modelo]
    
    classDef default fill:#111827,stroke:#84cc16,stroke-width:1px,color:#d1d5db
    classDef decision fill:#3f6212,stroke:#84cc16,stroke-width:2px,color:#fff
    class C decision
        </pre>

    </div>
</div>


<section id="glosario" class="py-16 bg-white dark:bg-gray-950 transition-colors duration-300">
    <div class="container mx-auto px-6">
        <div class="flex items-center gap-4 mb-12">
            <div class="w-2 h-10 bg-purple-500 rounded-full"></div>
            <h2 class="text-4xl font-bold text-gray-900 dark:text-white">Glosario Académico</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Equilibrio de Nash
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Situación en la cual ningún jugador puede mejorar su utilidad mediante un cambio unilateral de estrategia, dadas las estrategias de los demás participantes.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Competencia de Bertrand
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Modelo de oligopolio donde las empresas compiten fijando precios. En equilibrio, el precio iguala al coste marginal, eliminando los beneficios económicos extraordinarios.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Modelo de Stackelberg
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Juego secuencial donde una empresa líder elige su nivel de producción primero, condicionando la respuesta de las empresas seguidoras en el mercado.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Inducción hacia atrás
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Procedimiento de resolución de juegos dinámicos que consiste en determinar las acciones óptimas desde el último periodo hacia el inicio para hallar equilibrios creíbles.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Diseño de mecanismos
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Rama de la teoría de juegos que busca crear reglas e instituciones que incentiven a los agentes a revelar información privada para alcanzar objetivos sociales.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Compatibilidad de incentivos
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Condición que asegura que los agentes maximicen su propia utilidad al actuar de acuerdo con los objetivos previstos por el diseñador del mecanismo.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Racionalidad individual
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Requisito de participación que garantiza que los agentes obtengan una utilidad al menos tan alta como su mejor alternativa externa al aceptar un contrato o mecanismo.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Equilibrio perfecto en subjuegos
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Refinamiento del equilibrio de Nash aplicable a juegos dinámicos, que exige que las estrategias constituyan un equilibrio de Nash en cada etapa o subjuego posible.
                </p>
            </div>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Teoría de Juegos ME4</p>
</footer>

</div>
