<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-indigo-500 rounded-full"></div>
        <span class="text-indigo-400 font-black text-[10px] uppercase tracking-[0.4em]">Economics Master Series</span>
    </div>
    <h1 class="text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8">
        MIC1
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-indigo-500/15 text-indigo-300 border border-indigo-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Zero-Noise UX</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">v9.0 · Dark Mode</span>
    </div>
</header>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4"><!-- HERO --></p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4"></p>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📖</span>
    <div>
        <h2 class="text-xl md:text-3xl font-black tracking-tight bg-gradient-to-r from-indigo-300 to-violet-400 bg-clip-text text-transparent">Fundamentos Axiomáticos de las Preferencias y Conjuntos de Consumo</h2>
        <div class="w-10 md:w-14 h-1 bg-indigo-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">En la teoría microeconómica avanzada, el análisis del comportamiento del consumidor comienza con la definición formal del <strong>conjunto de consumo</strong> y las <strong>relaciones de preferencia</strong>. Un consumidor es descrito parcialmente por su conjunto de consumo, denotado usualmente como $X_i \subset \mathbb{R}^L$, el cual representa el espacio de todas las canastas de bienes física y legalmente posibles que el agente puede consumir <span class="hidden" data-ref="1" aria-hidden="true"></span>.</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Para modelar la elección racional, establecemos una relación binaria de preferencia, denotada por $\succeq$, sobre el conjunto $X$. La expresión $x \succeq y$ indica que la cesta $x$ es "al menos tan preferida como" la cesta $y$ <span class="hidden" data-ref="2" aria-hidden="true"></span>. Para garantizar la existencia de una función de utilidad y la racionalidad de las decisiones, imponemos los siguientes axiomas fundamentales:</p>

<div class="flex items-start gap-5 p-5 bg-indigo-500/10 rounded-2xl my-3 border bg-indigo-500/20 hover:bg-indigo-500/15 transition-all">
    <!-- step:1 -->
    <div class="bg-indigo-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Completitud:</strong> Para todo par de cestas $x, y \in X$, se cumple que $x \succeq y$, o $y \succeq x$, o ambos. Esto implica que el consumidor es capaz de comparar y ordenar todas las canastas posibles, eliminando la indecisión <span class="hidden" data-ref="3" aria-hidden="true"></span>, <span class="hidden" data-ref="4" aria-hidden="true"></span>.</div>
</div>

<div class="flex items-start gap-5 p-5 bg-indigo-500/10 rounded-2xl my-3 border bg-indigo-500/20 hover:bg-indigo-500/15 transition-all">
    <!-- step:2 -->
    <div class="bg-indigo-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Transitividad:</strong> Para cualquier terna de cestas $x, y, z \in X$, si $x \succeq y$ y $y \succeq z$, entonces $x \succeq z$. Este axioma impone coherencia en las elecciones y elimina la posibilidad de ciclos de preferencias, permitiendo un preorden completo <span class="hidden" data-ref="3" aria-hidden="true"></span>, <span class="hidden" data-ref="4" aria-hidden="true"></span>.</div>
</div>

<div class="flex items-start gap-5 p-5 bg-indigo-500/10 rounded-2xl my-3 border bg-indigo-500/20 hover:bg-indigo-500/15 transition-all">
    <!-- step:3 -->
    <div class="bg-indigo-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">3</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Continuidad:</strong> Para todo $x \in X$, los conjuntos de contorno superior $\{y \in X | y \succeq x\}$ e inferior $\{y \in X | x \succeq y\}$ son cerrados. Matemáticamente, esto asegura que no existan "saltos" en las preferencias; si una secuencia de cestas preferidas a $x$ converge a $y$, entonces $y$ también debe ser preferida a $x$. Este supuesto es crucial para demostrar la existencia de una función de utilidad continua <span class="hidden" data-ref="5" aria-hidden="true"></span>, <span class="hidden" data-ref="6" aria-hidden="true"></span>.</div>
</div>

