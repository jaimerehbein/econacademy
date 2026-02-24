<div class="max-w-4xl mx-auto p-8 bg-transparent shadow-2xl rounded-3xl border border-white/10 my-10 font-sans text-slate-200">
    <header class="mb-12 border-l-8 border-violet-600 pl-6 py-4 bg-violet-500/10 rounded-r-xl">
        <h1 class="text-4xl font-extrabold text-violet-300 tracking-tight">A5: Matemáticas</h1>
        <p class="text-lg text-violet-700 font-medium mt-2">Profesor Catedrático de Análisis Matemático</p>
    </header>

    <section class="mb-10 p-6 bg-slate-800/40 rounded-2xl border border-white/10">
        <h2 class="text-2xl font-bold text-white mb-4 flex items-center">
            <span class="bg-violet-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">1</span>
            Resumen Ejecutivo
        </h2>
        <p class="italic leading-relaxed">
            Esta asignatura aborda las herramientas cuantitativas esenciales para la economía: álgebra lineal, cálculo diferencial de una y varias variables, e integración. Se profundiza en la optimización de funciones y el análisis de sistemas de ecuaciones.
        </p>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-violet-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">2</span>
            Núcleo Teórico: Álgebra Lineal y Matrices
        </h2>
        <div class="prose prose-violet max-w-none">
            <p>
                El estudio del espacio vectorial $\mathbb{R}^n$ y las operaciones matriciales permite modelar relaciones complejas entre múltiples variables económicas simultáneamente. La resolución de sistemas mediante la <strong>Regla de Cramer</strong> o la inversión matricial es el núcleo de muchos modelos econométricos.
            </p>
            <div class="my-8 p-6 bg-transparent border-2 border-dashed border-violet-500/30 rounded-xl">
                <p class="font-semibold text-violet-300 mb-2">Temas Clave:</p>
                <ul class="list-disc pl-6 space-y-2">
                    <li><strong>Matrices y Determinantes:</strong> Cálculo de inversas y propiedades de transposición.</li>
                    <li><strong>Sistemas de Ecuaciones:</strong> Teorema de Rouché-Frobenius para la discusión de sistemas.</li>
                    <li><strong>Cálculo Diferencial:</strong> Límites, continuidad y derivadas para el análisis de variaciones.</li>
                </ul>
            </div>
        </div>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-violet-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">3</span>
            Desarrollo Matemático: Optimización y Derivadas
        </h2>
        <div class="bg-violet-900 text-violet-100 p-8 rounded-2xl shadow-inner font-mono overflow-x-auto mb-6">
            <p class="mb-4 text-violet-300"># Definición de la Derivada</p>
            <div class="text-xl">
                $$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$
            </div>
            <p class="mt-8 mb-4 text-violet-300"># Inversión Matricial</p>
            <div class="text-xl">
                $$A^{-1} = \frac{1}{|A|} Adj(A)^T$$
            </div>
        </div>
        <div class="bg-amber-500/10 border-l-4 border-amber-400 p-6 rounded-r-xl">
            <h3 class="text-amber-300 font-bold mb-3 uppercase tracking-wider text-sm">Optimización: Teorema de Weierstrass</h3>
            <p class="text-amber-300">
                Asegura la existencia de máximos y mínimos absolutos para funciones continuas en conjuntos compactos, fundamental para la teoría del consumidor.
            </p>
        </div>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-violet-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">4</span>
            Aplicación Práctica: Elasticidades y Análisis Marginal
        </h2>
        <div class="bg-transparent border border-white/10 p-6 rounded-2xl shadow-sm">
            <p class="leading-relaxed">
                Mediante el uso de derivados, podemos calcular la elasticidad de una función de demanda o el costo marginal de una empresa. La integración permite luego recuperar funciones totales a partir de marginales (e.g., obtener la función de costo total integrando el costo marginal).
            </p>
            <div class="flex justify-center my-6 bg-gray-800/40 py-16 rounded-xl">
                <span class="text-slate-500 font-mono">[Image of 3D Surface for f(x,y) showing Saddle Points]</span>
            </div>
        </div>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-violet-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">5</span>
            Conexión Interdisciplinaria
        </h2>
        <div class="p-6 bg-gradient-to-br from-violet-500 to-indigo-600 rounded-2xl text-white">
            <p class="font-medium">
                ¿Cómo se vincula esto con <strong>A19: Econometría</strong>?
            </p>
            <p class="mt-2 text-violet-100 opacity-90">
                La econometría utiliza extensivamente el álgebra matricial presentada aquí para estimar coeficientes mediante Mínimos Cuadrados Ordinarios ($\hat{\beta} = (X'X)^{-1}X'Y$).
            </p>
        </div>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-violet-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">6</span>
            Autoevaluación
        </h2>
        <div class="space-y-6">
            <div class="p-5 border border-white/10 rounded-xl hover:bg-gray-800/40 transition-colors">
                <p class="font-bold">1. Si el determinante de una matriz es cero, la matriz es:</p>
                <ul class="mt-3 space-y-2 text-sm">
                    <li>A) Identidad.</li>
                    <li class="p-2 bg-green-500/10 border border-green-500/30 rounded text-green-300 font-medium">B) Singular (No invertible).</li>
                    <li>C) Ortogonal.</li>
                </ul>
            </div>
        </div>
    </section>

    <footer class="mt-12 pt-8 border-t border-white/10 text-center text-slate-500 text-sm">
        &copy; 2026 Tech Institute | Licenciatura en Economía | Generado por Agente Académico O-3
    </footer>
</div>

<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-blue-500 font-mono text-xs">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-xl">Esquema Conceptual Módulo A5</h3>
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

    </div>
</div>
