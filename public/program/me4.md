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



<!-- GLOSARIO -->
<!-- GLOSARIO v9.5 -->
<section id="glosario" class="mt-24 mb-16 relative">
    <div class="flex items-center gap-4 mb-10">
        <div class="w-1.5 h-8 bg-violet-500 rounded-full"></div>
        <h2 class="text-2xl font-black text-white tracking-tight uppercase italic">Glosario Técnico</h2>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 relative z-10">
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Interacción estratégica
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Proceso donde los resultados de las decisiones de los individuos dependen de las acciones de los demás.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Equilibrio de Nash
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Situación en la que ningún jugador tiene incentivos para desviarse unilateralmente de su estrategia, dada la estrategia de los demás.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Competencia de Bertrand
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Modelo de competencia empresarial donde las empresas fijan precios, llevando en el equilibrio básico a precios iguales al coste marginal y beneficios nulos.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Modelo de Stackelberg
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Juego secuencial en el que una empresa líder se compromete con una cantidad antes que su competidor seguidor, obteniendo una ventaja.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Juego secuencial
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Tipo de juego donde los jugadores toman decisiones en un orden preestablecido, como se ilustra en el Modelo de Stackelberg.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Inducción Hacia Atrás
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Método de resolución para juegos de información perfecta que opera desde el último periodo hacia el inicio para identificar el Equilibrio Perfecto en Subjuegos.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Juegos de información perfecta
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Clase de juegos donde todos los movimientos previos son conocidos por los jugadores, permitiendo su resolución mediante inducción hacia atrás.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Estrategias de castigo (Grit-Trigger)
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Estrategias empleadas en juegos repetidos infinitamente para mantener cualquier asignación individualmente racional como un equilibrio.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Juegos repetidos infinitamente
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Juegos que se juegan un número ilimitado de veces, permitiendo que asignaciones individualmente racionales se mantengan como equilibrio a través de estrategias de castigo.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Diseño de Mecanismos
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Enfoque de 'ingeniería inversa' en economía que busca establecer reglas e incentivos para que los agentes revelen su verdadera información, con el fin de alcanzar un objetivo social.
            </p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Teoría de Juegos ME4</p>
</footer>

</div>
