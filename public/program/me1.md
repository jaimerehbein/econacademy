<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-violet-500 rounded-full"></div>
        <span class="text-violet-400 font-black text-[10px] uppercase tracking-[0.4em]">ME1 · Módulo Fundamental</span>
    </div>
    <h1 class="text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8">
        OPTIMIZACIÓN<br/>ESTÁTICA
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-violet-500/15 text-violet-300 border border-violet-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Cálculo Variacional</span>
        <span class="bg-cyan-500/15 text-cyan-300 border border-cyan-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Kuhn-Tucker</span>
    </div>
</header>

<!-- INTRO -->
<p class="text-slate-300 text-lg leading-relaxed mb-16">
    Toda decisión económica es, en esencia, un problema de optimización bajo restricciones. Este módulo establece el rigor matemático necesario para analizar la conducta del consumidor y la firma, utilizando las herramientas de cálculo multivariado avanzado.
</p>

<!-- TAXONOMY (WIKIPEDIA ENRICHMENT) -->
<section class="mb-24 grid grid-cols-1 md:grid-cols-2 gap-8">
    <div class="p-8 bg-white/5 border border-white/10 rounded-3xl">
        <h4 class="text-violet-400 font-black text-[9px] uppercase tracking-widest mb-4">Economía Positiva vs. Normativa</h4>
        <p class="text-white text-xs leading-relaxed mb-4">
            Los modelos <strong>descriptivos</strong> explican "lo que es" (basados en hechos), mientras que los <strong>normativos</strong> o directivos proponen "lo que debería ser" (basados en juicios de valor).
        </p>
    </div>
    <div class="p-8 bg-white/5 border border-white/10 rounded-3xl">
        <h4 class="text-cyan-400 font-black text-[9px] uppercase tracking-widest mb-4">Conceptuales vs. Matemáticos</h4>
        <p class="text-white text-xs leading-relaxed mb-4">
            La distinción entre marcos lógicos cualitativos y la formalización rigurosa mediante ecuaciones deterministas o estocásticas.
        </p>
    </div>
</section>

<!-- SECTION 1 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-violet-500 font-mono text-xs">[01]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">El Método de Lagrange</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed">
        <p>
            Para maximizar una función $f(x)$ sujeta a $g(x) = c$, introducimos el multiplicador $\lambda$ que representa el <strong>valor sombra</strong> de la restricción.
        </p>
        <div class="bg-white/5 border border-white/10 rounded-3xl p-10 font-mono text-white text-center text-xl md:text-3xl">
            $\mathcal{L}(x, \lambda) = f(x) + \lambda [c - g(x)]$
        </div>
        <p class="text-xs text-slate-500 uppercase tracking-widest text-center mt-4 font-bold">Primer Orden: $\nabla \mathcal{L} = 0$</p>
    </div>
</section>

<!-- SECTION 2 (KUHN-TUCKER) -->
<section class="mb-24 p-12 bg-violet-600/5 border border-violet-500/10 rounded-[3rem]">
    <h4 class="text-violet-500 font-black text-[10px] uppercase tracking-[0.4em] mb-8 uppercase">Optimización con Desigualdades</h4>
    <h3 class="text-white text-3xl font-black tracking-tighter mb-6">Condiciones de Kuhn-Tucker</h3>
    <p class="text-slate-400 text-sm leading-relaxed mb-8">
        Cuando las restricciones son del tipo $g(x) \leq c$, el multiplicador debe satisfacer la condición de <strong>holgura complementaria</strong>:
    </p>
    <div class="bg-black/40 p-8 rounded-2xl border border-white/5 space-y-4">
        <div class="flex items-center gap-4">
            <span class="w-1.5 h-1.5 bg-cyan-400 rounded-full"></span>
            <p class="text-white text-xs font-mono">$\lambda \geq 0$</p>
        </div>
        <div class="flex items-center gap-4">
            <span class="w-1.5 h-1.5 bg-cyan-400 rounded-full"></span>
            <p class="text-white text-xs font-mono">$\lambda [c - g(x)] = 0$</p>
        </div>
    </div>
</section>

<!-- SECTION 3 (DUALIDAD) -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-violet-500 font-mono text-xs">[02]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Dualidad y Valor Sombra</h2>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="p-8 border border-white/10 rounded-3xl">
            <h5 class="text-violet-400 font-black text-[10px] uppercase mb-4 tracking-widest uppercase">Primal</h5>
            <p class="text-white text-sm font-bold leading-tight">Maximización de la Utilidad sujeta al Presupuesto.</p>
        </div>
        <div class="p-8 border border-white/10 rounded-3xl bg-white/5">
            <h5 class="text-cyan-400 font-black text-[10px] uppercase mb-4 tracking-widest uppercase">Dual</h5>
            <p class="text-white text-sm font-bold leading-tight">Minimización del Gasto sujeta a un Nivel de Utilidad.</p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Optimización Estática ME1</p>
</footer>

</div>
