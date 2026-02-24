<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-indigo-500 rounded-full"></div>
        <span class="text-indigo-400 font-black text-[10px] uppercase tracking-[0.4em]">Economics Master Series</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
        MIC9
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-indigo-500/15 text-indigo-300 border border-indigo-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Zero-Noise UX</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">v9.0 · Dark Mode</span>
    </div>
</header>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4"><!-- HERO --></p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Información Asimétrica</p>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">💻</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r from-indigo-300 to-violet-400 bg-clip-text text-transparent break-words leading-tight">Fundamentos Microeconómicos de la Información Asimétrica</h2>
        <div class="w-10 md:w-14 h-1 bg-indigo-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La teoría económica neoclásica tradicional, en sus modelos de equilibrio general competitivo, se sustenta sobre el supuesto de la información perfecta y completa. Bajo este paradigma, ejemplificado en los teoremas del bienestar, los precios actúan como estadísticos suficientes que resumen toda la información relevante para la toma de decisiones de consumo y producción <span class="hidden" data-ref="1" aria-hidden="true"></span>, <span class="hidden" data-ref="2" aria-hidden="true"></span>. Sin embargo, la realidad de los mercados dista de este ideal.</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La <strong>Economía de la Información</strong> relaja este supuesto, introduciendo la noción de que los agentes poseen diferentes conjuntos de información. Esta asimetría no es una mera fricción, sino una característica estructural que altera la asignación de recursos, modificando las condiciones de eficiencia y equidad <span class="hidden" data-ref="3" aria-hidden="true"></span>, <span class="hidden" data-ref="4" aria-hidden="true"></span>. En este módulo, formalizaremos cómo la información asimétrica genera fallas de mercado a través de dos mecanismos primordiales: la selección adversa (características ocultas) y el riesgo moral (acciones ocultas).</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-indigo-500/15 border-indigo-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📖</span>
    <h3 class="text-xl font-bold text-indigo-300 tracking-tight">Incertidumbre y Utilidad Esperada (Fundamento Matemático)</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Para modelar la asimetría de información, primero debemos establecer cómo los agentes toman decisiones bajo incertidumbre. Basándonos en la teoría de Von Neumann-Morgenstern, un agente no maximiza la utilidad de un valor esperado, sino la <strong>utilidad esperada</strong> de los resultados <span class="hidden" data-ref="5" aria-hidden="true"></span>.</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Sea $L$ una lotería (o un activo riesgoso) con resultados $w_{1}, \dots, w_{n}$ y probabilidades asociadas $p_{1}, \dots, p_{n}$ tal que $\sum p_{i} = 1$. La utilidad esperada se define como:</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    $$ U(L) = \sum_{i=1}^{n} p_{i}u(w_{i}) $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Donde $u(\cdot)$ es la función de utilidad de Bernoulli. La actitud del agente frente al riesgo es determinante en escenarios de información asimétrica. Un agente es <strong>averso al riesgo</strong> si su función de utilidad es estrictamente cóncava, es decir, $u''(w) < 0$. Esto implica que prefiere el valor esperado de una lotería con certeza antes que jugar la lotería misma <span class="hidden" data-ref="6" aria-hidden="true"></span>, <span class="hidden" data-ref="7" aria-hidden="true"></span>:</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    $$ u(E[L]) > E[u(L)] $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Esta desigualdad de Jensen es la base para la existencia de los mercados de seguros y la prima de riesgo, elementos centrales donde la asimetría informativa tiene efectos devastadores.</p>

<div class="bg-gradient-to-br from-indigo-950/90 to-slate-900/90 border border-indigo-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-indigo-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-indigo-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La teoría económica neoclásica tradicional, en sus modelos de equilibrio general competitivo, se sustenta sobre el supuesto de la información perfecta y completa.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-indigo-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La Economía de la Información relaja este supuesto, introduciendo la noción de que los agentes poseen diferentes conjuntos de información.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-indigo-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Para modelar la asimetría de información, primero debemos establecer cómo los agentes toman decisiones bajo incertidumbre.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-indigo-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Sea $L$ una lotería (o un activo riesgoso) con resultados $w_{1}, \dots, w_{n}$ y probabilidades asociadas $p_{1}, \dots, p_{n}$ tal que $\sum p_{i} = 1$.</span></li>
        </ul>
    </div>
