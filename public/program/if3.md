<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-emerald-500 rounded-full"></div>
        <span class="text-emerald-400 font-black text-[10px] uppercase tracking-[0.4em]">IF3 · Módulo Técnico</span>
    </div>
    <h1 class="text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8">
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
        <h2 class="text-white text-3xl font-black tracking-tighter">Basis Swaps de Tenor</h2>
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
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-xl">Esquema Conceptual Módulo IF3</h3>
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
    <div class="flex items-center gap-3 mb-10">
        <span class="text-emerald-500 font-mono text-xs">[GL]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter">Glosario del Módulo</h2>
    </div>
    <div class="space-y-3">
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Riesgo Cero (Risk-Free)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Tasa de rendimiento de una inversión que se asume sin riesgo de default, generalmente asociada a bonos del Tesoro de EE.UU.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Prima de Riesgo</span>
            <p class="text-slate-400 text-sm leading-relaxed">El rendimiento adicional que un inversor espera recibir por asumir el riesgo de invertir en un activo en comparación con uno libre de riesgo.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Varianza y Desviación Estándar</span>
            <p class="text-slate-400 text-sm leading-relaxed">Medidas de dispersión de los retornos de un activo. En finanzas clásicas, asimiladas directamente al riesgo total del activo.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Diversificación</span>
            <p class="text-slate-400 text-sm leading-relaxed">Estrategia de gestión de riesgos que mezcla una amplia variedad de inversiones. Reduce el riesgo no sistemático (idiosincrático) del portafolio.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Riesgo Sistemático</span>
            <p class="text-slate-400 text-sm leading-relaxed">Riesgo inherente al mercado en su conjunto. No se puede eliminar mediante diversificación. Medido por Beta.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Riesgo Idiosincrático</span>
            <p class="text-slate-400 text-sm leading-relaxed">Riesgo específico de una empresa o industria. Puede ser eliminado mediante diversificación eficiente.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Covarianza y Correlación</span>
            <p class="text-slate-400 text-sm leading-relaxed">Métricas de cómo dos activos se mueven juntos. Una correlación negativa es el motor principal para la drástica reducción del riesgo de la cartera en Markowitz.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Frontera Eficiente</span>
            <p class="text-slate-400 text-sm leading-relaxed">Curva de los portafolios óptimos de Markowitz que ofrecen el mayor rendimiento esperado para un nivel definido de riesgo o el menor riesgo para un retorno dado.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Capital Allocation Line (CAL)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Gráfico de todas las combinaciones posibles de carteras de un activo libre de riesgo y el portafolio óptimo de activos riesgosos.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Sharpe Ratio</span>
            <p class="text-slate-400 text-sm leading-relaxed">Métrica para evaluar el rendimiento ajustado al riesgo. Calculada como el exceso de retorno sobre la tasa libre de riesgo dividido por la desviación estándar del portafolio.</p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Ingenieria Financiera IF3</p>
</footer>

</div>
