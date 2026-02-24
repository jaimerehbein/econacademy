<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-indigo-500 rounded-full"></div>
        <span class="text-indigo-400 font-black text-[10px] uppercase tracking-[0.4em]">Economics Master Series</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
        MIC10
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-indigo-500/15 text-indigo-300 border border-indigo-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Zero-Noise UX</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">v9.0 · Dark Mode</span>
    </div>
</header>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4"><!-- HERO --></p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Equilibrio General y Eficiencia</p>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📖</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r from-indigo-300 to-violet-400 bg-clip-text text-transparent break-words leading-tight">Fundamentos del Equilibrio General y la Economía Abierta</h2>
        <div class="w-10 md:w-14 h-1 bg-indigo-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">El análisis del equilibrio general representa la culminación de la teoría microeconómica neoclásica, integrando el comportamiento de consumidores y productores en un sistema de mercados simultáneos. A diferencia del equilibrio parcial, que aísla un mercado asumiendo <em>ceteris paribus</em>, el equilibrio general endogeniza los precios y las cantidades de todos los bienes, permitiendo el estudio de la interdependencia económica y los efectos de retroalimentación.</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-indigo-500/15 border-indigo-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">🔢</span>
    <h3 class="text-xl font-bold text-indigo-300 tracking-tight">El Modelo Walrasiano Formalizado</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Basándonos en la formalización de Gérard Debreu, una economía se define por los conjuntos de consumo, las preferencias y las dotaciones iniciales de los agentes, así como por los conjuntos de producción de las firmas. Sea una economía $E$ con $m$ consumidores y $n$ productores. Un estado de la economía se define como una tupla de vectores en $\mathbb{R}^L$ (donde $L$ es el número de mercancías) <span class="hidden" data-ref="1" aria-hidden="true"></span>.</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">El equilibrio walrasiano (o competitivo) se define por un vector de precios $p^* \in \mathbb{R}^L$ y una asignación $((x_i^*), (y_j^*))$ tal que:</p>
<p class="text-slate-400 text-base mb-6">$$ \sum_{i=1}^m x_i^* - \sum_{j=1}^n y_j^* - \sum_{i=1}^m \omega_i = 0 $$</p>

<div class="flex items-start gap-5 p-5 bg-indigo-500/10 rounded-2xl my-3 border bg-indigo-500/20 hover:bg-indigo-500/15 transition-all">
    <!-- step:1 -->
    <div class="bg-indigo-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Maximización de la Utilidad:</strong> Para cada consumidor $i$, $x_i^*$ maximiza su utilidad $u_i(x_i)$ sujeto a la restricción presupuestaria $p^* \cdot x_i \leq p^* \cdot \omega_i + \sum_{j=1}^n \theta_{ij} p^* \cdot y_j^*$, donde $\omega_i$ es la dotación inicial y $\theta_{ij}$ la participación en los beneficios de la firma $j$ <span class="hidden" data-ref="2" aria-hidden="true"></span>.</div>
</div>

<div class="flex items-start gap-5 p-5 bg-indigo-500/10 rounded-2xl my-3 border bg-indigo-500/20 hover:bg-indigo-500/15 transition-all">
    <!-- step:2 -->
    <div class="bg-indigo-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Maximización del Beneficio:</strong> Para cada firma $j$, el plan de producción $y_j^*$ maximiza el beneficio $\pi_j(p) = p^* \cdot y_j$ dado el conjunto de producción tecnológicamente factible $Y_j$ <span class="hidden" data-ref="3" aria-hidden="true"></span>.</div>
</div>

<div class="flex items-start gap-5 p-5 bg-indigo-500/10 rounded-2xl my-3 border bg-indigo-500/20 hover:bg-indigo-500/15 transition-all">
    <!-- step:3 -->
    <div class="bg-indigo-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">3</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Vaciado de Mercados:</strong> La demanda neta agregada es cero (o menor o igual a cero con precios nulos para bienes libres):</div>
