<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-emerald-500 rounded-full"></div>
        <span class="text-emerald-400 font-black text-[10px] uppercase tracking-[0.4em]">IF5 · Procesos Estocásticos</span>
    </div>
    <h1 class="text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8">
        SALTOS Y<br/>DIFUSIÓN
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-emerald-500/15 text-emerald-300 border border-emerald-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Poisson</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Merton Jump · Levy</span>
    </div>
</header>

<!-- SECTION 1 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[01]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Limitaciones de la Difusión Pura</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed mb-12">
        <p>
            El Movimiento Browniano Geométrico asume trayectorias continuas. Sin embargo, los precios reales muestran <strong>saltos bruscos</strong> (GAPS) ante noticias o shocks de mercado. Los modelos de difusión puras no capturan las "colas pesadas" de las distribuciones de retorno empíricas.
        </p>
    </div>

    <!-- INSIGHT BOX -->
    <div class="p-8 border border-emerald-500/20 bg-emerald-500/5 rounded-3xl">
        <h4 class="text-emerald-500 font-black text-[10px] uppercase tracking-widest mb-4">Jump-Diffusion de Merton</h4>
        <p class="text-slate-300 text-sm italic">
            Añade un componente de Poisson al proceso de difusión. Los saltos ocurren aleatoriamente y su tamaño sigue una distribución normal.
        </p>
        <div class="mt-6 text-white font-mono text-xl text-center">
            $$dS_t = S_t [ \mu dt + \sigma dW_t + d(\sum_{i=1}^{N_t} (Y_i - 1)) ]$$
        </div>
    </div>
</section>

<!-- SECTION 2 -->
<section class="mb-24 px-12 py-16 bg-white/5 border border-white/10 rounded-[4rem]">
    <div class="flex items-center gap-3 mb-10 text-center justify-center">
        <span class="text-emerald-500 font-mono text-sm uppercase">Colas Pesadas</span>
        <h2 class="text-white text-3xl font-black tracking-tighter">Procesos de Lévy</h2>
    </div>
    <p class="text-slate-300 text-sm leading-relaxed mb-10 text-center">
        Generalizan los procesos estocásticos con incrementos independientes y estacionarios. Permiten modelar la asimetría y el exceso de curtosis sin necesidad de componentes de difusión continua, utilizando procesos de actividad finita o infinita.
    </p>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 font-mono">
        <div class="p-6 bg-white/5 border border-white/10 rounded-2xl">
            <h5 class="text-emerald-500 font-black text-[9px] mb-3">Variance Gamma (VG)</h5>
            <p class="text-slate-400 text-[10px]">Un proceso de subordinación donde el tiempo evoluciona según un proceso gamma, permitiendo una mayor flexibilidad en las colas.</p>
        </div>
        <div class="p-6 bg-white/5 border border-white/10 rounded-2xl">
            <h5 class="text-emerald-500 font-black text-[9px] mb-3">Normal Inverse Gaussian (NIG)</h5>
            <p class="text-slate-400 text-[10px]">Excelente capacidad para ajustar la sonrisa de volatilidad de corto plazo en mercados de divisas y acciones.</p>
        </div>
    </div>
</section>

<!-- SECTION 3 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[03]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Criterio de Sobrefuncionamiento</h2>
    </div>
    <div class="p-10 border border-white/10 rounded-3xl bg-white/5">
        <p class="text-slate-400 text-sm leading-relaxed mb-6">
            Para la gestión de riesgos extremas (Fat-Tailed Risk), es imperativo calibrar los parámetros de salto utilizando datos históricos de crisis, ya que la volatilidad implícita suele subestimar la probabilidad de eventos "Cisne Negro".
        </p>
        <div class="flex items-center gap-4">
            <div class="h-0.5 flex-1 bg-emerald-500/20"></div>
            <span class="text-emerald-500 font-mono text-[10px]">TAIL RISK ANALYSIS</span>
            <div class="h-0.5 flex-1 bg-emerald-500/20"></div>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Ingenieria Financiera IF5</p>
</footer>

</div>
