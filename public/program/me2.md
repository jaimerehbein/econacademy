---
titulo: "Modelos Microeconómicos"
modulo: "ME2"
---

<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-emerald-500 rounded-full"></div>
        <span class="text-emerald-300 font-black text-[10px] uppercase tracking-[0.4em]">Master en Modelos Económicos</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
        ME2
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-emerald-500/10 text-emerald-300 border border-emerald-500/20 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Zero-Noise UX</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">v9.5 · Modelos Microeconómicos</span>
    </div>
</header>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La Microeconomía modela el comportamiento individual de los agentes optimizadores (consumidores y empresas) sometidos a restricciones tangibles. Se centra en el mecanismo de fijación de precios y la asignación eficiente de recursos limitados mediante cálculo marginal.</p>

<!-- DIAGRAMA INICIAL -->
<div class="bg-slate-900/50 border border-white/5 rounded-3xl p-8 my-12 shadow-2xl relative overflow-hidden group">
    <div class="absolute top-0 right-0 p-4 opacity-20 group-hover:opacity-40 transition-opacity">
        <span class="text-4xl">📊</span>
    </div>
    <h3 class="text-xl font-bold text-white mb-6 flex items-center gap-3">
        Archivonomía Visual del Modelo
    </h3>
    <div class="overflow-hidden rounded-xl border border-white/5 bg-slate-950/50 p-6 flex justify-center">
        <pre class="mermaid w-full flex justify-center">
flowchart LR
    A["Microeconomía"] --> B["Producción"]
    A --> C["Consumo"]
    B --> B1["Cobb-Douglas"]
    B --> B2["Leontief"]
    C --> C1["Maximización Utilidad"]
    C --> C2["Restricción Presupuestaria"]
    
    style A fill:#064e3b,stroke:#10b981,stroke-width:2px,color:#ecfdf5
    style B fill:#064e3b,stroke:#059669,stroke-width:1px,color:#d1fae5
    style C fill:#064e3b,stroke:#059669,stroke-width:1px,color:#d1fae5
        </pre>
    </div>
</div>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📌</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r from-emerald-300 to-teal-400 bg-clip-text text-transparent break-words leading-tight">Topologías de la Función de Producción</h2>
        <div class="w-10 md:w-14 h-1 bg-emerald-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La función de producción abstracta abstrae cómo la tecnología combina inputs físicos (Capital $K$, Trabajo $L$) para generar valor económico. El modelo de Cobb-Douglas es la especificación más utilizada debido a sus propiedades algebraicas de elasticidad de sustitución constante.</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto text-slate-100 font-mono">
    $$ Q = A \cdot K^\alpha L^\beta $$
</div>

<div class="flex items-start gap-5 p-5 bg-emerald-500/10 rounded-2xl my-3 border border-emerald-500/20 hover:bg-emerald-500/15 transition-all">
    <div class="bg-emerald-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1">**Rendimientos a Escala:** Si $\alpha + \beta = 1$, la firma exhibe rendimientos constantes a escala.</div>
</div>
<div class="flex items-start gap-5 p-5 bg-emerald-500/10 rounded-2xl my-3 border border-emerald-500/20 hover:bg-emerald-500/15 transition-all">
    <div class="bg-emerald-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1">**Coeficientes Fijos (Leontief):** $Q = \min (K/a, L/b)$ para procesos industriales sin sustitución.</div>
</div>

</section>
<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📌</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r from-emerald-300 to-teal-400 bg-clip-text text-transparent break-words leading-tight">Estructuras de Fallo: Monopolio</h2>
        <div class="w-10 md:w-14 h-1 bg-emerald-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La firma controla monopólicamente la variable precio reconociendo la demanda agregada inversa del mercado $P(Q)$. Esto genera una brecha ineficiente entre el precio y el costo marginal.</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto text-slate-100 font-mono">
    $$ \frac{P - CMg}{P} = \frac{1}{|\epsilon_d|} $$
</div>

<div class="flex items-start gap-5 p-5 bg-emerald-500/10 rounded-2xl my-3 border border-emerald-500/20 hover:bg-emerald-500/15 transition-all">
    <div class="bg-emerald-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1">**Índice de Lerner:** Mide el poder de mercado como el margen sobre el costo marginal.</div>
</div>
<div class="flex items-start gap-5 p-5 bg-emerald-500/10 rounded-2xl my-3 border border-emerald-500/20 hover:bg-emerald-500/15 transition-all">
    <div class="bg-emerald-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1">**Pérdida de Bienestar:** El monopolio reduce el excedente total de la sociedad comparado con la competencia perfecta.</div>
</div>

</section>


<div class="bg-gradient-to-br from-slate-900/90 to-black border border-emerald-500/20 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-emerald-300 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave del Módulo
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-emerald-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La optimización restringida es el núcleo de las decisiones del agente representativo.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-emerald-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Bajo competencia perfecta, los teoremas del bienestar garantizan asignaciones Pareto-eficientes.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-emerald-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>El monopolio desvía el equilibrio competitivo, forzando la intervención normativa.</span></li>

        </ul>
    </div>
</div>

</div>
