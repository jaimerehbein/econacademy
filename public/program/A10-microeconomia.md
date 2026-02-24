<div class="max-w-4xl mx-auto p-8 bg-transparent shadow-2xl rounded-3xl border border-white/10 my-10 font-sans text-slate-200">
    <header class="mb-12 border-l-8 border-indigo-600 pl-6 py-4 bg-indigo-500/10 rounded-r-xl">
        <h1 class="text-4xl font-extrabold text-indigo-300 tracking-tight">A10: Microeconomía</h1>
        <p class="text-lg text-indigo-700 font-medium mt-2">Profesor Catedrático de Análisis Microeconómico</p>
    </header>

    <section class="mb-10 p-6 bg-slate-800/40 rounded-2xl border border-white/10">
        <h2 class="text-2xl font-bold text-white mb-4 flex items-center">
            <span class="bg-indigo-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">1</span>
            Resumen Ejecutivo
        </h2>
        <p class="italic leading-relaxed">
            Esta asignatura profundiza en el comportamiento de los agentes económicos individuales, la teoría de juegos, las estructuras de mercado oligopólicas y los fallos de mercado derivados de externalidades e información asimétrica.
        </p>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-indigo-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">2</span>
            Núcleo Teórico: Teoría de Juegos y Estrategia
        </h2>
        <div class="prose prose-indigo max-w-none">
            <p>
                La microeconomía moderna utiliza la <strong>Teoría de Juegos</strong> para modelar la interdependencia estratégica. En situaciones de oligopolio, las decisiones de una empresa (precio, producción) dependen de las expectativas sobre las reacciones de sus competidores.
            </p>
            <div class="my-8 p-6 bg-transparent border-2 border-dashed border-indigo-500/30 rounded-xl">
                <p class="font-semibold text-indigo-300 mb-2">Equilibrios y Modelos:</p>
                <ul class="list-disc pl-6 space-y-2">
                    <li><strong>Equilibrio de Nash:</strong> Situación donde ningún jugador tiene incentivos para cambiar su estrategia unilateralmente.</li>
                    <li><strong>Modelo de Cournot:</strong> Competencia por cantidades simultánea.</li>
                    <li><strong>Modelo de Stackelberg:</strong> Competencia secuencial con un líder y un seguidor.</li>
                </ul>
            </div>
            
            <div class="flex justify-center my-10 bg-gray-500/10 py-16 rounded-2xl relative overflow-hidden">
                <table class="table-auto border-collapse border border-white/10 bg-transparent shadow-sm">
                    <thead>
                        <tr class="bg-gray-200">
                            <th class="border p-2">Jugador A \ B</th>
                            <th class="border p-2">Cooperar</th>
                            <th class="border p-2">Traicionar</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="border p-2 font-bold">Cooperar</td>
                            <td class="border p-2 text-center">(3, 3)</td>
                            <td class="border p-2 text-center">(0, 5)</td>
                        </tr>
                        <tr>
                            <td class="border p-2 font-bold">Traicionar</td>
                            <td class="border p-2 text-center">(5, 0)</td>
                            <td class="border p-2 text-center bg-indigo-500/10 font-bold">(1, 1)</td>
                        </tr>
                    </tbody>
                </table>
                <div class="absolute bottom-4 right-4 bg-transparent/80 px-3 py-1 rounded-full text-xs text-gray-500">Dilema del Prisionero (Nash)</div>
            </div>
        </div>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-indigo-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">3</span>
            Desarrollo Matemático: Optimización del Consumidor
        </h2>
        <div class="bg-indigo-900 text-indigo-100 p-8 rounded-2xl shadow-inner font-mono overflow-x-auto mb-6">
            <p class="mb-4 text-indigo-300"># Problema de Maximización de la Utilidad</p>
            <div class="text-xl">
                $$\max U(x, y) \quad \text{s.t.} \quad P_x x + P_y y = I$$
            </div>
            <p class="mt-8 mb-4 text-indigo-300"># Condición de Primer Orden (Lagrange)</p>
            <div class="text-xl">
                $$RMS = \frac{UMg_x}{UMg_y} = \frac{P_x}{P_y}$$
            </div>
        </div>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-indigo-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">4</span>
            Fallos de Mercado e Información Asimétrica
        </h2>
        <div class="bg-transparent border border-white/10 p-6 rounded-2xl shadow-sm">
            <p class="mb-4 leading-relaxed">
                Analizamos por qué los mercados no siempre son eficientes. La <strong>selección adversa</strong> y el <strong>riesgo moral</strong> (Moral Hazard) son fenómenos críticos en los mercados de seguros y salud, donde una de las partes posee más información que la otra.
            </p>
        </div>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-indigo-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">5</span>
            Conexión Interdisciplinaria
        </h2>
        <div class="p-6 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-2xl text-white">
            <p class="font-medium">
                ¿Cómo se vincula esto con <strong>A15: Macroeconomía I</strong>?
            </p>
            <p class="mt-2 text-indigo-100 opacity-90">
                La macroeconomía moderna se basa en los <strong>microfundamentos</strong>. El comportamiento agregado del consumo o la inversión que estudiarás en Macro I parte de los modelos de elección intertemporal desarrollados en esta asignatura.
            </p>
        </div>
    </section>

    <footer class="mt-12 pt-8 border-t border-white/10 text-center text-slate-500 text-sm">
        &copy; 2026 Tech Institute | Licenciatura en Economía | Generado por Agente Académico O-3
    </footer>
