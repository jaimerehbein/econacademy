<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-4">
        <span class="text-amber-500 font-black text-[10px] uppercase tracking-[0.4em]">Módulo 07</span>
        <div class="w-8 h-px bg-white/20"></div>
    </div>
    <h1 class="text-4xl md:text-6xl font-black text-white tracking-tighter leading-none mb-6">
        MITOS Y PENSAMIENTO
    </h1>
    <p class="text-slate-400 text-sm uppercase tracking-[0.2em] font-medium">Falacias y Conclusiones Finales</p>
</header>

<div class="space-y-12 text-slate-300 text-lg leading-relaxed">

    <!-- SECTION 1 -->
    <section>
        <h2 class="text-xl font-bold text-white mb-6 uppercase tracking-tight border-b border-white/5 pb-2">01. La Falacia de la Tarta Fija</h2>
        <p class="mb-4">
            Muchos creen que para que un rico gane, un pobre debe perder. En la realidad económica, la "tarta" crece mediante la producción y el intercambio.
        </p>
        <ul class="list-none space-y-4">
            <li class="flex gap-3">
                <span class="text-amber-500 font-bold">•</span>
                <span>**Distribución vs. Creación:** Sowell enfatiza que el problema no es cómo se "distribuye" la riqueza, sino cómo se crea en primer lugar.</span>
            </li>
            <li class="flex gap-3">
                <span class="text-amber-500 font-bold">•</span>
                <span>**Ingreso por Edades:** Las estadísticas de desigualdad a menudo ignoran que la mayoría de las personas cambian de quintil de ingresos a lo largo de su vida.</span>
            </li>
        </ul>
    </section>

    <!-- SECTION 2 -->
    <section>
        <h2 class="text-xl font-bold text-white mb-6 uppercase tracking-tight border-b border-white/5 pb-2">02. El Sentido Común ante la Falacia</h2>
        <p class="mb-6">
            Desmontar mitos como la teoría del "goteo" o la idea de que los recursos naturales son la única fuente de riqueza. Sowell enfatiza que el desarrollo depende más del <strong>Capital Humano</strong> (conocimientos, habilidades, disciplina) que de la geografía.
        </p>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
            <div class="p-6 bg-amber-500/5 border border-amber-500/10 rounded-2xl">
                <h5 class="text-amber-500 font-black text-[9px] uppercase mb-2">Control de Rentas</h5>
                <p class="text-slate-400 text-xs leading-relaxed">Lejos de ayudar a los pobres, el control de precios reduce la oferta de vivienda, degrada la calidad de los edificios existentes y crea mercados negros donde el "favoritismo" sustituye al precio.</p>
            </div>
            <div class="p-6 bg-amber-500/5 border border-amber-500/10 rounded-2xl">
                <h5 class="text-amber-500 font-black text-[9px] uppercase mb-2">Salario Mínimo</h5>
                <p class="text-slate-400 text-xs leading-relaxed">Funciona como una barrera que prohíbe trabajar a quienes tienen menor productividad. Elimina el primer peldaño de la escalera del éxito para los jóvenes y los menos capacitados.</p>
            </div>
        </div>

        <!-- MERMAID DIAGRAM -->
        <div class="bg-amber-500/5 p-8 rounded-3xl border border-amber-500/10 mb-10 overflow-hidden">
            <pre class="mermaid bg-transparent flex justify-center">
graph LR
    PControl[Control de Precios] --> SupplyDec[Caída de la Oferta]
    PControl --> DemandInc[Aumento de Demanda]
    SupplyDec --> Shortage[ESCASEZ / MERCADO NEGRO]
    DemandInc --> Shortage
    
    style PControl fill:#451a03,stroke:#f59e0b,color:#fff
    style Shortage fill:#450a0a,stroke:#dc2626,color:#fff
            </pre>
            <p class="text-center text-amber-500/40 text-[9px] uppercase tracking-widest mt-6 font-mono italic">Consecuencias Involuntarias de la Intervención</p>
        </div>

        <div class="bg-white/5 p-6 rounded-2xl border border-white/10 italic text-slate-400">
            "El conocimiento es el recurso más escaso de todos, y los precios son el sistema de coordenadas que permite coordinarlo sin dictaduras."
        </div>
    </section>

    <!-- SECTION 3 -->
    <section>
        <h2 class="text-xl font-bold text-white mb-6 uppercase tracking-tight border-b border-white/5 pb-2">03. Incentivos y Consecuencias</h2>
        <p class="mb-4">
            La economía no trata de "intenciones sociales", sino de <strong>incentivos sistémicos</strong>. Cuando los políticos juzgan sus propias leyes por sus metas proclamadas en lugar de por sus resultados reales, el desastre es inevitable.
        </p>
        <div class="space-y-4">
            <div class="flex gap-4 items-start p-4 bg-white/5 rounded-xl border border-white/10">
                <div class="text-amber-500 font-black italic">!</div>
                <p class="text-xs text-slate-400">Los subsidios a la agricultura a menudo encarecen la comida para los mismos ciudadanos que pagan los impuestos para financiar el subsidio.</p>
            </div>
            <div class="flex gap-4 items-start p-4 bg-white/5 rounded-xl border border-white/10">
                <div class="text-amber-500 font-black italic">!</div>
                <p class="text-xs text-slate-400">Las leyes de protección laboral excesiva terminan desincentivando la contratación, aumentando el desempleo estructural.</p>
            </div>
        </div>
        <p class="text-sm mt-8">
            Cerramos este viaje con una lección fundamental: la economía es una herramienta para la libertad. Ignorar sus leyes no nos hace más morales; nos hace más pobres y menos libres.
        </p>
    </section>

    <!-- KEY POINTS -->
    <section class="bg-amber-500/5 border border-amber-500/20 p-8 rounded-2xl">
        <h2 class="text-sm font-black text-amber-500 uppercase tracking-[0.3em] mb-6">Puntos Clave</h2>
        <ul class="grid gap-4 md:grid-cols-2 text-sm">
            <li class="flex gap-3">
                <div class="w-1 h-1 bg-amber-500 rounded-full mt-1.5 grayscale shrink-0"></div>
                <span>La riqueza es algo que se crea, no un fijo que se reparte.</span>
            </li>
            <li class="flex gap-3">
                <div class="w-1 h-1 bg-amber-500 rounded-full mt-1.5 grayscale shrink-0"></div>
                <span>La envidia no es una política económica viable.</span>
            </li>
            <li class="flex gap-3">
                <div class="w-1 h-1 bg-amber-500 rounded-full mt-1.5 grayscale shrink-0"></div>
                <span>El capital humano vale más que el petróleo.</span>
            </li>
            <li class="flex gap-3">
                <div class="w-1 h-1 bg-amber-500 rounded-full mt-1.5 grayscale shrink-0"></div>
                <span>Piense siempre: ¿Y qué pasará después?</span>
            </li>
        </ul>
    </section>


