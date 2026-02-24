<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-violet-500 rounded-full"></div>
        <span class="text-violet-400 font-black text-[10px] uppercase tracking-[0.4em]">ME3 · Módulo Temporal</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
        MODELOS<br/>DINÁMICOS
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-violet-500/15 text-violet-300 border border-violet-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Hamiltoniano</span>
        <span class="bg-cyan-500/15 text-cyan-300 border border-cyan-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Crecimiento Endógeno</span>
    </div>
</header>

<!-- INTRO -->
<p class="text-slate-300 text-lg leading-relaxed mb-16">
    La economía no es estática. Las decisiones de hoy afectan las posibilidades de mañana. Este módulo introduce las herramientas de cálculo variacional y control óptimo para modelar el crecimiento económico y la acumulación de capital a través del tiempo.
</p>

<!-- SECTION 1 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-violet-500 font-mono text-xs">[01]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Control Óptimo</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed">
        <p>
            Maximizar una funcional integral (como la utilidad intertemporal) sujeta a una ley de movimiento para una variable de estado (como el capital).
        </p>
        <div class="bg-white/5 border border-white/10 rounded-3xl p-10">
            <div class="text-violet-400 font-mono text-xs mb-4 uppercase tracking-widest">El Hamiltoniano</div>
            <div class="text-white text-2xl md:text-4xl font-mono text-center mb-8">
                $H = u(c) e^{-\rho t} + \mu [f(k) - (n+\delta)k - c]$
            </div>
            <p class="text-[10px] text-slate-500 italic text-center uppercase tracking-widest">Donde $u(c)$ es la utilidad, $k$ la variable de estado y $\mu$ la variable de co-estado.</p>
        </div>
    </div>
</section>

<!-- SECTION 2 (MODELO RAMSEY) -->
<section class="mb-24 grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
    <div class="p-8 border border-white/10 rounded-3xl bg-violet-900/10">
        <h4 class="text-violet-500 font-black text-[10px] uppercase tracking-widest mb-4">Ramsey-Cass-Koopmans</h4>
        <p class="text-white text-xs leading-relaxed">
            A diferencia del modelo de Solow (tasa de ahorro exógena), aquí los agentes eligen su consumo de forma óptima a lo largo del tiempo, derivando la <strong>Ecuación de Euler</strong>:
        </p>
        <div class="mt-6 font-mono text-cyan-400 text-lg">
            $\frac{\dot{c}}{c} = \frac{1}{\theta} [f'(k) - \rho]$
        </div>
    </div>
    <div class="grayscale opacity-30 select-none">
        <!-- SVG Placeholder for Phase Diagram -->
        <svg viewBox="0 0 100 80" class="w-full h-auto text-violet-500">
            <path d="M10,70 L90,70" stroke="currentColor" stroke-width="0.5" />
            <path d="M10,10 L10,75" stroke="currentColor" stroke-width="0.5" />
            <path d="M20,60 Q50,10 80,60" fill="none" stroke="currentColor" stroke-width="1" />
            <line x1="50" y1="10" x2="50" y2="70" stroke="currentColor" stroke-width="0.5" stroke-dasharray="2" />
            <text x="92" y="72" fill="currentColor" font-size="4">k</text>
            <text x="5" y="10" fill="currentColor" font-size="4">c</text>
        </svg>
    </div>
</section>

<!-- SECTION 3 (CRECIMIENTO) -->
<section class="mb-24 px-8 py-10 bg-white/5 rounded-[3rem] border border-white/10 text-center">
    <h4 class="text-cyan-400 font-black text-[10px] uppercase tracking-[0.4em] mb-4">Crecimiento Endógeno</h4>
    <h3 class="text-white text-3xl font-black tracking-tighter mb-4">Capital Humano e Ideas</h3>
    <p class="text-slate-400 text-sm leading-relaxed max-w-xl mx-auto italic">
        "El crecimiento sostenido es posible gracias a la acumulación de conocimiento que evita los rendimientos decrecientes del capital físico."
    </p>
</section>


<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">
        <span class="text-lime-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo ME3</h3>
    </div>
    <div class="bg-black/30 p-2 md:p-6 rounded-2xl border border-white/5 overflow-x-auto">
        
        <pre class="mermaid bg-transparent flex justify-center">
graph LR
    A[Fundamentos Teóricos] --> B(Aplicación Práctica)
    B --> C{Análisis Crítico}
    C -->|Evaluación| D[Validación Empírica]
    C -->|Revisión| E[Ajuste de Modelo]
    
    classDef default fill:#111827,stroke:#84cc16,stroke-width:1px,color:#d1d5db
    classDef decision fill:#3f6212,stroke:#84cc16,stroke-width:2px,color:#fff
    class C decision
        </pre>

    </div>
</div>



<!-- GLOSARIO -->
<!-- GLOSARIO v9.5 -->
<section id="glosario" class="mt-24 mb-16 relative">
    <div class="flex items-center gap-4 mb-10">
        <div class="w-1.5 h-8 bg-violet-500 rounded-full"></div>
        <h2 class="text-2xl font-black text-white tracking-tight uppercase italic">Glosario Técnico</h2>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 relative z-10">
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Modelos Dinámicos
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Herramientas analíticas utilizadas para estudiar cómo las decisiones económicas actuales influyen en las posibilidades futuras y para modelar la evolución del crecimiento económico y la acumulación de capital a lo largo del tiempo.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Cálculo Variacional
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Rama de las matemáticas que se ocupa de encontrar funciones que maximizan o minimizan funcionales, a menudo integrales, y es fundamental en la resolución de problemas de optimización dinámica.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Control Óptimo
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Metodología para maximizar una funcional integral (como la utilidad intertemporal) sujeta a una ley de movimiento que rige la evolución de una variable de estado (como el capital) a lo largo del tiempo.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Funcional Integral
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Una función de funciones, típicamente una integral que evalúa una trayectoria o secuencia de decisiones a lo largo del tiempo, cuyo valor se busca maximizar o minimizar en problemas de optimización dinámica.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Variable de Estado
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Una variable que describe el estado de un sistema en un momento dado (ej. capital físico) y cuya evolución a lo largo del tiempo está sujeta a una ley de movimiento o ecuación diferencial.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Hamiltoniano
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                En control óptimo, es una función auxiliar que combina la función objetivo instantánea (utilidad) con la ley de movimiento de la variable de estado, ponderada por una variable de co-estado, para facilitar la optimización intertemporal.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Variable de Co-estado
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                En el contexto del Hamiltoniano, representa el valor marginal de la variable de estado en el tiempo, o el precio sombra del capital, indicando cuánto aumentaría el valor total de la funcional si la variable de estado aumentara marginalmente.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Modelo Ramsey-Cass-Koopmans
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Un modelo de crecimiento económico neoclásico donde los agentes económicos optimizan su consumo a lo largo del tiempo, determinando endógenamente la tasa de ahorro y la acumulación de capital.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Ecuación de Euler
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Una condición necesaria para la optimización intertemporal en problemas de cálculo variacional y control óptimo, que describe la trayectoria óptima de una variable de control (ej. consumo) a lo largo del tiempo.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Crecimiento Endógeno
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Teoría económica que explica el crecimiento económico sostenido a través de factores internos al sistema, como la acumulación de capital humano y el progreso tecnológico (ideas), que contrarrestan los rendimientos decrecientes del capital físico.
            </p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Modelos Dinámicos ME3</p>
</footer>

</div>
