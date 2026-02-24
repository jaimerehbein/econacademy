<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-emerald-500 rounded-full"></div>
        <span class="text-emerald-400 font-black text-[10px] uppercase tracking-[0.4em]">IF9 · Productos Estructurados</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
        CAPITAL E<br/>HIPOTECAS
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-emerald-500/15 text-emerald-300 border border-emerald-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Swaptions</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">MBS · Prepago</span>
    </div>
</header>

<!-- SECTION 1 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[01]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Swaptions y Opcionalidad</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed mb-12">
        <p>
            Una swaption es una opción para entrar en un swap de tasas de interés. Son herramientas fundamentales para gestionar la opcionalidad incrustada en productos de deuda y para la ingeniería de flujos de capital protegidos.
        </p>
    </div>

    <!-- FORMULA BOX -->
    <div class="px-8 py-12 bg-white/5 border border-white/10 rounded-[3rem] text-center mb-12">
        <div class="text-[10px] font-black text-emerald-500 uppercase tracking-widest mb-6 font-mono">Fórmula de Black para Swaptions</div>
        <div class="text-white text-2xl font-mono mb-6">
            $$V = A \times [F_{swap} N(d_1) - K N(d_2)]$$
        </div>
        <p class="text-slate-500 text-[10px] uppercase font-bold tracking-widest mt-6">
            $A$: Factor de Anualidad · $F_{swap}$: Tasa Swap Forward
        </p>
    </div>
</section>

<!-- SECTION 2 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[02]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">MBS y Riesgo de Prepago</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed mb-12">
        <p>
            Los Mortgage-Backed Securities (MBS) presentan <strong>convexidad negativa</strong> debido al derecho de los propietarios de viviendas a pagar anticipadamente sus hipotecas cuando las tasas bajan. Este riesgo de prepago se valúa utilizando la teoría de swaptions.
        </p>
    </div>

    <!-- GRID -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12 font-mono">
        <div class="p-8 bg-white/5 rounded-3xl border border-white/10">
            <h5 class="text-emerald-500 font-black text-[10px] uppercase tracking-widest mb-4">CPPI</h5>
            <p class="text-slate-300 text-sm">
                Constant Proportion Portfolio Insurance. Estrategia dinámica para garantizar un piso de capital mientras se participa en mercados de riesgo.
            </p>
        </div>
        <div class="p-8 bg-white/5 rounded-3xl border border-white/10">
            <h5 class="text-emerald-500 font-black text-[10px] uppercase tracking-widest mb-4">Convexidad Negativa</h5>
            <p class="text-slate-300 text-sm">
                Cuando el precio del bono no aumenta de forma lineal ante bajadas de tasas debido a la opcionalidad implícita.
            </p>
        </div>
    </div>
</section>

</section>

<!-- SECTION 3 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[03]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Modelado de Prepago (SMM/CPR)</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed mb-12">
        <p>
            El flujo de caja de un MBS es incierto debido al <strong>Prepago</strong>. Se utilizan métricas estandarizadas como el Single Monthly Mortality (SMM) y el Conditional Prepayment Rate (CPR) para proyectar la velocidad a la que los deudores liquidan sus préstamos, influenciados por incentivos de refinanciación y factores demográficos.
        </p>
    </div>

    <!-- FORMULA BOX -->
    <div class="px-8 py-12 bg-white/5 border border-white/10 rounded-[3rem] text-center mb-12">
        <div class="text-[10px] font-black text-emerald-500 uppercase tracking-widest mb-6 font-mono">Relación SMM-CPR</div>
        <div class="text-white text-3xl font-mono mb-6">
            $$1 - CPR = (1 - SMM)^{12}$$
        </div>
        <p class="text-slate-500 text-[10px] uppercase font-bold tracking-widest mt-6">
            $CPR$: Tasa anualizada · $SMM$: Probabilidad mensual de prepago
        </p>
    </div>
</section>