<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-amber-500 font-mono text-xs">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-xl">Esquema Conceptual Módulo EB7</h3>
    </div>
    <div class="bg-black/30 p-2 md:p-6 rounded-2xl border border-white/5 overflow-x-auto">
        
        <pre class="mermaid bg-transparent flex justify-center">
graph LR
    A[Fundamentos Teóricos] --> B(Aplicación Práctica)
    B --> C{Análisis Crítico}
    C -->|Evaluación| D[Validación Empírica]
    C -->|Revisión| E[Ajuste de Modelo]
    
    classDef default fill:#111827,stroke:#f59e0b,stroke-width:1px,color:#d1d5db
    classDef decision fill:#78350f,stroke:#f59e0b,stroke-width:2px,color:#fff
    class C decision
        </pre>

    </div>
</div>

<!-- GLOSARIO -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-10">
        <span class="text-amber-500 font-mono text-xs">[GL]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter">Glosario del Módulo</h2>
    </div>
    <div class="space-y-3">
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-amber-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Sistema de Precios</span>
            <p class="text-slate-400 text-sm leading-relaxed">Mecanismo descentralizado de coordinación económica. Los precios transmiten información dispersa sobre escasez relativa y preferencias con una eficiencia que ningún planificador central puede replicar.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-amber-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Incentivos</span>
            <p class="text-slate-400 text-sm leading-relaxed">Fuerzas que moldean el comportamiento económico. Sowell enfatiza que los agentes responden a incentivos reales, no a intenciones declaradas. Las políticas bien intencionadas con malos incentivos fracasan siempre.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-amber-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Escasez</span>
            <p class="text-slate-400 text-sm leading-relaxed">Principio fundamental: los recursos son limitados frente a necesidades ilimitadas. Toda decisión económica implica un trade-off. El precio es la señal que raciona los recursos escasos entre usos alternativos.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-amber-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Costo de Oportunidad</span>
            <p class="text-slate-400 text-sm leading-relaxed">El verdadero costo de una decisión es lo que se sacrifica al no elegir la mejor alternativa disponible. No aparece en ninguna factura, pero es el costo más real de la economía.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-amber-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Control de Precios</span>
            <p class="text-slate-400 text-sm leading-relaxed">Regulación gubernamental que fija precios por debajo (precio máximo) o por encima (precio mínimo) del equilibrio de mercado. Genera escasez o excedentes respectivamente, y distorsiona la asignación de recursos.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-amber-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Salario Mínimo</span>
            <p class="text-slate-400 text-sm leading-relaxed">Precio mínimo del trabajo. Si se fija por encima del salario de equilibrio, reduce la cantidad demandada de trabajo (desempleo) y puede sustituir mano de obra joven/poco calificada por automatización.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-amber-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Control de Rentas</span>
            <p class="text-slate-400 text-sm leading-relaxed">Precio máximo para el alquiler de viviendas. Beneficia a los inquilinos actuales pero reduce la oferta futura, deteriora el mantenimiento de inmuebles y crea mercados negros. Historia universal de fracaso documentado.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-amber-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Consecuencias No Previstas</span>
            <p class="text-slate-400 text-sm leading-relaxed">Efectos no intencionados de las intervenciones, frecuentemente contrarios al objetivo buscado. Principio central de Sowell: juzgar las políticas por sus resultados, no por sus intenciones.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-amber-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Visión Constrained</span>
            <p class="text-slate-400 text-sm leading-relaxed">En "A Conflict of Visions" de Sowell: perspectiva que reconoce las limitaciones inherentes de la naturaleza humana. Las instituciones (mercado, derecho, tradición) canalizan intereses egoístas hacia resultados sociales positivos.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-amber-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Conocimiento Disperso</span>
            <p class="text-slate-400 text-sm leading-relaxed">En Hayek: el conocimiento económico relevante está disperso entre millones de individuos y no puede ser centralizado. El mercado lo agrega eficientemente a través de precios; la planificación central no puede reemplazarlo.</p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">EconAcademy · Economía Básica EB7</p>
</footer>

</div>

</div>
