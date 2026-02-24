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

<!-- GLOSARIO -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-10">
        <span class="text-purple-500 font-mono text-xs">[GL]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter">Glosario de Modelos Económicos</h2>
    </div>
    <div class="space-y-3">
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-purple-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Choques Estocásticos</span>
            <p class="text-slate-400 text-sm leading-relaxed">Convulsiones o espasmos latentes incontrolables vibraciones impredecibles aleatorias telúricas o azarosas disrupciones inasibles que azotan acribillando y bombardeando incesante o irrumpiendo exógicamente los asintóticos letargos de los modelos macroeconómicos (ej. cataclismos climáticos fulminantes inusitados inyectando o mermando la productividad agrícola o histerias pandémicas infartando redes operativas). Son la simiente basal purificada detonadora que eyecta al ecosistema y la órbita de su tumba inerte estacionaria forzando volatilidades dinámicas febriles oscilantes cíclicas.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-purple-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Filtro de Kalman</span>
            <p class="text-slate-400 text-sm leading-relaxed">Herramienta algorítmica oracular matemática y radar depurador estocástico supremo de inferencia estadística dinámica para escudriñar escanear limpiar decantar purificar y desentrañar asintomática la trayectoria pura oculta e inescrutable de una variable subyacente inobservada (ej. producto potencial o tasa natural latente) a partir de un aluvión nebuloso ensordecedor distorsionado de señales fácticas sucias o datas empíricas ruidosas volátiles plagadas preñadas de imperfecciones o errores de medición de corto aliento.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-purple-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Proceso de Márkov</span>
            <p class="text-slate-400 text-sm leading-relaxed">Arquitectura estocástica dogmática determinista-probabilista estipulando que el devenir fáctico de la transición de mañana o futuro mediato asimila y gravita irremediablemente pende enraizada y acoplada a merced en grilletes exclusiva aislada y estricta asimétricamente del ecosistema posicional o estado factual que el sistema exhibe, impera e inmoviliza estrictamente hoy, decapitada y escindida eximiendo y amnésica borrando ignorando aniquilando despojando exenta e irrelevante de forma total la memoria atávica lastres empíricos arrastres preestablecidos o sendas de la génesis pasada inmutable originaria exógena.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-purple-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Linealización Logarítmica (Log-Linear)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Artificio transmutador quirúrgico algebraico alquimia matemática para amordazar domar anestesiar y escindir las fútiles letalidades computacionales inmanejables insolucionables salvajes inestables u oprimentes de ecuaciones no lineales abismales intrincadas monstruosas. Transfigurando transigiendo y aplanando asimétrica las órbitas en variaciones fraccionales desviaciones elásticas suaves dóciles domadas aproximadas porcentuales adyacentes llanas en las inmediateces colindantes tangenciales al seguro asintótico estado estacionario inerte pacifico ancla.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-purple-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Vectores Autorregresivos (VAR)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Poderío y escáner macro-econométrico aglutinante agnóstico metodológico que agrupa engloba amalgama e interpola en un bloque matricial sinfónico simultáneo indisoluble una amalgama simbiótica coral pluralizada colindante de series temporales endógenas permitiendo dictaminar ex-post auscultar rastrear y proyectar cómo un bombardeo o impulso un choque exógeno único purificado impacta rezagado percutiendo rebotando diseminado asfixiado arrastrando encadenante a la integridad coral holística predeterminada sin presuponer y asumiendo coactivamente dictadura de rigideces estructurales previas inmanentes opresoras.</p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Modelos Macroeconométricos ME5</p>
</footer>

</div>
