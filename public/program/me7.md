<section class="max-w-4xl mx-auto space-y-12">

<!-- Hero Section -->
<div class="relative overflow-hidden rounded-[2rem] border border-white/10 bg-gradient-to-br from-slate-900 to-slate-800 p-8 lg:p-12 mb-12 shadow-2xl">
    <div class="absolute top-0 right-0 w-96 h-96 bg-cyan-500/10 rounded-full blur-[80px] -translate-y-1/2 translate-x-1/3 pointer-events-none"></div>

    <div class="relative z-10">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/20 text-cyan-400 text-[10px] font-black tracking-widest uppercase mb-6">
            Módulo ME7
        </div>

        <h1 class="text-4xl lg:text-5xl font-black text-white tracking-tight mb-6 leading-tight">
            Integrales Impropias y <br/><span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-teal-400">Flujos Continuos</span>
        </h1>

        <p class="text-lg text-slate-400 max-w-2xl leading-relaxed">
            Las finanzas corporativas y la macroeconomía lidian con proyectos del estado o flujos de caja perpetuos. Descubre cómo calcular integrales cuando el horizonte de tiempo corre literalmente hacia el infinito.
        </p>
    </div>
</div>

<!-- Relearning: Intuicion -->
<div class="mb-12">
    <h2 class="text-xs font-black text-slate-500 uppercase tracking-[0.2em] border-b border-white/10 pb-4 mb-8">Paso 1: Intuición Económica</h2>
    
    <div class="prose prose-invert max-w-none">
        <p>¿Cuánto vale hoy una acción de una empresa que planea repartir dividendos eternamente? Si el tiempo es infinito, ¿no valdría la empresa también infinito? La respuesta rotunda de la economía financiera es no. El dinero de hoy vale más que el dinero de mañana debido al tipo de interés (coste de oportunidad temporal).</p>
        <p>Si descontamos cada flujo futuro a una tasa de interés constante y sumamos esos flujos para siempre (desde el año cero hasta el año infinito), obtenemos un límite matemático. Este límite se llama <b>Integral Impropia de primera especie</b>.</p>
    </div>
</div>

<!-- Relearning: Formalizacion Impropia -->
<div class="mb-12">
    <div class="bg-gradient-to-r from-slate-900 to-slate-800 rounded-2xl border border-white/5 p-6 md:p-8 relative overflow-hidden">
        <h3 class="text-xl font-bold text-white mb-4">Límites de Integración Infinitos</h3>
        
        <p class="text-slate-300 mb-6">
            Una integral impropia se procesa reemplazando el infinito por una variable genérica $t$ y empujando esa variable hacia el infinito usando un límite estructural riguroso.
        </p>

        <div class="bg-black/30 rounded-xl p-6 border border-white/5 text-center font-mono overflow-x-auto">
            <span class="text-cyan-300 text-lg">
                $$ \int_{a}^{+\infty} f(x) dx = \lim_{t \to +\infty} \int_{a}^{t} f(x) dx $$
            </span>
        </div>

        <div class="mt-6 flex items-start gap-4">
            <div class="w-1.5 h-auto self-stretch bg-emerald-500 rounded-full"></div>
            <div>
                <p class="text-sm text-slate-400">Si este límite da un número finito (real), decimos que la integral impropia <b>converge</b>. Si el límite explota (infinito) o fluctúa sin acercarse a un valor, entonces la integral <b>diverge</b> y el activo tendería a tener un precio matemáticamente ilógico.</p>
            </div>
        </div>
    </div>
</div>

<!-- Relearning: Aplicacion Financiera Continua -->
<div class="mb-12">
    <h2 class="text-xs font-black text-cyan-400 uppercase tracking-[0.2em] border-b border-cyan-500/20 pb-4 mb-8">Paso 3: Valor Presente a Tiempo Continuo</h2>

    <div class="bg-slate-800/50 border border-white/5 rounded-2xl p-6 md:p-8">
        <p class="text-slate-300 mb-6">Un flujo de caja tradicional (VAN) es discreto. Cobra intereses una vez al año. Pero en mercados financieros de alta frecuencia o flujos macroeconómicos nacionales corporativos, el dinero fluye a cada segundo. Utilizamos una capitalización continua dictada por la función $e^{-rt}$ que trae dinero futuro al valor presente.</p>

        <div class="bg-black/40 border border-white/10 rounded-xl p-5 font-mono text-center mb-6">
            <div class="text-emerald-400 text-lg mb-2">$$ VP = \int_{0}^{+\infty} f(t) \cdot e^{-rt} \, dt $$</div>
            <p class="text-xs text-slate-500 mt-2 font-sans text-left px-4">Donde $f(t)$ es la función del flujo de ingresos en el instante $t$, y $r$ es la tasa de interés continua.</p>
        </div>

        <h4 class="font-bold text-white mt-8 mb-4">Caso Práctico: Renta Perpetua Constante</h4>
        <p class="text-sm text-slate-400 mb-4">
            Si una propiedad genera una renta de $C$ constante por el resto de la eternidad. ¿Cuál es su precio justo total hoy? Es el límite impropio resuelto:
        </p>

        <div class="bg-cyan-900/20 border border-cyan-500/20 py-4 px-6 rounded-lg font-mono text-center overflow-x-auto text-sm text-slate-300">
            $$ VP = \int_{0}^{\infty} C e^{-rt} dt = \lim_{x \to \infty} \left[ -\frac{C}{r} e^{-rt} \right]_0^x = \lim_{x \to \infty} \left( -\frac{C}{r} e^{-rx} - \left( -\frac{C}{r} \right) \right) = 0 + \frac{C}{r} = \frac{C}{r} $$
        </div>

        <p class="text-sm text-emerald-400 mt-4 font-bold text-center">¡El increíble colapso! El valor infinito matemático se reduce a la sencilla ecuación C/r gracias a la convergencia.</p>
    </div>
</div>

</section>
