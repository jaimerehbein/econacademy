---
titulo: "Modelos Macroeconómicos"
modulo: "ME1"
---

<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-blue-500 rounded-full"></div>
        <span class="text-blue-300 font-black text-[10px] uppercase tracking-[0.4em]">Master en Modelos Económicos</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
        ME1
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-blue-500/10 text-blue-300 border border-blue-500/20 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Zero-Noise UX</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">v9.5 · Modelos Macroeconómicos</span>
    </div>
</header>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Los modelos macroeconómicos operan como laboratorios matemáticos donde ecuaciones simultáneas determinan estados estacionarios o dinámicos para el conjunto de una economía. El núcleo lógico divide la resolución del sistema dependiendo de la velocidad de ajuste de precios frente a las rigideces del mercado.</p>

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
    A["Macroeconomía"] --> B["Corto Plazo (Keynes)"]
    A --> C["Largo Plazo (Clásico)"]
    B --> B1["IS-LM"]
    B --> B2["OA-DA Dinámico"]
    C --> C1["Pleno Empleo"]
    C --> C2["Neutralidad Monetaria"]
    
    style A fill:#0f172a,stroke:#3b82f6,stroke-width:2px,color:#eff6ff
    style B fill:#1e293b,stroke:#64748b,stroke-width:1px,color:#e2e8f0
    style C fill:#1e293b,stroke:#64748b,stroke-width:1px,color:#e2e8f0
        </pre>
    </div>
</div>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📌</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r from-blue-300 to-indigo-400 bg-clip-text text-transparent break-words leading-tight">El Paradigma Clásico y la Oferta</h2>
        <div class="w-10 md:w-14 h-1 bg-blue-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La piedra angular clásica postula que los mercados siempre vacían instantáneamente (precios perfectamente flexibles). La producción real ($Y$) está fijada exógenamente en el largo plazo por la función de producción y el trabajo ($L$) de pleno empleo: $Y = F(K, \bar{L})$.</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto text-slate-100 font-mono">
    $$ M \times V = P \times Y \implies P = \frac{M \cdot V}{\bar{Y}} $$
</div>

<div class="flex items-start gap-5 p-5 bg-blue-500/10 rounded-2xl my-3 border border-blue-500/20 hover:bg-blue-500/15 transition-all">
    <div class="bg-blue-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1">**Flexibilidad de precios:** El mecanismo de precios garantiza el vaciado instantáneo de todos los mercados.</div>
</div>
<div class="flex items-start gap-5 p-5 bg-blue-500/10 rounded-2xl my-3 border border-blue-500/20 hover:bg-blue-500/15 transition-all">
    <div class="bg-blue-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1">**Neutralidad del dinero:** Las políticas monetarias solo afectan el nivel de precios nominales, no la producción real.</div>
</div>

</section>
<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📌</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r from-blue-300 to-indigo-400 bg-clip-text text-transparent break-words leading-tight">Modelos Keynesianos y Rigideces (IS-LM)</h2>
        <div class="w-10 md:w-14 h-1 bg-blue-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">John Maynard Keynes revolucionó el modelado al introducir fricciones nominales y rigideces salariales: los precios 'no observan' instantáneamente la cantidad de dinero. La ecuación fundamental de Demanda Agregada dicta la producción a corto plazo.</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto text-slate-100 font-mono">
    $$ Y = C(Y-T) + I(r) + G + NX $$
</div>

<div class="flex items-start gap-5 p-5 bg-blue-500/10 rounded-2xl my-3 border border-blue-500/20 hover:bg-blue-500/15 transition-all">
    <div class="bg-blue-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1">**Curva IS (Bienes):** Representa el equilibrio donde la inversión planeada iguala al ahorro.</div>
</div>
<div class="flex items-start gap-5 p-5 bg-blue-500/10 rounded-2xl my-3 border border-blue-500/20 hover:bg-blue-500/15 transition-all">
    <div class="bg-blue-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1">**Curva LM (Dinero):** Representa la preferencia por la liquidez frente a la oferta monetaria fija del banco central.</div>
</div>

</section>


<div class="bg-gradient-to-br from-slate-900/90 to-black border border-blue-500/20 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-blue-300 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave del Módulo
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-blue-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La macroeconomía modela el agregado sistémico mediante ecuaciones de equilibrio general simplificadas.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-blue-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>El modelo IS-LM explica las fluctuaciones de corto plazo mediante rigideces nominales.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-blue-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La síntesis neoclásica integra expectativas racionales y el retorno al pleno empleo.</span></li>

        </ul>
    </div>
</div>

</div>
