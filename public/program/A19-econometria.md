<div class="max-w-4xl mx-auto p-8 bg-transparent shadow-2xl rounded-3xl border border-white/10 my-10 font-sans text-slate-200">
    <header class="mb-12 border-l-8 border-indigo-700 pl-6 py-4 bg-indigo-500/10 rounded-r-xl">
        <h1 class="text-4xl font-extrabold text-indigo-300 tracking-tight">A19: Econometría</h1>
        <p class="text-lg text-indigo-300 font-medium mt-2">Profesor Catedrático de Análisis Empírico</p>
    </header>

    <section class="mb-10 p-6 bg-slate-800/40 rounded-2xl border border-white/10">
        <h2 class="text-2xl font-bold text-white mb-4 flex items-center">
            <span class="bg-indigo-700 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">1</span>
            Resumen Ejecutivo
        </h2>
        <p class="italic leading-relaxed">
            La econometría une la teoría económica, la matemática y la estadística. Esta asignatura se centra en el Modelo de Regresión Lineal Múltiple, la validación de sus supuestos clásicos, y el tratamiento de problemas como la heterocedasticidad y la autocorrelación en datos económicos reales.
        </p>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-indigo-700 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">2</span>
            Núcleo Teórico: Mínimos Cuadrados Ordinarios (MCO)
        </h2>
        <div class="prose prose-indigo max-w-none">
            <p>
                El estimador de <strong>Mínimos Cuadrados Ordinarios (MCO)</strong> es el corazón de la econometría. Busca encontrar los coeficientes $\beta$ que minimizan la suma de los residuos al cuadrado, proporcionando la "mejor" línea de ajuste para los datos observados bajo los supuestos de Gauss-Markov.
            </p>
            <div class="my-8 p-6 bg-transparent border-2 border-dashed border-indigo-500/30 rounded-xl">
                <p class="font-semibold text-indigo-300 mb-2">Propiedades del Estimador:</p>
                <ul class="list-disc pl-6 space-y-2">
                    <li><strong>Insesgadez:</strong> En promedio, recuperamos el parámetro real.</li>
                    <li><strong>Eficiencia:</strong> Es el estimador con la varianza mínima entre todos los lineales e insesgados.</li>
                    <li><strong>Consistencia:</strong> Al aumentar el tamaño de la muestra, el estimador converge al valor real.</li>
                </ul>
            </div>
            
            <div class="flex justify-center my-10 bg-gray-500/10 py-20 rounded-2xl relative overflow-hidden">
                <span class="text-slate-500 font-mono">[Image of Regression Cloud with Residual Lines (Vertical Errors)]</span>
                <div class="absolute bottom-4 right-4 bg-transparent/80 px-3 py-1 rounded-full text-xs text-gray-500">Visual Designer Placeholder (T-3)</div>
            </div>
        </div>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-indigo-700 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">3</span>
            Desarrollo Matemático: Especificación Matricial
        </h2>
        <div class="bg-indigo-950 text-indigo-100 p-8 rounded-2xl shadow-inner font-mono overflow-x-auto mb-6">
            <p class="mb-4 text-indigo-400"># El Modelo Matricial</p>
            <div class="text-xl">
                $$Y = X\beta + \epsilon$$
            </div>
            <p class="mt-8 mb-4 text-indigo-400"># El Estimador MCO ($\hat{\beta}$)</p>
            <div class="text-xl">
                $$\hat{\beta} = (X'X)^{-1}X'Y$$
            </div>
        </div>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-indigo-700 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">4</span>
            Aplicación Práctica: Función de Salarios (Mincer)
        </h2>
        <div class="bg-transparent border border-white/10 p-6 rounded-2xl shadow-sm">
            <p class="mb-4 leading-relaxed">
                Utilizando datos de la <strong>Encuesta CASEN (Chile)</strong>, podemos estimar el retorno de la educación:
            </p>
            <div class="bg-slate-800/40 p-4 rounded-lg font-mono text-sm border border-white/10">
                reg log_ingreso educacion experiencia genero
            </div>
            <p class="mt-4">
                El coeficiente de 'educacion' nos indica el incremento porcentual esperado en el ingreso por cada año adicional de estudio, manteniendo las demás variables constantes (Ceteris Paribus).
            </p>
        </div>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-indigo-700 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">5</span>
            Conexión Interdisciplinaria
        </h2>
        <div class="p-6 bg-gradient-to-br from-indigo-700 to-indigo-900 rounded-2xl text-white">
            <p class="font-medium">
                ¿Cómo se vincula esto con <strong>A26: Estadística II</strong>?
            </p>
            <p class="mt-2 text-indigo-100 opacity-90">
                Mientras que aquí nos enfocamos en el modelado de relaciones estructurales, en Estadística II aprenderás los fundamentos de la inferencia asintótica y los métodos bayesianos que permiten expandir estas herramientas a modelos no lineales.
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
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo A19</h3>
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


    </div>
</div>
