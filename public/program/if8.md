<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-emerald-500 rounded-full"></div>
        <span class="text-emerald-400 font-black text-[10px] uppercase tracking-[0.4em]">IF8 · Riesgo de Crédito</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
        DERIVADOS DE<br/>CRÉDITO
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-emerald-500/15 text-emerald-300 border border-emerald-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">CDS</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Hazard Rate · Smile</span>
    </div>
</header>

<!-- SECTION 1 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[01]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Credit Default Swaps (CDS)</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed mb-12">
        <p>
            Un CDS es un seguro contra el incumplimiento de una entidad de referencia. El comprador paga una prima (spread) y el vendedor se compromete a compensar la pérdida si ocurre un evento de crédito.
        </p>
    </div>

    <!-- FORMULA BOX -->
    <div class="px-8 py-12 bg-white/5 border border-white/10 rounded-[3rem] text-center mb-12">
        <div class="text-[10px] font-black text-emerald-500 uppercase tracking-widest mb-6 font-mono">Valuación del CDS Spread</div>
        <div class="text-white text-3xl font-mono mb-6">
            $$\text{Spread} \approx (1 - R) \times \lambda$$
        </div>
        <p class="text-slate-500 text-[10px] uppercase font-bold tracking-widest mt-6">
            $R$: Tasa de Recuperación · $\lambda$: Hazard Rate (Intensidad)
        </p>
    </div>
</section>

<!-- SECTION 2 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[02]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">La Sonrisa de Volatilidad</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed mb-12">
        <p>
            El <strong>Volatility Smile</strong> refleja que las opciones con diferentes precios de ejercicio tienen volatilidades implícitas distintas, desafiando el supuesto de Black-Scholes. En la ingeniería financiera, esto requiere modelos de volatilidad estocástica o de saltos.
        </p>
    </div>
</section>

<!-- SECTION 3 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[03]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Modelo de Merton (Structural Model)</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed mb-12">
        <p>
            El <strong>Modelo de Merton</strong> trata las acciones de una empresa como una opción de compra (call) sobre sus activos totales. El incumplimiento ocurre si al vencimiento el valor de los activos es menor que la deuda nominal.
        </p>
    </div>

    <!-- MERTON VISUALIZATION -->
    <div class="mb-12 rounded-[2.5rem] overflow-hidden border border-white/10">
        <img src="/assets/merton_model_visualization_1771877550219.png" alt="Merton Model Visualization" class="w-full h-auto" />
        <p class="bg-white/5 py-4 text-center text-slate-500 text-[9px] uppercase tracking-widest border-t border-white/10 italic font-mono">
            Figura 1: Valor del Activo vs Umbral de Deuda (Merton Model)
        </p>
    </div>

    <!-- FORMULA BOX -->
    <div class="px-8 py-12 bg-white/5 border border-white/10 rounded-[3rem] text-center mb-12">
        <div class="text-[10px] font-black text-emerald-500 uppercase tracking-widest mb-6 font-mono">Probabilidad de Incumplimiento (PD)</div>
        <div class="text-white text-3xl font-mono mb-6">
            $$PD = N(-d_2)$$
        </div>
        <div class="text-white text-xl font-mono mb-6">
            $$d_2 = \frac{\ln(V_0/D) + (r - \sigma_V^2/2)T}{\sigma_V \sqrt{T}}$$
        </div>
        <p class="text-slate-500 text-[10px] uppercase font-bold tracking-widest mt-6">
            $V_0$: Valor Activos · $D$: Deuda · $\sigma_V$: Volatilidad Activos
        </p>
    </div>
</section>

<!-- SECTION 4 -->
<section class="mb-24 px-12 py-16 bg-white/5 border border-white/10 rounded-[3.5rem]">
    <div class="flex items-center gap-3 mb-10">
        <span class="text-emerald-500 font-mono text-sm uppercase">Correlación de Default</span>
        <h2 class="text-white text-2xl sm:text-3xl font-black tracking-tighter break-words leading-tight">Cópulas Gaussianas</h2>
    </div>
    <p class="text-slate-300 text-sm leading-relaxed mb-8">
        Para valuar derivados de crédito multi-nombre (CDO), se utilizan cópulas para modelar la estructura de dependencia entre los tiempos de incumplimiento de distintos activos sin asumir que siguen una distribución normal individualmente.
    </p>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="p-6 bg-emerald-500/5 border border-emerald-500/20 rounded-2xl">
            <h5 class="text-emerald-400 font-black text-[9px] uppercase tracking-widest mb-3">One-Factor Model</h5>
            <p class="text-slate-500 text-xs">Utilizada en el estándar de mercado para correlacionar los activos mediante un factor latente común (el estado de la economía).</p>
        </div>
        <div class="p-6 bg-emerald-500/5 border border-emerald-500/20 rounded-2xl">
            <h5 class="text-emerald-400 font-black text-[9px] uppercase tracking-widest mb-3">Probabilidad Conjunta</h5>
            <p class="text-slate-500 text-xs">$$C(u, v) = \Phi_2(\Phi^{-1}(u), \Phi^{-1}(v); \rho)$$</p>
        </div>
    </div>
</section>


<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo IF8</h3>
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
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Credit Default Swap (CDS)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Contrato derivado de crédito donde el comprador paga una prima periódica a cambio de una compensación económica del vendedor ante el incumplimiento de una entidad de referencia.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Hazard Rate</span>
            <p class="text-slate-400 text-sm leading-relaxed">Parámetro que mide la intensidad o probabilidad instantánea de incumplimiento de un emisor en un intervalo de tiempo infinitesimal, asumiendo que el evento no ha ocurrido previamente.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Volatility Smile</span>
            <p class="text-slate-400 text-sm leading-relaxed">Patrón que describe cómo la volatilidad implícita de las opciones varía respecto al precio de ejercicio, contradiciendo el supuesto de volatilidad constante del modelo estándar de Black-Scholes.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Modelo de Merton</span>
            <p class="text-slate-400 text-sm leading-relaxed">Modelo estructural que valúa el patrimonio de una empresa como una opción de compra sobre sus activos totales, estableciendo el default cuando el valor de estos cae.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Cópulas Gaussianas</span>
            <p class="text-slate-400 text-sm leading-relaxed">Funciones matemáticas utilizadas para modelar la estructura de dependencia y correlación entre los tiempos de incumplimiento de múltiples activos dentro de una cartera o derivado multi-nombre.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Tasa de Recuperación</span>
            <p class="text-slate-400 text-sm leading-relaxed">Porcentaje del valor nominal de una deuda que el acreedor logra rescatar tras la ocurrencia de un evento de crédito, inversamente relacionado con la severidad de la pérdida.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Probabilidad de Incumplimiento (PD)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Medida estadística que cuantifica la posibilidad de que un deudor sea incapaz de cumplir con sus obligaciones contractuales de pago en un horizonte temporal específico.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Spread de CDS</span>
            <p class="text-slate-400 text-sm leading-relaxed">Prima o diferencial anualizado, expresado generalmente en puntos básicos, que el comprador de protección debe pagar para transferir el riesgo de crédito al vendedor.</p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Ingenieria Financiera IF8</p>
</footer>

</div>
