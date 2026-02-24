<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-emerald-500 rounded-full"></div>
        <span class="text-emerald-400 font-black text-[10px] uppercase tracking-[0.4em]">IF1 · Módulo Profesional</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
        FUNDAMENTOS Y<br/>MERCADOS
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-emerald-500/15 text-emerald-300 border border-emerald-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Teoría de Bloques</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">ACT/360 · Sintéticos</span>
    </div>
</header>

<!-- INTRO -->
<p class="text-slate-300 text-lg leading-relaxed mb-16">
    La ingeniería financiera no es simplemente la aplicación de fórmulas; es el arte de descomponer instrumentos complejos en sus <strong>bloques de construcción</strong> fundamentales para crear soluciones sintéticas y gestionar riesgos de manera eficiente.
</p>

<!-- SECTION 1 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[01]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Instrumentos Sintéticos</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed">
        <p>
            Un instrumento sintético es un activo financiero creado artificialmente para imitar los flujos de efectivo de otro activo. La premisa es:
        </p>
        <div class="bg-white/5 border border-white/10 p-8 rounded-2xl italic text-slate-200">
            "Si dos estrategias tienen exactamente los mismos flujos de efectivo en el futuro, deben tener el mismo precio hoy."
        </div>
        <p>
            La ingeniería financiera busca instrumentos con <strong>valor inicial cero</strong>. Esto permite entrar en posiciones sin comprometer capital inmediato, optimizando el uso de recursos y el apalancamiento.
        </p>
    </div>
</section>

<!-- SECTION 2 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[02]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Convencionalismos de Mercado</h2>
    </div>
    
    <div class="bg-white/5 border border-white/10 rounded-3xl overflow-hidden mb-8">
        <table class="w-full text-left text-sm">
            <thead class="bg-white/5 text-emerald-400 font-black uppercase tracking-widest text-[9px]">
                <tr>
                    <th class="px-6 py-4">Mercado</th>
                    <th class="px-6 py-4">Base de Días</th>
                    <th class="px-6 py-4">Aplicación</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-white/5 text-slate-400">
                <tr>
                    <td class="px-6 py-4 font-bold text-white uppercase">Dinero</td>
                    <td class="px-6 py-4">ACT/360</td>
                    <td class="px-6 py-4">Libor, Papel Comercial</td>
                </tr>
                <tr>
                    <td class="px-6 py-4 font-bold text-white uppercase">Bonos</td>
                    <td class="px-6 py-4">30/360</td>
                    <td class="px-6 py-4">Bonos Corporativos (EEUU)</td>
                </tr>
                <tr>
                    <td class="px-6 py-4 font-bold text-white uppercase">Treasuries</td>
                    <td class="px-6 py-4">ACT/ACT</td>
                    <td class="px-6 py-4">Bonos del Tesoro</td>
                </tr>
            </tbody>
        </table>
    </div>
</section>

<!-- FORMULA BOX -->
<section class="mb-24 px-8 py-12 bg-emerald-500 rounded-[3rem] relative overflow-hidden">
    <div class="absolute top-0 right-0 p-12 opacity-10">
        <svg class="w-32 h-32 text-black" fill="currentColor" viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-2 10h-4v4h-2v-4H7v-2h4V7h2v4h4v2z"></path></svg>
    </div>
    <h4 class="text-black font-black text-xs uppercase tracking-[0.4em] mb-8">Factor de Descuento</h4>
    <div class="text-white text-3xl md:text-4xl font-mono mb-8">
        $$B(t, T) = \frac{1}{1 + R_T \times \delta}$$
    </div>
    <p class="text-emerald-950 text-sm font-bold leading-relaxed max-w-xl">
        Donde $\delta$ es la fracción de año calculada según el convencionalismo pertinente. Este factor es el átomo de la valuación en renta fija.
    </p>
</section>