</div>
</section>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📌</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r from-cyan-300 to-blue-400 bg-clip-text text-transparent break-words leading-tight">Selección Adversa: El Problema de las Características Ocultas</h2>
        <div class="w-10 md:w-14 h-1 bg-cyan-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La selección adversa ocurre <em>ex-ante</em> a la transacción. Surge cuando una de las partes (generalmente el vendedor o el agente) posee información privada sobre la calidad o el riesgo inherente del bien o servicio que la contraparte (el comprador o principal) no puede observar <span class="hidden" data-ref="8" aria-hidden="true"></span>.</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-cyan-500/15 border-cyan-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">🔢</span>
    <h3 class="text-xl font-bold text-cyan-300 tracking-tight">El Modelo de los "Limones" (Akerlof)</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">George Akerlof formalizó este fenómeno utilizando el mercado de automóviles usados. Supongamos un mercado donde existen vehículos de buena calidad ("cerezas") y de mala calidad ("limones").</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Sea $q$ la calidad del vehículo, donde $q \sim U[9]$. Los vendedores conocen $q$, pero los compradores solo conocen la distribución de probabilidad de $q$. Si el precio de mercado es $p$, y los vendedores tienen un precio de reserva que depende de la calidad, digamos $r(q) = q$, entonces un vendedor solo ofrecerá su vehículo si:</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    $$ p \geq q $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Esto implica que, para un precio dado $p$, solo se venderán los coches cuya calidad sea inferior o igual a $p$. La calidad promedio de los vehículos ofrecidos en el mercado, $\mu(p)$, será:</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    $$ \mu(p) = E[q | q \leq p] $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Bajo una distribución uniforme, esto resulta en $\mu(p) = \frac{p}{2}$. Si los compradores son racionales y conocen este mecanismo, su disposición a pagar dependerá de la calidad esperada. Si su valoración es igual a la calidad esperada, estarían dispuestos a pagar a lo más $p = \frac{p}{2}$, lo cual solo es posible si $p = 0$.</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4"><strong>Consecuencia en el Equilibrio:</strong> El mercado colapsa. Los bienes de alta calidad son expulsados del mercado porque el precio de equilibrio refleja la calidad promedio, la cual se ve degradada por la presencia de bienes de baja calidad ("limones"). Este proceso de expulsión impide que se realicen intercambios mutuamente beneficiosos, generando una pérdida irrecuperable de eficiencia <span class="hidden" data-ref="10" aria-hidden="true"></span>, <span class="hidden" data-ref="11" aria-hidden="true"></span>.</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-cyan-500/15 border-cyan-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📈</span>
    <h3 class="text-xl font-bold text-cyan-300 tracking-tight">Aplicación al Mercado de Seguros</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">En el mercado de seguros, la selección adversa se manifiesta cuando los individuos con mayor riesgo oculto (por ejemplo, problemas de salud preexistentes no observables) son los más propensos a contratar seguros.</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Sea $w_{0}$ la riqueza inicial y $P$ la pérdida potencial en caso de accidente, con probabilidad $\alpha$. La utilidad esperada sin seguro es:</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    $$ UE_{0} = (1 - \alpha)u(w_{0}) + \alpha u(w_{0} - P) $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Si la aseguradora ofrece una prima promedio basada en la población general, los individuos con bajo riesgo ($\alpha_{bajo}$) encontrarán la prima demasiado cara en relación a su riesgo real y saldrán del mercado. Esto eleva la siniestralidad promedio de la cartera restante, forzando a la aseguradora a subir la prima, lo que a su vez expulsa a los siguientes individuos de menor riesgo. En el límite, el mercado puede desaparecer o solo cubrir a los de riesgo extremo <span class="hidden" data-ref="12" aria-hidden="true"></span>, <span class="hidden" data-ref="13" aria-hidden="true"></span>.</p>

<div class="bg-gradient-to-br from-cyan-950/90 to-slate-900/90 border border-cyan-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-cyan-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-cyan-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La selección adversa ocurre ex-ante a la transacción.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-cyan-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>George Akerlof formalizó este fenómeno utilizando el mercado de automóviles usados.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-cyan-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Sea $q$ la calidad del vehículo, donde $q \sim U[9]$.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-cyan-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Esto implica que, para un precio dado $p$, solo se venderán los coches cuya calidad sea inferior o igual a $p$.</span></li>
        </ul>
    </div>
