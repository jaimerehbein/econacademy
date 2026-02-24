<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-violet-500 rounded-full"></div>
        <span class="text-violet-400 font-black text-[10px] uppercase tracking-[0.4em]">ME7 · Módulo Dinámico-Estocástico</span>
    </div>
    <h1 class="text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8">
        MODELADO<br/>ESTOCÁSTICO
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-violet-500/15 text-violet-300 border border-violet-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Monte Carlo</span>
        <span class="bg-cyan-500/15 text-cyan-300 border border-cyan-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Agent-Based</span>
    </div>
</header>

<!-- INTRO -->
<p class="text-slate-300 text-lg leading-relaxed mb-16">
    El mundo real está lleno de azar. Este módulo final aborda la complejidad emergente a través de la simulación de agentes heterogéneos y el uso de métodos numéricos para resolver modelos que no tienen solución analítica cerrada.
</p>

<!-- SECTION 1 -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-violet-500 font-mono text-xs">[01]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter text-balance">Modelos de Agentes (ABM)</h2>
    </div>
    
    <div class="space-y-6 text-slate-400 leading-relaxed">
        <p>
            A diferencia de los modelos basados en el "agente representativo", los ABM simulan miles de agentes con reglas de comportamiento locales e interacciones directas, observando cómo emerge el fenómeno macro (ej. crisis, segregación).
        </p>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 my-10">
            <div class="p-6 border border-white/10 rounded-2xl bg-white/5">
                <h5 class="text-violet-400 font-black text-[8px] uppercase tracking-widest mb-3">Heterogeneidad</h5>
                <p class="text-white text-[10px] font-bold">Diferentes niveles de riqueza, información y racionalidad.</p>
            </div>
            <div class="p-6 border border-white/10 rounded-2xl bg-white/5">
                <h5 class="text-violet-400 font-black text-[8px] uppercase tracking-widest mb-3">Interacción</h5>
                <p class="text-white text-[10px] font-bold">Aprendizaje social e imitación de conductas exitosas.</p>
            </div>
            <div class="p-6 border border-white/10 rounded-2xl bg-white/5">
                <h5 class="text-violet-400 font-black text-[8px] uppercase tracking-widest mb-3">Emergencia</h5>
                <p class="text-white text-[10px] font-bold">Patrones macro no predecibles sumando las partes.</p>
            </div>
        </div>
    </div>
</section>

<!-- SECTION 2 (NUMERICAL METHODS) -->
<section class="mb-24 p-12 bg-white/5 border border-white/10 rounded-[3rem]">
    <h4 class="text-violet-500 font-black text-[10px] uppercase tracking-[0.4em] mb-10 text-center uppercase">Métodos Numéricos</h4>
    <div class="flex flex-col md:flex-row gap-12 items-center">
        <div class="flex-1 space-y-6">
            <h3 class="text-white text-3xl font-black tracking-tighter">Monte Carlo & Cadenas de Markov</h3>
            <p class="text-slate-400 text-sm leading-relaxed">
                Utilizamos simulaciones masivas de caminos aleatorios para estimar distribuciones de probabilidad complejas, fundamentales en la economía financiera y la gestión de riesgos.
            </p>
            <div class="font-mono text-cyan-400 text-sm p-4 bg-black/40 rounded-xl">
                E[f(X)] \approx \frac{1}{N} \sum_{i=1}^N f(x_i)
            </div>
        </div>
        <div class="w-48 h-48 bg-violet-500/20 rounded-full border border-violet-500/30 flex items-center justify-center relative">
            <div class="absolute inset-0 flex items-center justify-center opacity-30">
                <div class="w-32 h-32 border-2 border-dashed border-cyan-500 rounded-full animate-spin-slow"></div>
            </div>
            <span class="text-white font-black text-sm uppercase tracking-widest">Simulación</span>
        </div>
    </div>
</section>

