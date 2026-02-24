# Guía de Estudio: Asignatura 5. Matemáticas

Esta guía ha sido elaborada integrando estrictamente los contenidos de las fuentes proporcionadas, estructurada según el "Temario Oficial de Matemáticas" [1].

## 5.1. Elementos básicos del álgebra lineal y matricial

### 5.1.1. El espacio vectorial de IRn , funciones y variables
El espacio vectorial $\mathbb{R}^n$ es la colección de todas las listas (o $n$-adas ordenadas) de $n$ números reales. Estos vectores se escriben habitualmente como matrices columna. Si $n$ es un entero positivo, $\mathbb{R}^n$ representa el espacio coordenado donde se definen operaciones de suma y producto por escalar [2]. Un espacio vectorial es una estructura matemática que permite tratar vectores con independencia de su naturaleza, verificando axiomas como la conmutatividad y asociatividad de la suma, y la existencia de elemento neutro y opuesto [3], [4].

### 5.1.2. Representación gráfica de conjuntos de R
Los vectores en $\mathbb{R}^2$ se representan geométricamente como puntos en un plano coordenado o como flechas desde el origen. De igual manera, los vectores en $\mathbb{R}^3$ se representan en un espacio tridimensional [2]. Las soluciones de sistemas lineales pueden visualizarse como puntos, líneas o planos que no necesariamente pasan por el origen [5].

### 5.1.3. Conceptos básicos de funciones reales de varias variables. Operaciones con funciones
Las funciones de varias variables aparecen en situaciones donde una magnitud depende de varios factores [6]. Se definen operaciones básicas como la suma, producto y composición de funciones. Definir una función implica establecer un dominio y un codominio [7].

### 5.1.4. Clases de funciones
Existen diversas funciones elementales como las polinómicas, racionales, raíces, trigonométricas, exponenciales y logarítmicas. Las funciones pueden clasificarse también por propiedades como paridad (simetría respecto al eje Y) o imparidad (simetría respecto al origen) [8], [9].

### 5.1.5. Teorema de Weirtrass
En el contexto de la continuidad en intervalos, el Teorema de Weierstrass es fundamental. Establece que una función continua en un intervalo cerrado y acotado alcanza sus valores máximo y mínimo absolutos en dicho intervalo [10].

### 5.1.6. Optimización con restricciones de desiguales
La optimización con restricciones busca minimizar o maximizar una función $f(x)$ sujeta a restricciones $g_i(x) \leq 0$. Las condiciones de optimalidad para estos problemas, conocidas como condiciones de Karush-Kuhn-Tucker (KKT), involucran gradientes y multiplicadores [11], [12].

### 5.1.7. El método gráfico de dos variables
En problemas de programación lineal con dos variables, las restricciones definen un poliedro o región factible en el plano. La solución óptima se encuentra frecuentemente en uno de los vértices o puntos extremos de este poliedro [13], [14].

### 5.1.8. Clases de funciones
*Nota: Se reitera el concepto de 5.1.4.* Las funciones se agrupan en familias con características comunes, como las funciones elementales (polinomios, racionales, etc.) que sirven de base para el análisis matemático [8].

### 5.1.9. Variables separadas
Este concepto se aplica en la resolución de ecuaciones diferenciales y en la integración sobre regiones rectangulares donde las funciones pueden factorizarse en productos de funciones de una sola variable, facilitando el cálculo mediante integrales iteradas [15], [16].

### 5.1.10. Variables polinómicas
Los polinomios son funciones formadas por la suma de potencias enteras no negativas de la variable multiplicadas por coeficientes. En álgebra lineal, el conjunto de polinomios de grado menor o igual a $n$, denotado $P_n$, forma un espacio vectorial [17], [18].

### 5.1.11. Racionales
Las funciones racionales son el cociente de dos polinomios. Su dominio excluye los puntos donde el denominador se anula. En el álgebra, el conjunto de números racionales $\mathbb{Q}$ tiene estructura de cuerpo [19], [20].

### 5.1.12. Formas cuadráticas
Una forma cuadrática es una función $Q(x) = x^T A x$ donde $A$ es una matriz simétrica. Surgen en aplicaciones de ingeniería y estadística. Pueden ser definidas positivas, negativas o indefinidas dependiendo de los valores que toma $Q(x)$ para $x \neq 0$ [21], [22].

## 5.2. Matrices: tipos, conceptos y operaciones

