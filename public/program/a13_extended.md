# Guía de Estudio Académica: Estadística I

Esta guía ha sido elaborada siguiendo estrictamente el **Temario Oficial de Estadística I** proporcionado en las fuentes, cubriendo todos los niveles jerárquicos requeridos.

---

## 13.1. Introducción a la estadística

### 13.1.1. Conceptos básicos
La estadística se define como el estudio de los métodos empleados en la recolección, organización, resumen, análisis e interpretación de datos [1]. Su objetivo es dar sentido a los datos recolectados para sustentar la toma de decisiones, transformando datos en información útil [2, 3]. Se distingue entre **población**, que es el conjunto total de elementos a estudiar, y **muestra**, que es una parte representativa de dicha población [4-6].

### 13.1.2. Tipos de variables
Una variable es cualquier característica de una población que puede tomar distintos valores [7]. Se clasifican en:
*   **Cualitativas (o categóricas):** Describen cualidades y utilizan escalas nominales u ordinales [8].
*   **Cuantitativas:** Se expresan numéricamente y pueden ser **discretas** (toman valores determinados, usualmente conteos) o **continuas** (pueden tomar cualquier valor dentro de un intervalo, producto de mediciones) [9, 10].

### 13.1.3. Información estadística
La información estadística se basa en datos de interés que permiten analizar relaciones significativas. No toda información es dato estadístico; debe ser capaz de ser comparada, analizada e interpretada [11]. El correcto manejo de esta información determina el éxito en la toma de decisiones en organizaciones y la investigación científica [12].

## 13.2. Ordenación y clasificación del registro de datos

### 13.2.1. Descripción de variables
La descripción de variables implica identificar si son cualitativas o cuantitativas y su escala de medición (nominal, ordinal, intervalo, razón) [13]. Esta etapa es fundamental para decidir qué indicadores y gráficos son adecuados para descubrir la estructura inmersa en el conjunto de datos [14].

### 13.2.2. Tabla de distribución de frecuencias
La tabla de frecuencias es un arreglo que resume la información. Incluye:
*   **Frecuencia absoluta ($f_i$):** Número de veces que aparece un valor [15].
*   **Frecuencia relativa ($f_{ri}$):** Proporción del dato respecto al total ($f_i/n$) [16].
*   **Frecuencia acumulada ($F_i$):** Suma de frecuencias hasta un intervalo dado [17].
Permite volcar un gran número de datos de forma resumida para facilitar su lectura [18].

### 13.2.3. Cuantitativas y cualitativas
*   **Cualitativas:** Se tabulan contando la frecuencia de cada categoría (ej. nivel de escolaridad) [19]. No tienen frecuencia acumulada con sentido numérico estricto si son nominales [20].
*   **Cuantitativas:** Se ordenan de forma creciente. Si son muchos datos, se agrupan en **intervalos de clase**, calculando el rango, el número de intervalos (regla de Sturges) y la amplitud de clase [21, 22].

## 13.3. Aplicaciones de las tecnologías de información y comunicación y sistemas prácticos

### 13.3.1. Conceptos básicos
Debido al volumen de cálculos que conllevan las técnicas estadísticas, aunque conceptualmente sencillas, se requiere el uso de computadoras para procesar la información eficientemente [23].

### 13.3.2. Herramientas
Existen paquetes estadísticos especializados. Se destacan:
*   **Microsoft Excel:** Cuenta con herramientas como "Análisis de datos" para estadística descriptiva (media, error típico, mediana, moda, desviación, etc.) [24, 25].
*   **SPSS (IBM SPSS):** Software diseñado para ciencias sociales que permite definir variables (tipo, anchura, etiquetas) y generar tablas y gráficos complejos [26-28].

### 13.3.3. Representación de datos
La representación gráfica ofrece una visión de conjunto rápida. Los tipos principales son:
*   **Histograma:** Rectángulos con áreas proporcionales a las frecuencias para variables continuas [29].
*   **Polígono de frecuencias:** Línea que une los puntos medios (marcas de clase) de los intervalos [30].
*   **Diagrama de barras y circular (pastel):** Para variables cualitativas o discretas [31, 32].
*   **Ojiva:** Polígono de frecuencias acumuladas [33].

## 13.4. Medidas resumen de los datos I

### 13.4.1. Medidas descriptivas
Son valores numéricos que resumen características de una muestra (estadígrafos) o de una población (parámetros) [34]. Se enfocan en la tendencia central, la dispersión y la forma de la distribución.

### 13.4.2. Medidas de centralización
Indican el centro de la distribución:
*   **Media aritmética ($\bar{x}$):** Promedio de los datos. Es sensible a valores extremos [35, 36].
*   **Mediana ($Me$):** Valor que divide al conjunto de datos ordenados en dos partes iguales (50% superior e inferior) [37, 38].
*   **Moda ($Mo$):** Valor que se presenta con mayor frecuencia [39, 40].