<!-- GLOSARIO -->
<section class="mb-24">
    <div class="flex items-center gap-3 mb-10">
        <span class="text-purple-500 font-mono text-xs">[GL]</span>
        <h2 class="text-white font-black text-2xl uppercase tracking-tighter">Glosario de Modelos Económicos</h2>
    </div>
    <div class="space-y-3">
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-purple-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Convergencia Asintótica</span>
            <p class="text-slate-400 text-sm leading-relaxed">Mandamiento dinámico destino gravitacional y órbita inevitable de resoluciones donde la órbita variable en zozobra, turbulencia transicional colosal inestable fútil asimétrica o tránsitos erráticos inescrutables de desviaciones tras choques abismales se va sosegando pacificando frenando inyectivamente declinando ex-post sus fuerzas motrices residuales percutiendo mermando y acercando empíricamente ineludible y arrastrada lenta agónica ineluctantemente infinitamente a su ancla clímax reposo final y tumba estéril inmovilizada originaria estado estacionario perpetuable.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-purple-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Punto de Silla (Saddle Point)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Encrucijada letal filo de navaja inestable e instable inescrutable estandar o topografía matemática y encrucijada extrema de dinámica inestable condicional macroeconómica. Si y excluyentemente sólo si la pre-implantación e inyección premonitoria traccional del resolutivamente asimétrico decisor ubica empíricamente e inmaculado al vector variable exacto ciego predeterminado asintótico infalible en la senda estable del riel del lomo ensillado cabalgado dictaminador, predecirá empírica infalible y decantará estancantemente inmutable directo rauda inexorable a la convergencia pacífica redentora vaciadora, o de fallar un suspiro ínfimo marginal aberrante asimétrico errático mínimo pífido milimétrico inicial originario inestable abismal resbalador precipitará eclosionador eyectivo indomeñable apocalíptico fugador trágico expulsor e irreversible inestabillizador detonante divergente abismal explosivo destructor fatal fútil perdedor infinito.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-purple-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Inconsistencia Dinámica</span>
            <p class="text-slate-400 text-sm leading-relaxed">Tragedia praxeológica deslegitimadora trampa subyugante asoladora institucional asfixiante abismal donde el plan de ruta anuncio edicto o manifiesto proferido u optado óptimo inmaculado y solemne y redentor que el soberano prometía dogmático salvacionista férreo dictaminador inviolable incondicionado en el alba $t=0$, al mutar transmutarse el inescrutable mañana asintótico rodando inexorable el reloj cronológico claudicante cediendo efímero a $t=1$, caduca y se le transmuta trágico mutando y tornándose insoportable fútil ruinosa o tentadora prebendarla estigmatizantemente inferior sub-óptima induciendo irresistible fatal corroyente a traicionarse arrepentirse desertar dimitir o auto-defectando pergeñar mutando unilateral asimétricamente asimilador y cambiar oportunista fútilmente la veredita proferida preestablecida claudicándola rompiéndose la magia fiduciaria vaciando credibilidad evaporándola exuda reputación cínica estigmatizante desfondada de anclas promisotrias credenciales pre-fijadoras normativas basales dictaminadas originarias nulas.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-purple-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Efecto de Contagio</span>
            <p class="text-slate-400 text-sm leading-relaxed">Diseminación epidémica pánico pírrico histeria cruzada esparcimiento irracional pavoroso red ignífuga deflagración sísmica paralizadora devaluadora sistémica o derrumbe estigmatizante inorgánica colosal de dominó de un centroide epicentro originario exótico en quiebres fútiles letales que gangrena infecta atemorizando indiscriminada ciegamente arrastrando e insolventando carcomiendo las trincheras plazos de deudores blindajes inoperantes o resguardos fiduciarios preexistentes fronterizos lejanos de países vecinos y plazas desvinculadas pre-sanas ajenas infectándose irremediablemente eclosionadas destartallante por fuga instintiva estampida ciega asintomática sin purificar escrutar puros dictámenes subyacentes o fundamentos de escollos y falencias sistémicas simbióticas asfixiantes irracionales y puritanamente histéricas contagiosas ciegamente asimiladas inescrutables asimétricas devoradoras absolutas catastróficas de letal rebaño manada global y terror bursátil irracional abarcativo sinfónico destructor abismador imparable.</p>
        </div>
        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-purple-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">Modelos de Agentes Heterogéneos (HANK)</span>
            <p class="text-slate-400 text-sm leading-relaxed">Cisma revulsivo vanguardista inorgánico redentor neokeynesiano fracturando e incinerando la utopía irreal emparedada absolutista canónica inerte ciega inoperante castrante y limitante y castigadora del postulado fútil ciego o dogma reduccionista iluso e ineficiente abismal e incapaz y obsoleto o de ceguera paramétrica asimétrica del inútil agente representativo clon idéntico clónico estéril representate único. Estas sinfónicas laberínticas arquitecturas admiten, desglosan radiografían amalgaman la muchedumbre dispar abismal caótica asimétrica de ricos y desvalidos adinerados embaucados y paupérrimos desprovistos integrando a desempleados ilíquidos sin chequeras inescrutables contra acaparadores colosales asimétricos inversores exponenciales abismalmente desigualados captando e integrando rigurosa fáctica o insobornablemente las puras asimetrías de fortunas fútiles vulnerabilidades rentistas inmiscuyendo frívolamente o propensiones de choque letárgicas asimétricas distributivas que dislocan diametral empíricamente la asimilación arrastrada del consumo frente a disrupciones macropolíticas dictaminadas agregadas neutralizadoras dictadas esterilizadas ciegas asimilables letales.</p>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="pt-10 border-t border-white/10 text-center">
    <p class="text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">LiceCon Portal · Modelado Estocástico ME7</p>
</footer>

</div>
