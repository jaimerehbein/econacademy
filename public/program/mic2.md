<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-indigo-500 rounded-full"></div>
        <span class="text-indigo-400 font-black text-[10px] uppercase tracking-[0.4em]">Economics Master Series</span>
    </div>
    <h1 class="text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8">
        MIC2
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-indigo-500/15 text-indigo-300 border border-indigo-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Zero-Noise UX</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">v9.0 · Dark Mode</span>
    </div>
</header>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4"><!-- HERO --></p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Elección Intertemporal e Incertidumbre</p>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📖</span>
    <div>
        <h2 class="text-xl md:text-3xl font-black tracking-tight bg-gradient-to-r from-indigo-300 to-violet-400 bg-clip-text text-transparent">Fundamentos de la Elección Intertemporal</h2>
        <div class="w-10 md:w-14 h-1 bg-indigo-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">El análisis microeconómico estándar, en su versión estática, asume que las decisiones de consumo y producción ocurren en un único periodo. Sin embargo, una perspectiva de maestría requiere relajar este supuesto para incorporar la dimensión temporal. La elección intertemporal modela la toma de decisiones de los agentes económicos considerando que el consumo presente y el consumo futuro son bienes distintos, vinculados a través de los mercados de capitales.</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-indigo-500/15 border-indigo-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-indigo-300 tracking-tight">Restricción Presupuestaria Intertemporal y Valor Descontado</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Consideremos un agente representativo que vive durante dos periodos, $t=1$ (presente) y $t=2$ (futuro). El agente recibe una dotación de ingresos exógenos $m_1$ y $m_2$ en cada periodo y decide sus niveles de consumo $c_1$ y $c_2$. El mercado financiero permite transferir riqueza entre periodos a una tasa de interés $r$.</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    Si el consumidor decide ahorrar $s$ en el periodo 1 (donde $s = m_1 - c_1$), en el periodo 2 podrá consumir su ingreso $m_2$ más el ahorro capitalizado: $$ c_2 = m_2 + (m_1 - c_1)(1+r) $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Reordenando los términos, obtenemos la <strong>Restricción Presupuestaria Intertemporal</strong> en términos de valor presente <span class="hidden" data-ref="1" aria-hidden="true"></span>:</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    $$ c_1 + \frac{c_2}{1+r} = m_1 + \frac{m_2}{1+r} $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">El lado derecho de la ecuación representa el <strong>Valor Descontado (o Valor Presente)</strong> de la riqueza total del individuo. El término $\frac{1}{1+r}$ es el precio del consumo futuro en términos del consumo presente. Económicamente, esto implica que renunciar a una unidad de consumo hoy permite obtener $(1+r)$ unidades mañana.</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-indigo-500/15 border-indigo-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-indigo-300 tracking-tight">Preferencias Intertemporales y la Tasa Marginal de Preferencia Temporal</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Las preferencias del individuo sobre los flujos de consumo $(c_1, c_2)$ se representan mediante una función de utilidad intertemporal $U(c_1, c_2)$, la cual generalmente adopta una forma aditiva separable:</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    $$ U(c_1, c_2) = u(c_1) + \beta u(c_2) $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Donde $\beta$ es el factor de descuento subjetivo, tal que $0 < \beta < 1$, reflejando la impaciencia del consumidor (valora más la utilidad presente que la futura) <span class="hidden" data-ref="2" aria-hidden="true"></span>.</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La pendiente de la curva de indiferencia en este espacio intertemporal se define como la <strong>Relación Marginal de Sustitución Intertemporal</strong> o <strong>Relación Marginal de Preferencia Temporal (RMPT)</strong>. Matemáticamente:</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    $$ RMPT = \frac{\partial U / \partial c_1}{\partial U / \partial c_2} $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">En el óptimo, el consumidor maximiza su utilidad sujeto a su restricción presupuestaria. La condición de primer orden (tangencia) iguala la valoración subjetiva del tiempo con la valoración de mercado:</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    $$ RMPT = 1+r $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Esta condición establece que el consumidor ajustará su patrón de consumo y ahorro hasta que la tasa a la que <em>está dispuesto</em> a intercambiar consumo presente por futuro iguale la tasa a la que el mercado le <em>permite</em> hacer ese intercambio <span class="hidden" data-ref="3" aria-hidden="true"></span>.</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-indigo-500/15 border-indigo-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-indigo-300 tracking-tight">Estática Comparativa: Efectos de la Tasa de Interés</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Un cambio en la tasa de interés $r$ genera dos efectos contrapuestos en las decisiones de ahorro, análogos a los efectos ingreso y sustitución en la teoría del consumidor estática <span class="hidden" data-ref="3" aria-hidden="true"></span>, <span class="hidden" data-ref="4" aria-hidden="true"></span>:</p>