### 5.2.1. Definiciones básicas
Una matriz es una ordenación rectangular de escalares (números). Es una herramienta fundamental del álgebra lineal utilizada para representar sistemas de ecuaciones y aplicaciones lineales [23], [24].

### 5.2.2. Matriz de orden mxn
Una matriz de orden $m \times n$ tiene $m$ filas y $n$ columnas. El conjunto de estas matrices con coeficientes en un cuerpo $K$ se denota por $M_{m \times n}(K)$. Los elementos se denotan $a_{ij}$ [24].

### 5.2.3. Matrices cuadradas
Son matrices donde el número de filas es igual al número de columnas ($m=n$). Estas matrices son fundamentales para el cálculo de determinantes y el estudio de la diagonalización [24], [25].

### 5.2.4. Matriz identidad
Es una matriz cuadrada, denotada usualmente como $I$ o $I_n$, que tiene unos en la diagonal principal y ceros en el resto de las entradas. Actúa como elemento neutro para la multiplicación de matrices [4], [26].

### 5.2.5. Operaciones con matrices
Las operaciones algebraicas básicas con matrices incluyen la suma, el producto por un escalar y el producto de matrices. Estas operaciones dotan al conjunto de matrices de estructura algebraica [20].

### 5.2.6. Suma de matrices
La suma de dos matrices $A$ y $B$ del mismo tamaño se obtiene sumando las entradas correspondientes. Es una operación conmutativa y asociativa [27], [28].

### 5.2.7. Producto de un número real por una matriz
El producto de una matriz por un escalar (número real) se obtiene multiplicando cada entrada de la matriz por dicho escalar [27], [29].

### 5.2.8. Producto de matrices
El producto de matrices se realiza mediante la regla fila-columna. Para que el producto $AB$ esté definido, el número de columnas de $A$ debe coincidir con el número de filas de $B$. Esta operación no es conmutativa en general [30], [31].

## 5.3. Transposición matricial

### 5.3.1. Matriz diagonizable
Una matriz cuadrada $A$ es diagonalizable si existe una matriz invertible $P$ y una matriz diagonal $D$ tales que $A = PDP^{-1}$. Esto está íntimamente ligado a los valores y vectores propios de la matriz [32], [33].

### 5.3.2. Propiedades de la transposición de matrices
La transpuesta de una matriz $A$, denotada $A^T$, se obtiene intercambiando filas por columnas. Propiedades clave incluyen $(A^T)^T = A$, $(A+B)^T = A^T + B^T$ y $(AB)^T = B^T A^T$ [34], [35].

### 5.3.3. Propiedad involutiva
Una matriz es involutiva si es su propia inversa, es decir $A^2 = I$. En el contexto de la transposición, esto se relaciona con matrices ortogonales donde $A^T = A^{-1}$. La operación de transposición en sí misma es involutiva ya que trasponer dos veces retorna a la matriz original [36], [37].

## 5.4. Determinantes: cálculo y definición

### 5.4.1. Concepto de determinantes
El determinante es un número asociado a una matriz cuadrada que proporciona información importante, como si la matriz es invertible (determinante no nulo) o el factor de escala de volumen de una transformación lineal [25], [38].

### 5.4.2. Definición de determinantes
Se define inductivamente mediante un desarrollo por cofactores a lo largo de una fila. Para una matriz $1 \times 1$, es el propio escalar [39].

### 5.4.3. Matriz cuadrada de orden 2,3 y superior a 3
Para orden 2, el determinante de $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ es $ad - bc$. Para orden 3 y superior, se utilizan métodos como la regla de Sarrus (solo orden 3) o el desarrollo por cofactores y operaciones elementales para reducir el orden [25], [40].

### 5.4.4. Matrices triangulares
Una matriz es triangular si todos los elementos por encima (triangular inferior) o por debajo (triangular superior) de la diagonal principal son cero [41].

### 5.4.5. Cálculo de la matriz triangular
El determinante de una matriz triangular es simplemente el producto de las entradas de su diagonal principal [42].

### 5.4.6. Cálculo de la matriz cuadrada no triangular
Para matrices no triangulares, se emplean operaciones elementales de fila para transformarlas en una forma escalonada (triangular) y facilitar el cálculo del determinante [25].

### 5.4.7. Propiedades de los determinantes
Propiedades clave incluyen: $det(AB) = det(A)det(B)$, $det(A^T) = det(A)$, y si se intercambian dos filas el determinante cambia de signo. Si una fila es múltiplo de otra, el determinante es cero [43], [40].