</div>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    La existencia de este equilibrio se garantiza bajo supuestos de convexidad de los conjuntos de preferencias y producción, aplicando teoremas de punto fijo como los de Brouwer o Kakutani sobre la correspondencia de exceso de demanda $z(p)$ <span class="hidden" data-ref="4, 5" aria-hidden="true"></span>. La <strong>Ley de Walras</strong> es fundamental aquí, estableciendo que el valor del exceso de demanda agregado es idénticamente nulo para cualquier sistema de precios $p$: $$ p \cdot z(p) \equiv 0 $$ Esto implica que si $L-1$ mercados están en equilibrio, el mercado $L$-ésimo también lo estará.
</div>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-indigo-500/15 border-indigo-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">🌐</span>
    <h3 class="text-xl font-bold text-indigo-300 tracking-tight">La Economía Abierta y las Ganancias del Comercio</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Extendiendo el modelo de autarquía (economía cerrada) a una economía abierta, introducimos el concepto de <strong>precios mundiales</strong> ($P^W$). Siguiendo la lógica ricardiana y de Heckscher-Ohlin presentada en los textos de Mankiw, el comercio permite separar la producción del consumo <span class="hidden" data-ref="6" aria-hidden="true"></span>.</p>
<p class="text-slate-400 text-base mb-4">En una economía abierta pequeña, el país es tomador de precios. El equilibrio se altera de la siguiente manera:</p>
<ul class="my-6 space-y-3">
<li class="flex items-start gap-3 text-slate-300 text-base leading-relaxed"><span class="text-indigo-400 mt-1 flex-shrink-0">▸</span><span>Si el precio mundial $P^W$ es mayor que el precio de autarquía $P^A$, el país exporta el bien. La cantidad producida aumenta hasta que el costo marginal iguala a $P^W$, mientras que el consumo doméstico disminuye.</span></li>
<li class="flex items-start gap-3 text-slate-300 text-base leading-relaxed"><span class="text-indigo-400 mt-1 flex-shrink-0">▸</span><span>Si $P^W < P^A$, el país importa. La producción doméstica se contrae y el consumo aumenta.</span></li>
</ul>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Formalmente, el beneficio del comercio se demuestra mediante la expansión del conjunto de consumo factible. Aunque la Frontera de Posibilidades de Producción (FPP) permanece inalterada (restricción tecnológica), la "Frontera de Posibilidades de Consumo" se expande gracias a los términos de intercambio. El bienestar total ($W$) aumenta, medido como la suma del excedente del consumidor ($EC$) y del productor ($EP$) <span class="hidden" data-ref="7" aria-hidden="true"></span>:</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    $$ \Delta W = \Delta EC + \Delta EP > 0 $$
</div>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    En el equilibrio de libre comercio, la Relación Marginal de Transformación (RMT) iguala a los precios mundiales, que a su vez igualan a la Relación Marginal de Sustitución (RMS) de los consumidores: $$ RMT_{xy} = \frac{P_x^W}{P_y^W} = RMS_{xy} $$ Esto asegura la eficiencia en el intercambio y en la producción a nivel global, aunque genera efectos distributivos internos (ganadores y perdedores) <span class="hidden" data-ref="8, 9" aria-hidden="true"></span>.
</div>

<div class="bg-gradient-to-br from-indigo-950/90 to-slate-900/90 border border-indigo-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-indigo-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-indigo-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>El análisis del equilibrio general representa la culminación de la teoría microeconómica neoclásica, integrando el comportamiento de consumidores y productores en un sistema de mercados simultáneos.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-indigo-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Basándonos en la formalización de Gérard Debreu, una economía se define por los conjuntos de consumo, las preferencias y las dotaciones iniciales de los agentes, así como por los conjuntos de producción de las firmas.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-indigo-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>El equilibrio walrasiano (o competitivo) se define por un vector de precios $p^* \in \mathbb{R}^L$ y una asignación $((x_i^*), (y_j^*))$ tal que:.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-indigo-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Extendiendo el modelo de autarquía (economía cerrada) a una economía abierta, introducimos el concepto de precios mundiales ($P^W$).</span></li>
        </ul>
    </div>
</div>
</section>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">🌱</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r from-cyan-300 to-blue-400 bg-clip-text text-transparent break-words leading-tight">Eficiencia de Pareto y Teoremas del Bienestar</h2>
        <div class="w-10 md:w-14 h-1 bg-cyan-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">El concepto normativo central en la teoría del equilibrio general es la <strong>Eficiencia de Pareto</strong>. Una asignación es Pareto-eficiente si no es posible reasignar recursos para mejorar el bienestar de un agente sin empeorar el de otro <span class="hidden" data-ref="10, 11" aria-hidden="true"></span>.</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-cyan-500/15 border-cyan-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-cyan-300 tracking-tight">Condiciones Marginales de Eficiencia</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Para que una asignación sea eficiente en una economía con producción, deben cumplirse tres condiciones simultáneas, derivadas del análisis de la Caja de Edgeworth y la FPP <span class="hidden" data-ref="12, 13" aria-hidden="true"></span>:</p>
