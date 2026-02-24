# Guía de Estudio Académica: Asignatura 19. Econometría

Esta guía ha sido elaborada siguiendo estrictamente la estructura del "Temario Oficial de Econometría" proporcionado en las fuentes, integrando definiciones, metodologías y propiedades extraídas de los textos académicos disponibles.

## 19.1. El método de estimación mínimos cuadrados ordinarios (MCO)

### 19.1.1. Modelo de regresión lineal
El modelo de regresión lineal es la base del análisis econométrico. Se define matemáticamente para relacionar una variable dependiente ($Y$) con una o más variables explicativas ($X$). En su forma múltiple, se expresa como $y_i = \beta_0 + \beta_1x_{i1} + \dots + \beta_px_{ip} + \epsilon_i$, donde $y_i$ es la respuesta, $x_{ij}$ son los regresores, $\beta$ son los coeficientes a estimar y $\epsilon_i$ representa el error aleatorio [1]. Matricialmente, se resume como $y = X\beta + \epsilon$, asumiendo que el rango de la matriz $X$ es completo ($p+1$) [2].

### 19.1.2. Tipos de contenidos
El análisis econométrico maneja distintos tipos de datos que determinan el modelo a utilizar. Estos incluyen:
1.  **Series de tiempo:** Observaciones de una variable en intervalos regulares (diario, anual), donde el orden temporal es crucial y pueden presentar tendencias o estacionalidad [3].
2.  **Corte transversal:** Datos de múltiples individuos o unidades en un mismo punto del tiempo [4], [5].
3.  **Datos de panel:** Combinación de los anteriores, donde se observa a las mismas unidades transversales a lo largo de varios periodos de tiempo [6].