### 5.4.8. Simplificación de cálculos
Las propiedades de los determinantes, especialmente las operaciones de fila (reemplazo), permiten simplificar la matriz introduciendo ceros antes de desarrollar por cofactores, reduciendo la complejidad del cálculo [25].

### 5.4.9. Cálculo, en cualquier caso
El método general implica la reducción por filas para llevar la matriz a una forma escalonada o el uso del desarrollo por cofactores a lo largo de cualquier fila o columna conveniente [44].

## 5.5. La inversión matricial

### 5.5.1. Propiedades de la inversión matricial
Si existe, la inversa $A^{-1}$ es única. Se cumple que $(A^{-1})^{-1} = A$, $(AB)^{-1} = B^{-1}A^{-1}$ y $(A^T)^{-1} = (A^{-1})^T$ [34], [45].

### 5.5.2. Concepto de inversión
Una matriz cuadrada $A$ es invertible (o no singular) si existe una matriz $B$ tal que $AB = BA = I$. Esta matriz $B$ se llama inversa de $A$ [46], [20].

### 5.5.3. Definiciones y conceptos básicos asociados
Conceptos asociados incluyen la matriz singular (no invertible), la matriz adjunta y el teorema de la matriz invertible que relaciona la invertibilidad con el rango, el determinante y la independencia lineal de las columnas [47], [48].

### 5.5.4. Cálculo de la inversión matricial
Se puede calcular utilizando la fórmula con la matriz adjunta y el determinante, o mediante la reducción por filas de la matriz aumentada $[A | I]$ hasta llegar a $[I | A^{-1}]$ [43], [49].

### 5.5.5. Métodos y cálculo
El algoritmo de reducción por filas es eficiente para el cálculo. Para matrices $2 \times 2$ existe una fórmula sencilla: $\frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ [34].

### 5.5.6. Excepciones y ejemplos
Las matrices con determinante igual a cero no tienen inversa (son singulares). Ejemplo: una matriz con una fila de ceros o columnas linealmente dependientes no es invertible [50].

### 5.5.7. Expresión y ecuación matricial
Los sistemas de ecuaciones lineales pueden escribirse como una ecuación matricial $Ax = b$. La manipulación algebraica de estas expresiones permite resolver para $x$ usando la inversa: $x = A^{-1}b$ [51], [52].

### 5.5.8. Expresión matricial
Una expresión matricial involucra matrices, vectores y operaciones algebraicas. Permite compactar sistemas complejos de relaciones lineales [52].

### 5.5.9. Ecuación matricial
La ecuación $Ax = b$ es fundamental. Si $A$ es invertible, la solución es única. Esta ecuación es equivalente a una ecuación vectorial que involucra combinaciones lineales de las columnas de $A$ [52].

## 5.6. Resolución de sistemas de ecuaciones

### 5.6.1. Ecuaciones lineales
Una ecuación lineal tiene la forma $a_1x_1 + \dots + a_nx_n = b$. Un sistema es una colección de estas ecuaciones [53].

### 5.6.2. Discusión del sistema. Teorema de Rouché-Fobenius
Este teorema permite discutir la existencia de soluciones comparando el rango de la matriz de coeficientes $A$ con el rango de la matriz aumentada $(A|b)$. El sistema es compatible si los rangos coinciden [54].

### 5.6.3. Regla de Cramer: resolución del sistema
Es una fórmula explícita para la solución de sistemas $Ax=b$ donde $A$ es invertible. Cada incógnita $x_i$ se calcula como el cociente de dos determinantes [55], [56].

### 5.6.4. Los sistemas homogéneos
Un sistema es homogéneo si se escribe como $Ax = 0$. Siempre tiene al menos la solución trivial ($x=0$). Tiene soluciones no triviales si hay variables libres [57], [58].

### 5.6.5. Espacios vectoriales
Un espacio vectorial es un conjunto de objetos (vectores) con operaciones de suma y producto por escalar que cumplen diez axiomas. Ejemplos incluyen $\mathbb{R}^n$, polinomios y funciones [59], [60].

### 5.6.6. Propiedades del espacio vectorial
Incluyen la existencia del vector cero, propiedades distributivas y cerradura bajo las operaciones. Un subespacio es un subconjunto que mantiene estas propiedades [61], [4].