<p class="text-slate-400 text-base mb-6">$$ RMS_{xy}^A = RMS_{xy}^B $$ $$ RMST_{LK}^X = RMST_{LK}^Y = \frac{w}{r} $$ $$ RMT_{xy} = RMS_{xy} $$</p>

<div class="flex items-start gap-5 p-5 bg-cyan-500/10 rounded-2xl my-3 border bg-cyan-500/20 hover:bg-cyan-500/15 transition-all">
    <!-- step:1 -->
    <div class="bg-cyan-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Eficiencia en el Intercambio:</strong> Las tasas marginales de sustitución entre cualquier par de bienes deben ser iguales para todos los consumidores:</div>
</div>

<div class="flex items-start gap-5 p-5 bg-cyan-500/10 rounded-2xl my-3 border bg-cyan-500/20 hover:bg-cyan-500/15 transition-all">
    <!-- step:2 -->
    <div class="bg-cyan-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Eficiencia en la Producción:</strong> Las tasas marginales de sustitución técnica (RMST) entre factores deben ser iguales para todas las empresas (minimización de costos eficiente):</div>
</div>

<div class="flex items-start gap-5 p-5 bg-cyan-500/10 rounded-2xl my-3 border bg-cyan-500/20 hover:bg-cyan-500/15 transition-all">
    <!-- step:3 -->
    <div class="bg-cyan-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">3</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Eficiencia en la Mezcla de Productos (Eficiencia Top-Level):</strong> La tasa a la que la economía <em>puede</em> transformar un bien en otro (RMT) debe igualar la tasa a la que los consumidores <em>desean</em> intercambiarlos (RMS):</div>
</div>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-cyan-500/15 border-cyan-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-cyan-300 tracking-tight">Los Teoremas Fundamentales</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La conexión entre el equilibrio competitivo y la eficiencia se formaliza en dos teoremas <span class="hidden" data-ref="14, 15" aria-hidden="true"></span>:</p>
<ul class="my-6 space-y-3">
<li class="flex items-start gap-3 text-slate-300 text-base leading-relaxed"><span class="text-cyan-400 mt-1 flex-shrink-0">▸</span><span><strong>Primer Teorema del Bienestar:</strong> Si las preferencias son localmente no saciadas y existen mercados completos, todo equilibrio competitivo (Walrasiano) es Pareto-eficiente. Este teorema formaliza la intuición de la "mano invisible" de Adam Smith, indicando que los mercados descentralizados logran la eficiencia asignativa sin necesidad de un planificador central <span class="hidden" data-ref="16" aria-hidden="true"></span>.</span></li>
<li class="flex items-start gap-3 text-slate-300 text-base leading-relaxed"><span class="text-cyan-400 mt-1 flex-shrink-0">▸</span><span><strong>Segundo Teorema del Bienestar:</strong> Bajo supuestos de convexidad en preferencias y tecnología, cualquier asignación Pareto-eficiente puede sostenerse como un equilibrio competitivo mediante una redistribución adecuada de las dotaciones iniciales (transferencias de suma fija o <em>lump-sum</em>) y dejando que el mercado actúe. Este teorema separa las cuestiones de eficiencia de las de equidad distributiva <span class="hidden" data-ref="17" aria-hidden="true"></span>.</span></li>
</ul>

<div class="bg-gradient-to-br from-cyan-950/90 to-slate-900/90 border border-cyan-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-cyan-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-cyan-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>El concepto normativo central en la teoría del equilibrio general es la Eficiencia de Pareto.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-cyan-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Para que una asignación sea eficiente en una economía con producción, deben cumplirse tres condiciones simultáneas, derivadas del análisis de la Caja de Edgeworth y la FPP :.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-cyan-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La conexión entre el equilibrio competitivo y la eficiencia se formaliza en dos teoremas :.</span></li>
        </ul>
    </div>
