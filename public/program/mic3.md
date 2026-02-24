<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans overflow-hidden">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-indigo-500 rounded-full"></div>
        <span class="text-indigo-400 font-black text-[10px] uppercase tracking-[0.4em]">Economics Master Series</span>
    </div>
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8 break-words hyphens-auto">
        MIC3
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-indigo-500/15 text-indigo-300 border border-indigo-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Zero-Noise UX</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">v9.0 · Dark Mode</span>
    </div>
</header>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4"><!-- HERO --></p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Teoría de Juegos Estáticos y Dinámicos</p>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📊</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r from-indigo-300 to-violet-400 bg-clip-text text-transparent break-words leading-tight">Fundamentos de la Teoría de Juegos: Interacción Estratégica y Equilibrio</h2>
        <div class="w-10 md:w-14 h-1 bg-indigo-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La Teoría de Juegos constituye el marco analítico fundamental para modelar situaciones de interdependencia estratégica, donde el bienestar de un agente económico no depende exclusivamente de sus propias acciones, sino también de las decisiones adoptadas por otros agentes. En el nivel de Maestría, trascendemos la simple descripción de matrices de pagos para formalizar las condiciones de existencia del equilibrio y la racionalidad de los agentes en contextos estáticos y dinámicos <span class="hidden" data-ref="1" aria-hidden="true"></span>.</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">El análisis se divide en dos grandes arquitecturas: la <strong>forma normal</strong>, utilizada predominantemente para juegos estáticos con información imperfecta sobre las acciones simultáneas de los rivales, y la <strong>forma extensiva</strong>, idónea para modelar la secuencialidad, la información asimétrica y la credibilidad de las amenazas en el tiempo <span class="hidden" data-ref="2, 3" aria-hidden="true"></span>.</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-indigo-500/15 border-indigo-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">⚖️</span>
    <h3 class="text-xl font-bold text-indigo-300 tracking-tight">Juegos Estáticos en Forma Normal</h3>
</div>

<p class="text-slate-400 text-base mb-4">Un juego en forma normal se define formalmente como una tupla $G = \{N, (S_i)_{i \in N}, (u_i)_{i \in N}\}$, donde:</p>
<ul class="my-6 space-y-3">
<li class="flex items-start gap-3 text-slate-300 text-base leading-relaxed"><span class="text-indigo-400 mt-1 flex-shrink-0">▸</span><span>$N = \{1.., n\}$ es el conjunto finito de jugadores.</span></li>
<li class="flex items-start gap-3 text-slate-300 text-base leading-relaxed"><span class="text-indigo-400 mt-1 flex-shrink-0">▸</span><span>$S_i$ representa el espacio de estrategias disponibles para el jugador $i$.</span></li>
<li class="flex items-start gap-3 text-slate-300 text-base leading-relaxed"><span class="text-indigo-400 mt-1 flex-shrink-0">▸</span><span>$u_i: S_1 \times .. \times S_n \to \mathbb{R}$ es la función de pagos (utilidad) del jugador $i$, que asigna un valor a cada perfil de estrategias resultante <span class="hidden" data-ref="4" aria-hidden="true"></span>.</span></li>
</ul>
<div class="flex items-center gap-3 mt-8 mb-3">
    <span class="text-sm">🎯</span>
    <h4 class="text-sm font-black text-indigo-300 uppercase tracking-[0.15em]">Racionalidad y Estrategias Dominantes</h4>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La premisa subyacente es la racionalidad maximizadora. Un concepto inicial de solución es la <strong>estrategia dominante</strong>. Sea $s_i$ una estrategia del jugador $i$ y $s_{-i}$ el perfil de estrategias de los oponentes. Se dice que $s_i^*$ es una estrategia estrictamente dominante si:</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    $$ u_i(s_i^*, s_{-i}) > u_i(s_i, s_{-i}) \quad \forall s_{-i}, \forall s_i \neq s_i^* $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Cuando cada jugador posee una estrategia dominante, el resultado del juego es un <strong>Equilibrio en Estrategias Dominantes</strong> <span class="hidden" data-ref="5" aria-hidden="true"></span>. Este es el caso del <em>Dilema del Prisionero</em>, donde la racionalidad individual conduce a un resultado Pareto-ineficiente (ambos confiesan), a pesar de que la cooperación generaría mayores pagos conjuntos <span class="hidden" data-ref="6, 7" aria-hidden="true"></span>.</p>