<div class="flex items-start gap-5 p-5 bg-indigo-500/10 rounded-2xl my-3 border bg-indigo-500/20 hover:bg-indigo-500/15 transition-all">
    <!-- step:4 -->
    <div class="bg-indigo-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">4</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Monotonía (No Saciabilidad):</strong> Se asume comúnmente que "más es mejor". En su versión estricta, si la cesta $x$ contiene más de cada bien que la cesta $y$, entonces $x \succ y$. La no saciabilidad local, una versión más débil, establece que en cualquier entorno de una cesta $x$, existe otra cesta que es estrictamente preferida <span class="hidden" data-ref="7" aria-hidden="true"></span>, <span class="hidden" data-ref="8" aria-hidden="true"></span>.</div>
</div>

<div class="flex items-start gap-5 p-5 bg-indigo-500/10 rounded-2xl my-3 border bg-indigo-500/20 hover:bg-indigo-500/15 transition-all">
    <!-- step:5 -->
    <div class="bg-indigo-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">5</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Convexidad:</strong> Si $x \succeq z$ y $y \succeq z$, entonces para cualquier $\alpha \in [9]$, la combinación lineal $\alpha x + (1-\alpha)y \succeq z$. Económicamente, esto implica que los consumidores prefieren cestas balanceadas o "medias" a los extremos. Si la convexidad es estricta, las curvas de indiferencia no contienen segmentos lineales, garantizando la unicidad del óptimo en la maximización de la utilidad <span class="hidden" data-ref="10" aria-hidden="true"></span>, <span class="hidden" data-ref="11" aria-hidden="true"></span>.</div>
</div>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-indigo-500/15 border-indigo-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-indigo-300 tracking-tight">La Función de Utilidad y el Mapa de Indiferencia</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La utilidad es un concepto ordinal que permite asignar un número real a cada cesta de consumo tal que se respete el orden de preferencias establecido por $\succeq$.</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    <strong>Teorema de Existencia:</strong> Si las preferencias son completas, transitivas, continuas y monótonas sobre un conjunto conexo $X \subset \mathbb{R}^L$, existe una función de utilidad continua $U: X \to \mathbb{R}$ tal que: $$ U(x) \geq U(y) \iff x \succeq y $$ Esta función no es única; cualquier transformación monótona positiva de $U$ representa las mismas preferencias, confirmando el carácter ordinal y no cardinal de la utilidad en la teoría moderna <span class="hidden" data-ref="12" aria-hidden="true"></span>, <span class="hidden" data-ref="13" aria-hidden="true"></span>.
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Las <strong>curvas de indiferencia</strong> son el lugar geométrico de los puntos que representan cestas de consumo que otorgan el mismo nivel de utilidad ($U(x) = \bar{u}$). Basado en los axiomas, estas curvas tienen pendiente negativa, no se cruzan entre sí, son densas en el espacio de bienes y, bajo el supuesto de convexidad de preferencias, son convexas hacia el origen <span class="hidden" data-ref="14" aria-hidden="true"></span>, <span class="hidden" data-ref="15" aria-hidden="true"></span>, <span class="hidden" data-ref="10" aria-hidden="true"></span>.</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    La pendiente de la curva de indiferencia se denomina <strong>Tasa Marginal de Sustitución (TMS)</strong>. Matemáticamente se define como la relación de las utilidades marginales: $$ TMS_{1,2} = - \frac{dx_2}{dx_1} = \frac{\partial U / \partial x_1}{\partial U / \partial x_2} $$ La TMS mide la cantidad del bien 2 a la que el individuo está dispuesto a renunciar para obtener una unidad adicional del bien 1, manteniendo constante su nivel de utilidad. Se asume que la TMS es decreciente a lo largo de la curva de indiferencia <span class="hidden" data-ref="14" aria-hidden="true"></span>.
</div>

<div class="bg-gradient-to-br from-indigo-950/90 to-slate-900/90 border border-indigo-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-indigo-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-indigo-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>En la teoría microeconómica avanzada, el análisis del comportamiento del consumidor comienza con la definición formal del conjunto de consumo y las relaciones de preferencia.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-indigo-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Para modelar la elección racional, establecemos una relación binaria de preferencia, denotada por $\succeq$, sobre el conjunto $X$.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-indigo-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La utilidad es un concepto ordinal que permite asignar un número real a cada cesta de consumo tal que se respete el orden de preferencias establecido por $\succeq$.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-indigo-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Las curvas de indiferencia son el lugar geométrico de los puntos que representan cestas de consumo que otorgan el mismo nivel de utilidad ($U(x) = \bar{u}$).</span></li>
        </ul>
    </div>
