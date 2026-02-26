---
titulo: "Modelos de Crecimiento Económico"
modulo: "ME3"
---

<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-amber-500 rounded-full"></div>
        <span class="text-amber-300 font-black text-[10px] uppercase tracking-[0.4em]">Master en Modelos Económicos</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
        ME3
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-amber-500/10 text-amber-300 border border-amber-500/20 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Zero-Noise UX</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">v9.5 · Modelos de Crecimiento Económico</span>
    </div>
</header>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">A diferencia de la Macroeconomía de fluctuaciones, los Modelos de Crecimiento trazan la expansión fundamental del nivel de producción tendencial ($Y_t$). Desplazan el horizonte temporal hacia las décadas, cuantificando la acumulación demográfica de factores físicos y el milagro del salto tecnológico.</p>

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
    A["Crecimiento"] --> B["Exógeno (Solow)"]
    A --> C["Endógeno (Romer/Lucas)"]
    B --> B1["Estado Estacionario"]
    B --> B2["Progreso Técnico Exógeno"]
    C --> C1["Capital Humano"]
    C --> C2["I+D y Conocimiento"]
    
    style A fill:#451a03,stroke:#f59e0b,stroke-width:2px,color:#fffbeb
    style B fill:#451a03,stroke:#d97706,stroke-width:1px,color:#fef3c7
    style C fill:#451a03,stroke:#d97706,stroke-width:1px,color:#fef3c7
        </pre>
    </div>
</div>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📌</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r from-amber-300 to-orange-400 bg-clip-text text-transparent break-words leading-tight">Evolución Exógena: Modelo de Solow-Swan</h2>
        <div class="w-10 md:w-14 h-1 bg-amber-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Robert Solow estructuró la primera calibración matemática del crecimiento convergente. Demostró que por culpa de los rendimientos marginales decrecientes del capital, toda acumulación física choca asintóticamente contra un muro de depreciación.</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto text-slate-100 font-mono">
    $$ \dot{k} = s f(k) - (n + g + \delta)k $$
</div>

<div class="flex items-start gap-5 p-5 bg-amber-500/10 rounded-2xl my-3 border border-amber-500/20 hover:bg-amber-500/15 transition-all">
    <div class="bg-amber-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1">**Ahorro y Depreciación:** El motor temporal del crecimiento físico lucha contra la obsolescencia de las máquinas.</div>
</div>
<div class="flex items-start gap-5 p-5 bg-amber-500/10 rounded-2xl my-3 border border-amber-500/20 hover:bg-amber-500/15 transition-all">
    <div class="bg-amber-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1">**Estado Estacionario:** Punto de gravedad donde $\dot{k} = 0$, requiriendo tecnología externa para crecer.</div>
</div>

</section>
<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📌</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r from-amber-300 to-orange-400 bg-clip-text text-transparent break-words leading-tight">Segunda Generación: Crecimiento Endógeno</h2>
        <div class="w-10 md:w-14 h-1 bg-amber-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La Revolución Endógena de 1990 transmutó el milagro inexplicable de Solow convirtiéndolo en un producto interno voluntario. Modelaron la mente humana y las externalidades como motores inagotables.</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto text-slate-100 font-mono">
    $$ \dot{H} = H_t \cdot \delta(1 - u) $$
</div>

<div class="flex items-start gap-5 p-5 bg-amber-500/10 rounded-2xl my-3 border border-amber-500/20 hover:bg-amber-500/15 transition-all">
    <div class="bg-amber-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1">**Capital Humano:** La educación es un factor que no padece rendimientos decrecientes.</div>
</div>
<div class="flex items-start gap-5 p-5 bg-amber-500/10 rounded-2xl my-3 border border-amber-500/20 hover:bg-amber-500/15 transition-all">
    <div class="bg-amber-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1">**Conocimiento:** Las ideas son bienes no rivales que permiten crecimiento perpetuo.</div>
</div>

</section>


<div class="bg-gradient-to-br from-slate-900/90 to-black border border-amber-500/20 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-amber-300 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave del Módulo
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-amber-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Solow demostró los límites de la acumulación bruta de infraestructura física.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-amber-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Romer y Lucas elevaron el crecimiento al ámbito de las ideas y la educación.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-amber-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>El crecimiento de largo plazo depende de la capacidad de innovación tecnológica.</span></li>

        </ul>
    </div>
</div>

</div>