<div class="flex items-center gap-3 mt-8 mb-3">
    <span class="text-sm">📌</span>
    <h4 class="text-sm font-black text-indigo-300 uppercase tracking-[0.15em]">El Equilibrio de Nash (EN)</h4>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Dado que las estrategias dominantes rara vez existen en entornos económicos complejos, recurrimos al concepto de Equilibrio de Nash. Definido formalmente por John Nash (1950), un perfil de estrategias $s^* = (s_1^*.., s_n^*)$ constituye un equilibrio de Nash si la estrategia de cada jugador es la mejor respuesta a las estrategias de equilibrio de los demás <span class="hidden" data-ref="8" aria-hidden="true"></span>. Matemáticamente:</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    $$ u_i(s_i^*, s_{-i}^*) \geq u_i(s_i, s_{-i}^*) \quad \forall s_i \in S_i, \forall i \in N $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">En este estado, ningún agente tiene incentivos unilaterales para desviarse. Es crucial notar que el EN no garantiza eficiencia ni unicidad. Existen juegos con múltiples equilibrios (como la "Batalla de los Sexos" o juegos de coordinación) y juegos sin equilibrio en estrategias puras, lo que obliga a la introducción de <strong>estrategias mixtas</strong>, donde los jugadores asignan una distribución de probabilidad sobre su espacio de acciones $S_i$ <span class="hidden" data-ref="9, 10" aria-hidden="true"></span>.</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-indigo-500/15 border-indigo-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-indigo-300 tracking-tight">Juegos Dinámicos en Forma Extensiva</h3>
</div>

<p class="text-slate-400 text-base mb-6">La representación en forma normal oscurece la estructura temporal de las decisiones. Para analizar la <strong>racionalidad secuencial</strong>, utilizamos la <strong>forma extensiva</strong> o árbol de juego. Un juego en forma extensiva especifica:</p>

<div class="flex items-start gap-5 p-5 bg-indigo-500/10 rounded-2xl my-3 border bg-indigo-500/20 hover:bg-indigo-500/15 transition-all">
    <!-- step:1 -->
    <div class="bg-indigo-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1">El conjunto de jugadores.</div>
</div>

<div class="flex items-start gap-5 p-5 bg-indigo-500/10 rounded-2xl my-3 border bg-indigo-500/20 hover:bg-indigo-500/15 transition-all">
    <!-- step:2 -->
    <div class="bg-indigo-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1">El orden de los movimientos (nodos de decisión).</div>
</div>

<div class="flex items-start gap-5 p-5 bg-indigo-500/10 rounded-2xl my-3 border bg-indigo-500/20 hover:bg-indigo-500/15 transition-all">
    <!-- step:3 -->
    <div class="bg-indigo-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">3</div>
    <div class="text-slate-200 text-base leading-snug pt-1">Los conjuntos de información $H_i$ (lo que sabe el jugador en cada nodo).</div>
</div>

<div class="flex items-start gap-5 p-5 bg-indigo-500/10 rounded-2xl my-3 border bg-indigo-500/20 hover:bg-indigo-500/15 transition-all">
    <!-- step:4 -->
    <div class="bg-indigo-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">4</div>
    <div class="text-slate-200 text-base leading-snug pt-1">Las acciones factibles en cada nodo.</div>
</div>

<div class="flex items-start gap-5 p-5 bg-indigo-500/10 rounded-2xl my-3 border bg-indigo-500/20 hover:bg-indigo-500/15 transition-all">
    <!-- step:5 -->
    <div class="bg-indigo-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">5</div>
    <div class="text-slate-200 text-base leading-snug pt-1">Los pagos finales en los nodos terminales <span class="hidden" data-ref="11, 12" aria-hidden="true"></span>.</div>
