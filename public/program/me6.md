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


<section id="glosario" class="py-16 bg-white dark:bg-gray-950 transition-colors duration-300">
    <div class="container mx-auto px-6">
        <div class="flex items-center gap-4 mb-12">
            <div class="w-2 h-10 bg-purple-500 rounded-full"></div>
            <h2 class="text-4xl font-bold text-gray-900 dark:text-white">Glosario Académico</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Ciencia de redes
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Estudio interdisciplinario de sistemas complejos representados como grafos, analizando las propiedades estructurales y dinámicas de las interacciones entre sus componentes interdependientes.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Contagio financiero
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Transmisión de choques económicos o crisis entre instituciones interconectadas, resultando en una propagación de insolvencia a través de vínculos financieros directos o indirectos.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Matriz de adyacencia
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Representación matemática de un grafo mediante una matriz cuadrada, cuyos elementos indican la existencia y magnitud de conexiones entre los pares de nodos.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Algoritmo Gale-Shapley
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Procedimiento algorítmico diseñado para resolver problemas de emparejamiento estable entre dos conjuntos de agentes basándose en sus respectivas jerarquías de preferencias.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Mecanismo VCG
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Protocolo de diseño de mecanismos que garantiza la eficiencia económica al incentivar a los agentes a revelar sus verdaderas valoraciones mediante pagos compensatorios.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Centralidad de PageRank
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Métrica de importancia que cuantifica la influencia de un nodo en una red basándose en la cantidad y calidad de los enlaces recibidos.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Topología de redes
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Configuración estructural de los nodos y enlaces en un sistema, la cual determina la capacidad de difusión y la vulnerabilidad ante choques externos.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Grafo dirigido
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Estructura matemática compuesta por nodos conectados por aristas con una orientación definida, representando flujos unidireccionales de recursos o información.
                </p>
            </div>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Redes y Computación ME6</p>
</footer>

</div>
