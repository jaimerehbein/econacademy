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
                Vectores Autorregresivos (VAR)
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Modelos introducidos por Christopher Sims que tratan todas las variables como endógenas, utilizados para el pronóstico económico y el análisis de interacciones dinámicas.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Modelos de Equilibrio General Dinámico Estocástico (DSGE)
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Modelos macroeconómicos basados en microfundamentos, donde los agentes optimizan su comportamiento sujetos a choques estocásticos y fricciones de mercado, siendo el estado del arte en el análisis de bancos centrales.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Modelo IS-LM
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Modelo fundamental que integra el mercado de bienes y servicios con el mercado de activos financieros (dinero), representando el punto de partida del modelado macroeconómico agregado.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Microfundamentos
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Principios que establecen que los modelos macroeconómicos deben derivarse del comportamiento optimizador de agentes económicos individuales (hogares, empresas).
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Choques Estocásticos
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Perturbaciones aleatorias e impredecibles que afectan las variables económicas y el comportamiento de los agentes en los modelos dinámicos, como los DSGE.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Fricciones de Mercado
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Imperfecciones o restricciones en el funcionamiento de los mercados, como los precios rígidos, que impiden el ajuste instantáneo de las variables económicas y afectan la optimización de los agentes.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Funciones de Impulso-Respuesta
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Herramienta analítica que ilustra cómo un choque inesperado en una variable se propaga y afecta a otras variables dentro de un sistema económico a lo largo del tiempo.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Cointegración
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Técnica econométrica para identificar relaciones de equilibrio de largo plazo entre variables no estacionarias que se mueven conjuntamente en el tiempo, separando la dinámica de corto plazo del equilibrio de largo plazo.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                VECM (Vector Error Correction Model)
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Modelo que permite analizar la dinámica de corto plazo y la convergencia hacia el equilibrio de largo plazo entre variables que han sido identificadas como cointegradas.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Regla de Taylor
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Un componente estructural de los modelos DSGE que describe cómo un banco central ajusta la tasa de interés nominal en respuesta a desviaciones de la inflación y la producción respecto a sus objetivos.
            </p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Modelos Macroeconométricos ME5</p>
</footer>

</div>