</div>
<div class="flex items-center gap-3 mt-8 mb-3">
    <span class="text-sm">🎯</span>
    <h4 class="text-sm font-black text-indigo-300 uppercase tracking-[0.15em]">Información y Estrategias en Juegos Dinámicos</h4>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Una distinción crítica en la forma extensiva es la calidad de la información. <em> <strong>Información Perfecta:</strong> Cada conjunto de información contiene un solo nodo; el jugador conoce toda la historia previa del juego (ej. Ajedrez, Stackelberg). </em> <strong>Información Imperfecta:</strong> Al menos un conjunto de información contiene más de un nodo; el jugador no sabe exactamente en qué punto del árbol se encuentra (ej. decisiones simultáneas modeladas en árboles) <span class="hidden" data-ref="13" aria-hidden="true"></span>.</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Una <strong>estrategia</strong> en un juego dinámico es un plan de acción completo y contingente: debe especificar qué acción tomará el jugador en <em>cada</em> conjunto de información donde le toque jugar, incluso en aquellos que nunca se alcancen en la trayectoria de equilibrio <span class="hidden" data-ref="14" aria-hidden="true"></span>.</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-indigo-500/15 border-indigo-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-indigo-300 tracking-tight">Inducción Hacia Atrás y Equilibrio de Nash Perfecto en Subjuegos (ENPS)</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">El concepto de Equilibrio de Nash, cuando se aplica a juegos dinámicos, puede admitir soluciones sustentadas en <strong>amenazas no creíbles</strong>. Para refinar el equilibrio, Selten (1965) introdujo el concepto de Perfección en Subjuegos.</p>
<div class="flex items-center gap-3 mt-8 mb-3">
    <span class="text-sm">📖</span>
    <h4 class="text-sm font-black text-indigo-300 uppercase tracking-[0.15em]">El Principio de Racionalidad Secuencial</h4>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La racionalidad secuencial exige que el comportamiento de los jugadores sea óptimo no solo al inicio del juego, sino en cualquier punto en el que se encuentren, independientemente de cómo se haya llegado a ese punto. Una amenaza es creíble solo si, llegado el momento de ejecutarla, el jugador maximiza su utilidad cumpliéndola <span class="hidden" data-ref="15" aria-hidden="true"></span>.</p>
<div class="flex items-center gap-3 mt-8 mb-3">
    <span class="text-sm">📌</span>
    <h4 class="text-sm font-black text-indigo-300 uppercase tracking-[0.15em]">Equilibrio de Nash Perfecto en Subjuegos (ENPS)</h4>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Un perfil de estrategias es un ENPS si induce un equilibrio de Nash en cada subjuego del juego original. Este concepto elimina los equilibrios basados en amenazas vanas.</p>
<div class="flex items-center gap-3 mt-8 mb-3">
    <span class="text-sm">📌</span>
    <h4 class="text-sm font-black text-indigo-300 uppercase tracking-[0.15em]">Algoritmo de Inducción Hacia Atrás</h4>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Para hallar el ENPS en juegos finitos de información perfecta, utilizamos la <strong>inducción hacia atrás</strong>. 1. Nos situamos en los nodos de decisión finales (previos a los pagos). 2. Determinamos la acción óptima para el jugador en ese nodo. 3. Reemplazamos el nodo de decisión por el pago resultante de la acción óptima. 4. Retrocedemos al nodo anterior y repetimos el proceso hasta llegar al nodo inicial <span class="hidden" data-ref="16" aria-hidden="true"></span>.</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Este procedimiento garantiza que las estrategias seleccionadas sean óptimas en cada etapa, satisfaciendo la consistencia temporal.</p>

<div class="bg-gradient-to-br from-indigo-950/90 to-slate-900/90 border border-indigo-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-indigo-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-indigo-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La Teoría de Juegos constituye el marco analítico fundamental para modelar situaciones de interdependencia estratégica, donde el bienestar de un agente económico no depende exclusivamente de sus propias acciones, sino también de las decisiones adoptadas por otros agentes.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-indigo-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>El análisis se divide en dos grandes arquitecturas: la forma normal, utilizada predominantemente para juegos estáticos con información imperfecta sobre las acciones simultáneas de los rivales, y la forma extensiva, idónea para modelar la secuencialidad, la información asimétrica y la credibilidad de las amenazas en el tiempo.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-indigo-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La premisa subyacente es la racionalidad maximizadora.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-indigo-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Cuando cada jugador posee una estrategia dominante, el resultado del juego es un Equilibrio en Estrategias Dominantes.</span></li>
        </ul>
    </div>