<!-- SECTION 4 -->
<section class="mb-24 px-12 py-16 bg-white/5 border border-white/10 rounded-[3.5rem]">
    <div class="flex items-center gap-3 mb-10">
        <span class="text-emerald-500 font-mono text-sm uppercase">Cascada de Pagos</span>
        <h2 class="text-white text-2xl sm:text-3xl font-black tracking-tighter break-words leading-tight">Tranche Hierarchy (CMO)</h2>
    </div>
    <p class="text-slate-300 text-sm leading-relaxed mb-8">
        Para gestionar los riesgos, los MBS se estructuran en <strong>Collateralized Mortgage Obligations (CMO)</strong> con diferentes tramos (Tranches). Esto permite redistribuir el riesgo de prepago y crédito según el perfil del inversor.
    </p>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
        <div class="p-6 border border-emerald-500/20 bg-emerald-500/5 rounded-2xl text-center">
            <h5 class="text-white font-black text-[10px]">Senior</h5>
            <p class="text-slate-500 text-[9px] mt-2 italic">Protección máxima. Menor rendimiento.</p>
        </div>
        <div class="p-6 border border-emerald-500/20 bg-emerald-500/5 rounded-2xl text-center">
            <h5 class="text-white font-black text-[10px]">Mezzanine</h5>
            <p class="text-slate-500 text-[9px] mt-2 italic">Riesgo moderado. Absorción intermedia.</p>
        </div>
        <div class="p-6 border border-rose-500/20 bg-rose-500/5 rounded-2xl text-center">
            <h5 class="text-rose-400 font-black text-[10px]">Equity / First Loss</h5>
            <p class="text-slate-500 text-[9px] mt-2 italic">Recibe los primeros impagos. Alto retorno.</p>
        </div>
    </div>

    <!-- MERMAID DIAGRAM -->
    <div class="bg-white/5 p-8 rounded-3xl border border-white/10 mb-8 overflow-hidden">
        <pre class="mermaid bg-transparent flex justify-center">
graph TD
    Collateral[Pool de Hipotecas] --> waterfall{Cascada de Pagos}
    waterfall --> Senior[Tramo Senior A]
    waterfall --> Mezz[Tramo Mezzanine B]
    waterfall --> Equity[Tramo Equity Z]
    
    style Collateral fill:#064e3b,stroke:#10b981,color:#fff
    style waterfall fill:#1e293b,stroke:#94a3b8,color:#fff
    style Senior fill:#064e3b,stroke:#059669,color:#fff
    style Mezz fill:#064e3b,stroke:#059669,color:#fff
    style Equity fill:#450a0a,stroke:#dc2626,color:#fff
        </pre>
        <p class="text-center text-slate-500 text-[9px] uppercase tracking-widest mt-6">Flujo de Caja y Prioridad de Pago (Waterfall Structure)</p>
    </div>
</section>


<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo IF9</h3>
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
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Swaption</span>
            <p class="text-slate-400 text-sm leading-relaxed">Contrato financiero que otorga al tenedor el derecho, pero no la obligación, de entrar en un swap de tasas de interés en una fecha y términos específicos.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Mortgage-Backed Securities (MBS)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Títulos de deuda cuyo colateral y flujos de efectivo provienen de un conjunto de préstamos hipotecarios, transformando activos ilíquidos en valores negociables en mercados secundarios.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Convexidad Negativa</span>
            <p class="text-slate-400 text-sm leading-relaxed">Propiedad de ciertos activos de renta fija donde el aumento del precio es limitado ante caídas en las tasas de interés debido a la opcionalidad de pago anticipado.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Constant Proportion Portfolio Insurance (CPPI)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Estrategia dinámica de gestión de carteras diseñada para garantizar un valor mínimo del capital mediante la reasignación periódica entre activos con riesgo y activos sin riesgo.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Conditional Prepayment Rate (CPR)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Métrica anualizada que representa la proporción del saldo principal de un conjunto de préstamos que se liquida anticipadamente antes de su vencimiento programado.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Collateralized Mortgage Obligation (CMO)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Producto estructurado que segmenta los flujos de caja de un pool de hipotecas en tramos con diferentes niveles de riesgo, prioridad de pago y vencimiento.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Single Monthly Mortality (SMM)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Indicador que mide el porcentaje mensual de reducción del saldo principal de una hipoteca derivado de pagos anticipados, neto de los pagos programados de capital.</p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Ingenieria Financiera IF9</p>
</footer>

</div>
