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
                Modelado Estocástico
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Enfoque que aborda la complejidad emergente mediante la simulación de agentes heterogéneos y el uso de métodos numéricos para resolver modelos sin solución analítica cerrada, incorporando el azar inherente al mundo real.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Modelos de Agentes (ABM)
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Paradigma de simulación que modela sistemas complejos mediante la interacción de múltiples agentes individuales con reglas de comportamiento locales, permitiendo la observación de fenómenos macroeconómicos emergentes.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Agente Representativo
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Concepto en modelado económico donde un único agente idealizado encapsula las características promedio o agregadas de todos los individuos en un sistema, a menudo simplificando la heterogeneidad y las interacciones.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Heterogeneidad (en ABM)
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Característica de los Modelos de Agentes que permite a los individuos poseer diferentes atributos, como niveles de riqueza, información o grados de racionalidad, reflejando la diversidad del mundo real.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Interacción (en ABM)
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Mecanismo fundamental en los Modelos de Agentes que describe cómo los individuos influyen mutuamente a través de comportamientos como el aprendizaje social o la imitación de estrategias exitosas.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Emergencia (en ABM)
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Propiedad de los sistemas complejos modelados con ABM donde patrones o fenómenos macro a nivel del sistema surgen de las interacciones locales de los agentes, sin ser directamente programados o predecibles a partir de las partes individuales.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Métodos Numéricos
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Conjunto de técnicas algorítmicas utilizadas para encontrar soluciones aproximadas a problemas matemáticos que no pueden resolverse de forma analítica o cerrada, especialmente en modelos complejos.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Simulación Monte Carlo
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Técnica computacional que emplea muestreos aleatorios repetidos para obtener resultados numéricos, utilizada para estimar distribuciones de probabilidad complejas y calcular integrales o expectativas.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Cadenas de Markov
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Proceso estocástico que describe una secuencia de eventos en la que la probabilidad de cada estado futuro depende únicamente del estado actual, y no de la secuencia de eventos que lo precedieron.
            </p>
        </div>
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-violet-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-violet-500/5">
            <h3 class="text-sm font-black text-violet-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse"></span>
                Distribuciones de Probabilidad Complejas
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Funciones matemáticas que describen la probabilidad de ocurrencia de diferentes resultados para una variable aleatoria, caracterizadas por formas o dependencias intrincadas que dificultan su análisis analítico directo.
            </p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Modelado Estocástico ME7</p>
</footer>

</div>
