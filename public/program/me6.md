---
titulo: "Modelos Informáticos de Optimización"
modulo: "ME6"
---

<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-cyan-500 rounded-full"></div>
        <span class="text-cyan-300 font-black text-[10px] uppercase tracking-[0.4em]">Master en Modelos Económicos</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
        ME6
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-cyan-500/10 text-cyan-300 border border-cyan-500/20 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Zero-Noise UX</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">v9.5 · Modelos Informáticos de Optimización</span>
    </div>
</header>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Los modelos de Optimización computan normativamente el protocolo definitivo máximo matemático a seguir imperativamente por una entidad logística bajo escasez fatal de recursos.</p>

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
    A["Optimización"] --> B["Programación Lineal"]
    A --> C["Gestión de Inventarios"]
    B --> B1["Simplex de Dantzig"]
    B --> B2["Modelos de Transporte"]
    C --> C1["Lote Económico (EOQ)"]
    C --> C2["Just-In-Time"]
    
    style A fill:#083344,stroke:#06b6d4,stroke-width:2px,color:#ecfeff
    style B fill:#083344,stroke:#0891b2,stroke-width:1px,color:#cffafe
    style C fill:#083344,stroke:#0891b2,stroke-width:1px,color:#cffafe
        </pre>
    </div>
</div>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📌</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r from-cyan-300 to-blue-400 bg-clip-text text-transparent break-words leading-tight">Programación Lineal y Simplex</h2>
        <div class="w-10 md:w-14 h-1 bg-cyan-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Asignación de recursos (capital, horas, materiales) para maximizar beneficios o minimizar costos dentro de un polítopo de restricciones.</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto text-slate-100 font-mono">
    $$ \max Z = C^T X \quad \text{s.t.} \quad A X \leq B $$
</div>

<div class="flex items-start gap-5 p-5 bg-cyan-500/10 rounded-2xl my-3 border border-cyan-500/20 hover:bg-cyan-500/15 transition-all">
    <div class="bg-cyan-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1">**Frontera Viable:** El conjunto de todas las soluciones que cumplen las restricciones.</div>
</div>
<div class="flex items-start gap-5 p-5 bg-cyan-500/10 rounded-2xl my-3 border border-cyan-500/20 hover:bg-cyan-500/15 transition-all">
    <div class="bg-cyan-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1">**Vértices Óptimos:** El Simplex recorre los vértices del poliedro para hallar el máximo.</div>
</div>

</section>
<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📌</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r from-cyan-300 to-blue-400 bg-clip-text text-transparent break-words leading-tight">Modelo de Transporte e Inventarios</h2>
        <div class="w-10 md:w-14 h-1 bg-cyan-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Optimización del flujo logístico desde orígenes a destinos y cálculo del lote óptimo de pedido para minimizar costos de almacenamiento.</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto text-slate-100 font-mono">
    $$ Q^* = \sqrt{\frac{2 \cdot D \cdot C_p}{C_h}} $$
</div>

<div class="flex items-start gap-5 p-5 bg-cyan-500/10 rounded-2xl my-3 border border-cyan-500/20 hover:bg-cyan-500/15 transition-all">
    <div class="bg-cyan-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1">**Minimización de Flete:** Distribución que reduce el costo total de envío trans-fronterizo.</div>
</div>
<div class="flex items-start gap-5 p-5 bg-cyan-500/10 rounded-2xl my-3 border border-cyan-500/20 hover:bg-cyan-500/15 transition-all">
    <div class="bg-cyan-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1">**Wilson (EOQ):** Equilibrio perfecto entre el costo de pedir y el costo de guardar.</div>
</div>

</section>


<div class="bg-gradient-to-br from-slate-900/90 to-black border border-cyan-500/20 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-cyan-300 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave del Módulo
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-cyan-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La programación lineal guía los megaproyectos logísticos mundiales.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-cyan-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>El algoritmo EOQ es el pilar de la eficiencia industrial SAP ERP.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-cyan-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La optimización es la ventaja competitiva final en un mundo de recursos finitos.</span></li>

        </ul>
    </div>
</div>

</div>