### 13.4.3. Medidas de dispersión
Indican qué tan alejados están los datos del centro:
*   **Rango:** Diferencia entre el valor máximo y mínimo [41].
*   **Varianza ($s^2$ o $\sigma^2$):** Promedio de los cuadrados de las desviaciones respecto a la media [42, 43].
*   **Desviación estándar ($s$ o $\sigma$):** Raíz cuadrada de la varianza; se expresa en las unidades originales de los datos [43, 44].
*   **Coeficiente de Variación (CV):** Medida relativa ($s/\bar{x}$) útil para comparar la dispersión entre conjuntos con distintas unidades [45, 46].

### 13.4.4. Medidas de forma o posición
*   **Posición (Cuantiles):** Dividen la distribución en partes iguales. Incluyen **Cuartiles** ($Q_k$, 4 partes), **Deciles** ($D_k$, 10 partes) y **Percentiles** ($P_k$, 100 partes) [47, 48].
*   **Forma:**
    *   **Asimetría (Sesgo):** Indica la falta de simetría (positiva/derecha o negativa/izquierda) [49].
    *   **Curtosis (Apuntamiento):** Indica la elevación o achatamiento de la distribución (leptocúrtica, mesocúrtica, platicúrtica) [50].

## 13.5. Medidas resumen de los datos II

### 13.5.1. Diagrama de caja
Conocido como *box and whiskers*, utiliza cinco estadísticos: mínimo, primer cuartil ($Q_1$), mediana, tercer cuartil ($Q_3$) y máximo. La "caja" abarca el rango intercuartílico ($Q_3 - Q_1$) [51].

### 13.5.2. Identificación de valores atípicos
El diagrama de caja permite identificar valores atípicos (outliers). Se calculan referencias (REF) usando el rango intercuartílico ($RI$). Un dato es atípico si cae fuera de los límites calculados (ej. $Q_1 - 1.5 RI$ o $Q_3 + 1.5 RI$) [52, 53].

### 13.5.3. Transformación de una variable
Para describir una observación en relación con su grupo, se pueden transformar las puntuaciones brutas en **puntuaciones Z** (estandarización). La fórmula es $Z = (X - \mu) / \sigma$. Esto convierte la distribución a una escala con media 0 y desviación estándar 1, permitiendo comparar datos de distintas distribuciones [46, 54].

## 13.6. Análisis del conjunto de dos variables estadísticas

### 13.6.1. Tabulación de dos variables
Permite analizar simultáneamente el comportamiento de dos variables mediante **tablas de contingencia** o cruzadas. Se ubican las categorías de una variable en filas y la otra en columnas [55, 56].

### 13.6.2. Tablas de contingencia y representaciones gráficas
Las tablas pueden mostrar porcentajes de fila, de columna o del total para analizar la relación [57, 58]. Gráficamente, se pueden usar diagramas de barras agrupadas o tridimensionales para visualizar la asociación entre categorías [59].

### 13.6.3. Relación lineal entre variables cuantitativas
Para variables cuantitativas, se analiza la relación mediante la **covarianza**, definida para dos variables aleatorias $X$ e $Y$. Si son independientes, ciertas propiedades de la esperanza matemática y varianza se cumplen [60]. (Nota: El análisis gráfico usual es el diagrama de dispersión y la medida clave es la correlación, implícita en el estudio de la relación lineal).

## 13.7. Series temporales y números índices

### 13.7.1. Las series temporales
El análisis de series de tiempo estudia los cambios en actividades económicas o de negocios a lo largo del tiempo [61].

### 13.7.2. Tasas de variación
Permiten medir los cambios relativos sufridos por precios y cantidades entre dos periodos [62]. Se derivan de la comparación de valores en distintos puntos temporales.

### 13.7.3. Números índices
Son indicadores que comparan el comportamiento de una variable respecto a un periodo base (base = 100) [63].
*   **Índices simples:** Para un solo artículo [63].
*   **Índices agregados:** Para un grupo de artículos. Incluyen el **Índice de Laspeyres** (pondera con cantidades del periodo base) y el **Índice de Paasche** (pondera con cantidades del periodo actual) [64, 65].

### 13.7.4. El índice del precio al consumidor y series temporales deflactadas
*   **IPC:** Elaborado por el Banco de México, mide el incremento de precios de una canasta representativa de consumo [65].
*   **Deflación:** Proceso (implícito en el uso de índices de precios) para eliminar el efecto de la inflación en una serie temporal y analizar valores reales.

## 13.8. Introducción a la probabilidad: cálculo y conceptos básicos

### 13.8.1. Conceptos básicos
La probabilidad cuantifica la duda o certeza sobre la ocurrencia de un evento. Existen tres enfoques:
1.  **Clásico (a priori):** Basado en resultados igualmente posibles (ej. dados) [66].
2.  **Empírico:** Basado en la frecuencia relativa de eventos pasados.
3.  **Subjetivo:** Basado en la creencia personal [67].

### 13.8.2. Teoría de conjuntos
Se define el **espacio muestral** como el conjunto de todos los resultados posibles. Los **eventos** son subconjuntos del espacio muestral (ej. que salga un número par) [68, 69].

### 13.8.3. Cálculo de probabilidades
Se basa en axiomas formulados por Kolmogórov [70, 71]. Reglas fundamentales:
*   **Regla de la suma:** Para eventos mutuamente excluyentes o no excluyentes.
*   **Regla de la multiplicación:** Para la probabilidad conjunta [68, 72].