</div>

<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">
        <span class="text-blue-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo A10</h3>
    </div>
    <div class="bg-black/30 p-2 md:p-6 rounded-2xl border border-white/5 overflow-x-auto">
        
        <pre class="mermaid bg-transparent flex justify-center">
graph LR
    A[Fundamentos Teóricos] --> B(Aplicación Práctica)
    B --> C{Análisis Crítico}
    C -->|Evaluación| D[Validación Empírica]
    C -->|Revisión| E[Ajuste de Modelo]
    
    classDef default fill:#111827,stroke:#3b82f6,stroke-width:1px,color:#d1d5db
    classDef decision fill:#1e3a8a,stroke:#3b82f6,stroke-width:2px,color:#fff
    class C decision
        </pre>
<!-- GLOSARIO -->

<!-- GLOSARIO v9.5 -->
<section id="glosario" class="mt-24 mb-16 relative">
    <div class="flex items-center gap-4 mb-10">
        <div class="w-1.5 h-8 bg-indigo-500 rounded-full shadow-[0_0_15px_rgba(var(--color-rgb),0.5)]"></div>
        <h2 class="text-2xl font-black text-white tracking-tight uppercase italic">Glosario Técnico</h2>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 relative z-10">

        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-indigo-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-indigo-500/5">
            <h3 class="text-sm font-black text-indigo-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-indigo-500 animate-pulse"></span>
                Microeconomía
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Rama de la ciencia económica que se ocupa del estudio del comportamiento de los agentes individuales y de la asignación de recursos escasos en mercados específicos a través del mecanismo de precios.
            </p>
        </div>

        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-indigo-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-indigo-500/5">
            <h3 class="text-sm font-black text-indigo-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-indigo-500 animate-pulse"></span>
                Teoría de Juegos
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Marco analítico formal utilizado para modelar la interdependencia estratégica entre agentes, donde el resultado para cada participante depende no solo de sus propias acciones, sino también de las decisiones de los demás.
            </p>
        </div>

        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-indigo-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-indigo-500/5">
            <h3 class="text-sm font-black text-indigo-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-indigo-500 animate-pulse"></span>
                Equilibrio de Nash
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Perfil de estrategias en el cual ningún jugador tiene incentivos para desviarse unilateralmente, dado que cada agente está maximizando su utilidad o beneficio en función de las estrategias adoptadas por el resto.
            </p>
        </div>

        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-indigo-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-indigo-500/5">
            <h3 class="text-sm font-black text-indigo-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-indigo-500 animate-pulse"></span>
                Oligopolio
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Estructura de mercado caracterizada por la presencia de un número reducido de oferentes con capacidad de influir en el precio, lo que genera una interdependencia mutua en la toma de decisiones estratégicas.
            </p>
        </div>

        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-indigo-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-indigo-500/5">
            <h3 class="text-sm font-black text-indigo-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-indigo-500 animate-pulse"></span>
                Modelo de Cournot
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Modelo de competencia oligopólica en el cual las empresas deciden simultáneamente la cantidad de producto que ofrecerán, asumiendo como dada la producción de sus competidores.
            </p>
        </div>

        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-indigo-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-indigo-500/5">
            <h3 class="text-sm font-black text-indigo-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-indigo-500 animate-pulse"></span>
                Modelo de Stackelberg
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Modelo de competencia estratégica secuencial donde una empresa actúa como líder, fijando su nivel de producción primero, mientras que la empresa seguidora optimiza su respuesta tras observar la decisión de la líder.
            </p>
        </div>

        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-indigo-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-indigo-500/5">
            <h3 class="text-sm font-black text-indigo-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-indigo-500 animate-pulse"></span>
                Relación Marginal de Sustitución (RMS)
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Tasa a la cual un consumidor está dispuesto a intercambiar un bien por otro manteniendo constante su nivel de utilidad; matemáticamente equivale al cociente de las utilidades marginales y a la pendiente de la curva de indiferencia.
            </p>
        </div>

        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-indigo-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-indigo-500/5">
            <h3 class="text-sm font-black text-indigo-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-indigo-500 animate-pulse"></span>
                Fallos de Mercado
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Situaciones en las que el mecanismo de mercado no logra una asignación eficiente de los recursos en el sentido de Pareto, frecuentemente debido a la presencia de externalidades, bienes públicos o información asimétrica.
            </p>
        </div>

        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-indigo-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-indigo-500/5">
            <h3 class="text-sm font-black text-indigo-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-indigo-500 animate-pulse"></span>
                Información Asimétrica
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Falla de mercado que ocurre cuando una de las partes involucradas en una transacción posee un conocimiento superior o privado sobre las características del bien o el comportamiento del agente, respecto a la otra parte.
            </p>
        </div>

        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-indigo-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-indigo-500/5">
            <h3 class="text-sm font-black text-indigo-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-indigo-500 animate-pulse"></span>
                Selección Adversa
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                Problema de información asimétrica previo a la contratación, donde la falta de observabilidad de la calidad de los bienes o el riesgo de los agentes provoca que los productos o individuos de 'baja calidad' desplacen a los de 'alta calidad'.
            </p>
        </div>

    </div>
</section>








    </div>
</div>