<div class="flex items-start gap-5 p-5 bg-indigo-500/10 rounded-2xl my-3 border bg-indigo-500/20 hover:bg-indigo-500/15 transition-all">
    <!-- step:1 -->
    <div class="bg-indigo-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Efecto Sustitución:</strong> Un aumento en $r$ encarece el consumo presente relativo al futuro. El consumidor racional tenderá a reducir $c_1$ y aumentar el ahorro.</div>
</div>

<div class="flex items-start gap-5 p-5 bg-indigo-500/10 rounded-2xl my-3 border bg-indigo-500/20 hover:bg-indigo-500/15 transition-all">
    <!-- step:2 -->
    <div class="bg-indigo-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Efecto Ingreso:</strong> Para un ahorrador neto, un aumento en $r$ incrementa su riqueza total futura. Como el consumo es un bien normal, esto incentiva aumentar el consumo en ambos periodos ($c_1$ y $c_2$), lo que tiende a reducir el ahorro.</div>
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">El efecto neto sobre el ahorro es ambiguo y depende de la magnitud relativa de ambos efectos <span class="hidden" data-ref="4" aria-hidden="true"></span>.</p>
<div class="my-16 border-t border-white/10"></div>

<div class="bg-gradient-to-br from-indigo-950/90 to-slate-900/90 border border-indigo-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-indigo-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-indigo-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>El análisis microeconómico estándar, en su versión estática, asume que las decisiones de consumo y producción ocurren en un único periodo.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-indigo-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Consideremos un agente representativo que vive durante dos periodos, $t=1$ (presente) y $t=2$ (futuro).</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-indigo-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Reordenando los términos, obtenemos la Restricción Presupuestaria Intertemporal en términos de valor presente :.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-indigo-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>El lado derecho de la ecuación representa el Valor Descontado (o Valor Presente) de la riqueza total del individuo.</span></li>
        </ul>
    </div>
</div>
</section>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📌</span>
    <div>
        <h2 class="text-xl md:text-3xl font-black tracking-tight bg-gradient-to-r from-cyan-300 to-blue-400 bg-clip-text text-transparent">Elección bajo Incertidumbre</h2>
        <div class="w-10 md:w-14 h-1 bg-cyan-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">En el mundo real, los resultados de las decisiones económicas raramente son certeros. La Teoría de la Utilidad Esperada de von Neumann-Morgenstern (VNM) proporciona el marco analítico riguroso para modelar la elección en situaciones de riesgo.</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-cyan-500/15 border-cyan-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-cyan-300 tracking-tight">Loterías y Axiomas de Elección</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Formalizamos una situación de riesgo como una <strong>lotería</strong> $L$. Una lotería simple es una distribución de probabilidad sobre un conjunto de resultados o premios (normalmente niveles de riqueza o consumo) <span class="hidden" data-ref="5" aria-hidden="true"></span>. Sea $L = ((x_1, x_2.., x_n), (p_1, p_2.., p_n))$, donde $x_i$ son los resultados posibles y $p_i$ sus probabilidades asociadas, tal que $\sum_{i=1}^n p_i = 1$.</p>
<p class="text-slate-400 text-base mb-6">Para que exista una función de utilidad que represente las preferencias sobre estas loterías, deben cumplirse axiomas fundamentales <span class="hidden" data-ref="6" aria-hidden="true"></span>, <span class="hidden" data-ref="7" aria-hidden="true"></span>:</p>

<div class="flex items-start gap-5 p-5 bg-cyan-500/10 rounded-2xl my-3 border bg-cyan-500/20 hover:bg-cyan-500/15 transition-all">
    <!-- step:1 -->
    <div class="bg-cyan-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Completitud y Transitividad:</strong> El agente puede ordenar todas las loterías de manera consistente.</div>
</div>