</div>
</section>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📈</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r from-emerald-300 to-teal-400 bg-clip-text text-transparent break-words leading-tight">Intervención Gubernamental: Distorsiones de Precios e Impuestos</h2>
        <div class="w-10 md:w-14 h-1 bg-emerald-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Cuando el gobierno interviene en el mecanismo de precios, se rompe la igualdad entre la valoración marginal de los consumidores y el costo marginal de los productores, generando ineficiencias (Pérdida Irrecuperable de Eficiencia - PIE).</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-emerald-500/15 border-emerald-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📈</span>
    <h3 class="text-xl font-bold text-emerald-300 tracking-tight">Controles de Precios: Máximos y Mínimos</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Las restricciones directas a los precios impiden el ajuste del mercado hacia el equilibrio $(Q^*, P^*)$.</p>
<p class="text-slate-400 text-base mb-6"><strong>Efecto:</strong> Genera un exceso de demanda (escasez), dado que $Q_D(P_{max}) > Q_S(P_{max})$. <strong>Mecanismo de racionamiento:</strong> Al no ajustar el precio, surgen mecanismos no relacionados con precios (colas, mercado negro, discriminación). <strong>Análisis de Bienestar:</strong> El excedente del consumidor puede aumentar para quienes consiguen el bien, pero el excedente del productor cae drásticamente. El resultado es una pérdida neta de bienestar porque la cantidad transada $Q_{trans} = \min(Q_D, Q_S) = Q_S$ es menor que la cantidad eficiente $Q^*$ [18-21].</p>

<div class="flex items-start gap-5 p-5 bg-emerald-500/10 rounded-2xl my-3 border bg-emerald-500/20 hover:bg-emerald-500/15 transition-all">
    <!-- step:1 -->
    <div class="bg-emerald-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Precio Máximo ($P_{max} < P^*$):</strong> Se establece legalmente un precio por debajo del equilibrio (ej. control de alquileres).</div>
</div>
<p class="text-slate-400 text-base mb-6"><strong>Efecto:</strong> Genera un exceso de oferta (excedente), dado que $Q_S(P_{min}) > Q_D(P_{min})$. <strong>Ineficiencia:</strong> Se produce desempleo de factores o acumulación de inventarios no deseados. La cantidad transada se limita a la demanda: $Q_{trans} = Q_D < Q^*$. Al igual que en el precio máximo, se genera una PIE representada por el área entre las curvas de oferta y demanda entre $Q_{trans}$ y $Q^*$ [22-24].</p>

<div class="flex items-start gap-5 p-5 bg-emerald-500/10 rounded-2xl my-3 border bg-emerald-500/20 hover:bg-emerald-500/15 transition-all">
    <!-- step:2 -->
    <div class="bg-emerald-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Precio Mínimo ($P_{min} > P^*$):</strong> Se establece un piso legal (ej. salario mínimo).</div>
</div>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-emerald-500/15 border-emerald-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">🏛️</span>
    <h3 class="text-xl font-bold text-emerald-300 tracking-tight">Efecto de Impuestos Indirectos y Pérdida de Eficiencia</h3>
</div>


<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    Los impuestos indirectos (ad valorem o específicos) crean una "cuña" (<em>tax wedge</em>) entre el precio que paga el comprador ($P_c$) y el que recibe el vendedor ($P_v$): $$ P_c = P_v + t $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La incidencia del impuesto no depende de sobre quién recae legalmente, sino de las <strong>elasticidades relativas</strong> de la oferta y la demanda. La carga del impuesto recae más fuertemente sobre el lado más inelástico del mercado (Principio de la Incidencia Fiscal) <span class="hidden" data-ref="25" aria-hidden="true"></span>.</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    <strong>Pérdida Irrecuperable de Eficiencia (PIE):</strong> El impuesto reduce la cantidad de equilibrio de $Q^*$ a $Q_t$. La pérdida de bienestar social se debe a que se dejan de realizar transacciones mutuamente beneficiosas donde la valoración del consumidor excedía el costo del productor. Formalmente, la PIE se aproxima mediante el triángulo de Harberger: $$ PIE \approx \frac{1}{2} \cdot t \cdot (Q^* - Q_t) $$ O en términos de elasticidades ($\epsilon_D, \epsilon_S$): $$ PIE \approx \frac{1}{2} \cdot t^2 \cdot \frac{P \cdot Q}{P} \cdot \frac{\epsilon_D \cdot \epsilon_S}{\epsilon_D + \epsilon_S} $$ Nótese que la PIE crece con el cuadrado de la tasa impositiva ($t^2$), lo que implica que impuestos marginales altos son desproporcionadamente distorsionantes <span class="hidden" data-ref="26, 27" aria-hidden="true"></span>.
</div>