</div>
</section>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">🔢</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r from-cyan-300 to-blue-400 bg-clip-text text-transparent break-words leading-tight">Modelización Avanzada de Oligopolio: El Modelo de Stackelberg</h2>
        <div class="w-10 md:w-14 h-1 bg-cyan-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">El modelo de Stackelberg representa la aplicación paradigmática de los juegos dinámicos en la organización industrial. A diferencia del modelo de Cournot (simultáneo y estático), Stackelberg introduce una jerarquía temporal: una empresa <strong>Líder</strong> (Firma 1) mueve primero, y una empresa <strong>Seguidora</strong> (Firma 2) observa la decisión del líder y responde <span class="hidden" data-ref="17, 18" aria-hidden="true"></span>.</p>
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-cyan-500/15 border-cyan-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-cyan-300 tracking-tight">Formalización Matemática</h3>
</div>


<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    Supongamos un duopolio con una demanda de mercado lineal inversa dada por: $$ P(Q) = a - bQ $$ Donde $Q = q_1 + q_2$. Supongamos costos marginales constantes e idénticos para ambas firmas, $CMg = c$, y costos fijos nulos.
</div>
<div class="flex items-center gap-3 mt-8 mb-3">
    <span class="text-sm">📌</span>
    <h4 class="text-sm font-black text-cyan-300 uppercase tracking-[0.15em]">Fase 2: El problema de la Seguidora</h4>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Siguiendo la inducción hacia atrás, resolvemos primero el problema de la Firma 2. La seguidora observa $q_1$ (que ya es un dato fijo) y maximiza su beneficio:</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    $$ \max_{q_2} \pi_2 = [P(q_1 + q_2) - c]q_2 $$ $$ \max_{q_2} \pi_2 = [a - b(q_1 + q_2) - c]q_2 $$
</div>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    Obtenemos la Condición de Primer Orden (CPO): $$ \frac{\partial \pi_2}{\partial q_2} = a - bq_1 - 2bq_2 - c = 0 $$
</div>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    Despejando $q_2$, obtenemos la <strong>Función de Reacción</strong> de la seguidora, $R_2(q_1)$: $$ q_2 = \frac{a - c - bq_1}{2b} = \frac{a-c}{2b} - \frac{1}{2}q_1 $$
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Nótese que esta es idéntica a la función de reacción en Cournot, pero aquí la Firma 2 reacciona a un <em>fait accompli</em> (hecho consumado) <span class="hidden" data-ref="18" aria-hidden="true"></span>.</p>
<div class="flex items-center gap-3 mt-8 mb-3">
    <span class="text-sm">📌</span>
    <h4 class="text-sm font-black text-cyan-300 uppercase tracking-[0.15em]">Fase 1: El problema de la Líder</h4>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La Firma 1, conociendo la racionalidad de la Firma 2, anticipa su reacción. Incorpora $R_2(q_1)$ directamente en su función de beneficios. La líder no toma $q_2$ como dado, sino que sabe que $q_2$ depende de su propia producción.</p>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    $$ \max_{q_1} \pi_1 = [P(q_1 + R_2(q_1)) - c]q_1 $$ $$ \max_{q_1} \pi_1 = \left[ a - b\left( q_1 + \left( \frac{a-c}{2b} - \frac{q_1}{2} \right) \right) - c \right] q_1 $$
</div>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    Simplificando la expresión dentro del corchete (el precio anticipado): $$ P = a - bq_1 - \frac{a-c}{2} + \frac{b q_1}{2} - c = \frac{a+c}{2} - \frac{b q_1}{2} $$
</div>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    La función de beneficio de la líder se convierte en: $$ \pi_1 = \left( \frac{a-c}{2} - \frac{b q_1}{2} \right) q_1 $$
</div>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    Maximizando respecto a $q_1$: $$ \frac{\partial \pi_1}{\partial q_1} = \frac{a-c}{2} - bq_1 = 0 $$
</div>

<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    De donde obtenemos la producción óptima de la líder: $$ q_1^* = \frac{a-c}{2b} $$
</div>
<div class="flex items-center gap-3 mt-8 mb-3">
    <span class="text-sm">📌</span>
    <h4 class="text-sm font-black text-cyan-300 uppercase tracking-[0.15em]">Equilibrio y Comparación</h4>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Sustituyendo $q_1^*$ en la función de reacción de la seguidora: $$ q_2^* = \frac{a-c}{2b} - \frac{1}{2}\left( \frac{a-c}{2b} \right) = \frac{a-c}{4b} $$</p>
<p class="text-slate-400 text-base mb-6"><strong>Resultados Clave:</strong></p>

