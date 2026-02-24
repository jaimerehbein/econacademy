<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-emerald-500 rounded-full"></div>
        <span class="text-emerald-400 font-black text-[10px] uppercase tracking-[0.4em]">IF4 · Algoritmo Dinámico</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
        REPLICACIÓN<br/>DINÁMICA
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-emerald-500/15 text-emerald-300 border border-emerald-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Delta Hedging</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Autofinanciado</span>
    </div>
</header>

<!-- SECTION 1 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[01]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">El Portafolio Replicante</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed mb-12">
        <p>
            A diferencia de la replicación estática, donde los pesos se mantienen fijos, la <strong>replicación dinámica</strong> requiere reajustes continuos para igualar las sensibilidades del activo objetivo ante cambios en el precio del subyacente y el paso del tiempo.
        </p>
    </div>

    <!-- FORMULA BOX -->
    <div class="px-8 py-12 bg-white/5 border border-white/10 rounded-[3rem] text-center mb-12">
        <div class="text-[10px] font-black text-emerald-500 uppercase tracking-widest mb-6 font-mono">Ecuación de Composición</div>
        <div class="text-white text-3xl font-mono mb-6">
            $$\theta_{stock} S_t + \theta_{bond} B_t = V_{opción}$$
        </div>
        <p class="text-slate-500 text-[10px] uppercase font-bold tracking-widest mt-6">
            $\theta$: Cantidad de activos · $S_t$: Precio subyacente · $B_t$: Bono libre de riesgo
        </p>
    </div>
</section>

<!-- SECTION 2 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[02]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Condición de Autofinanciamiento</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed mb-12">
        <p>
            Un portafolio es autofinanciado si después del inicio no se inyecta ni se retira capital. Los cambios en los pesos $(\theta)$ se financian exclusivamente vendiendo un activo para comprar el otro.
        </p>
        <div class="bg-emerald-500/10 border-l-4 border-emerald-500 p-8 rounded-r-2xl italic text-slate-200">
            "En tiempo discreto (Árboles Binomiales), el valor del portafolio al final de un periodo debe ser igual al valor del nuevo portafolio rebalanceado."
        </div>
    </div>
</section>

</section>

<!-- SECTION 3 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[03]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Método Vanna-Volga</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed mb-12">
        <p>
            En mercados reales, la superficie de volatilidad no es plana. El método <strong>Vanna-Volga</strong> se utiliza para ajustar el precio de Black-Scholes capturando los riesgos de segundo orden: <strong>Vanna</strong> (sensibilidad del Vega al subyacente) y <strong>Volga</strong> (sensibilidad del Vega a la volatilidad).
        </p>
    </div>

    <!-- FORMULA BOX -->
    <div class="px-8 py-12 bg-white/5 border border-white/10 rounded-[3rem] text-center mb-12 font-mono">
        <div class="text-[10px] font-black text-emerald-500 uppercase tracking-widest mb-6 font-mono">Ajuste de Sonrisa (Smile Cost)</div>
        <div class="text-white text-xl mb-4">
            $$V_{VV} = V_{BS} + \omega_{vega} Vega + \omega_{vanna} Vanna + \omega_{volga} Volga$$
        </div>
        <p class="text-slate-500 text-[10px] uppercase font-bold tracking-widest mt-6">
            Captura el costo de replicar la convexidad de la volatilidad.
        </p>
    </div>
</section>