<div class="bg-gradient-to-br from-emerald-950/90 to-slate-900/90 border border-emerald-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-emerald-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-emerald-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Cuando el gobierno interviene en el mecanismo de precios, se rompe la igualdad entre la valoración marginal de los consumidores y el costo marginal de los productores, generando ineficiencias (Pérdida Irrecuperable de Eficiencia - PIE).</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-emerald-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Las restricciones directas a los precios impiden el ajuste del mercado hacia el equilibrio $(Q^*, P^*)$.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-emerald-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La incidencia del impuesto no depende de sobre quién recae legalmente, sino de las elasticidades relativas de la oferta y la demanda.</span></li>
        </ul>
    </div>
</div>
</section>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📈</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r from-amber-300 to-orange-400 bg-clip-text text-transparent break-words leading-tight">Síntesis de Tipología de Fallos y Diseño de Mercados</h2>
        <div class="w-10 md:w-14 h-1 bg-amber-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">El Primer Teorema del Bienestar falla cuando no se cumplen sus supuestos fundamentales. Identificamos tres categorías principales de fallos de mercado que justifican, teóricamente, la intervención pública o el rediseño del mercado.</p>
<!-- section: 1. -->
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-amber-500/15 border-amber-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-amber-300 tracking-tight">Externalidades</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Ocurren cuando la función de utilidad o producción de un agente se ve afectada directamente por las acciones de otro agente, sin que exista una compensación de mercado <span class="hidden" data-ref="28, 29" aria-hidden="true"></span>. <em> <strong>Externalidad Negativa:</strong> El Costo Social Marginal ($CSM$) es mayor que el Costo Privado Marginal ($CPM$). El mercado produce en exceso ($Q_{mkt} > Q_{opt}$). Solución Pigouviana: Impuesto $t = CSM - CPM$ en el óptimo. </em> <strong>Externalidad Positiva:</strong> El Beneficio Social Marginal excede al privado. El mercado sub-produce. Solución: Subsidios o derechos de propiedad (Teorema de Coase).</p>
<!-- section: 2. -->
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-amber-500/15 border-amber-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-amber-300 tracking-tight">Bienes Públicos</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Bienes caracterizados por ser <strong>no rivales</strong> (el consumo de uno no reduce el de otro) y <strong>no excluyentes</strong> (no se puede impedir su uso). Esto genera el problema del <em>polizón</em> (free-rider), donde los individuos no revelan su verdadera valoración, llevando a una provisión sub-óptima por el mercado privado <span class="hidden" data-ref="29, 30" aria-hidden="true"></span>. La condición de eficiencia para bienes públicos es la regla de Samuelson: la suma de las Tasas Marginales de Sustitución debe igualar la Tasa Marginal de Transformación: $$ \sum_{i=1}^m RMS_{i} = RMT $$</p>
<!-- section: 3. -->
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-amber-500/15 border-amber-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">💻</span>
    <h3 class="text-xl font-bold text-amber-300 tracking-tight">Información Asimétrica</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Cuando una parte de la transacción posee más información que la otra. <em> <strong>Selección Adversa:</strong> Ocurre </em>antes<em> de la transacción (ej. mercado de seguros o autos usados de Akerlof). Los productos de baja calidad expulsan a los de alta calidad del mercado <span class="hidden" data-ref="31, 32" aria-hidden="true"></span>. </em> <strong>Riesgo Moral:</strong> Ocurre <em>después</em> de la transacción. Un agente cambia su comportamiento al estar asegurado o no monitoreado (problema principal-agente) <span class="hidden" data-ref="33" aria-hidden="true"></span>.</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-amber-500/15 border-amber-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📈</span>
    <h3 class="text-xl font-bold text-amber-300 tracking-tight">Diseño de Mercados y Teoría de Juegos</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Ante estos fallos, la teoría económica moderna utiliza la <strong>Teoría de Juegos</strong> y el <strong>Diseño de Mecanismos</strong> para estructurar reglas que incentiven la revelación de información verdadera y la eficiencia. <em> <strong>Subastas:</strong> Mecanismos para asignar recursos cuando la información sobre las valoraciones es privada. El diseño (primer precio, segundo precio, Vickrey) busca maximizar el ingreso del vendedor o la eficiencia de la asignación <span class="hidden" data-ref="34" aria-hidden="true"></span>. </em> <strong>Oligopolio y Estrategia:</strong> En mercados con pocos agentes (Cournot, Bertrand, Stackelberg), las empresas reconocen su interdependencia. El equilibrio de Nash describe situaciones donde ningún agente tiene incentivos a desviarse unilateralmente, lo cual suele resultar en precios superiores al costo marginal ($P > CMg$), generando ineficiencia asignativa <span class="hidden" data-ref="35, 36" aria-hidden="true"></span>.</p>