</div>
</section>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📌</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r from-emerald-300 to-teal-400 bg-clip-text text-transparent break-words leading-tight">Riesgo Moral: El Problema de las Acciones Ocultas</h2>
        <div class="w-10 md:w-14 h-1 bg-emerald-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">El riesgo moral (o azar moral) ocurre <em>ex-post</em> a la contratación. Surge cuando un agente realiza acciones que afectan la utilidad del principal, pero dichas acciones no son perfectamente observables o verificables por el principal <span class="hidden" data-ref="14" aria-hidden="true"></span>.</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-emerald-500/15 border-emerald-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-emerald-300 tracking-tight">El Problema Principal-Agente</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Considere una relación contractual donde el Principal contrata a un Agente. El beneficio del Principal depende del esfuerzo $e$ del Agente, pero el esfuerzo es costoso para el Agente, $C(e)$. El riesgo moral aparece porque el Agente tiene incentivos para reducir su esfuerzo (eludir responsabilidades) una vez que ha firmado un contrato que le asegura una remuneración, especialmente si el monitoreo es imperfecto <span class="hidden" data-ref="15" aria-hidden="true"></span>.</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Formalmente, si el Principal ofrece un salario fijo $w$, el problema del Agente es:</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    $$ \max_{e} u(w) - C(e) $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Como $u(w)$ es constante respecto a $e$ y $C'(e) > 0$, el agente racional minimizará el esfuerzo. Para alinear los incentivos, el contrato debe hacer que la remuneración dependa de los resultados observados, transfiriendo parte del riesgo al agente.</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-emerald-500/15 border-emerald-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-emerald-300 tracking-tight">Riesgo Moral en Seguros</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">En el contexto de seguros, si un individuo está completamente asegurado contra un siniestro (cobertura total), su incentivo para ejercer "cuidado" o prevención disminuye. Si $x$ es la cobertura del seguro y $\rho$ es la prima, la riqueza en el estado "malo" (siniestro) es $w_{0} - P + x - \rho x$. Si $x = P$ (seguro completo), la riqueza del individuo es constante independientemente de si ocurre el accidente o no.</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    $$ \frac{\partial UE}{\partial \text{esfuerzo}} \to 0 $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">El asegurado no internaliza el costo marginal de la prevención, aumentando la probabilidad $\alpha$ de que ocurra el siniestro. Esto rompe la condición de eficiencia donde el costo marginal de prevención debería igualar al beneficio marginal social de la reducción del riesgo <span class="hidden" data-ref="16" aria-hidden="true"></span>, <span class="hidden" data-ref="17" aria-hidden="true"></span>.</p>

<div class="bg-gradient-to-br from-emerald-950/90 to-slate-900/90 border border-emerald-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-emerald-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-emerald-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>El riesgo moral (o azar moral) ocurre ex-post a la contratación.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-emerald-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Considere una relación contractual donde el Principal contrata a un Agente.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-emerald-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Formalmente, si el Principal ofrece un salario fijo $w$, el problema del Agente es:.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-emerald-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Como $u(w)$ es constante respecto a $e$ y $C'(e) > 0$, el agente racional minimizará el esfuerzo.</span></li>
        </ul>
    </div>