<div class="flex items-start gap-5 p-5 bg-cyan-500/10 rounded-2xl my-3 border bg-cyan-500/20 hover:bg-cyan-500/15 transition-all">
    <!-- step:2 -->
    <div class="bg-cyan-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Continuidad:</strong> No existen "saltos" en las preferencias; si $L_1 \succ L_2 \succ L_3$, existe una probabilidad $\alpha$ tal que el agente es indiferente entre $L_2$ y una mezcla de $L_1$ y $L_3$.</div>
</div>

<div class="flex items-start gap-5 p-5 bg-cyan-500/10 rounded-2xl my-3 border bg-cyan-500/20 hover:bg-cyan-500/15 transition-all">
    <!-- step:3 -->
    <div class="bg-cyan-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">3</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Independencia:</strong> Si $L_1 \sim L_2$, entonces cualquier mezcla de probabilidad con una tercera lotería $L_3$ mantiene la indiferencia: $\alpha L_1 + (1-\alpha)L_3 \sim \alpha L_2 + (1-\alpha)L_3$.</div>
</div>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-cyan-500/15 border-cyan-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-cyan-300 tracking-tight">Valor Esperado vs. Utilidad Esperada</h3>
</div>


<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    Es crucial distinguir entre el valor esperado monetario de una lotería y la utilidad que reporta. El <strong>Valor Esperado</strong> se define como: $$ E(L) = \sum_{i=1}^n p_i x_i $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La <strong>Paradoja de San Petersburgo</strong> demostró que los individuos no toman decisiones basándose únicamente en el valor esperado (estarían dispuestos a pagar sumas infinitas por juegos con esperanza infinita, lo cual no ocurre empíricamente) <span class="hidden" data-ref="8" aria-hidden="true"></span>. La resolución reside en la <strong>Utilidad Esperada</strong>.</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Bajo los axiomas VNM, las preferencias del agente se representan maximizando la esperanza matemática de la utilidad de los resultados, no de los montos monetarios <span class="hidden" data-ref="9" aria-hidden="true"></span>:</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    $$ EU(L) = \sum_{i=1}^n p_i u(x_i) $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Donde $u(\cdot)$ es la función de utilidad de Bernoulli o función de utilidad elemental sobre la riqueza cierta.</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-cyan-500/15 border-cyan-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-cyan-300 tracking-tight">Actitudes ante el Riesgo</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La forma matemática de la función de utilidad $u(w)$ (donde $w$ es riqueza) determina la actitud del agente frente al riesgo <span class="hidden" data-ref="10" aria-hidden="true"></span>, <span class="hidden" data-ref="11" aria-hidden="true"></span>:</p>
<p class="text-slate-400 text-base mb-6">$$ u(E[L]) > EU(L) $$ Matemáticamente, esto implica que la función de utilidad es <strong>estrictamente cóncava</strong> ($u''(w) < 0$). Por la desigualdad de Jensen, la utilidad de la esperanza es mayor que la esperanza de la utilidad.</p>

<div class="flex items-start gap-5 p-5 bg-cyan-500/10 rounded-2xl my-3 border bg-cyan-500/20 hover:bg-cyan-500/15 transition-all">
    <!-- step:1 -->
    <div class="bg-cyan-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Aversión al Riesgo:</strong> Un agente es averso al riesgo si prefiere recibir el valor esperado de una lotería con certeza que jugar la lotería misma.</div>
</div>
<p class="text-slate-400 text-base mb-6">$$ u(E[L]) = EU(L) $$ La función de utilidad es <strong>lineal</strong> ($u''(w) = 0$).</p>

<div class="flex items-start gap-5 p-5 bg-cyan-500/10 rounded-2xl my-3 border bg-cyan-500/20 hover:bg-cyan-500/15 transition-all">
    <!-- step:2 -->
    <div class="bg-cyan-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Neutralidad al Riesgo:</strong> El agente es indiferente entre el valor esperado con certeza y la lotería.</div>
</div>
<p class="text-slate-400 text-base mb-6">$$ u(E[L]) < EU(L) $$ La función de utilidad es <strong>estrictamente convexa</strong> ($u''(w) > 0$).</p>