<div class="bg-gradient-to-br from-amber-950/90 to-slate-900/90 border border-amber-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-amber-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-amber-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>El Primer Teorema del Bienestar falla cuando no se cumplen sus supuestos fundamentales.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-amber-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Ocurren cuando la función de utilidad o producción de un agente se ve afectada directamente por las acciones de otro agente, sin que exista una compensación de mercado.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-amber-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Bienes caracterizados por ser no rivales (el consumo de uno no reduce el de otro) y no excluyentes (no se puede impedir su uso).</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-amber-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Cuando una parte de la transacción posee más información que la otra.</span></li>
        </ul>
    </div>
</div>
</section>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📌</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r from-rose-300 to-pink-400 bg-clip-text text-transparent break-words leading-tight">Aplicaciones Avanzadas - Perspectiva Master</h2>
        <div class="w-10 md:w-14 h-1 bg-rose-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Para consolidar la comprensión del equilibrio general y la eficiencia, sintetizamos la aplicación del modelo en contextos de producción endógena y análisis de bienestar.</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-rose-500/15 border-rose-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">🔢</span>
    <h3 class="text-xl font-bold text-rose-300 tracking-tight">Modelo del Agente Representativo: Robinson Crusoe</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Este modelo integra consumo y producción en un solo agente, sirviendo como base microeconómica para la macroeconomía. Crusoe debe decidir cuánto trabajar ($L$) y cuánto ocio disfrutar ($24-L$) para producir cocos ($F$) <span class="hidden" data-ref="37" aria-hidden="true"></span>.</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    <strong>Problema Centralizado (Autogestión):</strong> Maximizamos la utilidad $U(Ocio, F)$ sujeto a la función de producción $F = f(L)$. La condición de primer orden (CPO) implica que la pendiente de la curva de indiferencia (RMS) debe igualar la pendiente de la frontera de producción (Productividad Marginal del Trabajo, $PMg_L$): $$ RMS_{Ocio, F} = PMg_L $$
</div>
<p class="text-slate-400 text-base mb-6"><strong>Descentralización de Mercado:</strong> Podemos separar las decisiones introduciendo una empresa ("CruPesca S.A.") y un consumidor, mediados por un sistema de precios (salario $w$, precio del bien $p$) y beneficios $\Pi$.</p>

<div class="flex items-start gap-5 p-5 bg-rose-500/10 rounded-2xl my-3 border bg-rose-500/20 hover:bg-rose-500/15 transition-all">
    <!-- step:1 -->
    <div class="bg-rose-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Empresa:</strong> Maximiza $\Pi = pF - wL$. Condición: $p \cdot PMg_L = w$.</div>
</div>