</div>
</section>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📌</span>
    <div>
        <h2 class="text-xl md:text-3xl font-black tracking-tight bg-gradient-to-r from-cyan-300 to-blue-400 bg-clip-text text-transparent">La Restricción Presupuestaria y el Problema Primal</h2>
        <div class="w-10 md:w-14 h-1 bg-cyan-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>


<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    Los consumidores enfrentan limitaciones de recursos. La <strong>restricción presupuestaria</strong> define el conjunto de cestas factibles dado un vector de precios $p \gg 0$ y una riqueza o ingreso $m$. El conjunto presupuestario $B(p, m)$ se define como: $$ B(p,m) = \{x \in X | p \cdot x \le m \} $$ Donde $p \cdot x = \sum_{i=1}^n p_i x_i$ es el gasto total <span class="hidden" data-ref="16" aria-hidden="true"></span>, <span class="hidden" data-ref="17" aria-hidden="true"></span>. Geométricamente, en un espacio de dos bienes, la frontera de este conjunto es una recta con pendiente $-p_1/p_2$, que representa el precio relativo o costo de oportunidad de mercado entre los bienes <span class="hidden" data-ref="18" aria-hidden="true"></span>.
</div>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-cyan-500/15 border-cyan-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-cyan-300 tracking-tight">Maximización de la Utilidad (Problema Primal)</h3>
</div>


<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    El problema fundamental del consumidor es elegir la cesta $x$ que maximice su utilidad sujeto a su restricción presupuestaria: $$ \max_{x} U(x) $$ $$ \text{sujeto a } p \cdot x \le m $$
</div>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    Para resolver este problema, formamos el <strong>Lagrangiano</strong>: $$ \mathcal{L} = U(x_1.., x_n) + \lambda (m - \sum_{i=1}^n p_i x_i) $$ Las condiciones de primer orden (CPO) para una solución interior requieren: $$ \frac{\partial \mathcal{L}}{\partial x_i} = \frac{\partial U}{\partial x_i} - \lambda p_i = 0 \quad \forall i $$ $$ \frac{\partial \mathcal{L}}{\partial \lambda} = m - \sum_{i=1}^n p_i x_i = 0 $$
</div>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    De estas condiciones derivamos el <strong>principio equimarginal</strong>: $$ \frac{\frac{\partial U}{\partial x_i}}{p_i} = \frac{\frac{\partial U}{\partial x_j}}{p_j} = \lambda \quad \implies \quad \text{TMS}_{i,j} = \frac{p_i}{p_j} $$ En el óptimo, la tasa subjetiva de intercambio (TMS) debe igualarse a la tasa objetiva de mercado (relación de precios). El multiplicador de Lagrange, $\lambda$, se interpreta como la <strong>utilidad marginal del ingreso</strong>: cuánto aumenta la utilidad maximizada si se relaja la restricción presupuestaria en una unidad monetaria <span class="hidden" data-ref="19" aria-hidden="true"></span>, <span class="hidden" data-ref="20" aria-hidden="true"></span>.
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La solución a este problema primal genera las <strong>Funciones de Demanda Marshallianas</strong> (u ordinarias), denotadas como $x(p, m)$. Estas funciones indican la cantidad óptima demandada de cada bien dados los precios y el ingreso <span class="hidden" data-ref="21" aria-hidden="true"></span>.</p>

<div class="bg-gradient-to-br from-cyan-950/90 to-slate-900/90 border border-cyan-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-cyan-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-cyan-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La solución a este problema primal genera las Funciones de Demanda Marshallianas (u ordinarias), denotadas como $x(p, m)$.</span></li>
        </ul>
    </div>