<!-- KEY POINTS -->
<section class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-24">
    <div class="p-8 border border-white/10 rounded-3xl">
        <div class="w-8 h-8 bg-emerald-500 rounded-lg flex items-center justify-center text-white font-black mb-6">1</div>
        <p class="text-slate-300 leading-relaxed font-medium text-sm">
            La ingeniería financiera se basa en la <strong>linealidad</strong> de los flujos de efectivo para la replicación estática.
        </p>
    </div>
    <div class="p-8 border border-white/10 rounded-3xl">
        <div class="w-8 h-8 bg-emerald-500 rounded-lg flex items-center justify-center text-white font-black mb-6">2</div>
        <p class="text-slate-300 leading-relaxed font-medium text-sm">
            El <strong>arbitraje</strong> es la fuerza que iguala los precios de los instrumentos sintéticos y los reales.
        </p>
    </div>
</section>


<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo IF1</h3>
    </div>
    <div class="bg-black/30 p-2 md:p-6 rounded-2xl border border-white/5 overflow-x-auto">
        
        <pre class="mermaid bg-transparent flex justify-center">
graph LR
    A[Fundamentos Teóricos] --> B(Aplicación Práctica)
    B --> C{Análisis Crítico}
    C -->|Evaluación| D[Validación Empírica]
    C -->|Revisión| E[Ajuste de Modelo]
    
    classDef default fill:#111827,stroke:#10b981,stroke-width:1px,color:#d1d5db
    classDef decision fill:#064e3b,stroke:#10b981,stroke-width:2px,color:#fff
    class C decision
        </pre>

    </div>
</div>

<!-- GLOSARIO -->
<section class="mb-24">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-10">
        <span class="text-emerald-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[GL]</span>
        <h2 class="text-white font-black text-xl sm:text-2xl uppercase tracking-tighter break-words leading-tight">Glosario del Módulo</h2>
    </div>
    <div class="space-y-3">
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Instrumento Sintético</span>
            <p class="text-slate-400 text-sm leading-relaxed">Activo financiero diseñado para replicar los flujos de efectivo y perfiles de riesgo de otro instrumento mediante la combinación de diversos componentes básicos del mercado.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Ingeniería Financiera</span>
            <p class="text-slate-400 text-sm leading-relaxed">Disciplina que emplea métodos cuantitativos y herramientas matemáticas para el diseño, desarrollo e implementación de instrumentos y procesos financieros innovadores con fines de gestión de riesgos.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Factor de Descuento</span>
            <p class="text-slate-400 text-sm leading-relaxed">Valor actual de una unidad monetaria pagadera en una fecha futura, determinado por una tasa de interés específica y un convencionalismo de conteo de días definido.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Arbitraje</span>
            <p class="text-slate-400 text-sm leading-relaxed">Práctica financiera que consiste en la compra y venta simultánea de activos para beneficiarse de discrepancias en los precios, asegurando la eficiencia y el equilibrio del mercado.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Base de Días</span>
            <p class="text-slate-400 text-sm leading-relaxed">Convención técnica que establece cómo se cuenta el tiempo para el cálculo de intereses devengados, definiendo el número de días por mes y por año comercial.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Replicación Estática</span>
            <p class="text-slate-400 text-sm leading-relaxed">Técnica de ingeniería financiera que utiliza una combinación fija de instrumentos financieros para igualar los flujos de caja de una posición compleja sin requerir reequilibrios constantes.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Valor Inicial Cero</span>
            <p class="text-slate-400 text-sm leading-relaxed">Propiedad de ciertos contratos financieros, como los swaps, donde el valor presente de los flujos de entrada y salida es idéntico en el momento de la contratación.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-emerald-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">ACT/360</span>
            <p class="text-slate-400 text-sm leading-relaxed">Convencionalismo de mercado donde los intereses se calculan sobre los días reales transcurridos divididos por un año base de trescientos sesenta días, estándar en el mercado monetario.</p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Ingenieria Financiera IF1</p>
</footer>

</div>
