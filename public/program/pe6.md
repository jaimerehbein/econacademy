<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-stone-500 rounded-full"></div>
        <span class="text-stone-400 font-black text-[10px] uppercase tracking-[0.4em]">PE6 · Módulo Macro</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
        REVOLUCIÓN<br/>KEYNESIANA
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-stone-500/15 text-stone-300 border border-stone-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Macroeconomía</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Demanda Efectiva</span>
    </div>
</header>

<!-- INTRO -->
<p class="text-slate-300 text-lg leading-relaxed mb-16">
    La Gran Depresión de 1929 pulverizó la confianza en la capacidad de ajuste automático de los mercados. John Maynard Keynes desafió la Ley de Say y fundó la <strong>macroeconomía moderna</strong>, argumentando que la economía puede quedar atrapada en un equilibrio de bajo empleo si la demanda es insuficiente.
</p>

<!-- SECTION 1 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-stone-500 font-mono text-xs">[01]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">The General Theory (1936)</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed">
        <p>
            Keynes desplazó el foco de la oferta (clásicos) a la <strong>demanda agregada</strong>. Su análisis reveló que las decisiones de inversión y consumo son impulsadas por la incertidumbre y los "animal spirits".
        </p>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 my-10">
            <div class="p-8 bg-stone-950 border border-white/5 rounded-3xl">
                <h4 class="text-stone-500 font-black text-[9px] uppercase tracking-widest mb-4 italic">El Multiplicador</h4>
                <p class="text-white text-sm leading-relaxed mb-4">Un incremento en el gasto autónomo genera un aumento más que proporcional en la renta nacional.</p>
                <div class="text-mono text-stone-300 text-lg">$k = \frac{1}{1 - MPC}$</div>
            </div>
            <div class="p-8 bg-stone-950 border border-white/5 rounded-3xl">
                <h4 class="text-stone-500 font-black text-[9px] uppercase tracking-widest mb-4 italic">Trampa de Liquidez</h4>
                <p class="text-white text-sm leading-relaxed mb-4">Situación donde la política monetaria pierde tracción porque los agentes prefieren atesorar dinero ante tipos de interés bajísimos.</p>
            </div>
        </div>
    </div>
</section>

<!-- SECTION 2 -->
<section class="mb-24 bg-white/5 border border-white/10 rounded-[3rem] p-12">
    <h4 class="text-stone-500 font-black text-[10px] uppercase tracking-[0.4em] mb-8 text-center uppercase">El Modelo de la Síntesis</h4>
    <h3 class="text-white text-3xl font-black tracking-tighter mb-8 text-center">Modelo IS-LM</h3>
    <p class="text-slate-400 text-sm leading-relaxed mb-10 text-center max-w-2xl mx-auto">
        Desarrollado por John Hicks, este esquema unificó el mercado de bienes (IS) y el mercado monetario (LM), permitiendo simular el impacto de las políticas fiscales y monetarias.
    </p>
    <div class="flex justify-center items-center gap-12 py-8 grayscale opacity-40">
        <!-- SVG Simple Simulation of IS-LM -->
        <svg class="w-48 h-48 text-stone-400" viewBox="0 0 100 100">
            <line x1="10" y1="90" x2="90" y2="10" stroke="currentColor" stroke-width="2" />
            <line x1="10" y1="10" x2="90" y2="90" stroke="currentColor" stroke-width="2" />
            <text x="80" y="20" fill="white" font-size="6">LM</text>
            <text x="80" y="80" fill="white" font-size="6">IS</text>
        </svg>
    </div>
</section>

<!-- SECTION 3 (HIGHLIGHT) -->
<section class="mb-24 px-8 py-10 border-l-4 border-stone-500 bg-stone-500/5 rounded-r-3xl">
    <h4 class="text-stone-500 font-black text-[9px] uppercase tracking-widest mb-4">Postulado Central</h4>
    <p class="text-white text-xl font-medium leading-tight mb-4">
        "En el largo plazo, todos estaremos muertos."
    </p>
    <p class="text-slate-500 text-xs text-balance">
        Keynes defendía la intervención inmediata para corregir los desajustes del ciclo económico, rechazando la pasividad ante los "equilibrios a largo plazo".
    </p>
</section>


<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">
        <span class="text-blue-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo PE6</h3>
    </div>
    <div class="bg-black/30 p-2 md:p-6 rounded-2xl border border-white/5 overflow-x-auto">
        
        <pre class="mermaid bg-transparent flex justify-center">
graph LR
    A[Fundamentos Teóricos] --> B(Aplicación Práctica)
    B --> C{Análisis Crítico}
    C -->|Evaluación| D[Validación Empírica]
    C -->|Revisión| E[Ajuste de Modelo]
    
    classDef default fill:#111827,stroke:#3b82f6,stroke-width:1px,color:#d1d5db
    classDef decision fill:#1e3a8a,stroke:#3b82f6,stroke-width:2px,color:#fff
    class C decision
        </pre>

    </div>
</div>

<!-- GLOSARIO -->
<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Revolución Keynesiana PE6</p>
</footer>

</div>