</div>
</section>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📈</span>
    <div>
        <h2 class="text-xl md:text-3xl font-black tracking-tight bg-gradient-to-r from-emerald-300 to-teal-400 bg-clip-text text-transparent">Dualidad: Minimización del Gasto y Demandas Hicksianas</h2>
        <div class="w-10 md:w-14 h-1 bg-emerald-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La teoría del consumidor posee una estructura dual. Alternativamente a maximizar la utilidad dado un ingreso, el consumidor puede buscar minimizar el gasto necesario para alcanzar un nivel de utilidad objetivo $\bar{u}$.</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-emerald-500/15 border-emerald-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-emerald-300 tracking-tight">El Problema Dual</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">$$ \min_{x} p \cdot x $$ $$ \text{sujeto a } U(x) \ge \bar{u} $$</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La solución a este problema genera las <strong>Funciones de Demanda Hicksianas</strong> (o compensadas), denotadas como $h(p, u)$. Estas funciones representan la canasta más barata para lograr una utilidad $u$ a los precios $p$ <span class="hidden" data-ref="22" aria-hidden="true"></span>, <span class="hidden" data-ref="23" aria-hidden="true"></span>.</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-emerald-500/15 border-emerald-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-emerald-300 tracking-tight">Funciones de Valor y Relaciones de Dualidad</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">De los problemas primal y dual surgen dos funciones de valor fundamentales:</p>
<p class="text-slate-400 text-base mb-6">Homogénea de grado 0 en $(p, m)$. No creciente en $p$ y no decreciente en $m$. Cuasiconvexa en $p$.</p>

<div class="flex items-start gap-5 p-5 bg-emerald-500/10 rounded-2xl my-3 border bg-emerald-500/20 hover:bg-emerald-500/15 transition-all">
    <!-- step:1 -->
    <div class="bg-emerald-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Función de Utilidad Indirecta ($V(p, m)$):</strong> Se obtiene sustituyendo las demandas Marshallianas en la función de utilidad original. $V(p,m) = U(x(p,m))$. Representa la máxima utilidad alcanzable dados $p$ y $m$ <span class="hidden" data-ref="24" aria-hidden="true"></span>. Propiedades clave:</div>
</div>
<p class="text-slate-400 text-base mb-6">Homogénea de grado 1 en $p$. Cóncava en $p$. No decreciente en $p$.</p>

<div class="flex items-start gap-5 p-5 bg-emerald-500/10 rounded-2xl my-3 border bg-emerald-500/20 hover:bg-emerald-500/15 transition-all">
    <!-- step:2 -->
    <div class="bg-emerald-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Función de Gasto ($e(p, u)$):</strong> Se obtiene sustituyendo las demandas Hicksianas en la función objetivo del dual. $e(p,u) = p \cdot h(p,u)$. Representa el mínimo gasto necesario para alcanzar $u$ <span class="hidden" data-ref="22" aria-hidden="true"></span>. Propiedades clave:</div>
</div>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-emerald-500/15 border-emerald-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-emerald-300 tracking-tight">Identidades Clave</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Las herramientas matemáticas que conectan estas funciones son esenciales para el análisis empírico y teórico:</p>
<p class="text-slate-400 text-base mb-4">$$ x_i(p,m) = - \frac{\partial V(p,m) / \partial p_i}{\partial V(p,m) / \partial m} $$</p>
<ul class="my-6 space-y-3">
<li class="flex items-start gap-3 text-slate-300 text-base leading-relaxed"><span class="text-emerald-400 mt-1 flex-shrink-0">▸</span><span><strong>Identidad de Roy:</strong> Permite recuperar la demanda Marshalliana a partir de la utilidad indirecta <span class="hidden" data-ref="25" aria-hidden="true"></span>:</span></li>
</ul>
<p class="text-slate-400 text-base mb-4">$$ h_i(p,u) = \frac{\partial e(p,u)}{\partial p_i} $$</p>
<ul class="my-6 space-y-3">
<li class="flex items-start gap-3 text-slate-300 text-base leading-relaxed"><span class="text-emerald-400 mt-1 flex-shrink-0">▸</span><span><strong>Lema de Shephard:</strong> Permite obtener la demanda Hicksiana derivando la función de gasto respecto al precio <span class="hidden" data-ref="25" aria-hidden="true"></span>:</span></li>
</ul>