</div>
</section>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📌</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r from-amber-300 to-orange-400 bg-clip-text text-transparent break-words leading-tight">Mecanismos de Solución: Señalización y Cribado</h2>
        <div class="w-10 md:w-14 h-1 bg-amber-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">El mercado desarrolla mecanismos endógenos para mitigar las ineficiencias causadas por la asimetría informativa. Estos se clasifican según quién inicia la acción para revelar la información privada.</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-amber-500/15 border-amber-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-amber-300 tracking-tight">Señalización (Signalling)</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La <strong>señalización</strong> ocurre cuando la parte informada (agente) emprende una acción costosa para revelar sus características privadas a la parte no informada (principal) <span class="hidden" data-ref="18" aria-hidden="true"></span>.</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">El modelo clásico es el de <strong>Spence sobre el mercado laboral</strong>. Los trabajadores de alta productividad desean diferenciarse de los de baja productividad. La educación actúa como señal. Para que la señal sea efectiva y genere un <strong>equilibrio separador</strong>, debe cumplir con la <em>Condición de Cruce Único</em>: el costo de emitir la señal (adquirir educación) debe ser menor para los agentes de alta productividad que para los de baja productividad.</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Sea $c(y, \theta)$ el costo de adquirir $y$ nivel de educación para un tipo $\theta$ (donde $\theta_{H} > \theta_{L}$ representa la productividad). La señalización funciona si:</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    $$ \frac{\partial c(y, \theta_{L})}{\partial y} > \frac{\partial c(y, \theta_{H})}{\partial y} $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Si esta condición se cumple, las empresas pueden ofrecer salarios altos condicionados a un nivel de educación que sea rentable obtener solo para los trabajadores de tipo $\theta_{H}$, resolviendo parcialmente la selección adversa <span class="hidden" data-ref="19" aria-hidden="true"></span>, <span class="hidden" data-ref="20" aria-hidden="true"></span>.</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-amber-500/15 border-amber-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-amber-300 tracking-tight">Cribado (Screening)</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">El <strong>cribado</strong> ocurre cuando la parte <strong>no informada</strong> (principal) diseña un menú de contratos u opciones para inducir a la parte informada a revelar su tipo mediante la autoselección <span class="hidden" data-ref="21" aria-hidden="true"></span>.</p>
<p class="text-slate-400 text-base mb-6">En el mercado de seguros, las compañías ofrecen diferentes pólizas para separar a los clientes por su nivel de riesgo:</p>

<div class="flex items-start gap-5 p-5 bg-amber-500/10 rounded-2xl my-3 border bg-amber-500/20 hover:bg-amber-500/15 transition-all">
    <!-- step:1 -->
    <div class="bg-amber-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Póliza A:</strong> Prima alta, deducible bajo (cobertura total).</div>
</div>

<div class="flex items-start gap-5 p-5 bg-amber-500/10 rounded-2xl my-3 border bg-amber-500/20 hover:bg-amber-500/15 transition-all">
    <!-- step:2 -->
    <div class="bg-amber-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Póliza B:</strong> Prima baja, deducible alto.</div>
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Los agentes de alto riesgo (que saben que tienen alta probabilidad de accidente) preferirán la Póliza A, mientras que los de bajo riesgo, para ahorrar en la prima, aceptarán el riesgo del deducible alto de la Póliza B.</p>
<p class="text-slate-400 text-base mb-6">Matemáticamente, el diseño del contrato debe satisfacer dos restricciones:</p>

<div class="flex items-start gap-5 p-5 bg-amber-500/10 rounded-2xl my-3 border bg-amber-500/20 hover:bg-amber-500/15 transition-all">
    <!-- step:1 -->
    <div class="bg-amber-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Restricción de Participación (RP):</strong> El agente debe querer firmar el contrato (utilidad $\geq$ utilidad de reserva).</div>
</div>

<div class="flex items-start gap-5 p-5 bg-amber-500/10 rounded-2xl my-3 border bg-amber-500/20 hover:bg-amber-500/15 transition-all">
    <!-- step:2 -->
    <div class="bg-amber-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Restricción de Compatibilidad de Incentivos (RCI):</strong> El agente de tipo $\theta_{i}$ debe preferir el contrato diseñado para él sobre el contrato diseñado para el tipo $\theta_{j}$.</div>
</div>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    $$ U(\text{Contrato}_{i} | \theta_{i}) \geq U(\text{Contrato}_{j} | \theta_{i}) $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">El uso de deducibles es, por tanto, una herramienta de cribado para que los conductores revelen su información privada sobre su nivel de precaución o riesgo <span class="hidden" data-ref="22" aria-hidden="true"></span>.</p>

