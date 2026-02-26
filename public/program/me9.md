<section class="max-w-4xl mx-auto space-y-12">

<!-- Hero Section -->
<div class="relative overflow-hidden rounded-[2rem] border border-white/10 bg-gradient-to-br from-slate-900 to-slate-800 p-8 lg:p-12 mb-12 shadow-2xl">
    <div class="absolute inset-0 bg-[linear-gradient(to_right,#0ea5e91a_1px,transparent_1px),linear-gradient(to_bottom,#0ea5e91a_1px,transparent_1px)] bg-[size:24px_24px]"></div>

    <div class="relative z-10">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/20 text-cyan-400 text-[10px] font-black tracking-widest uppercase mb-6">
            Módulo ME9
        </div>

        <h1 class="text-4xl lg:text-5xl font-black text-white tracking-tight mb-6 leading-tight">
            Variables Aleatorias y <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-violet-400">Esperanza Matemática</span>
        </h1>

        <p class="text-lg text-slate-400 max-w-2xl leading-relaxed">
            La Teoría de la Inversión Moderna depende de cuantificar cosas que aún no han ocurrido. Las funciones de densidad y las integrales traen el caos al dominio de la certidumbre medible.
        </p>
    </div>
</div>

<!-- Relearning: Intuicion -->
<div class="mb-12">
    <h2 class="text-xs font-black text-slate-500 uppercase tracking-[0.2em] border-b border-white/10 pb-4 mb-8">Paso 1: Intuición Económica</h2>
    
    <div class="prose prose-invert max-w-none">
        <p>¿Aceptaría un banco de inversión darle cobertura y asegurar un barco lleno de mercancía contra una tormenta? El hundimiento no es "sí" o "no". Existen infinitas posibilidades continuas de la fuerza del viento, el tonelaje de daño, el tiempo en ruta.</p>
        <p>Para esto, ya no listamos casos discretos en una tabla excels. Diseñamos una <b>Variable Aleatoria Continua</b> sobre el monto del daño y calculamos una integral especial que dictará la prima perfecta de salvataje que cubre el riesgo.</p>
    </div>
</div>

<!-- Relearning: Formalizacion Continua -->
<div class="mb-12">
    <div class="bg-gradient-to-r from-slate-900 to-slate-800 rounded-2xl border border-white/5 p-6 md:p-8 relative overflow-hidden">
        <h3 class="text-xl font-bold text-white mb-4">Funciones de Densidad</h3>
        
        <p class="text-slate-300 mb-6">
            Sea $X$ una variable aleatoria continua. Su Comportamiento está descrito íntegramente por su Función de Densidad $f(x) \ge 0$. A diferencia de la suma discreta de probabilidades que daba igual a 1, ahora es el área total de la campana la que suma 1.
        </p>

        <div class="bg-black/30 rounded-xl p-4 border border-white/5 text-center font-mono my-6">
            <span class="text-cyan-300 text-lg">
                $$ \int_{-\infty}^{+\infty} f(x) dx = 1 $$
            </span>
        </div>

        <!-- Teorema Alert -->
        <div class="bg-violet-900/20 border border-violet-500/20 rounded-xl p-5 mt-6">
            <h4 class="font-bold text-violet-300 mb-2">Ley Estricta de Continuidad</h4>
            <p class="text-sm text-slate-300">La probabilidad de que una variable aleatoria continua caiga en un punto *exacto y microscópico* $a$ es cero ($P(X=a) = 0$). Solo podemos calcular y valorar económicamente probabilidades de que el suceso ocurra en **un intervalo o rango**: $\int_a^b f(x) dx$.</p>
        </div>
    </div>
</div>

<!-- Relearning: Aplicacion -->
<div class="mb-12">
    <h2 class="text-xs font-black text-cyan-400 uppercase tracking-[0.2em] border-b border-cyan-500/20 pb-4 mb-8">Paso 3: Esperanza y Mercado de Seguros</h2>

    <div class="bg-cyan-900/10 border border-cyan-500/20 rounded-2xl p-6 md:p-8">
        <h3 class="text-lg font-bold text-white mb-4">Cálculo del Valor Esperado Financiero ($E[X]$)</h3>
        <p class="text-slate-300 mb-6">
            La Esperanza Matemática es el centro de gravedad o promedio equilibrado del futuro. En finanzas, es el precio "favorable-neutral" base de los seguros y rentabilidades de un portfolio de acciones. Se calcula ponderando cada valor posible de la acción $x$ por su asombrosa "cuota" infinitesimal de densidad $f(x)$ y acumulándolo con una integral infinita.
        </p>

        <div class="bg-black/40 border border-white/10 rounded-xl p-5 font-mono text-center mb-6 overflow-x-auto">
            <span class="text-cyan-300 text-xl font-bold">
                $$ E[X] = \mu = \int_{-\infty}^{\infty} x \cdot f(x) dx $$
            </span>
        </div>

        <p class="text-sm text-slate-400 mt-6">
            <b>Ejemplo Táctico de Seguros:</b> Si el coste que le supone un accidente a una compañía de seguros varía aleatoriamente entre 0 y 50 millones, regido por $f(costo)$. Calcular $E[costo]$ determinará la "prima pura" (la tarifa piso por debajo de la cual matemáticamente se asoma a la quiebra absoluta tras cientos de siniestros).
        </p>
    </div>
</div>

</section>