<div class="bg-gradient-to-br from-emerald-950/90 to-slate-900/90 border border-emerald-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-emerald-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-emerald-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La teoría del consumidor posee una estructura dual.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-emerald-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>$$ \min_{x} p \cdot x $$ $$ \text{sujeto a } U(x) \ge \bar{u} $$.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-emerald-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La solución a este problema genera las Funciones de Demanda Hicksianas (o compensadas), denotadas como $h(p, u)$.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-emerald-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>De los problemas primal y dual surgen dos funciones de valor fundamentales:.</span></li>
        </ul>
    </div>
</div>
</section>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📈</span>
    <div>
        <h2 class="text-xl md:text-3xl font-black tracking-tight bg-gradient-to-r from-amber-300 to-orange-400 bg-clip-text text-transparent">La Ecuación de Slutsky y Variaciones en la Demanda</h2>
        <div class="w-10 md:w-14 h-1 bg-amber-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">El análisis de cómo cambia la demanda ante variaciones en los precios se sintetiza en la Ecuación de Slutsky, la cual descompone el efecto total de un cambio en el precio en dos componentes: el <strong>Efecto Sustitución (ES)</strong> y el <strong>Efecto Ingreso (EI)</strong> <span class="hidden" data-ref="26" aria-hidden="true"></span>, <span class="hidden" data-ref="27" aria-hidden="true"></span>, <span class="hidden" data-ref="28" aria-hidden="true"></span>.</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Partiendo de la identidad $h_i(p, u) = x_i(p, e(p,u))$, y derivando respecto a $p_j$, obtenemos:</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    $$ \frac{\partial x_i}{\partial p_j} = \underbrace{\frac{\partial h_i}{\partial p_j}}_{\text{Efecto Sustitución}} - \underbrace{x_j \frac{\partial x_i}{\partial m}}_{\text{Efecto Ingreso}} $$
</div>

<div class="flex items-start gap-5 p-5 bg-amber-500/10 rounded-2xl my-3 border bg-amber-500/20 hover:bg-amber-500/15 transition-all">
    <!-- step:1 -->
    <div class="bg-amber-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Efecto Sustitución ($\frac{\partial h_i}{\partial p_j}$):</strong> Mide el cambio en la cantidad demandada debido al cambio en los precios relativos, manteniendo la utilidad constante. Debido a la concavidad de la función de gasto, el efecto sustitución propio ($\frac{\partial h_i}{\partial p_i}$) es siempre negativo (o cero) <span class="hidden" data-ref="26" aria-hidden="true"></span>, <span class="hidden" data-ref="29" aria-hidden="true"></span>.</div>
</div>

<div class="flex items-start gap-5 p-5 bg-amber-500/10 rounded-2xl my-3 border bg-amber-500/20 hover:bg-amber-500/15 transition-all">
    <!-- step:2 -->
    <div class="bg-amber-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Efecto Ingreso ($- x_j \frac{\partial x_i}{\partial m}$):</strong> Mide el cambio en la demanda debido a la alteración del poder adquisitivo real del consumidor. Su signo depende de si el bien es <strong>normal</strong> ($\frac{\partial x_i}{\partial m} > 0$) o <strong>inferior</strong> ($\frac{\partial x_i}{\partial m} < 0$) <span class="hidden" data-ref="30" aria-hidden="true"></span>, <span class="hidden" data-ref="31" aria-hidden="true"></span>.</div>
</div>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-amber-500/15 border-amber-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📈</span>
    <h3 class="text-xl font-bold text-amber-300 tracking-tight">Clasificación de Bienes y Curvas de Demanda</h3>
</div>

<ul class="my-6 space-y-3">
<li class="flex items-start gap-3 text-slate-300 text-base leading-relaxed"><span class="text-amber-400 mt-1 flex-shrink-0">▸</span><span><strong>Bienes Normales:</strong> El EI refuerza al ES. Ante una caída en el precio, ambos efectos inducen un mayor consumo. La curva de demanda es decreciente.</span></li>
<li class="flex items-start gap-3 text-slate-300 text-base leading-relaxed"><span class="text-amber-400 mt-1 flex-shrink-0">▸</span><span><strong>Bienes Inferiores:</strong> El EI actúa en dirección opuesta al ES. Si el precio baja, el consumidor es "más rico", pero al ser un bien inferior, quiere consumir menos. Generalmente, el ES domina y la curva de demanda sigue siendo negativa <span class="hidden" data-ref="32" aria-hidden="true"></span>, <span class="hidden" data-ref="31" aria-hidden="true"></span>.</span></li>
<li class="flex items-start gap-3 text-slate-300 text-base leading-relaxed"><span class="text-amber-400 mt-1 flex-shrink-0">▸</span><span><strong>Bienes Giffen:</strong> Un caso teórico extremo de bien inferior donde el EI es tan fuerte que supera al ES. Ante una subida de precio, la cantidad demandada aumenta. Esto viola la Ley de la Demanda y genera una curva de demanda con pendiente positiva <span class="hidden" data-ref="32" aria-hidden="true"></span>, <span class="hidden" data-ref="33" aria-hidden="true"></span>.</span></li>
</ul>

