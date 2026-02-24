<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-emerald-500 rounded-full"></div>
        <span class="text-emerald-400 font-black text-[10px] uppercase tracking-[0.4em]">IF5 · Procesos Estocásticos</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
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
        <h2 class="text-white text-2xl sm:text-3xl font-black tracking-tighter break-words leading-tight">Procesos de Lévy</h2>
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


<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo IF5</h3>
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
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Derivado</span>
            <p class="text-slate-400 text-sm leading-relaxed">Contrato financiero cuyo valor estipulado se deriva de un activo subyacente (acciones, índices, materias primas, tasas).</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Contrato Forward</span>
            <p class="text-slate-400 text-sm leading-relaxed">Acuerdo privado bilateral para comprar o vender un activo en una fecha futura a un precio pactado hoy. No estandarizado y con riesgo de contraparte.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Contrato Futuro</span>
            <p class="text-slate-400 text-sm leading-relaxed">Acuerdo estandarizado y negociado en un mercado organizado (Exchange). Mitiga el riesgo de crédito mediante el uso de una cámara de compensación y márgenes diarios.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Opción Call</span>
            <p class="text-slate-400 text-sm leading-relaxed">Contrato que otorga al comprador el DERECHO (no obligación) de COMPRAR el activo subyacente a un precio específico en o antes de una fecha predeterminada.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Opción Put</span>
            <p class="text-slate-400 text-sm leading-relaxed">Contrato que otorga al comprador el DERECHO (no obligación) de VENDER el activo subyacente a un precio especificado en o antes de una fecha futura.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Precio de Ejercicio (Strike)</span>
            <p class="text-slate-400 text-sm leading-relaxed">El precio preestablecido al que el activo subyacente puede ser comprado (call) o vendido (put) al ejercer la opción.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Prima</span>
            <p class="text-slate-400 text-sm leading-relaxed">El costo inicial de adquirir un contrato de opciones pagado por el comprador al vendedor/emisor (Writer).</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">In The Money (ITM)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Condición de una opción que tiene valor intrínseco positivo. Una Call es ITM si Spot > Strike. Una Put es ITM si Spot < Strike.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Moneyness</span>
            <p class="text-slate-400 text-sm leading-relaxed">La clasificación del estado de la opción frente a su ejercicio económico actual: In-the-money (ITM), At-the-money (ATM) u Out-of-the-money (OTM).</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Griegas</span>
            <p class="text-slate-400 text-sm leading-relaxed">Medidas de la sensibilidad del precio de la opción frente a diversas variables. Delta (precio), Gamma (convexidad de Delta), Theta (tiempo), Vega (volatilidad) y Rho (tasa de interés).</p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Ingenieria Financiera IF5</p>
</footer>

</div>
