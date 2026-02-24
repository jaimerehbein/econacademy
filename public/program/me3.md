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


<section id="glosario" class="py-16 bg-white dark:bg-gray-950 transition-colors duration-300">
    <div class="container mx-auto px-6">
        <div class="flex items-center gap-4 mb-12">
            <div class="w-2 h-10 bg-purple-500 rounded-full"></div>
            <h2 class="text-4xl font-bold text-gray-900 dark:text-white">Glosario Académico</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Control Óptimo
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Técnica matemática empleada para maximizar una funcional sujeta a restricciones dinámicas, representadas mediante ecuaciones diferenciales que describen la evolución de variables de estado en el tiempo.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Hamiltoniano
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Función escalar utilizada en problemas de control óptimo que integra la función de utilidad instantánea y las restricciones dinámicas multiplicadas por variables de co-estado.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Variable de Estado
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Magnitud que representa la condición o stock de un sistema en un momento dado, cuya evolución temporal está determinada por las decisiones de control y parámetros exógenos.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Variable de Co-estado
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Multiplicador dinámico que indica el precio sombra o valor marginal de una unidad adicional de la variable de estado en el bienestar total del sistema.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Ecuación de Euler
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Condición necesaria para la optimización intertemporal que describe la trayectoria del consumo óptimo, igualando la tasa marginal de sustitución temporal con el rendimiento marginal del capital.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Crecimiento Endógeno
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Teoría económica que sostiene que el crecimiento sostenido surge de factores internos como el capital humano y la innovación, evitando los rendimientos decrecientes del capital físico.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Utilidad Intertemporal
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Suma descontada de los niveles de satisfacción obtenidos por un agente a lo largo de un horizonte temporal, ponderada por una tasa de preferencia por el consumo presente.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Capital Humano
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Conjunto de habilidades, conocimientos y experiencias de los trabajadores que incrementan su productividad y permiten el crecimiento económico sostenido mediante la generación de ideas.
                </p>
            </div>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Modelos Dinámicos ME3</p>
</footer>

</div>
