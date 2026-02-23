<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-violet-500 rounded-full"></div>
        <span class="text-violet-400 font-black text-[10px] uppercase tracking-[0.4em]">ME5 · Módulo de Validación</span>
    </div>
    <h1 class="text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8">
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

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Modelos Macroeconométricos ME5</p>
</footer>

</div>
