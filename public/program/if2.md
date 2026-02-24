<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-emerald-500 rounded-full"></div>
        <span class="text-emerald-400 font-black text-[10px] uppercase tracking-[0.4em]">IF2 · Módulo Técnico</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
        FORWARDS Y<br/>TASAS
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-emerald-500/15 text-emerald-300 border border-emerald-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">FRA</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">No-Arbitraje · FX Forward</span>
    </div>
</header>

<!-- SECTION 1 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[01]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Precio Forward de Divisas</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed mb-12">
        <p>
            El precio forward no es una predicción del futuro, sino un precio de <strong>no-arbitraje</strong> determinado por el diferencial de tasas de interés entre dos monedas.
        </p>
    </div>

    <!-- FORMULA BOX -->
    <div class="px-8 py-12 bg-white/5 border border-white/10 rounded-[3rem] text-center mb-12">
        <div class="text-[10px] font-black text-emerald-500 uppercase tracking-widest mb-6 font-mono">Interest Rate Parity</div>
        <div class="text-white text-3xl font-mono mb-6">
            $$F_{t_0} = e_{t_0} \frac{1 + r_d \delta}{1 + r_f \delta}$$
        </div>
        <p class="text-slate-500 text-[10px] uppercase font-bold tracking-widest mt-6">
            $e_{t_0}$: Spot · $r_d$: Tasa Doméstica · $r_f$: Tasa Foránea
        </p>
    </div>
</section>

<!-- SECTION 2 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[02]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Forward Rate Agreements (FRA)</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed mb-12">
        <p>
            Un FRA es un contrato para fijar una tasa de interés que se aplicará en un periodo futuro. Se liquida por la diferencia entre la tasa pactada y la tasa de mercado (ej. Libor) observada al inicio del periodo del préstamo.
        </p>
        <div class="p-8 bg-emerald-500/10 border-l-4 border-emerald-500 rounded-r-2xl italic text-slate-200">
            "El FRA es el bloque constructivo para la cobertura de riesgos de tasas de interés y la creación de swaps."
        </div>
    </div>

    <div class="bg-white/5 border border-white/10 p-12 rounded-[3rem]">
        <h4 class="text-emerald-400 font-black text-xs uppercase tracking-widest mb-8">Fórmula del Pago del FRA</h4>
        <div class="text-white text-2xl font-mono mb-8">
            $$\text{Pago} = N \times \frac{(L - F) \times \delta}{1 + L \times \delta}$$
        </div>
        <p class="text-slate-500 text-xs leading-relaxed font-medium">
            Donde $L$ es la tasa Libor, $F$ la tasa pactada y $\delta$ la fracción de año. El descuento $(1 + L\delta)$ ocurre porque el pago se realiza al inicio del periodo.
        </p>
    </div>
</section>

<!-- SUMMARY BOX -->
<section class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-24 font-mono">
    <div class="p-8 bg-white/5 rounded-3xl border border-white/10">
        <h5 class="text-emerald-500 font-black text-[10px] uppercase tracking-widest mb-4">Concepto Clave</h5>
        <p class="text-slate-300 text-sm">
            Tasa Forward Implícita: La tasa que iguala la inversión en un bono largo con la reinversión en dos bonos cortos consecutivos.
        </p>
    </div>
    <div class="p-8 bg-white/5 rounded-3xl border border-white/10">
        <h5 class="text-emerald-500 font-black text-[10px] uppercase tracking-widest mb-4">Arbitraje</h5>
        <p class="text-slate-300 text-sm">
            Si el precio forward se desvía de la fórmula, existe una oportunidad de arbitraje de "cash and carry".
        </p>
    </div>
</section>


<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo IF2</h3>
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
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Precio Forward de Divisas</span>
            <p class="text-slate-400 text-sm leading-relaxed">Precio de intercambio de monedas en una fecha futura, determinado por el diferencial de tasas de interés entre dos divisas bajo la condición de no-arbitraje.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">No-arbitraje</span>
            <p class="text-slate-400 text-sm leading-relaxed">Principio financiero que establece que, en mercados eficientes, no es posible obtener beneficios consistentes sin riesgo mediante la combinación de instrumentos financieros con precios desalineados.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Paridad de Tasas de Interés</span>
            <p class="text-slate-400 text-sm leading-relaxed">Relación teórica que iguala el diferencial de tasas de interés entre dos países con la diferencia porcentual entre el tipo de cambio spot y el tipo de cambio forward.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Forward Rate Agreement (FRA)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Contrato derivado donde las partes fijan una tasa de interés para un periodo futuro, liquidándose mediante el pago de la diferencia entre la tasa pactada y la de mercado.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Tasa Forward Implícita</span>
            <p class="text-slate-400 text-sm leading-relaxed">Tasa de interés proyectada para un periodo futuro, calculada a partir de las tasas spot actuales para que el rendimiento total sea indiferente entre plazos cortos y largos.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Arbitraje Cash and Carry</span>
            <p class="text-slate-400 text-sm leading-relaxed">Estrategia financiera que consiste en comprar un activo en el mercado spot y vender simultáneamente un contrato forward para aprovechar discrepancias en los precios de mercado.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Tasa Spot</span>
            <p class="text-slate-400 text-sm leading-relaxed">Tipo de cambio o precio de mercado vigente para la liquidación inmediata de un activo financiero o divisa en el momento de la operación.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Diferencial de Tasas</span>
            <p class="text-slate-400 text-sm leading-relaxed">Diferencia aritmética entre los tipos de interés de dos economías distintas, que constituye el factor determinante en la valoración de contratos forward de divisas.</p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Ingenieria Financiera IF2</p>
</footer>

</div>
