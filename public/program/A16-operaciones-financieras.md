<div class="max-w-4xl mx-auto p-8 bg-transparent shadow-2xl rounded-3xl border border-white/10 my-10 font-sans text-slate-200">
    <header class="mb-12 border-l-8 border-violet-600 pl-6 py-4 bg-violet-500/10 rounded-r-xl">
        <h1 class="text-4xl font-extrabold text-violet-300 tracking-tight">A16: Operaciones financieras</h1>
        <p class="text-lg text-violet-700 font-medium mt-2">Profesor Catedrático de Ingeniería Financiera</p>
    </header>

    <section class="mb-10 p-6 bg-slate-800/40 rounded-2xl border border-white/10">
        <h2 class="text-2xl font-bold text-white mb-4 flex items-center">
            <span class="bg-violet-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">1</span>
            Resumen Ejecutivo
        </h2>
        <p class="italic leading-relaxed">
            Esta asignatura domina el valor del dinero en el tiempo. Se analizan leyes financieras de capitalización y descuento, valoración de rentas constantes y variables, y los sistemas de amortización de préstamos fundamentales en el mercado financiero.
        </p>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-violet-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">2</span>
            Núcleo Teórico: Valoración Financiera
        </h2>
        <div class="prose prose-violet max-w-none">
            <p>
                Toda la ingeniería financiera se basa en la equivalencia de capitales. Comparamos flujos de caja en diferentes momentos del tiempo mediante el uso de <strong>leyes financieras</strong> (simples y compuestas).
            </p>
            <div class="my-8 p-6 bg-transparent border-2 border-dashed border-violet-500/30 rounded-xl">
                <p class="font-semibold text-violet-300 mb-2">Conceptos Clave:</p>
                <ul class="list-disc pl-6 space-y-2">
                    <li><strong>Capitalización Compuesta:</strong> Interés sobre interés, fundamental para el largo plazo.</li>
                    <li><strong>Valoración de Rentas:</strong> Series de pagos (periódicos, perpetuos, diferidos).</li>
                    <li><strong>TAE (Tasa Anual Equivalente):</strong> El estándar real para comparar el coste de las operaciones.</li>
                </ul>
            </div>
            
            <p>
                Los <strong>sistemas de amortización</strong> (Francés, Americano) permiten estructurar la devolución de capital e intereses en préstamos bancarios y emisiones de deuda, cada uno con perfiles de riesgo y liquidez distintos.
            </p>
        </div>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-violet-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">3</span>
            Desarrollo Matemático: Rentas y Amortización
        </h2>
        <div class="bg-violet-950 text-violet-100 p-8 rounded-2xl shadow-inner font-mono overflow-x-auto mb-6 text-center">
            <p class="mb-4 text-violet-400"># Valor Actual de una Renta Constante</p>
            <div class="text-2xl">
                $$V_0 = a \cdot \frac{1 - (1+i)^{-n}}{i}$$
            </div>
            <p class="mt-8 mb-4 text-violet-400"># Cuota Sistema Francés</p>
            <div class="text-xl">
                $$C = P \cdot \frac{i}{1 - (1+i)^{-n}}$$
            </div>
        </div>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-violet-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">4</span>
            Operaciones a Corto Plazo y Mercados de Deuda
        </h2>
        <div class="bg-transparent border border-white/10 p-6 rounded-2xl shadow-sm">
            <p class="leading-relaxed">
                Estudiamos herramientas de liquidez como el <strong>descuento de efectos comerciales</strong>, letras del tesoro y cuentas de crédito. La gestión eficiente del circulante es vital para la supervivencia operativa de cualquier entidad económica.
            </p>
        </div>
    </section>

    <section class="mb-10">
        <h2 class="text-2xl font-bold text-white mb-6 flex items-center">
            <span class="bg-violet-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">5</span>
            Conexión Interdisciplinaria
        </h2>
        <div class="p-6 bg-gradient-to-br from-violet-600 to-indigo-800 rounded-2xl text-white">
            <p class="font-medium">
                ¿Cómo se vincula esto con <strong>A31: Análisis de las decisiones de inversión</strong>?
            </p>
            <p class="mt-2 text-violet-100 opacity-90">
                Las fórmulas de valoración de rentas son el motor del VAN (Valor Actual Neto) y la TIR (Tasa Interna de Retorno) que utilizarás en A31 para decidir si un proyecto es rentable o debe descartarse.
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
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo A16</h3>
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