### 5.6.7. Combinación lineal de vectores
Un vector es combinación lineal de otros si se puede escribir como suma de múltiplos escalares de ellos: $y = c_1v_1 + \dots + c_p v_p$ [62], [63].

### 5.6.8. Dependencia e independencia lineales
Un conjunto de vectores es linealmente independiente si la ecuación $c_1v_1 + \dots + c_p v_p = 0$ solo tiene la solución trivial. Si hay coeficientes no nulos que satisfacen la ecuación, son dependientes [64], [65].

### 5.6.9. Coordenadas de un vector
Si se tiene una base $B$, cualquier vector $x$ en el espacio puede representarse de forma única como combinación lineal de los elementos de la base. Los pesos de esta combinación son las coordenadas de $x$ respecto a $B$ [66], [67].

### 5.6.10. Teorema de las bases
Cualquier conjunto linealmente independiente en un espacio vectorial $V$ puede extenderse a una base, y cualquier conjunto que genere $V$ contiene una base. Todas las bases de un espacio vectorial de dimensión finita tienen el mismo número de elementos [18], [68].

## 5.7. Formas cuadráticas

### 5.7.1. Concepto y definición de las formas cuadráticas
Una forma cuadrática es una función $Q: \mathbb{R}^n \to \mathbb{R}$ definida por $Q(x) = x^T A x$, donde $A$ es una matriz simétrica $n \times n$. Involucra términos cuadráticos ($x_i^2$) y términos cruzados ($x_i x_j$) [21], [69].

### 5.7.2. Matrices cuadráticas
La matriz $A$ asociada a una forma cuadrática es siempre simétrica. Esta simetría garantiza que $A$ sea diagonalizable ortogonalmente [33].

### 5.7.3. Ley de inercia de las formas cuadráticas
La Ley de Inercia de Sylvester establece que el número de coeficientes positivos y negativos en la forma diagonal de una forma cuadrática es invariante, independientemente del cambio de base utilizado [70].

### 5.7.4. Estudio del signo por auto-valores
Una forma cuadrática es definida positiva si todos los autovalores de su matriz $A$ son positivos; definida negativa si todos son negativos; e indefinida si tiene autovalores positivos y negativos [22].

### 5.7.5. Estudio del signo por menores
El criterio de Sylvester permite determinar el signo analizando los determinantes de los menores principales de la matriz $A$. Por ejemplo, es definida positiva si todos los menores principales son positivos [70].

## 5.8. Funciones de una variable

### 5.8.1. Análisis del comportamiento de una magnitud
El análisis de funciones permite estudiar la dependencia entre variables y describir fenómenos. Se utilizan herramientas como límites y derivadas para entender el comportamiento asintótico y las tasas de cambio [71], [72].

### 5.8.2. Análisis local
El análisis local estudia el comportamiento de una función en el entorno de un punto, utilizando conceptos como derivadas, extremos relativos y polinomios de Taylor para aproximaciones locales [73], [74].

### 5.8.3. Continuidad
Una función es continua en un punto si el límite al acercarse al punto coincide con el valor de la función. Gráficamente, no presenta saltos ni interrupciones [10], [75].

### 5.8.4. Continuidad restringida
Se refiere al estudio de la continuidad en un subconjunto del dominio, como un intervalo cerrado. Es condición necesaria para teoremas fundamentales como el de Weierstrass [76].

## 5.9. Límites de funciones, dominio e imagen en funciones reales

### 5.9.1. Funciones de varias variables
Son funciones donde el dominio es un subconjunto de $\mathbb{R}^n$. Se utilizan para modelar situaciones donde una magnitud depende de múltiples factores independientes [6].

### 5.9.2. Vectorial de varias variables
Hace referencia a funciones que toman valores vectoriales (funciones $f: \mathbb{R}^n \to \mathbb{R}^m$). Involucran conceptos de límites y continuidad extendidos a espacios métricos [77].

### 5.9.3. Dominio de una función
El dominio es el conjunto de valores para los cuales la función está definida. Determinarlo es el primer paso en el análisis de una función [7].

### 5.9.4. Concepto y aplicaciones
Las funciones y sus límites son herramientas esenciales para modelar fenómenos físicos, económicos y biológicos, permitiendo predecir comportamientos y optimizar resultados [8].

### 5.9.5. Límites de funciones
El límite describe el comportamiento de una función cuando la variable independiente se aproxima a un valor determinado, sin importar el valor de la función en ese punto [78].