## 13.9. Variables aleatorias y funciones de probabilidad

### 13.9.1. Variables aleatorias
Es una función que asigna un valor numérico a cada resultado de un experimento aleatorio [10, 73]. Pueden ser discretas (valores puntuales) o continuas (valores en un intervalo) [74].

### 13.9.2. Medidas de las variables
Al igual que en estadística descriptiva, las variables aleatorias tienen parámetros:
*   **Esperanza matemática ($E[X]$):** El promedio ponderado de los valores posibles por sus probabilidades [75].
*   **Varianza ($V[X]$):** Medida de dispersión de la variable aleatoria [60].

### 13.9.3. Función de probabilidad
*   **Caso discreto:** Asigna probabilidad a cada valor puntual $P(X=x_i)$.
*   **Caso continuo:** Se usa una **función de densidad** $f(x)$, donde la probabilidad es el área bajo la curva.
*   **Función de distribución ($F(x)$):** Probabilidad acumulada $P(X \le x)$ [75, 76].

## 13.10. Modelos de probabilidad para variables aleatorias

### 13.10.1. Cálculo de probabilidades
Implica el uso de fórmulas específicas o tablas estandarizadas dependiendo del modelo de distribución que sigan los datos para resolver problemas prácticos [77].

### 13.10.2. Variables aleatorias discretas
Modelos notables:
*   **Binomial:** Número de éxitos en $n$ ensayos independientes con probabilidad $p$ constante [74, 78].
*   **Poisson:** Promedio de éxitos en un intervalo de tiempo o espacio [74, 79].
*   **Hipergeométrica:** Muestreo sin reemplazo [74, 80].
*   **Multinomial:** Extensión de la binomial para más de dos resultados [74].

### 13.10.3. Variables aleatorias continuas
Modelos notables:
*   **Exponencial:** Útil para tiempos de espera [74, 81].
*   **Uniforme:** Probabilidad constante en un intervalo [81].

### 13.10.4. Modelos derivados de la distribución normal
La **Distribución Normal** (Campana de Gauss) es la más importante. Definida por su media ($\mu$) y desviación estándar ($\sigma$) [82, 83].
*   **Normal Estándar:** Se usa la tabla Z transformando la variable ($Z$).
*   **Teorema Central del Límite:** Establece que la suma de variables aleatorias independientes tiende a una distribución normal cuando el tamaño de la muestra es grande [78].

---

### Resumen de 3 puntos clave

1.  **Proceso Estadístico Integral:** La asignatura abarca desde la recolección descriptiva y visualización de datos (tablas, histogramas, medidas de tendencia central y dispersión) hasta el análisis inferencial, permitiendo transformar datos brutos en información estratégica para la toma de decisiones.
2.  **Fundamento Probabilístico:** Se establece una base sólida en teoría de probabilidad (axiomas, variables aleatorias y funciones de distribución), diferenciando estrictamente entre modelos discretos (Binomial, Poisson) y continuos, con énfasis central en la Distribución Normal y el Teorema Central del Límite.
3.  **Herramientas de Análisis:** Se integran herramientas analíticas para una y dos variables (regresión, correlación, tablas de contingencia), así como métodos para el análisis temporal (números índices y series temporales), apoyados por el uso de tecnologías como Excel y SPSS para el procesamiento eficiente.
<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">
        <span class="text-blue-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Distribución Normal Estadística</h3>
    </div>
    <div class="bg-black/30 p-2 md:p-6 rounded-2xl border border-white/5 overflow-x-auto">
        
<div class="my-10 bg-gray-900/60 p-8 rounded-3xl border border-blue-500/20">
    <h3 class="text-blue-400 font-bold text-xl mb-6">La Campana de Gauss (Distribución Normal)</h3>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
        <div>
            <div class="font-mono text-sm text-center py-4 bg-black/50 rounded-lg mb-4">
                $$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}$$
            </div>
            <p class="text-gray-300 text-sm mb-4">
                El pilar paramétrico de la inferencia estadística cuantitativa. Su simetría absoluta dictamina probabilísticamente dónde orbita la manada muestral respecto a su centro de gravedad ($\mu$) y su esquizofrenia volátil ($\sigma$).
            </p>
        </div>
        <div class="bg-black/40 rounded-xl p-4 border border-gray-700">
            <h4 class="text-blue-300 font-bold text-sm mb-3">Postulados de Dispersión Empírica:</h4>
            <ul class="space-y-2 text-sm text-gray-400 font-mono">
                <li><span class="text-purple-400">[μ ± 1σ]</span> → Aglutina ≈ 68.2% del acervo.</li>
                <li><span class="text-purple-500">[μ ± 2σ]</span> → Aglutina ≈ 95.4% del acervo.</li>
                <li><span class="text-purple-600">[μ ± 3σ]</span> → Aglutina ≈ 99.7% del acervo.</li>
            </ul>
        </div>
    </div>
</div>
<!-- GLOSARIO -->


    </div>
</div>
