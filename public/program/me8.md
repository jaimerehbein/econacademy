<section class="max-w-4xl mx-auto space-y-12">

<!-- Hero Section -->
<div class="relative overflow-hidden rounded-[2rem] border border-white/10 bg-gradient-to-br from-slate-900 to-slate-800 p-8 lg:p-12 mb-12 shadow-2xl">
    <div class="absolute inset-0 bg-[linear-gradient(to_right,#6366f11a_1px,transparent_1px),linear-gradient(to_bottom,#6366f11a_1px,transparent_1px)] bg-[size:16px_16px]"></div>

    <div class="relative z-10">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 text-[10px] font-black tracking-widest uppercase mb-6">
            Módulo ME8
        </div>

        <h1 class="text-4xl lg:text-5xl font-black text-white tracking-tight mb-6 leading-tight">
            Ecuaciones Diferenciales y <span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-violet-400">Dinámica</span>
        </h1>

        <p class="text-lg text-slate-400 max-w-2xl leading-relaxed">
            Las economías no están quietas; evolucionan a lo largo del tiempo. Las Ecuaciones Diferenciales son el lenguaje de la acumulación de capital, el crecimiento poblacional y la degradación del dinero.
        </p>
    </div>
</div>

<!-- Relearning: Intuicion -->
<div class="mb-12">
    <h2 class="text-xs font-black text-slate-500 uppercase tracking-[0.2em] border-b border-white/10 pb-4 mb-8">Paso 1: Intuición Económica</h2>
    
    <div class="prose prose-invert max-w-none">
        <p>Imagina una cuenta bancaria con capitalización continua. La asombrosa característica geométrica del interés compuesto es que tu velocidad de acumulación de riqueza hoy (la derivada de tu capital), depende directamente del nivel de riqueza acumulada que posees hoy (el propio capital).</p>
        <p>Una ecuación que mezcla una función y la derivada de esa misma función en la misma línea matemática se denomina <b>Ecuación Diferencial</b>.</p>
    </div>
</div>

<!-- Relearning: Formalizacion -->
<div class="mb-12">
    <h2 class="text-xs font-black text-indigo-400 uppercase tracking-[0.2em] border-b border-white/10 pb-4 mb-8">Paso 2: Formalización Matemática</h2>
    
    <div class="bg-gradient-to-r from-slate-900 to-slate-800 rounded-2xl border border-white/5 p-6 md:p-8 relative overflow-hidden">
        <h3 class="text-xl font-bold text-white mb-4">Ecuaciones de Variables Separables</h3>
        
        <p class="text-slate-300 mb-6">
            La forma más elemental es separar todo lo que tenga $y$ a un lado de la igualdad y todo lo que tenga $t$ (términos independientes del tiempo) al otro lado.
        </p>

        <div class="bg-black/30 rounded-xl p-6 border border-white/5 text-center font-mono overflow-x-auto">
            <span class="text-indigo-300 text-lg">
                $$ y' = f(t) \cdot g(y)$$<br/>
                $$ \frac{dy}{dt} = f(t) \cdot g(y)$$<br/>
                $$ \int \frac{1}{g(y)} dy = \int f(t) dt $$
            </span>
        </div>

        <p class="text-sm text-slate-400 mt-6">
            Al integrar ambos lados algebraicamente separables, y resolviendo para $y$, obtenemos no un número, sino una <b>familia inmensa de funciones curva</b> que describen todas las trayectorias posibles en el tiempo, a menos que fijemos una constante basada en un Problema de Valor Inicial ($K(0) = K_0$).
        </p>
    </div>
</div>

<!-- Relearning: Aplicacion Solow -->
<div class="mb-12">
    <h2 class="text-xs font-black text-cyan-400 uppercase tracking-[0.2em] border-b border-cyan-500/20 pb-4 mb-8">Paso 3: Modelo Dinámico de Crecimiento</h2>

    <div class="bg-indigo-900/20 border border-indigo-500/20 rounded-2xl p-6 md:p-8">
        <h3 class="text-lg font-bold text-white mb-4">El Motor de Crecimiento de Solow</h3>
        <p class="text-slate-300 mb-6">
            Define la regla de acumulación de stock de capital por trabajador, base fundacional de la macroeconomía moderna de largo plazo.
        </p>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center mb-8">
            <div class="space-y-4 font-mono text-sm text-slate-400">
                <p>1. Inversión bruta: <span class="text-white">$s \cdot f(k)$</span></p>
                <p>2. Depreciación total del trabajador: <span class="text-white">$(n + \delta) \cdot k$</span></p>
                
                <div class="p-4 bg-black/40 rounded-lg border border-white/5">
                    <span class="text-indigo-400">$$ \dot{k} = s f(k) - (n + \delta) k $$</span>
                </div>
            </div>

            <div class="bg-slate-800/80 p-5 rounded-xl border border-white/5">
                <p class="text-sm text-slate-300">
                    $\dot{k}$: Es la notación Newtoniana para la derivada temporal de $k$ ($dk/dt$). Indica el crecimiento neto del capital. El punto de "Estado Estacionario", el pilar de un país desarrollado, es matemáticamente aquel donde se paraliza la ecuación y la derivada se extingue: $\dot{k} = 0$.
                </p>
            </div>
        </div>
    </div>
</div>

</section>