### 5.9.6. Límites de una función en un punto
Formalmente definido mediante $\epsilon-\delta$, establece que $f(x)$ está arbitrariamente cerca de un límite $L$ cuando $x$ está suficientemente cerca de $a$ [79].

### 5.9.7. Límites laterales de una función
Son los límites al acercarse al punto desde la izquierda o la derecha. Para que el límite global exista, ambos límites laterales deben existir y ser iguales [78].

### 5.9.8. Límites de funciones racionales
Para funciones racionales, el límite en un punto del dominio se calcula por sustitución directa. En puntos donde el denominador es cero, se analizan indeterminaciones [80].

### 5.9.9. La indeterminación
Situaciones donde el límite no puede determinarse directamente (ej. $0/0, \infty/\infty$). Requieren manipulación algebraica o reglas como L'Hôpital para resolverse [81].

### 5.9.10. Indeterminación en funciones con raíces
Suelen resolverse multiplicando por el conjugado para eliminar la indeterminación, transformando la expresión en una más manejable [80].

### 5.9.11. Indeterminación 0/0
Es una de las formas indeterminadas más comunes. Se resuelve factorizando, racionalizando o aplicando derivadas (Regla de L'Hôpital) [81], [82].

### 5.9.12. Dominio e imagen de una función
La imagen es el conjunto de todos los valores que toma la función. Calcular dominio e imagen es crucial para entender el alcance y las restricciones de la función [7].

### 5.9.13. Concepto y características
Incluye propiedades como inyectividad, sobreyectividad, paridad y periodicidad, que describen el comportamiento global de la función [7].

### 5.9.14. Cálculo del dominio e imagen
Implica resolver desigualdades para asegurar que operaciones como raíces pares o logaritmos estén definidas, y analizar el recorrido de la función [7], [83].

## 5.10. Derivadas: análisis de comportamientos

### 5.10.1. Derivadas de una función en un punto
La derivada en un punto representa la tasa de cambio instantánea de la función y es la pendiente de la recta tangente a la gráfica en ese punto [84].

### 5.10.2. Concepto y características
La diferenciabilidad implica continuidad. La derivada mide la sensibilidad al cambio y permite aproximar la función linealmente cerca del punto [84], [85].

### 5.10.3. Interpretación geométrica
Geométricamente, la derivada es la pendiente de la tangente. Puntos con derivada cero corresponden a tangentes horizontales, candidatos a extremos [84].

### 5.10.4. Reglas de derivación
Son fórmulas para derivar combinaciones de funciones: suma, producto, cociente y composición (regla de la cadena) [85].

### 5.10.5. Derivación de una constante
La derivada de una función constante es siempre cero, ya que no hay cambio en su valor [86].

### 5.10.6. Derivación de una suma o una diferenciación
La derivada de una suma es la suma de las derivadas. Es una propiedad de linealidad del operador derivada [85].

### 5.10.7. Derivación de un producto
Sigue la regla: $(fg)' = f'g + fg'$. No es simplemente el producto de las derivadas [85].

### 5.10.8. Derivación de la opuesta
La derivada de $-f(x)$ es $-f'(x)$, consistente con la linealidad y el producto por el escalar -1 [86].

### 5.10.9. Derivación de la compuesta
Se utiliza la Regla de la Cadena: $(f(g(x)))' = f'(g(x))g'(x)$. Es esencial para derivar funciones complejas [85].

## 5.11. Aplicaciones derivadas al estudio de funciones

### 5.11.1. Propiedades de las funciones derivables
Las funciones derivables son suaves (sin picos) y continuas. Su comportamiento local puede predecirse mediante el signo de la derivada [82].

### 5.11.2. Teorema del máximo
Relacionado con la optimización, indica que en un intervalo cerrado una función continua alcanza un máximo. Si es derivable, ocurre en extremos o puntos críticos [87], [72].

### 5.11.3. Teorema del mínimo
Análogo al anterior, garantiza la existencia de un mínimo absoluto bajo las condiciones de continuidad en conjunto compacto [87].

### 5.11.4. Teorema de rolle
Si una función es continua en $[a,b]$, derivable en $(a,b)$ y $f(a)=f(b)$, existe un punto interior $c$ donde la derivada es cero ($f'(c)=0$) [82].

### 5.11.5. Teorema del valor medio
Generalización de Rolle: existe un punto $c$ donde la derivada instantánea iguala a la tasa de cambio promedio en el intervalo: $f'(c) = \frac{f(b)-f(a)}{b-a}$ [82].

### 5.11.6. Regla de l´Hôpital
Método para resolver límites indeterminados del tipo $0/0$ o $\infty/\infty$ derivando numerador y denominador [82].

### 5.11.7. Valoración de magnitudes económicas
La derivada se interpreta como coste, ingreso o utilidad marginal en economía, midiendo el cambio aproximado al producir una unidad adicional [71].

### 5.11.8. Diferenciabilidad
Propiedad de una función de tener derivada. En varias variables, implica la existencia de un plano tangente que aproxima bien la función [77].

## 5.12. Optimización de funciones de varias variables

### 5.12.1. Optimización de funciones
Busca encontrar máximos y mínimos locales o globales de funciones $f: \mathbb{R}^n \to \mathbb{R}$. Se analizan puntos críticos donde el gradiente es nulo [88].

### 5.12.2. Optimización con restricciones de igualdad
Utiliza el método de los multiplicadores de Lagrange para encontrar extremos de $f(x)$ sujetos a $g(x)=0$ [89].

### 5.12.3. Puntos críticos
Puntos donde las derivadas parciales son cero o no existen. Son candidatos a ser extremos locales [88].

### 5.12.4. Extremos relativos
Son puntos que tienen un valor mayor (máximo) o menor (mínimo) que todos los puntos en un entorno cercano [87], [88].

### 5.12.5. Funciones convexas y cóncavas
Las funciones convexas tienen la propiedad de que un segmento que une dos puntos de la gráfica queda por encima de la misma. Son fundamentales en minimización global [90].

### 5.12.6. Propiedades de las funciones convexas y cóncavas
En una función convexa diferenciable, la gráfica queda por encima del plano tangente. Un mínimo local de una función convexa es mínimo global [90].

### 5.12.7. Puntos de inflexión
Puntos donde cambia la concavidad de la función. En una variable, la segunda derivada se anula o cambia de signo [74], [83].

### 5.12.8. Crecimiento y decrecimiento
Determinado por el signo de la derivada (o gradiente). Derivada positiva indica crecimiento; negativa, decrecimiento [83].

## 5.13. Integrales indefinidas

### 5.13.1. Primitiva e integral indefinida
Una primitiva de $f$ es una función $F$ tal que $F' = f$. La integral indefinida es el conjunto de todas las primitivas, denotado $\int f(x) dx = F(x) + C$ [91].

### 5.13.2. Conceptos básicos
La integración es la operación inversa de la derivación. Es lineal y aditiva [91].

### 5.13.3. Métodos de cálculo
Incluyen métodos algebraicos y el uso de tablas de integrales inmediatas para encontrar primitivas [91].

### 5.13.4. Integrales inmediatas
Son aquellas que se obtienen directamente invirtiendo las reglas de derivación básicas (potencias, exponenciales, trigonométricas) [91].

### 5.13.5. Propiedades de las integrales inmediatas
Permiten integrar funciones compuestas sencillas mediante ajustes de constantes y propiedades de linealidad [91].

### 5.13.6. Métodos de integración
Técnicas avanzadas como integración por partes, sustitución (cambio de variable) y descomposición en fracciones simples para funciones racionales [91].

### 5.13.7. Integrales racionales
Se resuelven descomponiendo el cociente de polinomios en una suma de fracciones parciales más simples que se integran como logaritmos o arcotangentes [91].

## 5.14. Integrales definidas

### 5.14.1. Teorema de Barrow
Establece que la integral definida de una función continua en $[a,b]$ se puede calcular usando una primitiva $F$: $\int_a^b f(x) dx = F(b) - F(a)$ [91].

### 5.14.2. Definición del teorema
Conecta el cálculo diferencial con el integral, permitiendo evaluar áreas mediante la antiderivada [91].

### 5.14.3. Bases de cálculo
Se basa en las propiedades de linealidad y aditividad respecto al intervalo de integración [91].

### 5.14.4. Aplicaciones del teorema
Fundamental para calcular áreas bajo la curva, cambios totales acumulados y problemas físicos [91].

### 5.14.5. Corte de curvas en integrales definidas
Para calcular el área entre dos curvas, se determinan los puntos de intersección (corte) que definen los límites de integración [92].

### 5.14.6. Concepto del corte de curvas
Los puntos de corte se hallan igualando las funciones $f(x) = g(x)$. El área es la integral de la diferencia $|f(x) - g(x)|$ [92].

### 5.14.7. Bases de cálculo y estudio de las operaciones
Requiere descomponer el intervalo de integración en subintervalos determinados por los puntos de corte para eliminar el valor absoluto [92].

### 5.14.8. Aplicaciones del cálculo de corte de curvas
Permite determinar áreas de regiones acotadas complejas en el plano [92].

### 5.14.9. Teorema de la media
El Teorema del Valor Medio para integrales establece que existe un punto $c$ en $[a,b]$ tal que $\int_a^b f(x) dx = f(c)(b-a)$ [91].

### 5.14.10. Concepto teorema y del intervalo cerrado
Garantiza que la función alcanza su valor promedio en algún punto del intervalo cerrado de integración, asumiendo continuidad [91].

### 5.14.11. Bases de cálculo y estudio de las operaciones
Se utiliza para estimar integrales y en demostraciones teóricas del cálculo [91].

### 5.14.12. Aplicaciones del teorema
Utilizado para definir el valor promedio de una función y en la demostración del Teorema Fundamental del Cálculo [91].

---

### Resumen de Puntos Clave

1.  **Fundamentos Algebraicos y Matriciales:** El álgebra lineal proporciona la estructura vectorial ($\mathbb{R}^n$) y matricial necesaria para resolver sistemas de ecuaciones lineales y estudiar transformaciones lineales, siendo los determinantes y la inversión matricial herramientas operativas críticas.
2.  **Análisis de Funciones:** El estudio de funciones de una y varias variables se basa en los conceptos de límite, continuidad y derivada, permitiendo analizar el comportamiento local y global, así como optimizar funciones mediante el estudio de puntos críticos y convexidad.
3.  **Cálculo Integral:** La integración, conectada a la derivación por el Teorema Fundamental del Cálculo (Barrow), permite el cálculo de áreas y la acumulación de magnitudes, con métodos sistemáticos para resolver integrales indefinidas y aplicaciones geométricas mediante integrales definidas.
<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-blue-500 font-mono text-xs">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-xl">Fundamentos Analíticos: Límites, Derivadas e Integrales</h3>
    </div>
    <div class="bg-black/30 p-2 md:p-6 rounded-2xl border border-white/5 overflow-x-auto">
        
<div class="my-10 bg-gray-900/60 p-8 rounded-3xl border border-blue-500/20">
    <h3 class="text-blue-400 font-bold text-xl mb-6">El Triunvirato del Cálculo Infinitesimal</h3>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        <div class="p-5 bg-black/40 rounded-xl border border-gray-800">
            <h4 class="text-white font-semibold mb-3">1. Límite (Tendencia)</h4>
            <div class="font-mono text-sm text-center py-4 bg-black/50 rounded-lg mb-3">
                $$\lim_{x 	o a} f(x) = L$$
            </div>
            <p class="text-slate-400 text-xs text-justify">El comportamiento asintótico hacia donde converge inexorablemente una función cuando su variable independiente se acorrala infinitesimalmente cerca de un umbral.</p>
        </div>

        <div class="p-5 bg-black/40 rounded-xl border border-gray-800">
            <h4 class="text-white font-semibold mb-3">2. Derivada (Velocidad)</h4>
            <div class="font-mono text-sm text-center py-4 bg-black/50 rounded-lg mb-3">
                $$f'(x) = \lim_{h 	o 0} rac{f(x+h) - f(x)}{h}$$
            </div>
            <p class="text-slate-400 text-xs text-justify">La tasa de variación instantánea. Gráficamente, es el sismógrafo que dicta la pendiente (aceleración métrica) de la recta tangente en un punto exacto de la curva empírica.</p>
        </div>

        <div class="p-5 bg-black/40 rounded-xl border border-gray-800">
            <h4 class="text-white font-semibold mb-3">3. Integral (Acumulación)</h4>
            <div class="font-mono text-sm text-center py-4 bg-black/50 rounded-lg mb-3">
                $$\int_{a}^{b} f(x) dx = F(b) - F(a)$$
            </div>
            <p class="text-slate-400 text-xs text-justify">El acaparador macro. La sumatoria de infinitésimos de Riemann que halla el área confinada topográficamente bajo el trazo de la función, revelando acervos acumulados.</p>
        </div>
    </div>
</div>

    </div>
</div>
