<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-emerald-500 rounded-full"></div>
        <span class="text-emerald-400 font-black text-[10px] uppercase tracking-[0.4em]">IF6 · Probabilidad Avanzada</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
        VALUACIÓN Y<br/>MARTINGALAS
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-emerald-500/15 text-emerald-300 border border-emerald-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Medida Q</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Numeraire · Monte Carlo</span>
    </div>
</header>

<!-- SECTION 1 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[01]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Teorema Fundamental de Valuación</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed mb-12">
        <p>
            El primer teorema fundamental establece que un mercado es libre de arbitraje si y solo si existe al menos una <strong>medida de probabilidad neutral al riesgo (martingala)</strong> $Q$ bajo la cual los precios de los activos descontados son martingalas.
        </p>
    </div>

    <!-- FORMULA BOX -->
    <div class="px-8 py-12 bg-white/5 border border-white/10 rounded-[4rem] text-center mb-12">
        <div class="text-[10px] font-black text-emerald-500 uppercase tracking-widest mb-6 font-mono">Expectativa bajo la Medida Q</div>
        <div class="text-white text-3xl font-mono mb-6">
            $$P_t = E^Q [ e^{-\int_t^T r_u du} X_T | \mathcal{F}_t ]$$
        </div>
        <p class="text-slate-500 text-xs leading-relaxed max-w-lg mx-auto italic">
            El precio hoy es el valor esperado del pago futuro descontado a la tasa libre de riesgo, calculado bajo la probabilidad neutral al riesgo.
        </p>
    </div>
</section>

<!-- SECTION 2 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[02]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Cambio de Numeraire</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed mb-12">
        <p>
            Un <strong>numeraire</strong> es un activo utilizado para medir el valor de otros. El cambio de numeraire (ej. de efectivo a bono cupón cero) facilita enormemente la valuación de productos complejos como swaptions mediante el ajuste de la medida de probabilidad.
        </p>
    </div>
</section>

</section>

<!-- SECTION 3 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[03]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Teorema de Girsanov</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed mb-12">
        <p>
            El <strong>Teorema de Girsanov</strong> especifica cómo cambia el proceso de Wiener cuando cambiamos de la medida de mundo real ($P$) a la medida neutral al riesgo ($Q$). Es la herramienta fundamental para derivar precios de derivados sin arbitraje.
        </p>
    </div>

    <!-- GIRSANOV VISUALIZATION -->
    <div class="mb-12 rounded-[2.5rem] overflow-hidden border border-white/10">
        <img src="/assets/girsanov_measure_shift_visualization_1771877565177.png" alt="Girsanov Measure Shift" class="w-full h-auto" />
        <p class="bg-white/5 py-4 text-center text-slate-500 text-[9px] uppercase tracking-widest border-t border-white/10 italic font-mono">
            Figura 2: Cambio de Medida de Probabilidad ($dQ/dP$)
        </p>
    </div>

    <!-- FORMULA BOX -->
    <div class="px-8 py-12 bg-white/5 border border-white/10 rounded-[3rem] text-center mb-12">
        <div class="text-[10px] font-black text-emerald-500 uppercase tracking-widest mb-6 font-mono">Derivada de Radon-Nikodym</div>
        <div class="text-white text-3xl font-mono mb-6">
            $$\frac{dQ}{dP} = \exp \left( -\int_0^T \theta_t dW_t - \frac{1}{2} \int_0^T \theta_t^2 dt \right)$$
        </div>
        <p class="text-slate-500 text-[10px] uppercase font-bold tracking-widest mt-6">
            $\theta_t = \frac{\mu - r}{\sigma}$: Market Price of Risk
        </p>
    </div>
</section>

<!-- SECTION 4 -->
<section class="mb-24 px-12 py-16 bg-white/5 border border-white/10 rounded-[3.5rem]">
    <div class="flex items-center gap-3 mb-10">
        <span class="text-emerald-500 font-mono text-sm uppercase">Link Probabilístico</span>
        <h2 class="text-white text-2xl sm:text-3xl font-black tracking-tighter break-words leading-tight">Fórmula de Feynman-Kac</h2>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
        <p class="text-slate-300 text-sm leading-relaxed">
            Establece una conexión profunda entre las Ecuaciones Diferenciales Parciales (EDP) y los procesos estocásticos. Demuestra que la solución de una EDP parabólica (como Black-Scholes) puede representarse como una esperanza condicionada.
        </p>
        <div class="p-8 border border-emerald-500/20 bg-emerald-500/5 rounded-3xl text-center">
            <h4 class="text-white font-mono text-lg mb-4">EDP ↔ Valor Esperado</h4>
            <div class="text-emerald-400 font-mono text-sm italic">
                La derivada temporal + el generador infinitesimal del proceso = 0
            </div>
        </div>
    </div>
</section>


<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo IF6</h3>
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
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Martingala</span>
            <p class="text-slate-400 text-sm leading-relaxed">Proceso estocástico cuya esperanza condicional futura, dada la información disponible en el presente, es idéntica a su valor actual, fundamental para la modelización de mercados sin arbitraje.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Medida de Probabilidad Neutral al Riesgo</span>
            <p class="text-slate-400 text-sm leading-relaxed">Medida bajo la cual el valor esperado descontado de un activo financiero es una martingala, permitiendo valuar derivados utilizando la tasa de interés libre de riesgo.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Arbitraje</span>
            <p class="text-slate-400 text-sm leading-relaxed">Operación financiera que genera beneficios sin riesgo ni inversión neta inicial mediante el aprovechamiento de ineficiencias de precios en diferentes mercados o instrumentos.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Numeraire</span>
            <p class="text-slate-400 text-sm leading-relaxed">Activo financiero negociable y estrictamente positivo cuyo precio se utiliza para normalizar el valor de otros activos, facilitando el cálculo de expectativas bajo distintas medidas de probabilidad.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Teorema de Girsanov</span>
            <p class="text-slate-400 text-sm leading-relaxed">Resultado matemático que especifica cómo se transforma la deriva de un proceso estocástico al cambiar de medida de probabilidad, manteniendo la equivalencia entre dichas medidas.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Derivada de Radon-Nikodym</span>
            <p class="text-slate-400 text-sm leading-relaxed">Función que describe la tasa de cambio entre dos medidas de probabilidad, permitiendo la transición matemática entre la medida estadística real y la medida neutral al riesgo.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Fórmula de Feynman-Kac</span>
            <p class="text-slate-400 text-sm leading-relaxed">Teorema que establece un vínculo formal entre las ecuaciones diferenciales parciales parabólicas y los procesos estocásticos, representando soluciones de EDP como valores esperados condicionales.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Precio de Mercado del Riesgo</span>
            <p class="text-slate-400 text-sm leading-relaxed">Relación entre el exceso de rentabilidad esperada de un activo sobre la tasa libre de riesgo y su volatilidad, utilizada para ajustar la deriva en cambios de medida.</p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Ingenieria Financiera IF6</p>
</footer>

</div>