<div class="flex items-start gap-5 p-5 bg-cyan-500/10 rounded-2xl my-3 border bg-cyan-500/20 hover:bg-cyan-500/15 transition-all">
    <!-- step:1 -->
    <div class="bg-cyan-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">1</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Ventaja del Primer Movimiento:</strong> La líder produce el doble que la seguidora ($q_1^* = 2q_2^*$) y obtiene mayores beneficios. Esto contrasta con el modelo de Bertrand donde la competencia disipa beneficios, o Cournot donde son simétricos <span class="hidden" data-ref="19" aria-hidden="true"></span>.</div>
</div>

<div class="flex items-start gap-5 p-5 bg-cyan-500/10 rounded-2xl my-3 border bg-cyan-500/20 hover:bg-cyan-500/15 transition-all">
    <!-- step:2 -->
    <div class="bg-cyan-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">2</div>
    <div class="text-slate-200 text-base leading-snug pt-1"><strong>Eficiencia:</strong> La producción total en Stackelberg $Q_S = \frac{3(a-c)}{4b}$ es mayor que en Cournot $Q_C = \frac{2(a-c)}{3b}$, lo que implica un precio de mercado menor y un mayor excedente del consumidor, aunque sigue siendo ineficiente comparado con la competencia perfecta <span class="hidden" data-ref="20" aria-hidden="true"></span>.</div>
</div>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La capacidad de la líder para comprometerse a un nivel de producción alto (y hacerlo creíble al mover primero) obliga a la seguidora a contraer su producción para evitar deprimir excesivamente los precios. Esto demuestra cómo la estructura de información y el <em>timing</em> alteran radicalmente la distribución de rentas en el mercado.</p>

<div class="bg-gradient-to-br from-cyan-950/90 to-slate-900/90 border border-cyan-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-cyan-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-cyan-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>El modelo de Stackelberg representa la aplicación paradigmática de los juegos dinámicos en la organización industrial.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-cyan-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Siguiendo la inducción hacia atrás, resolvemos primero el problema de la Firma 2.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-cyan-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Nótese que esta es idéntica a la función de reacción en Cournot, pero aquí la Firma 2 reacciona a un fait accompli (hecho consumado).</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-cyan-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La Firma 1, conociendo la racionalidad de la Firma 2, anticipa su reacción.</span></li>
        </ul>
    </div>
</div>
</section>

<section class="mb-16 last:mb-0">
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📌</span>
    <div>
        <h2 class="text-xl md:text-2xl sm:text-3xl font-black tracking-tight bg-gradient-to-r from-emerald-300 to-teal-400 bg-clip-text text-transparent break-words leading-tight">Aplicaciones Avanzadas - Perspectiva Master</h2>
        <div class="w-10 md:w-14 h-1 bg-emerald-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">En el nivel de posgrado, la teoría de juegos se expande para incorporar las limitaciones cognitivas de los agentes y la complejidad de las interacciones repetidas, desafiando los supuestos neoclásicos estándar.</p>
