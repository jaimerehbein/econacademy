<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-emerald-500 rounded-full"></div>
        <span class="text-emerald-400 font-black text-[10px] uppercase tracking-[0.4em]">IF9 · Productos Estructurados</span>
    </div>
    <h1 class="text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8">
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
        <h2 class="text-white text-3xl font-black tracking-tighter">Tranche Hierarchy (CMO)</h2>
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
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-xl">Esquema Conceptual Módulo IF9</h3>
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
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[120px] pt-0.5">Hipoteca</span>
            <p class="text-slate-400 text-sm leading-relaxed">Préstamo garantizado por un inmueble. Si el deudor incumple, el acreedor puede ejecutar el bien. Base de toda la cadena de titulización MBS.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[120px] pt-0.5">Titulización</span>
            <p class="text-slate-400 text-sm leading-relaxed">Proceso de agrupar activos ilíquidos (hipotecas) y convertirlos en títulos negociables en el mercado de capitales, transfiriendo el riesgo del originador al inversor.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[120px] pt-0.5">MBS</span>
            <p class="text-slate-400 text-sm leading-relaxed">Mortgage-Backed Security. Bono respaldado por un pool de hipotecas. Los pagos mensuales de los deudores (principal + interés) fluyen hacia los tenedores del MBS.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[120px] pt-0.5">Riesgo de Prepago</span>
            <p class="text-slate-400 text-sm leading-relaxed">Posibilidad de que los deudores paguen anticipadamente cuando las tasas bajan. El inversor en MBS recibe el principal antes de lo esperado a un momento inconveniente para reinvertir.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[120px] pt-0.5">SMM / CPR</span>
            <p class="text-slate-400 text-sm leading-relaxed">Single Monthly Mortality / Conditional Prepayment Rate. Métricas de velocidad de prepago. CPR anual se relaciona con SMM mediante: $CPR = 1 - (1-SMM)^{12}$.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[120px] pt-0.5">PSA Benchmark</span>
            <p class="text-slate-400 text-sm leading-relaxed">Modelo estándar del mercado americano de hipotecas. Asume que los prepagos crecen 0.2% mensual durante los primeros 30 meses hasta alcanzar el 6% CPR anual constante.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[120px] pt-0.5">CMO</span>
            <p class="text-slate-400 text-sm leading-relaxed">Collateralized Mortgage Obligation. Estructura que reempaqueta MBS en tramos (tranches) con distintas prioridades de pago, riesgo y rendimiento esperado.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[120px] pt-0.5">Tramo Senior</span>
            <p class="text-slate-400 text-sm leading-relaxed">El primer tramo en recibir los pagos del pool. Tiene la mayor protección crediticia (credit enhancement). Por ello, recibe el menor retorno.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[120px] pt-0.5">Tramo Equity</span>
            <p class="text-slate-400 text-sm leading-relaxed">First Loss Piece. Absorbe las primeras pérdidas del pool. Alto riesgo, alto retorno potencial. Generalmente retenido por el originador como señal de alineación de incentivos.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[120px] pt-0.5">Waterfall</span>
            <p class="text-slate-400 text-sm leading-relaxed">Regla de distribución de flujos de caja en un CMO. Los pagos fluyen de Senior a Mezzanine a Equity en order estricto de prioridad, como el agua cayendo por una cascada.</p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Ingenieria Financiera IF9</p>
</footer>

</div>