<div class="bg-gradient-to-br from-amber-950/90 to-slate-900/90 border border-amber-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-amber-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-amber-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>El mercado desarrolla mecanismos endógenos para mitigar las ineficiencias causadas por la asimetría informativa.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-amber-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La señalización ocurre cuando la parte informada (agente) emprende una acción costosa para revelar sus características privadas a la parte no informada (principal).</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-amber-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>El modelo clásico es el de Spence sobre el mercado laboral.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-amber-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Sea $c(y, \theta)$ el costo de adquirir $y$ nivel de educación para un tipo $\theta$ (donde $\theta_{H} > \theta_{L}$ representa la productividad).</span></li>
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

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La teoría de la información asimétrica no se limita a mercados estáticos; sus ramificaciones explican fenómenos complejos en finanzas corporativas, política y diseño de mecanismos.</p>
<!-- section: 1. -->
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-rose-500/15 border-rose-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">💰</span>
    <h3 class="text-xl font-bold text-rose-300 tracking-tight">Racionamiento de Crédito y Crisis Financieras</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">En los mercados financieros, el precio (tasa de interés) no siempre vacía el mercado. Según Stiglitz y Weiss, aumentar la tasa de interés puede reducir la rentabilidad esperada del banco debido a dos efectos: <em> <strong>Selección Adversa:</strong> Tasas altas atraen solo a prestatarios con proyectos muy riesgosos (los prudentes se retiran). </em> <strong>Riesgo Moral:</strong> Una vez aceptado el préstamo a una tasa alta, el prestatario elige proyectos más riesgosos para cubrir los costos de la deuda. Por ello, los bancos prefieren <strong>racionar el crédito</strong> (limitar la oferta $Q$ incluso si hay demanda a la tasa vigente) en lugar de subir la tasa de interés para equilibrar el mercado <span class="hidden" data-ref="23" aria-hidden="true"></span>, <span class="hidden" data-ref="24" aria-hidden="true"></span>.</p>
<!-- section: 2. -->
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-rose-500/15 border-rose-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-rose-300 tracking-tight">Diseño de Subastas y la Maldición del Ganador</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">En teoría de juegos con información incompleta, las subastas son mecanismos de asignación bajo asimetría. En una subasta de <strong>valor común</strong> (donde el bien tiene el mismo valor para todos, pero este valor es desconocido, ej. un pozo petrolero), los postores estiman el valor basándose en señales privadas. El ganador de la subasta suele ser quien ha sobreestimado el valor del bien (la señal más optimista). Si no ajusta su oferta hacia abajo ("shading") considerando que ganar implica que los demás tenían señales más bajas, sufrirá la <strong>maldición del ganador</strong>: pagar más de lo que vale el bien. El equilibrio Bayesiano de Nash en subastas exige que los agentes racionales incorporen esta información condicional en sus estrategias de puja <span class="hidden" data-ref="25" aria-hidden="true"></span>, <span class="hidden" data-ref="26" aria-hidden="true"></span>.</p>
<!-- section: 3. -->
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-rose-500/15 border-rose-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📣</span>
    <h3 class="text-xl font-bold text-rose-300 tracking-tight">Regulación Bancaria y Productos Complejos</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La crisis financiera de 2008 y casos como el de las participaciones preferentes en España ilustran la asimetría informativa extrema entre bancos y consumidores minoristas. Los productos financieros complejos (derivados, estructurados) presentan características de riesgo que el consumidor promedio no puede evaluar (costo de información infinito). Desde la perspectiva del análisis económico del derecho, la mera "transparencia formal" (entregar el contrato) es insuficiente. Se requiere una intervención paternalista o regulación de conducta (MIFID en Europa) que obligue a evaluar la idoneidad del producto para el perfil de riesgo del cliente, transformando el deber de información en un deber de asesoramiento efectivo para mitigar la selección adversa sistémica y el riesgo moral de las entidades financieras <span class="hidden" data-ref="27" aria-hidden="true"></span>, <span class="hidden" data-ref="28" aria-hidden="true"></span>, <span class="hidden" data-ref="29" aria-hidden="true"></span>.</p>
<!-- section: 4. -->
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-rose-500/15 border-rose-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">🌱</span>
    <h3 class="text-xl font-bold text-rose-300 tracking-tight">Teoremas de Imposibilidad y Elección Social</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La información asimétrica también afecta la economía política. El Teorema de la Imposibilidad de Arrow sugiere que no existe un sistema de votación perfecto que agregue preferencias individuales en una decisión social consistente. La asimetría de información entre votantes y políticos (agentes) sobre las verdaderas intenciones o capacidades de estos últimos exacerba los problemas de agencia en la democracia, llevando a resultados donde el "votante mediano" determina el equilibrio, el cual no necesariamente es socialmente óptimo <span class="hidden" data-ref="30" aria-hidden="true"></span>, <span class="hidden" data-ref="31" aria-hidden="true"></span>.</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">&copy; 2026 Tech Institute | Master en Microeconomía | Generación O-3</p>