<!-- section: 1. -->
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-emerald-500/15 border-emerald-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-emerald-300 tracking-tight">Juegos Repetidos y Colusión Tácita</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Mientras que en el <em>Dilema del Prisionero</em> estático (un solo periodo) la estrategia dominante es "no cooperar" (confesar/competir), en entornos dinámicos infinitos o indefinidos, la cooperación puede sostenerse como un Equilibrio de Nash Perfecto en Subjuegos. <em> <strong>Teorema Popular (Folk Theorem):</strong> Si el factor de descuento $\delta$ (paciencia de los agentes) es suficientemente cercano a 1, cualquier pago factible e individualmente racional puede ser sostenido como un equilibrio. </em> <strong>Estrategias de Gatillo (Trigger Strategies):</strong> En el contexto de oligopolios (carteles), las firmas pueden acordar precios monopólicos y amenazar con una "guerra de precios" perpetua (reversión al equilibrio de Nash de etapa) si alguien hace trampa. Para que el cártel sea estable, el beneficio de corto plazo de desviarse debe ser menor que la pérdida acumulada de futuros beneficios de colusión descontados <span class="hidden" data-ref="21, 22" aria-hidden="true"></span>. <strong>Estrategia "Tit-for-Tat" (Ojo por Ojo):</strong> Ganadora en los torneos de Axelrod, esta estrategia implica cooperar en el primer periodo y luego replicar la acción previa del oponente. Es robusta porque es amable (inicia cooperando), provocable (castiga la traición) y clemente (retorna a la cooperación) <span class="hidden" data-ref="23, 24" aria-hidden="true"></span>.</p>
<!-- section: 2. -->
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-emerald-500/15 border-emerald-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-emerald-300 tracking-tight">Economía Conductual y Límites de la Racionalidad</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La evidencia empírica sugiere que el supuesto de egoísmo racional estricto (Homo Economicus) falla en predecir el comportamiento en ciertos juegos dinámicos. <em> <strong>El Juego del Ultimátum:</strong> Un Proponente (A) ofrece una división de una suma $S$ a un Respondedor (B). Si B acepta, se divide según lo propuesto; si rechaza, ambos obtienen cero. </em> <em>Predicción Teórica (SPNE):</em> A ofrece la cantidad mínima positiva $\epsilon$ y B acepta (porque $\epsilon > 0$). <em> </em>Evidencia Empírica:<em> Ofertas inferiores al 20-30% son frecuentemente rechazadas. Los agentes incorporan "preferencias sociales" o de equidad en su función de utilidad. Castigar una oferta injusta genera utilidad a B, aunque pierda dinero. Esto modifica el análisis de incentivos en contratos y negociaciones salariales <span class="hidden" data-ref="25, 26" aria-hidden="true"></span>. </em> <strong>Concurso de Belleza Keynesiano:</strong> Ilustra los niveles de razonamiento iterativo ($k$-level thinking). Los jugadores eligen un número entre 0 y 100, ganando quien se acerque más a 2/3 del promedio. El equilibrio de Nash es 0, pero empíricamente los resultados varían según la profundidad del razonamiento estratégico de los participantes (nivel 1 asume aleatoriedad, nivel 2 asume nivel 1, etc.) <span class="hidden" data-ref="27" aria-hidden="true"></span>.</p>
<!-- section: 3. -->
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-emerald-500/15 border-emerald-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-emerald-300 tracking-tight">Subastas y Diseño de Mecanismos</h3>
</div>

<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">La teoría de juegos con información incompleta es la base de la teoría de subastas (Premio Nobel 2020, Milgrom y Wilson). <em> <strong>Maldición del Ganador:</strong> En subastas de valor común (ej. pozos petroleros), el ganador suele ser quien ha sobreestimado el valor del activo, obteniendo a menudo rendimientos negativos. Un postor racional en un equilibrio Bayesiano debe sombrear su oferta (bid shading) a la baja para corregir este sesgo condicional <span class="hidden" data-ref="28" aria-hidden="true"></span>. </em> <strong>Equivalencia de Ingresos:</strong> Bajo supuestos de neutralidad al riesgo y valores privados independientes, los cuatro tipos de subastas estándar (Inglesa, Holandesa, Primer Precio, Segundo Precio) generan el mismo ingreso esperado para el vendedor <span class="hidden" data-ref="29" aria-hidden="true"></span>.</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">Estas aplicaciones demuestran que la Teoría de Juegos no es solo una abstracción matemática, sino una herramienta indispensable para el diseño de políticas públicas (regulación ambiental, antimonopolio), estrategias corporativas y la comprensión de las instituciones sociales.</p>
<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">&copy; 2026 Tech Institute | Master en Microeconomía | Generación O-3</p>

<div class="bg-gradient-to-br from-emerald-950/90 to-slate-900/90 border border-emerald-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-emerald-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-emerald-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>En el nivel de posgrado, la teoría de juegos se expande para incorporar las limitaciones cognitivas de los agentes y la complejidad de las interacciones repetidas, desafiando los supuestos neoclásicos estándar.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-emerald-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>Mientras que en el Dilema del Prisionero estático (un solo periodo) la estrategia dominante es "no cooperar" (confesar/competir), en entornos dinámicos infinitos o indefinidos, la cooperación puede sostenerse como un Equilibrio de Nash Perfecto en Subjuegos.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-emerald-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La evidencia empírica sugiere que el supuesto de egoísmo racional estricto (Homo Economicus) falla en predecir el comportamiento en ciertos juegos dinámicos.</span></li>
<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-emerald-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>La teoría de juegos con información incompleta es la base de la teoría de subastas (Premio Nobel 2020, Milgrom y Wilson).</span></li>
        </ul>
    </div>
