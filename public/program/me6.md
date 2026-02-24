<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-violet-500 rounded-full"></div>
        <span class="text-violet-400 font-black text-[10px] uppercase tracking-[0.4em]">ME6 · Módulo Computacional</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
        REDES Y<br/>COMPUTACIÓN
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-violet-500/15 text-violet-300 border border-violet-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Network Theory</span>
        <span class="bg-cyan-500/15 text-cyan-300 border border-cyan-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Algoritmos</span>
    </div>
</header>

<!-- INTRO -->
<p class="text-slate-300 text-lg leading-relaxed mb-16">
    La economía no ocurre en el vacío, sino a través de conexiones. Este módulo introduce la ciencia de redes y los métodos computacionales para analizar el contagio financiero, la difusión de innovación y las interacciones sociales complejas.
</p>

<!-- SECTION 1 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-violet-500 font-mono text-xs">[01]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Topología de Redes Económicas</h2>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 my-10">
        <div class="p-8 border border-white/10 rounded-3xl hover:bg-white/5 transition-all">
            <h4 class="text-violet-400 font-black text-[9px] uppercase tracking-widest mb-4">Redes de Suministro</h4>
            <p class="text-white text-xs leading-relaxed font-medium">Modelado de la producción global como un grafo dirigido donde los choques se propagan a través de nodos críticos.</p>
        </div>
        <div class="p-8 border border-white/10 rounded-3xl hover:bg-white/5 transition-all">
            <h4 class="text-cyan-400 font-black text-[9px] uppercase tracking-widest mb-4">Interbancario y Contagio</h4>
            <p class="text-white text-xs leading-relaxed font-medium">Análisis de estabilidad sistémica: Cómo la quiebra de un nodo central puede desencadenar una cascada de insolvencia.</p>
        </div>
    </div>
</section>

<!-- SECTION 2 (ADJACENCY) -->
<section class="mb-24 px-8 py-12 bg-stone-950 border border-white/5 rounded-[3rem] overflow-hidden relative">
    <div class="absolute -top-10 -left-10 w-48 h-48 bg-cyan-500/10 rounded-full blur-3xl"></div>
    <h4 class="text-violet-500 font-black text-[10px] uppercase tracking-[0.4em] mb-10 text-center uppercase">Formalización del Grafo</h4>
    <div class="max-w-md mx-auto aspect-video bg-black/40 rounded-2xl border border-white/5 flex items-center justify-center text-white font-mono text-lg overflow-hidden">
        <div class="grid grid-cols-3 gap-4 opacity-50">
            <span>0</span> <span>1</span> <span>0</span>
            <span>1</span> <span>0</span> <span>1</span>
            <span>0</span> <span>1</span> <span>0</span>
        </div>
    </div>
    <p class="text-slate-500 text-[10px] font-bold leading-relaxed mt-10 text-center uppercase tracking-[0.2em]">Matriz de Adyacencia: Capturando la arquitectura de las interacciones económicas.</p>
</section>

<!-- SECTION 3 (ALGORITHMS) -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-violet-500 font-mono text-xs">[02]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Algoritmos en Economía</h2>
    </div>
    <div class="space-y-4">
        <div class="p-6 bg-white/5 rounded-2xl border border-white/10 flex justify-between items-center group hover:border-violet-500/50 transition-all">
            <span class="text-white font-bold text-sm">Gale-Shapley (Matching)</span>
            <span class="text-slate-600 text-[10px] font-black group-hover:text-violet-400">ESTABLE</span>
        </div>
        <div class="p-6 bg-white/5 rounded-2xl border border-white/10 flex justify-between items-center group hover:border-violet-500/50 transition-all">
            <span class="text-white font-bold text-sm">Vickrey-Clarke-Groves (VCG)</span>
            <span class="text-slate-600 text-[10px] font-black group-hover:text-violet-400">REVELACIÓN</span>
        </div>
        <div class="p-6 bg-white/5 rounded-2xl border border-white/10 flex justify-between items-center group hover:border-violet-500/50 transition-all">
            <span class="text-white font-bold text-sm">Centralidad de PageRank Económico</span>
            <span class="text-slate-600 text-[10px] font-black group-hover:text-violet-400">INFLUENCIA</span>
        </div>
    </div>
</section>


<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">
        <span class="text-lime-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo ME6</h3>
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
                Ciencia de redes
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Disciplina que estudia las conexiones y estructuras de sistemas complejos, aplicando métodos computacionales para analizar fenómenos como el contagio financiero, la difusión de innovación y las interacciones sociales.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Métodos computacionales
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Herramientas y técnicas basadas en la computación utilizadas para analizar y modelar sistemas complejos, como las interacciones económicas y la propagación de fenómenos.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Contagio financiero
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Propagación de crisis o inestabilidad financiera a través de las conexiones de una red económica, donde la falla de un componente puede afectar a otros, desencadenando una cascada de insolvencia.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Difusión de innovación
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Proceso mediante el cual las nuevas ideas, tecnologías o prácticas se propagan a través de las conexiones dentro de un sistema o red.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Topología de Redes Económicas
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Estudio de la estructura y organización de las conexiones dentro de sistemas económicos, como las redes de suministro o interbancarias.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Redes de Suministro
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Modelado de la producción global como un grafo dirigido, donde los choques pueden propagarse a través de sus nodos críticos.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Grafo dirigido
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Estructura matemática utilizada para modelar sistemas, donde las conexiones entre nodos tienen una dirección específica, indicando un flujo o relación unidireccional.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Matriz de Adyacencia
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Representación matricial que describe la conectividad entre los nodos de un grafo, capturando la arquitectura de las interacciones económicas.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Estabilidad sistémica
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Capacidad de un sistema económico para resistir choques y evitar la propagación de fallas, como la quiebra de un nodo central que desencadena una cascada de insolvencia.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Algoritmos en Economía
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Conjunto de reglas computacionales utilizadas para resolver problemas económicos, optimizar procesos o analizar interacciones, como el emparejamiento (Gale-Shapley), la revelación de preferencias (VCG) o la evaluación de influencia (PageRank).
            </p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Redes y Computación ME6</p>
</footer>

</div>