<div class="flex items-start gap-5 p-5 bg-rose-500/10 rounded-2xl my-3 border bg-rose-500/20 hover:bg-rose-500/15 transition-all">
    <!-- step:2 -->
    <div class="bg-rose-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Consumidor:</strong> Maximiza utilidad sujeto a $pC \leq wL + \Pi$. Condición: $RMS = w/p$.</div>
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Combinando ambas condiciones, obtenemos $RMS = PMg_L$. Esto demuestra rigurosamente que el sistema de precios es capaz de replicar la solución del planificador central, validando los teoremas del bienestar en una economía con producción <span class="hidden" data-ref="38, 39" aria-hidden="true"></span>.</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-rose-500/15 border-rose-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">🌱</span>
    <h3 class="text-xl font-bold text-rose-300 tracking-tight">Cálculo de Pérdida de Bienestar en Monopolio (Equilibrio Parcial vs. General)</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">En un análisis de equilibrio parcial, la pérdida social del monopolio es el triángulo bajo la demanda. Sin embargo, en una perspectiva de <em>Equilibrio General</em>, debemos considerar que los recursos liberados por el sector monopolizado fluyen hacia el sector competitivo. Si el sector $X$ es monopolio y el $Y$ competencia perfecta: 1. El monopolista fija $P_x > CMg_x$, reduciendo $X$. 2. Los factores $L$ y $K$ fluyen hacia $Y$, aumentando su producción más allá del nivel óptimo. 3. La ineficiencia no es solo la "pérdida del triángulo" en $X$, sino una distorsión en la Tasa Marginal de Transformación de la economía, donde $RMT_{xy} \neq \frac{P_x}{P_y}$. La economía opera sobre la FPP pero en un punto incorrecto (ineficiencia asignativa top-level), donde la valoración relativa de los consumidores no coincide con el costo de oportunidad tecnológico <span class="hidden" data-ref="13, 40" aria-hidden="true"></span>.</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    $$ \text{Ineficiencia Global: } RMS_{xy} = \frac{P_x^{monop}}{P_y} > \frac{CMg_x}{CMg_y} = RMT_{xy} $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Esta discrepancia confirma que los fallos de mercado en un sector tienen efectos de derrame (spillover) en toda la economía, justificando el enfoque de equilibrio general para la evaluación de políticas públicas complejas.</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">&copy; 2026 Tech Institute | Master en Microeconomía | Generación O-3</p>

<div class="bg-gradient-to-br from-rose-950/90 to-slate-900/90 border border-rose-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-rose-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-rose-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Para consolidar la comprensión del equilibrio general y la eficiencia, sintetizamos la aplicación del modelo en contextos de producción endógena y análisis de bienestar.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-rose-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Este modelo integra consumo y producción en un solo agente, sirviendo como base microeconómica para la macroeconomía.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-rose-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Combinando ambas condiciones, obtenemos $RMS = PMg_L$.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-rose-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>En un análisis de equilibrio parcial, la pérdida social del monopolio es el triángulo bajo la demanda.</span></li>
        </ul>
    </div>
</div>
</section>


<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">
        <span class="text-fuchsia-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo MIC10</h3>
    </div>
    <div class="bg-black/30 p-2 md:p-6 rounded-2xl border border-white/5 overflow-x-auto">
        
        <pre class="mermaid bg-transparent flex justify-center">
graph LR
    A[Fundamentos Teóricos] --> B(Aplicación Práctica)
    B --> C{Análisis Crítico}
    C -->|Evaluación| D[Validación Empírica]
    C -->|Revisión| E[Ajuste de Modelo]
    
    classDef default fill:#111827,stroke:#d946ef,stroke-width:1px,color:#d1d5db
    classDef decision fill:#701a75,stroke:#d946ef,stroke-width:2px,color:#fff
    class C decision
        </pre>

    </div>
</div>

