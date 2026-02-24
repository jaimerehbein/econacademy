<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-violet-500 rounded-full"></div>
        <span class="text-violet-400 font-black text-[10px] uppercase tracking-[0.4em]">ME7 · Módulo Dinámico-Estocástico</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
        MODELADO<br/>ESTOCÁSTICO
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-violet-500/15 text-violet-300 border border-violet-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Monte Carlo</span>
        <span class="bg-cyan-500/15 text-cyan-300 border border-cyan-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Agent-Based</span>
    </div>
</header>

<!-- INTRO -->
<p class="text-slate-300 text-lg leading-relaxed mb-16">
    El mundo real está lleno de azar. Este módulo final aborda la complejidad emergente a través de la simulación de agentes heterogéneos y el uso de métodos numéricos para resolver modelos que no tienen solución analítica cerrada.
</p>

<!-- SECTION 1 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-violet-500 font-mono text-xs">[01]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Modelos de Agentes (ABM)</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed">
        <p>
            A diferencia de los modelos basados en el "agente representativo", los ABM simulan miles de agentes con reglas de comportamiento locales e interacciones directas, observando cómo emerge el fenómeno macro (ej. crisis, segregación).
        </p>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 my-10">
            <div class="p-6 border border-white/10 rounded-2xl bg-white/5">
                <h5 class="text-violet-400 font-black text-[8px] uppercase tracking-widest mb-3">Heterogeneidad</h5>
                <p class="text-white text-[10px] font-bold">Diferentes niveles de riqueza, información y racionalidad.</p>
            </div>
            <div class="p-6 border border-white/10 rounded-2xl bg-white/5">
                <h5 class="text-violet-400 font-black text-[8px] uppercase tracking-widest mb-3">Interacción</h5>
                <p class="text-white text-[10px] font-bold">Aprendizaje social e imitación de conductas exitosas.</p>
            </div>
            <div class="p-6 border border-white/10 rounded-2xl bg-white/5">
                <h5 class="text-violet-400 font-black text-[8px] uppercase tracking-widest mb-3">Emergencia</h5>
                <p class="text-white text-[10px] font-bold">Patrones macro no predecibles sumando las partes.</p>
            </div>
        </div>
    </div>
</section>

<!-- SECTION 2 (NUMERICAL METHODS) -->
<section class="mb-24 p-12 bg-white/5 border border-white/10 rounded-[3rem]">
    <h4 class="text-violet-500 font-black text-[10px] uppercase tracking-[0.4em] mb-10 text-center uppercase">Métodos Numéricos</h4>
    <div class="flex flex-col md:flex-row gap-12 items-center">
        <div class="flex-1 space-y-6">
            <h3 class="text-white text-3xl font-black tracking-tighter">Monte Carlo & Cadenas de Markov</h3>
            <p class="text-slate-400 text-sm leading-relaxed">
                Utilizamos simulaciones masivas de caminos aleatorios para estimar distribuciones de probabilidad complejas, fundamentales en la economía financiera y la gestión de riesgos.
            </p>
            <div class="font-mono text-cyan-400 text-sm p-4 bg-black/40 rounded-xl">
                E[f(X)] \approx \frac{1}{N} \sum_{i=1}^N f(x_i)
            </div>
        </div>
        <div class="w-48 h-48 bg-violet-500/20 rounded-full border border-violet-500/30 flex items-center justify-center relative">
            <div class="absolute inset-0 flex items-center justify-center opacity-30">
                <div class="w-32 h-32 border-2 border-dashed border-cyan-500 rounded-full animate-spin-slow"></div>
            </div>
            <span class="text-white font-black text-sm uppercase tracking-widest">Simulación</span>
        </div>
    </div>
</section>


<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">
        <span class="text-lime-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo ME7</h3>
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
                    Modelado Estocástico
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Marco matemático que incorpora variables aleatorias para representar la incertidumbre y predecir la distribución de resultados posibles en sistemas económicos y financieros complejos.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Modelos de Agentes (ABM)
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Simulación computacional que analiza las interacciones de individuos autónomos y heterogéneos para observar el surgimiento de fenómenos macroeconómicos globales a partir de reglas locales.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Heterogeneidad
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Propiedad que describe la diversidad entre agentes económicos respecto a sus niveles de riqueza, acceso a la información, dotaciones y grados de racionalidad operativa.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Emergencia
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Aparición de patrones macroscópicos complejos y no lineales que resultan de las interacciones descentralizadas de agentes individuales, no explicables únicamente por la suma de sus partes.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Simulación de Monte Carlo
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Técnica numérica que utiliza el muestreo aleatorio masivo para estimar distribuciones de probabilidad y resolver problemas matemáticos que carecen de una solución analítica cerrada.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Cadenas de Markov
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Procesos estocásticos donde la transición a un estado futuro depende exclusivamente del estado actual, asumiendo independencia de los eventos ocurridos en el pasado del sistema.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Métodos Numéricos
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Algoritmos y procedimientos matemáticos empleados para obtener aproximaciones cuantitativas precisas en modelos financieros cuya complejidad impide una resolución algebraica directa.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-purple-500/50 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-purple-500 transition-colors">
                    Caminos Aleatorios
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Modelos matemáticos que describen trayectorias compuestas por una sucesión de pasos estocásticos, fundamentales para la modelización del movimiento de precios en mercados financieros.
                </p>
            </div>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Modelado Estocástico ME7</p>
</footer>

</div>