### 19.1.3. Línea general y estimación de mínimos cuadrados ordinarios MCO
El método de Mínimos Cuadrados Ordinarios (MCO) busca obtener estimadores ($\hat{\beta}$) que minimicen la suma de los cuadrados de los residuos (la diferencia entre el valor observado y el estimado). Matemáticamente, el estimador se define como $\hat{\beta} = (X'X)^{-1}X'y$ [7]. Este método traza una línea (o hiperplano) que pasa a través de los datos muestrales de tal manera que las distancias verticales al cuadrado entre los puntos y la línea sean mínimas [8].

## 19.2. El método mínimos cuadrados ordinarios en otros supuestos

### 19.2.1. Abandono de supuestos básicos
El modelo clásico de regresión lineal se basa en supuestos estrictos como la homocedasticidad, no autocorrelación, exogeneidad estricta y ausencia de multicolinealidad perfecta [2], [9]. Cuando estos supuestos se violan, surgen problemas como la heterocedasticidad (varianza del error no constante), autocorrelación (errores correlacionados temporalmente) o endogeneidad (correlación entre regresores y el error), lo que requiere tratamientos especiales [9], [10].

### 19.2.2. Comportamientos del método
Cuando se abandonan los supuestos básicos, el comportamiento de los estimadores MCO cambia. Por ejemplo, ante la presencia de autocorrelación o heterocedasticidad, los estimadores MCO siguen siendo insesgados pero dejan de ser eficientes (ya no son de varianza mínima), lo que invalida las pruebas de hipótesis estándar ($t$ y $F$) debido a que los errores estándar estimados están sesgados [11]. En casos de endogeneidad (como variables omitidas o simultaneidad), los estimadores MCO se vuelven sesgados e inconsistentes [12].

### 19.2.3. Efecto de cambios de medidas
La especificación del modelo puede alterarse mediante transformaciones de las variables para corregir problemas o interpretar elasticidades. Esto incluye transformaciones Box-Cox para estabilizar la varianza [13] o el uso de logaritmos. Si se cambian las unidades de medida de las variables, los coeficientes estimados cambiarán proporcionalmente, pero la significancia estadística ($t$-stat) y el $R^2$ no se ven afectados, a menos que la transformación altere la forma funcional (por ejemplo, lineal a logarítmica) [14].

## 19.3. Propiedades de estimadores de mínimos cuadrados ordinarios

### 19.3.1. Momentos y propiedades
Bajo el cumplimiento de los supuestos de Gauss-Markov, los estimadores MCO poseen propiedades estadísticas deseables: son **insesgados** (su valor esperado es igual al verdadero parámetro poblacional, $E[\hat{\beta}] = \beta$) y son **eficientes** (tienen la varianza mínima dentro de la clase de estimadores lineales insesgados), propiedad conocida como ELIO o BLUE [2], [15].

### 19.3.2. Estimación de varianzas
La varianza de los estimadores es fundamental para la inferencia. Bajo homocedasticidad, la matriz de varianzas-covarianzas de los estimadores se define como $Var(\hat{\beta}) = \sigma^2(X'X)^{-1}$ [16], [17]. Dado que $\sigma^2$ (la varianza del error) es desconocida, se estima utilizando la suma de los residuos al cuadrado dividida por los grados de libertad ($n-k$), obteniendo $\hat{\sigma}^2$ [18].

### 19.3.3. Formas matriciales
La notación matricial compacta el análisis del modelo lineal general. El modelo es $Y = X\beta + \epsilon$. El estimador MCO es $\hat{\beta} = (X'X)^{-1}X'Y$. La matriz de proyección (hat matrix) que genera los valores ajustados $\hat{Y}$ es $P = X(X'X)^{-1}X'$, tal que $\hat{Y} = PY$ [19].

## 19.4. Cálculo de la varianza de mínimos cuadrados ordinarios

### 19.4.1. Conceptos básicos
El cálculo preciso de la varianza es vital para probar hipótesis. Se basa en la asunción de que la varianza de los errores es constante (homocedasticidad) y que los errores no están correlacionados entre sí ($E[\epsilon \epsilon'] = \sigma^2 I$) [20]. Si la varianza de los errores no es escalar (es decir, $\sigma^2 \Omega$ con $\Omega \neq I$), el cálculo estándar de la varianza de MCO es incorrecto [21].

### 19.4.2. Contrastes de hipótesis
Los contrastes se construyen comparando la estimación del parámetro con un valor hipotético, estandarizado por su desviación típica estimada. La validez de estos contrastes depende de la normalidad de los errores o de muestras suficientemente grandes para invocar el Teorema del Límite Central [22], [17].

### 19.4.3. Coeficientes del modelo
Cada coeficiente estimado $\hat{\beta}_j$ tiene una varianza asociada que corresponde al elemento $j$-ésimo de la diagonal principal de la matriz de varianzas-covarianzas $\sigma^2(X'X)^{-1}$. La raíz cuadrada de esta varianza es el error estándar del coeficiente, utilizado para construir intervalos de confianza y estadísticos $t$ [23].

## 19.5. Contrastes de hipótesis en el modelo de regresión lineal

### 19.5.1. Contraste T
Se utiliza para probar la significancia individual de un coeficiente. La hipótesis nula es usualmente $H_0: \beta_j = 0$. El estadístico se calcula como $t = \hat{\beta}_j / se(\hat{\beta}_j)$. Si el valor absoluto del estadístico $t$ es mayor que el valor crítico, se rechaza la hipótesis nula, indicando que la variable es estadísticamente significativa [24], [25].

### 19.5.2. Contraste F
Se emplea para probar la significancia conjunta de varios coeficientes (restricciones lineales múltiples). Se comparan la suma de cuadrados de los residuos del modelo restringido ($SCR_R$) y del modelo no restringido ($SCR_{NR}$). El estadístico es $F = \frac{(SCR_R - SCR_{NR})/q}{SCR_{NR}/(n-k)}$, donde $q$ es el número de restricciones. Si $F$ es alto, se rechaza la hipótesis nula de que las restricciones son ciertas [26], [27].

### 19.5.3. Contraste global
Es un caso específico del contraste F donde se prueba si *todos* los coeficientes de las pendientes son simultáneamente iguales a cero ($H_0: \beta_1 = \beta_2 = \dots = \beta_k = 0$). Si se rechaza, indica que el modelo en su conjunto tiene capacidad explicativa [28].

## 19.6. Intervalos de confianza

### 19.6.1. Objetivos
El objetivo de un intervalo de confianza es proporcionar un rango de valores que, con un cierto nivel de confianza (por ejemplo, 95%), contiene el verdadero valor del parámetro poblacional desconocido. Refleja la precisión de la estimación [29].

### 19.6.2. En un coeficiente
El intervalo de confianza para un coeficiente individual $\beta_j$ se construye como $\hat{\beta}_j \pm t_{\alpha/2} \cdot se(\hat{\beta}_j)$. Si este intervalo incluye el cero, no se puede rechazar la hipótesis de que la variable no tiene efecto sobre la variable dependiente [30].

### 19.6.3. En una combinación de coeficientes
A veces interesa estimar una combinación lineal de parámetros, como $H_0: \beta_1 + \beta_2 = 1$. El intervalo de confianza se construye utilizando el error estándar de la combinación lineal, el cual implica las varianzas de cada estimador y su covarianza: $Var(\hat{\beta}_1 + \hat{\beta}_2) = Var(\hat{\beta}_1) + Var(\hat{\beta}_2) + 2Cov(\hat{\beta}_1, \hat{\beta}_2)$ [25].

## 19.7. Problemas de especificación

### 19.7.1. Uso y concepto
Una especificación correcta implica que el modelo incluye todas las variables relevantes, omite las irrelevantes y tiene la forma funcional adecuada. Los errores de especificación ocurren cuando se viola alguno de estos principios, lo que invalida las propiedades de los estimadores MCO [31].

### 19.7.2. Tipos de problemas
Los principales errores de especificación son:
1.  **Omisión de variables relevantes:** Causa sesgo en los coeficientes estimados de las variables incluidas si estas están correlacionadas con la variable omitida [32].
2.  **Inclusión de variables irrelevantes:** No causa sesgo, pero reduce la eficiencia de los estimadores (aumenta la varianza) [33].
3.  **Forma funcional incorrecta:** Usar una relación lineal cuando la verdadera es no lineal (ej. logarítmica) [34].

### 19.7.3. Variables explicativas no observables
Frecuentemente, una variable teóricamente relevante (como la "habilidad" o "calidad institucional") no es medible directamente. Si se omite, causa sesgo. Para solucionarlo, se pueden usar **variables proxy** (variables aproximadas que correlacionan con la no observable) [35] o métodos de **variables instrumentales** si la proxy no es perfecta y genera endogeneidad [36].

## 19.8. Predicción en el modelo de regresión lineal

### 19.8.1. Predicción
El modelo de regresión se utiliza para predecir el valor de la variable dependiente dado un conjunto de valores de las variables independientes. La predicción puntual es $\hat{y}_0 = x_0'\hat{\beta}$. Es importante minimizar el error cuadrático medio de predicción [37].

### 19.8.2. Intervalos de un valor medio
Además de la predicción puntual, se puede construir un intervalo de confianza para el valor medio esperado de $Y$ dado $x_0$, es decir, $E[Y|x_0]$. La varianza de esta predicción depende de la varianza de los estimadores y de la distancia de $x_0$ respecto a la media de los datos muestrales [38].

### 19.8.3. Aplicaciones
Las aplicaciones incluyen pronósticos de ventas, crecimiento del PIB, o la evaluación de impacto de políticas. Se busca que los modelos tengan buena capacidad predictiva fuera de la muestra, utilizando criterios como el error cuadrático medio [39], [40].

## 19.9. Análisis de residuos en la predicción lineal

### 19.9.1. Objetivos y conceptos generales
El análisis de residuos ($\hat{\epsilon}_i = y_i - \hat{y}_i$) es fundamental para validar los supuestos del modelo. Los residuos deben comportarse como ruido blanco si el modelo está bien especificado. Se busca detectar patrones que indiquen heterocedasticidad, autocorrelación o no linealidad [2].

### 19.9.2. Herramientas de análisis
Se utilizan gráficos de residuos contra valores ajustados o contra variables independientes para detectar patrones visuales. También se emplean pruebas formales como el test de Jarque-Bera para normalidad [41] o correlogramas para autocorrelación [42].

### 19.9.3. El análisis de residuos
El examen detallado permite identificar **valores atípicos** (observaciones con residuos muy grandes) o **puntos influyentes** (observaciones que alteran significativamente los coeficientes estimados). Medidas como la distancia de Cook ayudan a identificar estos puntos [43], [44].

## 19.10. Variables cualitativas en el Modelo de Regresión Lineal General (MRLG) I

### 19.10.1. Fundamentos
Las variables cualitativas (sexo, región, estado civil) se incorporan en los modelos de regresión para capturar efectos de atributos no numéricos. Se representan mediante variables indicadoras o *dummies* [45].

### 19.10.2. Modelos con varios tipos de información
Es común mezclar variables cuantitativas (ingreso, edad) con cualitativas en un mismo modelo. Esto permite evaluar cambios en el intercepto (nivel) o en la pendiente (interacciones) de la relación entre variables cuantitativas según la categoría cualitativa [46].

### 19.10.3. Métricas lineales
La inclusión de variables cualitativas permite medir diferencias en medias condicionales. Por ejemplo, en una ecuación de salarios, el coeficiente de una variable "mujer" mide la diferencia salarial promedio respecto a los hombres, manteniendo constantes otros factores (*ceteris paribus*) [47].

## 19.11. Variables cualitativas en el Modelo de Regresión Lineal General (MRLG) II

### 19.11.1. Variables binarias
Son variables que toman solo dos valores, generalmente 0 y 1. Se utilizan para indicar la presencia o ausencia de una cualidad. El coeficiente asociado mide el cambio en el valor esperado de $Y$ cuando la variable binaria pasa de 0 a 1 [47].

### 19.11.2. Utilización de variables ficticias
Las variables ficticias (dummies) se usan para modelar efectos estacionales (trimestres), cambios estructurales en el tiempo, o categorías múltiples (evitando la trampa de las variables ficticias al omitir una categoría base) [48], [45]. También se usan en el modelo de efectos fijos en datos de panel [45].

### 19.11.3. Series temporales
En series de tiempo, las variables ficticias son cruciales para modelar estacionalidad (ej. ventas en diciembre), eventos atípicos (huelgas, desastres) o cambios de política económica que afectan la estructura de la serie en un momento específico [49].

## 19.12. Autocorrelación

### 19.12.1. Conceptos básicos
La autocorrelación ocurre cuando los términos de error de diferentes periodos están correlacionados ($Cov(\epsilon_t, \epsilon_{t-k}) \neq 0$). Es común en series de tiempo donde los efectos de un shock persisten en el tiempo [50], [33].

### 19.12.2. Consecuencias
La presencia de autocorrelación no sesga los coeficientes MCO (si no hay variables dependientes rezagadas), pero los estimadores dejan de ser eficientes. Además, las fórmulas estándar de varianza subestiman el verdadero error, lo que invalida las pruebas $t$ y $F$ (se tiende a rechazar hipótesis nulas verdaderas) [11].

### 19.12.3. Contraste
Para detectar autocorrelación se utiliza el estadístico **Durbin-Watson** (para autocorrelación de primer orden) [51] o la prueba de **Breusch-Godfrey** (para órdenes superiores). También se inspeccionan los correlogramas de los residuos [42], [52].

## 19.13. Heterocedasticidad

### 19.13.1. Concepto y contrastes
La heterocedasticidad implica que la varianza del error no es constante, sino que cambia con las observaciones ($Var(\epsilon_i) = \sigma_i^2$). Para detectarla, se usan contrastes como el de **Breusch-Pagan** (relaciona residuos al cuadrado con variables explicativas) o el de **White** (más general, incluye términos cuadráticos y cruzados) [53], [54].

### 19.13.2. Consecuencias
Al igual que la autocorrelación, la heterocedasticidad no causa sesgo en los coeficientes pero sí ineficiencia. Los errores estándar calculados por MCO son incorrectos, invalidando la inferencia estadística. Se requiere el uso de Mínimos Cuadrados Generalizados (MCG) o errores estándar robustos de White para corregir la inferencia [53], [21].

### 19.13.3. Series temporales
En series de tiempo, la heterocedasticidad puede manifestarse como volatilidad cambiante en el tiempo (volatilidad agrupada), lo cual es muy común en series financieras. Esto da lugar a modelos específicos como los ARCH (AutoRegressive Conditional Heteroskedasticity) para modelar la varianza condicional [13], [55].

***

### Resumen de 3 puntos clave:

1.  **Fundamentos de MCO y Supuestos:** El método de Mínimos Cuadrados Ordinarios es la herramienta central para estimar relaciones lineales, garantizando estimadores insesgados y eficientes (BLUE) solo si se cumplen los supuestos de Gauss-Markov (homocedasticidad, no autocorrelación, exogeneidad).
2.  **Diagnóstico y Corrección:** La violación de supuestos (heterocedasticidad, autocorrelación, endogeneidad) invalida la inferencia estadística estándar. Es obligatorio realizar contrastes (Durbin-Watson, White, Hausman) y aplicar correcciones como Mínimos Cuadrados Generalizados, Variables Instrumentales o errores robustos.
3.  **Flexibilidad del Modelo:** El modelo lineal general se adapta a variables cualitativas mediante *dummies* y a dinámicas temporales mediante retardos, permitiendo modelar fenómenos complejos como estacionalidad, cambios estructurales y efectos de políticas en datos de corte transversal, series de tiempo y panel.
<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">
        <span class="text-blue-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo A19</h3>
    </div>
    <div class="bg-black/30 p-2 md:p-6 rounded-2xl border border-white/5 overflow-x-auto">
        
<pre class="mermaid bg-transparent flex justify-center">
graph LR
    A[Concepto Base] --> B(Aplicación Empírica)
    B --> C{Resolución Analítica}
    C -->|Óptimo| D[Equilibrio]
    C -->|Falla| E[Intervención]
    
    classDef default fill:#111827,stroke:#3b82f6,stroke-width:1px,color:#d1d5db
    classDef decision fill:#1e3a8a,stroke:#60a5fa,stroke-width:2px,color:#fff
    class C decision
</pre>
<!-- GLOSARIO -->


    </div>
</div>
