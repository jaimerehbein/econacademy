<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-emerald-500 rounded-full"></div>
        <span class="text-emerald-400 font-black text-[10px] uppercase tracking-[0.4em]">IF7 · Estructura Temporal</span>
    </div>
    <h1 class="text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8">
        RENTA FIJA Y<br/>VOLATILIDAD
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-emerald-500/15 text-emerald-300 border border-emerald-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">HJM / BGM</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Hull-White · Vega</span>
    </div>
</header>

<!-- SECTION 1 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[01]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Modelado de la Curva</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed mb-12">
        <p>
            A diferencia de los modelos de tasa corta simples, los modelos de <strong>Estructura Temporal</strong> como HJM (Heath-Jarrow-Merton) modelan la evolución de toda la curva de tasas forward instantáneas, garantizando la consistencia con los precios de mercado iniciales.
        </p>
    </div>

    <!-- MERMAID DIAGRAM -->
    <div class="bg-white/5 p-8 rounded-3xl border border-white/10 mb-12 overflow-hidden">
        <pre class="mermaid bg-transparent flex justify-center">
graph LR
    CurvaT0[Curva Inicial t=0] --> Drift[Componente de Deriva]
    CurvaT0 --> Vol[Volatilidad Forward]
    Drift --> Stochastic{Evolución HJM}
    Vol --> Stochastic
    Stochastic --> CurvaT1[Nueva Curva t=1]
    
    style CurvaT0 fill:#064e3b,stroke:#10b981,color:#fff
    style CurvaT1 fill:#064e3b,stroke:#10b981,color:#fff
    style Stochastic fill:#1e293b,stroke:#94a3b8,color:#fff
    style Drift fill:#064e3b,stroke:#059669,color:#fff
    style Vol fill:#064e3b,stroke:#059669,color:#fff
        </pre>
        <p class="text-center text-slate-500 text-[9px] uppercase tracking-widest mt-6 italic font-mono">Evolución de la Estructura Temporal bajo HJM</p>
    </div>

    <!-- MODEL COMPARISON -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">
        <div class="p-8 bg-white/5 border border-white/10 rounded-3xl">
            <h4 class="text-white font-bold mb-4 uppercase text-xs tracking-widest text-emerald-500">HJM Model</h4>
            <p class="text-slate-400 text-sm leading-relaxed">
                Marco general para tasas forward instantáneas. Consistente pero complejo de implementar numéricamente.
            </p>
        </div>
        <div class="p-8 bg-white/5 border border-white/10 rounded-3xl">
            <h4 class="text-white font-bold mb-4 uppercase text-xs tracking-widest text-emerald-500">BGM / Libor Market</h4>
            <p class="text-slate-400 text-sm leading-relaxed">
                Modela tasas forward discretas y observables (Libor). Estándar para valorar Caps y Swaptions.
            </p>
        </div>
    </div>
</section>

<!-- SECTION 2 -->
<section class="mb-24 px-12 py-16 bg-white/5 border border-white/10 rounded-[3.5rem]">
    <div class="flex items-center gap-3 mb-10 text-center justify-center">
        <span class="text-emerald-500 font-mono text-sm uppercase">Reversión a la Media</span>
        <h2 class="text-white text-3xl font-black tracking-tighter uppercase tracking-[0.1em]">Modelo Hull-White</h2>
    </div>
    <p class="text-slate-300 text-sm leading-relaxed mb-10 text-center">
        Extiende el modelo de Vasicek permitiendo que los parámetros sean funciones del tiempo para ajustar perfectamente la curva de rendimiento actual. Es el modelo preferido para la valoración de Bermudan Swaptions y productos de cancelación anticipada.
    </p>
    <div class="p-8 border border-emerald-500/20 bg-emerald-500/5 rounded-3xl text-center font-mono">
        <div class="text-emerald-400 text-lg mb-2">$$dr_t = [\theta(t) - a r_t] dt + \sigma dW_t$$</div>
        <p class="text-slate-500 text-[10px]">La función $\theta(t)$ captura la estructura temporal de tasas hoy.</p>
    </div>
</section>

<!-- SECTION 3 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-emerald-500 font-mono text-xs">[03]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Ingeniería de la Volatilidad</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed mb-12">
        <p>
            Los <strong>Swaps de Volatilidad</strong> permiten a los inversores negociar volatilidad pura sin exposición direccional (Delta). El pago depende de la diferencia entre la volatilidad realizada y el strike.
        </p>
    </div>

    <!-- FORMULA BOX -->
    <div class="px-8 py-12 bg-white/5 border border-white/10 rounded-[3rem] text-center mb-12">
        <div class="text-[10px] font-black text-emerald-500 uppercase tracking-widest mb-6 font-mono">Pago Vol Swap</div>
        <div class="text-white text-3xl font-mono mb-6">
            $$\text{Pago} = N \times (\sigma_{realizada} - \sigma_{strike})$$
        </div>
    </div>
    
    <div class="p-8 bg-emerald-900/5 border border-emerald-500/10 rounded-3xl">
        <h5 class="text-emerald-400 font-black text-[9px] uppercase tracking-widest mb-3 italic">Volatility Surface</h5>
        <p class="text-slate-500 text-xs">Ajuste de la superficie de volatilidad mediante modelos de volatilidad estocástica (Heston) para capturar el skew y el smile presentes en las opciones de renta fija.</p>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Ingenieria Financiera IF7</p>
</footer>

</div>