<div class="bg-gradient-to-br from-amber-950/90 to-slate-900/90 border border-amber-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-amber-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-amber-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>El análisis de cómo cambia la demanda ante variaciones en los precios se sintetiza en la Ecuación de Slutsky, la cual descompone el efecto total de un cambio en el precio en dos componentes: el Efecto Sustitución (ES) y el Efecto Ingreso (EI) , ,.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-amber-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Partiendo de la identidad $h_i(p, u) = x_i(p, e(p,u))$, y derivando respecto a $p_j$, obtenemos:.</span></li>
        </ul>
    </div>
</div>
</section>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">🌱</span>
    <div>
        <h2 class="text-xl md:text-3xl font-black tracking-tight bg-gradient-to-r from-rose-300 to-pink-400 bg-clip-text text-transparent">Variaciones en el Bienestar: VC y VE</h2>
        <div class="w-10 md:w-14 h-1 bg-rose-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Dado que la utilidad no es directamente observable, utilizamos la dualidad para medir cambios en el bienestar ante variaciones de precios (de $p^0$ a $p^1$).</p>
<p class="text-slate-400 text-base mb-4">$$ VC = e(p^1, u^0) - e(p^0, u^0) $$ $$ VE = e(p^1, u^1) - e(p^0, u^1) $$</p>
<ul class="my-6 space-y-3">
<li class="flex items-start gap-3 text-slate-300 text-base leading-relaxed"><span class="text-rose-400 mt-1 flex-shrink-0">▸</span><span><strong>Variación Compensatoria (VC):</strong> La cantidad de dinero que debe compensarse al consumidor después del cambio de precios para restaurar su nivel de utilidad original ($u^0$). Se calcula usando la función de gasto:</span></li>
<li class="flex items-start gap-3 text-slate-300 text-base leading-relaxed"><span class="text-rose-400 mt-1 flex-shrink-0">▸</span><span><strong>Variación Equivalente (VE):</strong> La cantidad de dinero que habría que quitarle al consumidor a los precios originales para que su utilidad caiga al nuevo nivel ($u^1$) equivalente al cambio de precios.</span></li>
</ul>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Ambas medidas se relacionan con el área bajo las curvas de demanda Hicksianas <span class="hidden" data-ref="34" aria-hidden="true"></span>, <span class="hidden" data-ref="35" aria-hidden="true"></span>, <span class="hidden" data-ref="36" aria-hidden="true"></span>.</p>

<div class="bg-gradient-to-br from-rose-950/90 to-slate-900/90 border border-rose-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-rose-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-rose-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Dado que la utilidad no es directamente observable, utilizamos la dualidad para medir cambios en el bienestar ante variaciones de precios (de $p^0$ a $p^1$).</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-rose-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Ambas medidas se relacionan con el área bajo las curvas de demanda Hicksianas , ,.</span></li>
        </ul>
    </div>
