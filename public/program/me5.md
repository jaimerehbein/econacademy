---
titulo: "Modelos Estadísticos"
modulo: "ME5"
---

<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-teal-500 rounded-full"></div>
        <span class="text-teal-300 font-black text-[10px] uppercase tracking-[0.4em]">Master en Modelos Económicos</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
        ME5
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-teal-500/10 text-teal-300 border border-teal-500/20 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Zero-Noise UX</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">v9.5 · Modelos Estadísticos</span>
    </div>
</header>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Incluso la matriz teórica más sofisticada es meramente una hipótesis si no sobrevive a la colisión empírica. Los Modelos Estadísticos dotan a la economía de validación algorítmica y control sistemático paramétrico.</p>

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
flowchart TD
    A["Estadística"] --> B["Regresión (MCO)"]
    A --> C["Series Temporales"]
    B --> B1["Inferencia Lineal"]
    B --> B2["Modelos Logit/Probit"]
    C --> C1["Procesos Estocásticos"]
    C --> C2["VAR y Volatilidad"]
    
    style A fill:#042f2e,stroke:#14b8a6,stroke-width:2px,color:#f0fdfa
    style B fill:#042f2e,stroke:#0d9488,stroke-width:1px,color:#ccfbf1
    style C fill:#042f2e,stroke:#0d9488,stroke-width:1px,color:#ccfbf1
        </pre>
    </div>
</div>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📌</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r from-teal-300 to-cyan-400 bg-clip-text text-transparent break-words leading-tight">Fundamentos de Inferencia Lineal (MCO)</h2>
        <div class="w-10 md:w-14 h-1 bg-teal-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La Regresión Múltiple extrae el peso gravimétrico aislado de múltiples variables simultáneamente, permitiendo filtrar el ruido ambiental.</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto text-slate-100 font-mono">
    $$ \hat{\beta}_{MCO} = (X^T X)^{-1} X^T Y $$
</div>

<div class="flex items-start gap-5 p-5 bg-teal-500/10 rounded-2xl my-3 border border-teal-500/20 hover:bg-teal-500/15 transition-all">
    <div class="bg-teal-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1">**MELI (BLUE):** Bajo ciertos axiomas, MCO es el mejor estimador lineal insesgado.</div>
</div>
<div class="flex items-start gap-5 p-5 bg-teal-500/10 rounded-2xl my-3 border border-teal-500/20 hover:bg-teal-500/15 transition-all">
    <div class="bg-teal-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1">**Significancia Estadística:** Evaluación probabilística de si el efecto hallado es real o producto del azar.</div>
</div>

</section>
<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📌</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r from-teal-300 to-cyan-400 bg-clip-text text-transparent break-words leading-tight">Estimación Discreta y Series Temporales</h2>
        <div class="w-10 md:w-14 h-1 bg-teal-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Modelamos decisiones dicotómicas (Logit) y el eco histórico de los datos temporales (Series Temporales) para predecir fluctuaciones bursátiles o sociales.</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto text-slate-100 font-mono">
    $$ \sigma_t^2 = \alpha_0 + \alpha_1 \varepsilon_{t-1}^2 + \gamma \sigma_{t-1}^2 $$
</div>

<div class="flex items-start gap-5 p-5 bg-teal-500/10 rounded-2xl my-3 border border-teal-500/20 hover:bg-teal-500/15 transition-all">
    <div class="bg-teal-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1">**Arquitectura Logit:** Confinamiento de predicciones en el rango [0,1].</div>
</div>
<div class="flex items-start gap-5 p-5 bg-teal-500/10 rounded-2xl my-3 border border-teal-500/20 hover:bg-teal-500/15 transition-all">
    <div class="bg-teal-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1">**GARCH:** Modelado de la volatilidad arracimada en mercados financieros.</div>
</div>

</section>


<div class="bg-gradient-to-br from-slate-900/90 to-black border border-teal-500/20 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-teal-300 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave del Módulo
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-teal-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La econometría diferencia lo anecdótico de lo causal irrefutable.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-teal-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Los modelos discretos capturan la esencia de las decisiones binarias humanas.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-teal-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Las series temporales son el nervio central del trading algorítmico moderno.</span></li>

        </ul>
    </div>
</div>

</div>
