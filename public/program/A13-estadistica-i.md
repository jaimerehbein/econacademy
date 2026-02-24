<div class="max-w-4xl mx-auto p-8 bg-transparent shadow-2xl rounded-3xl border border-white/10 my-10 font-sans text-slate-200">
    <header class="mb-12 border-l-8 border-orange-600 pl-6 py-4 bg-orange-500/10 rounded-r-xl">
        <h1 class="text-4xl font-extrabold text-orange-300 tracking-tight">A13: Estadística I</h1>
        <p class="text-lg text-orange-700 font-medium mt-2">Profesor Catedrático de Métodos Estadísticos</p>
    </header>

    <section class="mb-10 p-6 bg-slate-800/40 rounded-2xl border border-white/10">
        <h2 class="text-2xl font-bold text-white mb-4 flex items-center">
            <span class="bg-orange-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">1</span>
            Resumen Ejecutivo
        </h2>
        <p class="italic leading-relaxed">
            Esta asignatura introduce las herramientas fundamentales para el análisis de datos. Se estudian medidas de tendencia central y dispersión, el análisis bivariante, series temporales, números índices y los fundamentos de la teoría de probabilidad y variables aleatorias.
        </p>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-orange-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">2</span>
            Núcleo Teórico: Análisis de Datos y Probabilidad
        </h2>
        <div class="prose prose-orange max-w-none">
            <p>
                La estadística es la ciencia de aprender de los datos. En una primera etapa, el <strong>análisis descriptivo</strong> nos permite resumir grandes volúmenes de información mediante indicadores clave y representaciones gráficas como los diagramas de caja (boxplots) para identificar valores atípicos.
            </p>
            <div class="my-8 p-6 bg-transparent border-2 border-dashed border-orange-500/30 rounded-xl">
                <p class="font-semibold text-orange-300 mb-2">Conceptos Clave:</p>
                <ul class="list-disc pl-6 space-y-2">
                    <li><strong>Medidas de Centralización:</strong> Media, mediana y moda.</li>
                    <li><strong>Medidas de Dispersión:</strong> Varianza, desviación estándar y coeficiente de variación.</li>
                    <li><strong>Distribución Normal:</strong> El modelo de probabilidad fundamental ($\mu, \sigma$).</li>
                </ul>
            </div>
            
            <div class="flex justify-center my-10 bg-gray-500/10 py-20 rounded-2xl relative overflow-hidden">
                <span class="text-slate-500 font-mono">[Image of Normal Distribution Bell Curve with Confidence Intervals]</span>
                <div class="absolute bottom-4 right-4 bg-transparent/80 px-3 py-1 rounded-full text-xs text-gray-500">Visual Designer Placeholder (T-3)</div>
            </div>
        </div>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-orange-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">3</span>
            Desarrollo Matemático: Varianza y Probabilidad
        </h2>
        <div class="bg-orange-900 text-orange-100 p-8 rounded-2xl shadow-inner font-mono overflow-x-auto mb-6 text-center">
            <p class="mb-4 text-orange-400"># Cálculo de la Varianza Poblacional</p>
            <div class="text-2xl">
                $$\sigma^2 = \frac{\sum (x_i - \mu)^2}{N}$$
            </div>
            <p class="mt-8 mb-4 text-orange-400"># Esperanza Matemática de una V.A. Discreta</p>
            <div class="text-xl">
                $$E[X] = \sum x_i P(x_i)$$
            </div>
        </div>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-orange-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">4</span>
            Aplicación Económica: Números Índices e IPC
        </h2>
        <div class="bg-transparent border border-white/10 p-6 rounded-2xl shadow-sm">
            <p class="mb-4 leading-relaxed">
                El Índice de Precios al Consumidor (<strong>IPC</strong>) es un número índice que mide la variación de los precios de una canasta de bienes. Es fundamental para deflactar series temporales y calcular el crecimiento real de la economía en comparación con el nominal.
            </p>
            <blockquote class="italic text-sm text-gray-600 border-l-4 border-orange-500/30 pl-4 py-2">
                "Deflactar es el proceso de convertir valores nominales (precios corrientes) a valores reales (precios constantes)."
            </blockquote>
        </div>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-orange-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">5</span>
            Conexión Interdisciplinaria
        </h2>
        <div class="p-6 bg-gradient-to-br from-orange-500 to-red-600 rounded-2xl text-white">
            <p class="font-medium">
                ¿Cómo se vincula esto con <strong>A19: Econometría</strong>?
            </p>
            <p class="mt-2 text-orange-100 opacity-90">
                La econometría comienza donde termina la estadística clásica. Los test de hipótesis (Z, t-Student, Chi-cuadrado) que aprendas aquí son la base para validar la significancia de los parámetros en los modelos de regresión del futuro.
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
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo A13</h3>
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