</div>
</section>


<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">
        <span class="text-fuchsia-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo MIC3</h3>
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
            <span class="text-indigo-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Efecto Sustitución</span>
            <p class="text-slate-400 text-sm leading-relaxed">Migración táctica u órbita compensatoria resolutiva asimilativa defensiva estricta de migración predileccional o resguardo hacia horizontes o bienes abaratados homólogos en detrimento purificador descartable e intercamio asintomático del abaratado descartando lo encarecido colindante ante mutaciones del vector exógeno $P$, simulando abstracciones exentas destiladas aisladas o purificando teóricamente sin injerencias aditivas colaterales mutativas e impurezas empobrecedoras simultáneas previsoras compensatorias inamovibles congeladoras pre-estabilizadoras y restitutivas de ingresos idénticos subyacentes compensaciones hicksianas utilitarias del umbral neutro inobjetable irreal basal pre-establecido de utilidad anclada o invariable compensada inamovible.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-indigo-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Efecto Renta</span>
            <p class="text-slate-400 text-sm leading-relaxed">Secuela macro colateral empobrecedora implícita o inyección puramente empujada de empoderamiento adquisitorio colindante indirecta virtual subyugante paralela o residual transaccional emanante y residual subproducente colateral e inintencionada adyacente inercial transicional de cualquier vaivén fluctuacional de encarecimientos $P$, donde el mismo estático e inamovible y crudo estanco cheque o bolsa nominal de salarios pre-asignada inamovible acusa y devela perversas depreciativas asfixiantes licuadoras caídas o rebosantes asimétricas exultantes excedentarias dilataciones ficticias del caudal fáctico transable palpable fraccional poder real de apropiaciones en el mundo físico de cuotas unitarias crudas palpadoras adquisitorias subyacentes.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-indigo-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Bien Normal</span>
            <p class="text-slate-400 text-sm leading-relaxed">Estructura ontológica mercantil o catálogo resolutivo predeterminado cuya elástica propensión correlativa estadística asimila subyugadamente sin rebeldías empujes ascendentes demandantes ávidos colaterales emparejados alineados paralelos inescrutables correspondientes ante empoderamientos u óbolos e inyecciones de incrementales sustanciosas u opulencias abultadas de tesoros bolsillos o alzas dotacionales de haberes de ingresos engrosando alicientes pre-ordenados $I \\uparrow \\implies Q \\uparrow$.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-indigo-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Bien Inferior</span>
            <p class="text-slate-400 text-sm leading-relaxed">Clasificación paradójica contraintuitiva pero recurrente empírica de productos estigmatizables arcaicos vulgares rudimentarios menesterosos de pobrezas o calidades empobrecidas degradadas sustituibles cuya ansia o apetito estadístico asimétrico consumidor se disuelve extinguiendo descarta expulsa en picada trágicamente o reduce en fuga repelente o exilios compensadores repudios asimétricos marginantes decrece $Q \\downarrow$ a expensas compensadas o en la eventualidad de riquezas o empujes fortificados rentísticos enriquecedores opulencias bonanzas ascendentes empoderamientos bolsillos engrosados ascendentes aliviadores $I \\uparrow$.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-indigo-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Bien Giffen</span>
            <p class="text-slate-400 text-sm leading-relaxed">Quimera teórica estrafalaria anómala insólita exótica inaudita irrestricta o atipicidad estadística abismalmente contra-teórica paradojal incomprensible irlandesa patológica rarísima donde la pre-ordenanza o propensión invertida destrozando simetrías clásicas de lógicas de curva $D$ estipula absurdamente inverosímil subyugante y demencialmente alicientes devoradores correlativos inescrutables de $Q \\uparrow$ si casualidades exógenas perversas elevan asfixiantes asoladores encareciendo letales agudas los índices de valores tasadores $P \\uparrow$. Esto por el devastador y canibalizador ultra-efecto abismal empobrecedor rentístico asimilador colosal letal asfixiador acaparador aniquilador de pauperización crudo inmanente extremo hiperempobrecedor asimétrico inmenso abrumador que opaca al sustitutorio inoperante e inferior hipertrofiado superándolo opacándolo avasallándolo eclipsante aniquilando excedentario superatriz aplastante insoslayable absorbente inusitado.</p>
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