</div>
</section>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📌</span>
    <div>
        <h2 class="text-xl md:text-3xl font-black tracking-tight bg-gradient-to-r from-fuchsia-300 to-purple-400 bg-clip-text text-transparent">Aplicaciones Avanzadas - Perspectiva Master</h2>
        <div class="w-10 md:w-14 h-1 bg-fuchsia-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<!-- section: 1. -->
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-fuchsia-500/15 border-fuchsia-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-fuchsia-300 tracking-tight">Integrabilidad y Preferencias Reveladas</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Un problema central en es el problema inverso: dada una función de demanda observable $x(p,m)$, ¿podemos recuperar la función de utilidad subyacente? Esto se conoce como el problema de <strong>integrabilidad</strong>. Para que un sistema de demanda sea generado por la maximización de utilidad racional, debe satisfacer la <strong>Matriz de Slutsky</strong>. Esta matriz de derivadas cruzadas de las demandas compensadas, $S_{ij} = \frac{\partial x_i}{\partial p_j} + x_j \frac{\partial x_i}{\partial m}$, debe ser: <em> <strong>Simétrica:</strong> $S_{ij} = S_{ji}$. </em> <strong>Semidefinida Negativa:</strong> $v^T S v \le 0$ para cualquier vector $v$.</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Esto está íntimamente ligado al <strong>Axioma Débil de Preferencia Revelada (WARP)</strong> y al <strong>Axioma Fuerte (SARP)</strong>. Si un consumidor elige la cesta $x^A$ cuando $x^B$ era asequible ($p^A x^A \ge p^A x^B$), entonces no debe elegir $x^B$ cuando $x^A$ sea asequible a los nuevos precios ($p^B x^B \le p^B x^A \implies \text{contradicción}$) <span class="hidden" data-ref="37" aria-hidden="true"></span>, <span class="hidden" data-ref="38" aria-hidden="true"></span>.</p>
<!-- section: 2. -->
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-fuchsia-500/15 border-fuchsia-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📈</span>
    <h3 class="text-xl font-bold text-fuchsia-300 tracking-tight">Modelo de Asignación de Tiempo y Oferta Laboral</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La teoría del consumidor se extiende a la oferta de factores. Si consideramos el ocio ($h$) como un bien y el consumo ($c$) como otro, sujeto a una restricción de tiempo total ($T = h + l$, donde $l$ es trabajo) y una restricción presupuestaria $c = w \cdot l$ (donde $w$ es el salario), el problema se convierte en: $$ \max U(c, h) \quad \text{s.a.} \quad c + w \cdot h = w \cdot T $$ Aquí, $w$ es el costo de oportunidad del ocio. La ecuación de Slutsky explica por qué la curva de oferta laboral puede volverse hacia atrás (backward-bending): si el efecto ingreso (ser más rico induce a consumir más ocio) domina al efecto sustitución (el ocio es más caro), una subida de salarios reduce las horas trabajadas <span class="hidden" data-ref="39" aria-hidden="true"></span>, <span class="hidden" data-ref="20" aria-hidden="true"></span>, <span class="hidden" data-ref="40" aria-hidden="true"></span>.</p>
<!-- section: 3. -->
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-fuchsia-500/15 border-fuchsia-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-fuchsia-300 tracking-tight">Elección Intertemporal</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">El modelo se aplica a decisiones de ahorro. El consumidor elige entre consumo presente ($c_1$) y futuro ($c_2$) con una tasa de interés $r$. La pendiente de la restricción presupuestaria es $-(1+r)$. $$ \max U(c_1, c_2) \quad \text{s.a.} \quad c_1 + \frac{c_2}{1+r} = m_1 + \frac{m_2}{1+r} $$ La condición de optimización iguala la Tasa Marginal de Preferencia Temporal con el precio relativo del dinero en el tiempo $(1+r)$. La Ecuación de Euler derivada de este proceso es fundamental en macroeconomía moderna para modelar el consumo agregado <span class="hidden" data-ref="41" aria-hidden="true"></span>, <span class="hidden" data-ref="42" aria-hidden="true"></span>.</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">&copy; 2026 Tech Institute | Master en Microeconomía | Generación O-3</p>

<div class="bg-gradient-to-br from-fuchsia-950/90 to-slate-900/90 border border-fuchsia-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-fuchsia-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-fuchsia-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Un problema central en es el problema inverso: dada una función de demanda observable $x(p,m)$, ¿podemos recuperar la función de utilidad subyacente.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-fuchsia-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Esto está íntimamente ligado al Axioma Débil de Preferencia Revelada (WARP) y al Axioma Fuerte (SARP).</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-fuchsia-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La teoría del consumidor se extiende a la oferta de factores.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-fuchsia-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>El modelo se aplica a decisiones de ahorro.</span></li>
        </ul>
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