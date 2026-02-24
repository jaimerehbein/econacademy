<div class="max-w-4xl mx-auto p-8 bg-transparent shadow-2xl rounded-3xl border border-white/10 my-10 font-sans text-slate-200">
    <header class="mb-12 border-l-8 border-violet-700 pl-6 py-4 bg-violet-500/10 rounded-r-xl">
        <h1 class="text-4xl font-extrabold text-violet-300 tracking-tight">A26: Estadística II</h1>
        <p class="text-lg text-violet-300 font-medium mt-2">Profesor Catedrático de Métodos Cuantitativos</p>
    </header>

    <section class="mb-10 p-6 bg-slate-800/40 rounded-2xl border border-white/10">
        <h2 class="text-2xl font-bold text-white mb-4 flex items-center">
            <span class="bg-violet-700 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">1</span>
            Resumen Ejecutivo
        </h2>
        <p class="italic leading-relaxed">
            Esta asignatura profundiza en la inferencia estadística y el modelado econométrico avanzado. Se cubren desde modelos de probabilidad y estimación puntual hasta contrastes de hipótesis no paramétricos y el modelo de regresión lineal múltiple, utilizando el software estadístico R como herramienta principal.
        </p>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-violet-700 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">2</span>
            Núcleo Teórico: Inferencia y Modelos
        </h2>
        <div class="prose prose-violet max-w-none">
            <p>
                La <strong>Inferencia Estadística</strong> nos permite extraer conclusiones sobre una población a partir de una muestra. Estudiamos los estimadores, sus propiedades (ausencia de sesgo, eficiencia) y la construcción de intervalos de confianza mediante métodos clásicos y técnicas modernas como el <strong>Bootstrap</strong>.
            </p>
            <div class="my-8 p-6 bg-transparent border-2 border-dashed border-violet-500/30 rounded-xl">
                <p class="font-semibold text-violet-300 mb-2">Instrumentos de Contraste:</p>
                <ul class="list-disc pl-6 space-y-2">
                    <li><strong>Prueba de Jarque-Bera:</strong> Contraste fundamental de normalidad.</li>
                    <li><strong>Bondad de Ajuste Chi-cuadrado:</strong> Verificación de distribuciones.</li>
                    <li><strong>ANOVA:</strong> Análisis de varianza para la significatividad global del modelo.</li>
                </ul>
            </div>
        </div>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-violet-700 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">3</span>
            Desarrollo Matemático: Regresión Múltiple
        </h2>
        <div class="bg-violet-950 text-violet-100 p-8 rounded-2xl shadow-inner font-mono overflow-x-auto mb-6">
            <p class="mb-4 text-violet-400"># Modelo de Regresión Lineal Múltiple</p>
            <div class="text-xl text-center">
                $$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_k X_k + \epsilon$$
            </div>
            <p class="mt-8 mb-4 text-violet-400"># Estimación MCO (Mínimos Cuadrados Ordinarios)</p>
            <div class="text-lg text-center">
                $$\hat{\beta} = (X'X)^{-1} X'Y$$
            </div>
        </div>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-violet-700 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">4</span>
            Análisis de Datos con R y Computación
        </h2>
        <div class="bg-transparent border border-white/10 p-6 rounded-2xl shadow-sm">
            <p class="leading-relaxed">
                El dominio del software <strong>R Commander</strong> y el lenguaje R es esencial para el economista moderno. Analizamos cómo realizar predicciones y aplicaciones para las Tecnologías de Información (TIC), gestionando errores de multicolinealidad y heterocedasticidad en grandes bases de datos.
            </p>
        </div>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-violet-700 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">5</span>
            Conexión Interdisciplinaria
        </h2>
        <div class="p-6 bg-gradient-to-br from-violet-600 to-indigo-900 rounded-2xl text-white">
            <p class="font-medium">
                ¿Cómo se vincula esto con <strong>A19: Econometría</strong>?
            </p>
            <p class="mt-2 text-violet-100 opacity-90">
                Esta asignatura provee la infraestructura estadística necesaria para la econometría. Los modelos de probabilidad y regresión que perfeccionas aquí son las herramientas que luego utilizarás en A19 para validar teorías económicas con datos reales y rigor científico.
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
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo A26</h3>
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