<!-- SECTION 4 -->
<section class="mb-24 px-12 py-16 bg-white/5 border border-white/10 rounded-[3.5rem]">
    <div class="flex items-center gap-3 mb-10">
        <span class="text-emerald-500 font-mono text-sm uppercase">Fricciones</span>
        <h2 class="text-white text-2xl sm:text-3xl font-black tracking-tighter break-words leading-tight">Costos de Transacción</h2>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-10">
        <p class="text-slate-300 text-sm leading-relaxed">
            La replicación continua es imposible debido a los costos de transacción (bid-ask spread). El modelo de <strong>Leland</strong> ajusta la volatilidad de Black-Scholes para incluir estos costos, penalizando las estrategias que requieren reajustes frecuentes.
        </p>
        <div class="p-8 bg-emerald-900/10 border border-emerald-500/20 rounded-3xl">
            <h5 class="text-emerald-500 font-black text-[9px] uppercase tracking-widest mb-4">Volatilidad de Leland</h5>
            <p class="text-white font-mono text-lg">$$\sigma^2_{L} = \sigma^2 \left( 1 + \sqrt{\frac{2}{\pi}} \frac{k}{\sigma \sqrt{\Delta t}} \right)$$</p>
            <p class="text-slate-500 text-[9px] mt-4 font-mono">$k$: Costo proporcional · $\Delta t$: Intervalo de rebalanceo</p>
        </div>
    </div>
</section>


<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo IF4</h3>
    </div>
    <div class="bg-black/30 p-2 md:p-6 rounded-2xl border border-white/5 overflow-x-auto">
        
        <pre class="mermaid bg-transparent flex justify-center">
graph LR
    A[Fundamentos Teóricos] --> B(Aplicación Práctica)
    B --> C{Análisis Crítico}
    C -->|Evaluación| D[Validación Empírica]
    C -->|Revisión| E[Ajuste de Modelo]
    
    classDef default fill:#111827,stroke:#10b981,stroke-width:1px,color:#d1d5db
    classDef decision fill:#064e3b,stroke:#10b981,stroke-width:2px,color:#fff
    class C decision
        </pre>

    </div>
</div>

<!-- GLOSARIO -->
<section class="mb-24">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-10">
        <span class="text-emerald-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[GL]</span>
        <h2 class="text-white font-black text-xl sm:text-2xl uppercase tracking-tighter break-words leading-tight">Glosario del Módulo</h2>
    </div>
    <div class="space-y-3">
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">CAPM</span>
            <p class="text-slate-400 text-sm leading-relaxed">Capital Asset Pricing Model. Modelo que describe la relación entre el riesgo sistemático y el rendimiento esperado de los activos. $E(R_i) = R_f + \\beta_i (E(R_m) - R_f)$.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Beta (β)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Medida de la volatilidad o riesgo de un activo en relación con el mercado en general. Un Beta de 1 implica que el activo se mueve junto con el mercado.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Alfa de Jensen (α)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Rendimiento excesivo ajustado por riesgo en comparación con la ganancia predictiva del modelo CAPM. Un Alfa positivo indica un rendimiento superior al esperado para su nivel de riesgo sistemático.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">CML (Capital Market Line)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Representa las carteras que combinan óptimamente riesgos y retornos cuando el activo libre de riesgo se une con la cartera de mercado.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">SML (Security Market Line)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Línea que representa gráficamente el modelo CAPM. Muestra la relación entre riesgo sistemático (Beta) y retorno esperado para valores individuales.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Arbitrage Pricing Theory (APT)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Modelo alternativo al CAPM para la fijación de precios de activos que postula retornos como función lineal de múltiples factores macroeconómicos estructurales.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Eficiencia Débil</span>
            <p class="text-slate-400 text-sm leading-relaxed">Nivel de la Hipótesis del Mercado Eficiente que sostiene que los precios reflejan toda la información histórica; el análisis técnico no genera alfa continuo.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Eficiencia Semifuerte</span>
            <p class="text-slate-400 text-sm leading-relaxed">Nivel donde los precios reflejan instantáneamente toda la información pública (balances, noticias). Invalida el análisis fundamental tradicional para lograr alfa.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Eficiencia Fuerte</span>
            <p class="text-slate-400 text-sm leading-relaxed">Postulado empíricamente cuestionado donde los precios reflejan toda información pública y privada (insider trading).</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Anomalías de Mercado</span>
            <p class="text-slate-400 text-sm leading-relaxed">Patrones empíricos inexplicados por el CAPM (ej. efecto tamaño, valor vs crecimiento, momentum) que abrieron paso a la ampliación factorial (Fama-French).</p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Ingenieria Financiera IF4</p>
</footer>

</div>