<div class="flex items-start gap-5 p-5 bg-cyan-500/10 rounded-2xl my-3 border bg-cyan-500/20 hover:bg-cyan-500/15 transition-all">
    <!-- step:3 -->
    <div class="bg-cyan-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">3</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Amante del Riesgo:</strong> El agente prefiere la lotería al valor esperado cierto.</div>
</div>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-cyan-500/15 border-cyan-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-cyan-300 tracking-tight">Equivalente Cierto y Prima de Riesgo</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Para cuantificar la aversión al riesgo, utilizamos dos conceptos clave:</p>
<p class="text-slate-400 text-base mb-6">$$ u(CE) = E[u(L)] = \sum p_i u(x_i) $$ Para un adverso al riesgo, $CE < E(L)$.</p>

<div class="flex items-start gap-5 p-5 bg-cyan-500/10 rounded-2xl my-3 border bg-cyan-500/20 hover:bg-cyan-500/15 transition-all">
    <!-- step:1 -->
    <div class="bg-cyan-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Equivalente Cierto (EC):</strong> Es la cantidad de riqueza garantizada que deja al individuo indiferente respecto a participar en la lotería $L$ <span class="hidden" data-ref="12" aria-hidden="true"></span>. Se define implícitamente como:</div>
</div>
<p class="text-slate-400 text-base mb-6">$$ \pi = E(L) - CE $$ Alternativamente, es el monto tal que: $$ u(E(L) - \pi) = EU(L) $$</p>

<div class="flex items-start gap-5 p-5 bg-cyan-500/10 rounded-2xl my-3 border bg-cyan-500/20 hover:bg-cyan-500/15 transition-all">
    <!-- step:2 -->
    <div class="bg-cyan-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Prima de Riesgo ($\pi$):</strong> Es la cantidad máxima de riqueza que un individuo está dispuesto a sacrificar (o pagar) para evitar el riesgo y obtener el valor esperado con certeza <span class="hidden" data-ref="13" aria-hidden="true"></span>.</div>
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Gráficamente, para un adverso al riesgo, la cuerda que une los puntos de utilidad sobre la curva cóncava (la utilidad esperada) está por debajo de la función de utilidad evaluada en el valor esperado <span class="hidden" data-ref="14" aria-hidden="true"></span>. La distancia horizontal entre la riqueza esperada y el equivalente cierto es la prima de riesgo.</p>
<div class="my-16 border-t border-white/10"></div>

<div class="bg-gradient-to-br from-cyan-950/90 to-slate-900/90 border border-cyan-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-cyan-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-cyan-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>En el mundo real, los resultados de las decisiones económicas raramente son certeros.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-cyan-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Formalizamos una situación de riesgo como una lotería $L$.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-cyan-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La Paradoja de San Petersburgo demostró que los individuos no toman decisiones basándose únicamente en el valor esperado (estarían dispuestos a pagar sumas infinitas por juegos con esperanza infinita, lo cual no ocurre empíricamente).</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-cyan-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Bajo los axiomas VNM, las preferencias del agente se representan maximizando la esperanza matemática de la utilidad de los resultados, no de los montos monetarios :.</span></li>
        </ul>
    </div>
</div>
</section>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📌</span>
    <div>
        <h2 class="text-xl md:text-3xl font-black tracking-tight bg-gradient-to-r from-emerald-300 to-teal-400 bg-clip-text text-transparent">Aplicaciones Avanzadas - Perspectiva Master</h2>
        <div class="w-10 md:w-14 h-1 bg-emerald-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">En este nivel de análisis, debemos integrar los conceptos de incertidumbre y tiempo para modelar mercados financieros, seguros y evaluar las limitaciones de los modelos estándar.</p>
<!-- section: 1. -->
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-emerald-500/15 border-emerald-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📈</span>
    <h3 class="text-xl font-bold text-emerald-300 tracking-tight">La Demanda de Seguros y el Teorema de Seguro Completo</h3>
</div>

