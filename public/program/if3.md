<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-emerald-500 rounded-full"></div>
        <span class="text-emerald-400 font-black text-[10px] uppercase tracking-[0.4em]">IF3 · Módulo Técnico</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
        SWAPS Y<br/>REPORTOS
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-emerald-500/15 text-emerald-300 border border-emerald-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">IRS</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Repo · FRN</span>
    </div>
</header>

<!-- SECTION 1 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[01]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Swaps de Tasas de Interés (IRS)</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed mb-12">
        <p>
            Un swap de tasas de interés es un intercambio de flujos de efectivo donde una parte paga una tasa fija y la otra una tasa flotante. La clave técnica es que el swap se valúa como la diferencia entre un bono de tasa fija y un bono de tasa flotante (FRN).
        </p>
    </div>

    <!-- FORMULA BOX -->
    <div class="px-8 py-12 bg-white/5 border border-white/10 rounded-[3rem] text-center mb-12">
        <div class="text-[10px] font-black text-emerald-500 uppercase tracking-widest mb-6 font-mono">Tasa Swap Par</div>
        <div class="text-white text-3xl font-mono mb-6">
            $$s = \frac{1 - B(t_0, t_n)}{\sum_{i=1}^{n} B(t_0, t_i) \delta}$$
        </div>
        <p class="text-slate-500 text-[10px] uppercase font-bold tracking-widest mt-6">
            $B(t_0, t_i)$: Factores de Descuento · $\delta$: Fracción de año
        </p>
    </div>
</section>

<!-- SECTION 2 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[02]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Mercado de Reportos (Repos)</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed mb-12">
        <p>
            Un Repos (Pacto de Recompra) es la venta de un valor con el compromiso de recompra a un precio y fecha pactados. Económicamente, es un <strong>préstamo colateralizado</strong> donde la tasa repo representa el costo del financiamiento.
        </p>
    </div>

    <!-- GRID -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12 font-mono">
        <div class="p-8 bg-white/5 rounded-3xl border border-white/10">
            <h5 class="text-emerald-500 font-black text-[10px] uppercase tracking-widest mb-4">Uso en Ingeniería</h5>
            <p class="text-slate-300 text-sm">
                Permite la creación de posiciones cortas sintéticas y el apalancamiento de portafolios de renta fija.
            </p>
        </div>
        <div class="p-8 bg-white/5 rounded-3xl border border-white/10">
            <h5 class="text-emerald-500 font-black text-[10px] uppercase tracking-widest mb-4">Costo Implícito</h5>
            <p class="text-slate-300 text-sm">
                Interés = $P_{recompra} - P_{venta}$. La tasa repo es el ancla de la liquidez en mercados QE.
            </p>
        </div>
    </div>
</section>

</section>

<!-- SECTION 3 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[03]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">OIS Discounting & Multicurve</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed mb-12">
        <p>
            Tras la crisis de 2008, el mercado abandonó el descuento único por LIBOR. Hoy se utiliza el <strong>OIS Discounting</strong> (Overnight Index Swap) como proxy de la tasa libre de riesgo, separando la curva de proyección de flujos (LIBOR/Euribor) de la curva de descuento (OIS/SOFR).
        </p>
    </div>

    <!-- FORMULA BOX -->
    <div class="px-8 py-12 bg-white/5 border border-white/10 rounded-[3rem] text-center mb-12">
        <div class="text-[10px] font-black text-emerald-500 uppercase tracking-widest mb-6 font-mono">Valuación Multicurva</div>
        <div class="text-white text-3xl font-mono mb-6">
            $$V = \sum_{i} P_{OIS}(t_0, t_i) \cdot L(t_{i-1}, t_i, \mathcal{F}_{forward}) \cdot \delta$$
        </div>
        <p class="text-slate-500 text-[10px] uppercase font-bold tracking-widest mt-6">
            $P_{OIS}$: Factor de descuento OIS · $L$: Tasa forward LIBOR proyectada
        </p>
    </div>
</section>

<!-- SECTION 4 -->
<section class="mb-24 px-12 py-16 bg-white/5 border border-white/10 rounded-[3.5rem]">
    <div class="flex items-center gap-3 mb-10">
        <span class="text-emerald-500 font-mono text-sm uppercase">Basis Risk</span>
        <h2 class="text-white text-2xl sm:text-3xl font-black tracking-tighter break-words leading-tight">Basis Swaps de Tenor</h2>
    </div>
    <p class="text-slate-300 text-sm leading-relaxed mb-8">
        Los <strong>Basis Swaps</strong> permiten intercambiar flujos de dos tasas flotantes distintas (ej. LIBOR 3M vs LIBOR 6M). El "spread de tenor" refleja el riesgo de liquidez y crédito diferencial entre los plazos, siendo un indicador crítico de estrés financiero.
    </p>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="p-8 border border-white/10 bg-white/5 rounded-3xl">
            <h5 class="text-emerald-500 font-black text-[9px] uppercase mb-4 tracking-widest">Cross-Currency Basis</h5>
            <p class="text-slate-400 text-xs">Intercambio de nominales y flujos en distintas divisas, capturando la escasez relativa de dólares en el mercado global.</p>
        </div>
        <div class="p-8 border border-white/10 bg-white/5 rounded-3xl">
            <h5 class="text-emerald-500 font-black text-[9px] uppercase mb-4 tracking-widest">Ajuste de Convexidad</h5>
            <p class="text-slate-400 text-xs">Necesario cuando la frecuencia de pago no coincide con el periodo de referencia de la tasa (ej. pagos mensuales sobre tasa 3M).</p>
        </div>
    </div>
</section>


<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo IF3</h3>
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
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Swap de Tasas de Interés (IRS)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Contrato derivado donde las partes intercambian flujos de intereses de tasa fija por tasa flotante sobre un capital nocional durante un periodo determinado.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Reporto (Repo)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Operación financiera de venta de valores con el compromiso simultáneo de recomprarlos a un precio y fecha futuros, funcionando como un préstamo colateralizado.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">OIS Discounting</span>
            <p class="text-slate-400 text-sm leading-relaxed">Metodología de valoración que utiliza la tasa de los Overnight Index Swaps para descontar flujos de caja, considerada un proxy preciso de la tasa libre de riesgo.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Basis Swap</span>
            <p class="text-slate-400 text-sm leading-relaxed">Contrato de permuta financiera donde se intercambian dos flujos de intereses calculados sobre tasas variables distintas, permitiendo gestionar riesgos de tenor o divisas.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Ajuste de Convexidad</span>
            <p class="text-slate-400 text-sm leading-relaxed">Corrección técnica aplicada en la valoración de derivados cuando la frecuencia de pago de los intereses no coincide con el periodo de referencia de la tasa.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Tasa Swap Par</span>
            <p class="text-slate-400 text-sm leading-relaxed">Tasa fija que iguala el valor presente de los pagos fijos con el valor presente de los pagos flotantes al inicio del contrato de swap.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Cross-Currency Basis</span>
            <p class="text-slate-400 text-sm leading-relaxed">Diferencial de costo que surge al intercambiar flujos y nominales en distintas divisas, reflejando la escasez relativa de liquidez entre diversos mercados monetarios.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Valuación Multicurva</span>
            <p class="text-slate-400 text-sm leading-relaxed">Marco analítico que separa la curva utilizada para proyectar flujos de caja futuros (tasas forward) de la curva empleada para el descuento de dichos flujos (OIS).</p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Ingenieria Financiera IF3</p>
</footer>

</div>