<!-- GLOSARIO -->
<section class="mb-24">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-10">
        <span class="text-indigo-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[GL]</span>
        <h2 class="text-white font-black text-xl sm:text-2xl uppercase tracking-tighter break-words leading-tight">Glosario de Microeconomía</h2>
    </div>
    <div class="space-y-3">
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-indigo-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Mecanismo de Subasta</span>
            <p class="text-slate-400 text-sm leading-relaxed">Protocolos ingenieriles arquitecturas de licitación subyacentes y arenas resolutorias pre-ensayadas artificiales de puja canónica acaparadora destiladoras extractivas asimétricas empedernidas e inquisidoras para rematar acervos raros o concesiones estatales donde la meta utilitarista del rematador expropiador maximizador no es meramente claudicar la cosa final adjudicadora asintótica sino extraer extirpar desnudar arrancar abismal subrepticia y empíricamente exprimir asfixiantemente inquisitiva ex-post implacable inescrutable estrujar dictatorial subyugando extorsiva el valor e inmenso anhelo oculto hermético inescrutable subjetivo resguardado opaco silenciado predispuesto celosamente inconfensable del rematante y bolsillos del adjudicatario estrujando y drenando asimilándole y arrebatándole su renuente escondida colosal y máxima renuente fáctica inconfesa ineluctable y velada valoración cruda.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-indigo-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Subasta Inglesa</span>
            <p class="text-slate-400 text-sm leading-relaxed">Liturgia teatral rematadora en escalada exultante viva aural ascendente coral donde las proferencias pujan incesantes desafiantes agigantando en estentóreas sobrepujas crecientes abismadoras desatadas el umbral P hasta destilar marginar diezmar ahogar espantar excluir e inhabilitar desbancar asfixiar desplomar y desfondar exhaustivamente a todos los lidiadores competentes contendientes acorralados cediendo la victoria y excedentario al último estoico sobreviviente titán impasible asimilado.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-indigo-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Subasta Holandesa</span>
            <p class="text-slate-400 text-sm leading-relaxed">Inquisición inversa tensa aural cronómetro depresivo fútil descendente agónico licuador vertiginosa y de pánico relámpago ineluctable precipitando precios exultantes abismales estrafalarios exorbitantes en picada asfixiante declinante licuacionista asimétrica ferial hasta que el inaguantable silencio asimilador se quiebra por un postor desesperado claudicando precipitado rompiendo el vacío aterrorizado aterrorizante de extraviar perder el lote parando frenando y asimilando el reloj anclando asimétrica su precio victorioso y acaparador.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-indigo-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Maldición del Ganador</span>
            <p class="text-slate-400 text-sm leading-relaxed">Resaca fatal inmoladora tragedia y escarmiento letal pírrico castigador ex-post del victorioso exultante rematador en subastas de lotes de valores ignotos o hidrocarburos ciegos yacimientos inescrutables empíricos opacos objetivos subyacentes donde, al adjudicarse la plaza, infiere aterrorizadamente abismal y dolorosamente desoladora y certera innegable fútilmente abismadora y colosalmente que su tasación inusitada ganadora fue la más desvariada absurda irracional descabellada y distorsionada optimista asintótica de la manada encumbrada exacerbada y distorsionada sobreestimada perdiendo y quemando irremediablemente expropiando asfixiado rentabilidades fútiles asimilando su ruinosa inmersión quebrando abismada y destartaladamente abultada ruina o pérdida implacable.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-indigo-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Diseño de Mecanismos</span>
            <p class="text-slate-400 text-sm leading-relaxed">Alquimia teórica ingeniería inversa ex-ante o arquitectura matriz praxeológica empírica regidora inquisitoria manipuladora coercitiva suprema. En vez de tomar empíricas estáticas fijas las normativas y esperar claudicantes apacibles qué ecosistema o resolutivas clímax resultan, el demiurgo legislador estipulador matriz supremo bosqueja ingenia teje laberínticamente reenseña pergeña enmarca perversa o idónea subyugante acoplante diseña inscribe traza implanta primero alocada el clímax Pareto o desiderátum que anhela recabar socialmente inelástico y modela forja transmutador fiduciaria e implacable las normativas laberintos alicientes encrucijadas encuadres coactivas inorgánicas paramétricas que acorralen y encaucen indefectible encarrilada matemáticamente obligando forzosamente a que el tropel racional maximizador reaccionario des emboque irremediablemente cayendo asimilable esclavo ex-post inexorable y colusoria irrefutable y asintóticamente infalible abocado al anhelado pre-estatuido y concebido fin meta objetivo dictaminado o dictado supremo original inamovible previsor absoluto manipulador subyugador.</p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="mt-28 pt-10 border-t border-white/10">
    <div class="flex flex-col md:flex-row justify-between items-center gap-6">
        <div class="flex items-center gap-4">
            <div class="w-9 h-9 bg-indigo-600 rounded-xl flex items-center justify-center text-white font-black text-xs shadow-md">TE</div>
            <div>
                <p class="font-black text-white text-sm">Tech Economics Institute</p>
                <p class="text-slate-500 text-[10px] uppercase tracking-[0.3em]">Zero-Noise Architecture v9</p>
            </div>
        </div>
        <div class="flex gap-8 text-[10px] font-black text-slate-600 uppercase tracking-widest">
            <a href="#" class="hover:text-indigo-400 transition-colors">Glosario</a>
            <a href="#" class="hover:text-indigo-400 transition-colors">Recursos</a>
        </div>
    </div>
</footer>

</div>