<p class="text-slate-400 text-base mb-4">Una aplicación directa de la aversión al riesgo es el mercado de seguros. Supongamos un agente con riqueza $w_0$ que enfrenta un riesgo de pérdida $P$ con probabilidad $\alpha$. Su riqueza es una variable aleatoria:</p>
<ul class="my-6 space-y-3">
<li class="flex items-start gap-3 text-slate-300 text-base leading-relaxed"><span class="text-emerald-400 mt-1 flex-shrink-0">▸</span><span>Estado bueno (prob. $1-\alpha$): $w_0$</span></li>
<li class="flex items-start gap-3 text-slate-300 text-base leading-relaxed"><span class="text-emerald-400 mt-1 flex-shrink-0">▸</span><span>Estado malo (prob. $\alpha$): $w_0 - P$</span></li>
</ul>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Si el agente puede comprar cobertura $x$ pagando una prima por unidad de cobertura $\rho$, su problema de maximización es <span class="hidden" data-ref="15" aria-hidden="true"></span>:</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    $$ \max_{x} \quad (1-\alpha)u(w_0 - \rho x) + \alpha u(w_0 - P + x - \rho x) $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4"><strong>Resultado Teórico Fundamental:</strong> Si el mercado de seguros es perfectamente competitivo y la prima es <strong>actuarialmente justa</strong> (es decir, el precio del seguro iguala la probabilidad de pérdida, $\rho = \alpha$), un agente averso al riesgo decidirá asegurarse completamente ($x^* = P$). La condición de primer orden implica que la utilidad marginal de la riqueza debe ser igual en ambos estados de la naturaleza. Esto ocurre solo si la riqueza es constante en ambos estados, eliminando totalmente el riesgo de consumo <span class="hidden" data-ref="16" aria-hidden="true"></span>.</p>
<!-- section: 2. -->
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-emerald-500/15 border-emerald-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">💰</span>
    <h3 class="text-xl font-bold text-emerald-300 tracking-tight">Decisiones de Inversión en Activos Riesgosos (Modelo de Portafolio)</h3>
</div>