<div class="bg-gradient-to-br from-rose-950/90 to-slate-900/90 border border-rose-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-rose-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-rose-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La teoría de la información asimétrica no se limita a mercados estáticos; sus ramificaciones explican fenómenos complejos en finanzas corporativas, política y diseño de mecanismos.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-rose-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>En los mercados financieros, el precio (tasa de interés) no siempre vacía el mercado.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-rose-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>En teoría de juegos con información incompleta, las subastas son mecanismos de asignación bajo asimetría.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-rose-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La crisis financiera de 2008 y casos como el de las participaciones preferentes en España ilustran la asimetría informativa extrema entre bancos y consumidores minoristas.</span></li>
        </ul>
    </div>
</div>
</section>


<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">
        <span class="text-fuchsia-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo MIC9</h3>
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


<section id="glosario" class="py-16 bg-white dark:bg-gray-950 transition-colors duration-300">
    <div class="container mx-auto px-6">
        <div class="flex items-center gap-4 mb-12">
            <div class="w-2 h-10 bg-indigo-500 rounded-full"></div>
            <h2 class="text-4xl font-bold text-gray-900 dark:text-white">Glosario Académico</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-indigo-500/50 hover:shadow-2xl hover:shadow-indigo-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-indigo-500 transition-colors">
                    Información Asimétrica
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Situación en la que las partes de una transacción poseen distintos niveles de información relevante, alterando la asignación eficiente de recursos y las condiciones de equilibrio del mercado.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-indigo-500/50 hover:shadow-2xl hover:shadow-indigo-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-indigo-500 transition-colors">
                    Selección Adversa
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Falla de mercado precontractual que surge cuando una parte posee información privada sobre características ocultas, provocando la expulsión de bienes de alta calidad por el precio promedio.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-indigo-500/50 hover:shadow-2xl hover:shadow-indigo-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-indigo-500 transition-colors">
                    Riesgo Moral
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Fenómeno postcontractual donde un agente realiza acciones inobservables que afectan la utilidad del principal, incentivado por la falta de monitoreo perfecto y la transferencia de riesgos.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-indigo-500/50 hover:shadow-2xl hover:shadow-indigo-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-indigo-500 transition-colors">
                    Utilidad Esperada
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Valoración ponderada de los resultados posibles de una lotería por sus probabilidades, criterio central en la toma de decisiones bajo condiciones de incertidumbre y riesgo.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-indigo-500/50 hover:shadow-2xl hover:shadow-indigo-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-indigo-500 transition-colors">
                    Aversión al Riesgo
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Preferencia de un agente por un resultado cierto frente a una lotería con igual valor esperado, representada matemáticamente por una función de utilidad de Bernoulli estrictamente cóncava.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-indigo-500/50 hover:shadow-2xl hover:shadow-indigo-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-indigo-500 transition-colors">
                    Señalización
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Mecanismo mediante el cual la parte informada incurre en acciones costosas y observables para revelar de manera creíble sus características privadas a la parte no informada.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-indigo-500/50 hover:shadow-2xl hover:shadow-indigo-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-indigo-500 transition-colors">
                    Cribado (Screening)
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Estrategia de la parte no informada consistente en diseñar un menú de contratos que induce a los agentes a revelar su información privada mediante la autoselección.
                </p>
            </div>

            <div class="group p-8 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-indigo-500/50 hover:shadow-2xl hover:shadow-indigo-500/10 transition-all duration-500">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4 group-hover:text-indigo-500 transition-colors">
                    Relación Principal-Agente
                </h3>
                <p class="text-gray-600 dark:text-gray-400 leading-relaxed">
                    Vínculo contractual donde el bienestar de una parte depende del esfuerzo no observable de otra, generando incentivos para el incumplimiento o la reducción del esfuerzo.
                </p>
            </div>
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