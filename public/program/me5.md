<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-violet-500 rounded-full"></div>
        <span class="text-violet-400 font-black text-[10px] uppercase tracking-[0.4em]">ME5 · Módulo de Validación</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
        MODELOS<br/>MACROECONOMÉTRICOS
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-violet-500/15 text-violet-300 border border-violet-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">DSGE</span>
        <span class="bg-cyan-500/15 text-cyan-300 border border-cyan-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">VAR/Bayesian</span>
    </div>
</header>

<!-- INTRO -->
<p class="text-slate-300 text-lg leading-relaxed mb-16">
    La unión de la teoría macroeconómica con la estadística rigurosa. Este módulo explora desde los vectores autorregresivos (VAR) para pronóstico hasta los modelos de equilibrio general dinámico estocástico (DSGE) que fundamentan la política monetaria moderna.
</p>

<!-- MACRO BASELINE (WIKIPEDIA ENRICHMENT) -->
<section class="mb-24 px-8 py-12 bg-white/5 border border-white/10 rounded-[3rem]">
    <h4 class="text-violet-500 font-black text-[10px] uppercase tracking-[0.4em] mb-8 text-center uppercase">La Síntesis Neoclásica</h4>
    <h3 class="text-white text-3xl font-black tracking-tighter mb-8 text-center">Modelo IS-LM</h3>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
        <div class="space-y-4">
            <p class="text-slate-400 text-xs font-mono">$\text{IS}: Y = C(Y-T) + I(i) + G$</p>
            <p class="text-slate-400 text-xs font-mono">$\text{LM}: M/P = L(i, Y)$</p>
        </div>
        <p class="text-slate-400 text-sm leading-relaxed">
            Representa el punto de partida del modelado agregado, integrando el mercado de bienes y servicios con el mercado de activos financieros (dinero).
        </p>
    </div>
</section>

<!-- SECTION 1 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-violet-500 font-mono text-xs">[01]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Modelos DSGE</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed">
        <p>
            Representan el estado del arte en el análisis de bancos centrales. Se basan en microfundamentos: agentes que optimizan sujetos a choques estocásticos y fricciones de mercado (precios rígidos).
        </p>
        <div class="bg-stone-950 p-10 rounded-[2rem] border border-white/5 space-y-6">
            <h4 class="text-violet-400 font-black text-[10px] uppercase tracking-widest text-center">La Estructura</h4>
            <div class="flex flex-col md:flex-row gap-4 items-center justify-center font-mono text-white text-sm">
                <span class="p-3 border border-white/10 rounded-lg">Euler Conm.</span>
                <span class="text-violet-500">+</span>
                <span class="p-3 border border-white/10 rounded-lg">Curva Phillips</span>
                <span class="text-violet-500">+</span>
                <span class="p-3 border border-white/10 rounded-lg">Regla Taylor</span>
            </div>
        </div>
    </div>
</section>

<!-- SECTION 2 (VAR) -->
<section class="mb-24 grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
    <div class="order-2 md:order-1">
        <div class="p-8 border border-white/10 rounded-3xl bg-white/5">
            <h4 class="text-cyan-400 font-black text-[10px] uppercase tracking-widest mb-4">Vectores Autorregresivos (VAR)</h4>
            <p class="text-white text-xs leading-relaxed mb-6 font-medium text-balance">
                Introducidos por Christopher Sims para evitar las restricciones "increíbles" de los modelos previos. Tratan todas las variables como endógenas.
            </p>
            <div class="text-mono text-violet-300 text-lg text-center font-bold">
                $y_t = A_1 y_{t-1} + ... + A_p y_{t-p} + B \epsilon_t$
            </div>
        </div>
    </div>
    <div class="order-1 md:order-2">
        <h4 class="text-violet-500 font-black text-[10px] uppercase tracking-[0.4em] mb-4">Funciones de Impulso-Respuesta</h4>
        <p class="text-slate-400 text-sm leading-relaxed">
            Permiten visualizar cómo un choque inesperado en una variable (ej. tasa de interés) se propaga a través de todo el sistema económico a lo largo del tiempo.
        </p>
    </div>
</section>

<!-- SECTION 3 (COINTEGRACION) -->
<section class="mb-24 px-8 py-10 border-l-4 border-violet-500 bg-violet-500/5 rounded-r-3xl">
    <h4 class="text-violet-500 font-black text-[9px] uppercase tracking-widest mb-4">Relaciones de Largo Plazo</h4>
    <h3 class="text-white font-bold text-xl mb-4">Cointegración y VECM</h3>
    <p class="text-slate-400 text-xs leading-relaxed">
        Técnicas para modelar variables que caminan juntas en el tiempo (ej. Consumo e Ingreso) a pesar de ser no-estacionarias. Permite separar la dinámica de corto plazo del equilibrio de largo plazo.
    </p>
</section>


<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">
        <span class="text-lime-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo ME5</h3>
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
                    Modelos DSGE
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Sistemas macroeconómicos basados en microfundamentos que analizan el comportamiento agregado mediante la optimización intertemporal de agentes sujetos a choques estocásticos y fricciones de mercado.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Vectores Autorregresivos (VAR)
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Modelos econométricos de series temporales que capturan las interdependencias dinámicas entre múltiples variables, tratándolas todas como endógenas y basándose en sus valores rezagados.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Modelo IS-LM
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Marco macroeconómico de síntesis neoclásica que representa el equilibrio simultáneo en los mercados de bienes y servicios (IS) y de activos financieros (LM).
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Cointegración
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Relación estadística de largo plazo entre variables no estacionarias cuyas series temporales comparten una tendencia común, evitando regresiones espurias en el análisis econométrico.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Funciones de Impulso-Respuesta
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Herramientas que trazan la reacción de las variables endógenas de un sistema ante un choque exógeno transitorio en una de las innovaciones del modelo.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    VECM
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Modelo de Corrección de Errores de Vector que permite estimar la dinámica de corto plazo y el ajuste hacia el equilibrio de largo plazo en sistemas cointegrados.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Regla de Taylor
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Ecuación de política monetaria que prescribe ajustes en la tasa de interés nominal basándose en las desviaciones de la inflación y el producto respecto a sus objetivos.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Microfundamentos
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Bases teóricas que sustentan los modelos macroeconómicos en el comportamiento individual y las decisiones de optimización de hogares y empresas.
                </p>
            </div>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Modelos Macroeconométricos ME5</p>
</footer>

</div>