<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    Considere un inversor que debe asignar su riqueza $w_0$ entre un activo libre de riesgo (dinero) y un activo riesgoso con rendimiento aleatorio $\tilde{r}$. Sea $\beta$ la cantidad invertida en el activo riesgoso. La riqueza final es: $$ \tilde{w} = w_0 + \beta \tilde{r} $$
</div>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    El problema es: $\max_{\beta} E[u(w_0 + \beta \tilde{r})]$. La condición de primer orden es <span class="hidden" data-ref="17" aria-hidden="true"></span>: $$ E[u'(\tilde{w}) \cdot \tilde{r}] = 0 $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4"><strong>Implicación de Arrow-Pratt:</strong> Incluso si el individuo es adverso al riesgo, invertirá una cantidad positiva ($\beta > 0$) en el activo riesgoso siempre que el rendimiento esperado del activo sea positivo ($E[\tilde{r}] > 0$). Esto demuestra que la aversión al riesgo no implica rechazo total al riesgo, sino que exige una compensación (prima) en términos de retorno esperado para asumirlo <span class="hidden" data-ref="17" aria-hidden="true"></span>.</p>
<!-- section: 3. -->
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-emerald-500/15 border-emerald-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-emerald-300 tracking-tight">Crítica desde la Economía del Comportamiento (Behavioral Economics)</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">El modelo de Utilidad Esperada y Descuento Exponencial, aunque matemáticamente elegante, a menudo falla en predecir el comportamiento real. Desde una perspectiva avanzada, debemos reconocer las desviaciones sistemáticas:</p>
<ul class="my-6 space-y-3">
<li class="flex items-start gap-3 text-slate-300 text-base leading-relaxed"><span class="text-emerald-400 mt-1 flex-shrink-0">▸</span><span><strong>Descuento Hiperbólico:</strong> A diferencia del descuento exponencial constante ($\beta^t$), la evidencia sugiere que los agentes tienen preferencias inconsistentes temporalmente ("sesgo hacia el presente"). Valoran mucho más el "ahora" frente a "mañana" que "dentro de un año" frente a "dentro de un año y un día". Esto se modela a menudo con preferencias $\beta-\delta$, donde el factor de descuento a corto plazo cae dramáticamente <span class="hidden" data-ref="18" aria-hidden="true"></span>, <span class="hidden" data-ref="19" aria-hidden="true"></span>.</span></li>
<li class="flex items-start gap-3 text-slate-300 text-base leading-relaxed"><span class="text-emerald-400 mt-1 flex-shrink-0">▸</span><span><strong>Teoría de la Prospección (Prospect Theory):</strong> Kahneman y Tversky demostraron que los individuos evalúan resultados respecto a un punto de referencia (no riqueza final) y exhiben <strong>aversión a las pérdidas</strong> (la desutilidad de perder $X$ es mayor que la utilidad de ganar $X$). Además, transforman las probabilidades objetivas, sobreponderando eventos de baja probabilidad <span class="hidden" data-ref="20" aria-hidden="true"></span>, <span class="hidden" data-ref="18" aria-hidden="true"></span>.</span></li>
<li class="flex items-start gap-3 text-slate-300 text-base leading-relaxed"><span class="text-emerald-400 mt-1 flex-shrink-0">▸</span><span><strong>Paradoja de Allais:</strong> Experimentos muestran que los agentes violan el axioma de independencia cuando se enfrentan a certezas versus probabilidades altas, prefiriendo desproporcionadamente la seguridad total, lo que contradice la linealidad en las probabilidades de la Utilidad Esperada <span class="hidden" data-ref="21" aria-hidden="true"></span>.</span></li>
</ul>
<!-- section: 4. -->
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-emerald-500/15 border-emerald-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">💻</span>
    <h3 class="text-xl font-bold text-emerald-300 tracking-tight">Información Asimétrica: Selección Adversa y Riesgo Moral</h3>
</div>

<p class="text-slate-400 text-base mb-4">Finalmente, la incertidumbre no es solo exógena (loterías naturales), sino endógena debido a la información privada.</p>
<ul class="my-6 space-y-3">
<li class="flex items-start gap-3 text-slate-300 text-base leading-relaxed"><span class="text-emerald-400 mt-1 flex-shrink-0">▸</span><span><strong>Selección Adversa:</strong> Ocurre <em>antes</em> de la transacción (modelos de "Limones" de Akerlof). En mercados de seguros o crédito, si la aseguradora no puede distinguir tipos de riesgo, ofrecerá un precio promedio. Esto expulsa a los agentes de bajo riesgo y deja solo a los de alto riesgo, pudiendo colapsar el mercado <span class="hidden" data-ref="22" aria-hidden="true"></span>.</span></li>
<li class="flex items-start gap-3 text-slate-300 text-base leading-relaxed"><span class="text-emerald-400 mt-1 flex-shrink-0">▸</span><span><strong>Riesgo Moral:</strong> Ocurre <em>después</em> de la transacción. Si el asegurado está totalmente cubierto y sus acciones no son observables (como la precaución), tendrá incentivos para comportarse de manera más riesgosa, alterando las probabilidades de la "lotería" que enfrenta la aseguradora <span class="hidden" data-ref="23" aria-hidden="true"></span>, <span class="hidden" data-ref="24" aria-hidden="true"></span>.</span></li>
</ul>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Estos fallos de mercado bajo incertidumbre justifican, desde la teoría microeconómica avanzada, mecanismos de diseño de contratos (deducibles, co-pagos) y señalización para restaurar la eficiencia.</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">&copy; 2026 Tech Institute | Master en Microeconomía | Generación O-3</p>

<div class="bg-gradient-to-br from-emerald-950/90 to-slate-900/90 border border-emerald-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-emerald-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-emerald-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>En este nivel de análisis, debemos integrar los conceptos de incertidumbre y tiempo para modelar mercados financieros, seguros y evaluar las limitaciones de los modelos estándar.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-emerald-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Si el agente puede comprar cobertura $x$ pagando una prima por unidad de cobertura $\rho$, su problema de maximización es :.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-emerald-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Resultado Teórico Fundamental: Si el mercado de seguros es perfectamente competitivo y la prima es actuarialmente justa (es decir, el precio del seguro iguala la probabilidad de pérdida, $\rho = \alpha$), un agente averso al riesgo decidirá asegurarse completamente ($x^* = P$).</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-emerald-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Implicación de Arrow-Pratt: Incluso si el individuo es adverso al riesgo, invertirá una cantidad positiva ($\beta > 0$) en el activo riesgoso siempre que el rendimiento esperado del activo sea positivo ($E[\tilde{r}] > 0$).</span></li>
        </ul>
    </div>
</div>
</section>


<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-fuchsia-500 font-mono text-xs">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-xl">Esquema Conceptual Módulo MIC2</h3>
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
    <div class="flex items-center gap-3 mb-10">
        <span class="text-indigo-500 font-mono text-xs">[GL]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter">Glosario de Microeconomía</h2>
    </div>
    <div class="space-y-3">
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-indigo-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Preferencia Revelada</span>
            <p class="text-slate-400 text-sm leading-relaxed">Axioma praxeológico purista empirico destilado y sin asunciones utópicas metafísicas intangibles interiores neuropsicológicas inescrutables de cerebros ciegos dictaminando e infiriendo consistencias lógicas ordinales o rankings de jerarquizaciones inamovibles inescrutables basándose exclusivamente asimétrica rigurosa observablemente empírica o fáctica y contundentemente decodificable y rastreable empíricamente en las liquidaciones tangibles y billeteras de acciones facturadas transadas ejecutadas palpablemente innegables evidentes manifestadas o exhibidas o plasmadas accionales irrefutables materializadas operativas externas reales expuestas exteriorizadas o manifestadas fácticamente palpables.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-indigo-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Curva de Indiferencia</span>
            <p class="text-slate-400 text-sm leading-relaxed">Lugar geométrico o valle de nivel isocuántico isotensional sopesando combinatorias interrelacionadas compensatorias transaccionales de dos fungibles $x,y$ delineando e igualando o atemperando unívocamente empíricamente o conceptualmente idénticos colmados exultantes techos absolutos inestables inasibles idénticos escalafones o mesetas topográficas de goces orgánicos y utilidades y asimilables cumbres de euforia simétricas psicológicas constantes inmutables empáticas o satisfactores homólogos subyacentes de utilitarismos neutras para acaparadores y hedonismos puros estables inmutables del consumidor resolutivo neutral frente a permutaciones mutables compensatorias interinas equilibrantes asimilativas transitorias compensables asintóticas simétricas neutras.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-indigo-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Relación Marginal de Sustitución (RMS)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Inclinación matemática y ratio fraccional o tangente de disposición claudicante compensable del dolor sustitutorio sopesable subjetiva sacrificable dictaminadora de la curva delineando exactamente cuántas e irrisorias o asimétricas fraccionales o enteras unidades fútiles de un satisfactor secundario $y$ condesciende claudicantemente y exige irrenunciable asintóticamente o compensante resignativo abdicar por acaparar marginal interfecto o inyectivo infinitesimal adicional del factor central predilecto unitario primario $x$ sin trastocar o devaluar su umbral empírico topográfico orgánico absoluto y estandar inamovible de idéntica plenitud isotópica incesante neutral inmutable idéntica preestablecida utilitaria o goce inestable basal pre-fijado neutral inafectado inalteable conservando invariable clímax.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-indigo-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Restricción Presupuestaria</span>
            <p class="text-slate-400 text-sm leading-relaxed">Muro inescrutable y arista aritmética de contención o clausura de fronteras infranqueables del vector dictatorial opresor excluyente contable de posibilidades de billetera anclando e inexorable delimitante cercenante y tajante estipulado asimétricamente de adquisiciones tangibles asumiendo e invirtiendo limitadas incondicionales rentas preasignadas deudoras finitas o bolsillos ingresos preestablecidos dados enfrentadas forzosamente en las combinatorias aditivas tasables transaccionales imponderables unitarias fraccionales por el régimen de etiquetados pre-asignados o escalafones del sistema mercado inelásticos exógenamente determinantes coercitivos limitantes dictaminados abisales nominalizados transables coartadores tasadores externos inobjetables objetivos fríos invariables restrictivos infranqueables inamovibles asintóticos.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-indigo-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Óptimo del Consumidor</span>
            <p class="text-slate-400 text-sm leading-relaxed">Intersección clímax euclídeo y cenit utilitarista tangente de coincidencia suprema de vaciamiento equilibrador donde el ratio de sacrificio sopesable individual asimétrico inmutable caprichoso y anhelo biológico (RMS) acopla matemáticamente clona irrestrictamente abraza comulgando y empatando milimétricamente el ratio inflexible de canje dictatorial o tasa marginal objetiva exógena inescrutable exterior transmutatoria de precios impuestos subyugador del mercado $(P_x/P_y)$ maximizando en tope eclosión coronada asintótica plena el límite superior máximo inelástico coronador factible del contorno adquisitivo fraccional delimitado presupuesto basal de frontera disponible estricta fraccional totalizante absoluta suprema alcanzable cumbre resolutiva.</p>
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