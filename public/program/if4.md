<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-emerald-500 rounded-full"></div>
        <span class="text-emerald-400 font-black text-[10px] uppercase tracking-[0.4em]">IF4 · Algoritmo Dinámico</span>
    </div>
    <h1 class="text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8">
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
        <h2 class="text-white text-3xl font-black tracking-tighter">Costos de Transacción</h2>
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

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Ingenieria Financiera IF4</p>
</footer>

</div>
