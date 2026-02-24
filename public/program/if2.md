<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-emerald-500 rounded-full"></div>
        <span class="text-emerald-400 font-black text-[10px] uppercase tracking-[0.4em]">IF2 · Módulo Técnico</span>
    </div>
    <h1 class="text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8">
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

<!-- GLOSARIO -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-10">
        <span class="text-emerald-500 font-mono text-xs">[GL]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter">Glosario del Módulo</h2>
    </div>
    <div class="space-y-3">
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Bono</span>
            <p class="text-slate-400 text-sm leading-relaxed">Instrumento de deuda emitido por una entidad (gobierno o corporación) para financiarse. El emisor promete devolver el principal y pagar intereses (cupones).</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Cupón</span>
            <p class="text-slate-400 text-sm leading-relaxed">El pago periódico de intereses que el emisor de un bono realiza a los tenedores. Típicamente expresado como un porcentaje del valor nominal.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Valor Nominal (Face Value)</span>
            <p class="text-slate-400 text-sm leading-relaxed">La cantidad que el emisor acuerda devolver al inversor en la fecha de vencimiento del bono. Generalmente base para el cálculo del cupón.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">YTM (Yield to Maturity)</span>
            <p class="text-slate-400 text-sm leading-relaxed">La tasa de retorno total anticipada en un bono si se mantiene hasta el vencimiento. Iguala el precio actual con el valor presente de los flujos futuros.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Precio Sucio vs Limpio</span>
            <p class="text-slate-400 text-sm leading-relaxed">El Precio Limpio es el precio del bono sin los intereses devengados. El Precio Sucio (invoice price) incluye el interés acumulado desde el último pago de cupón.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Bono a Descuento</span>
            <p class="text-slate-400 text-sm leading-relaxed">Un bono que se negocia por debajo de su valor nominal. Ocurre cuando su tasa cupón es menor que el YTM exigido por el mercado.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Bono con Prima</span>
            <p class="text-slate-400 text-sm leading-relaxed">Bono que se negocia por encima de su valor nominal. Ocurre cuando su tasa cupón es mayor que la tasa de rendimiento requerida (YTM).</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Duración de Macaulay</span>
            <p class="text-slate-400 text-sm leading-relaxed">Media ponderada del tiempo en que se reciben los flujos de caja del bono. Medida del riesgo de tasa de interés.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Duración Modificada</span>
            <p class="text-slate-400 text-sm leading-relaxed">Aproximación de la sensibilidad asintótica del precio de un bono ante cambios porcentuales en el YTM. Ecuación: $\\Delta P/P pprox -D_{mod} \\cdot \\Delta y$.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Convexidad</span>
            <p class="text-slate-400 text-sm leading-relaxed">La curvatura de la relación entre el precio de un bono y su rendimiento. La duración es una aproximación tangencial (lineal); la convexidad corrige la curvatura para grandes cambios de tasas.</p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Ingenieria Financiera IF2</p>
</footer>

</div>
