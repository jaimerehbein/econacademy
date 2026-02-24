# Guía de Estudio: Operaciones financieras

Esta guía desarrolla el Temario Oficial de la Asignatura 16 "Operaciones financieras", basándose estrictamente en los conceptos, definiciones y operaciones matemáticas detalladas en las fuentes proporcionadas.

## 16.1. Conceptos básicos

### 16.1.1. Términos esenciales para las operaciones financieras

#### 16.1.1.1. Capital financiero
En el ámbito de las matemáticas financieras, el capital financiero no se define solo por una cuantía monetaria, sino que es un concepto bidimensional. Se representa como un par de valores $(C, t)$, donde el primer valor es la **cuantía** (cantidad de unidades monetarias) y el segundo es el **vencimiento** (momento del tiempo en el que se entrega o está disponible dicho bien) [1], [2]. Esta definición es fundamental porque las matemáticas financieras asumen que los individuos tienen preferencia por la liquidez, valorando de forma distinta una misma cuantía dependiendo del momento en que se recibe [3].

#### 16.1.1.2. Ley Financiera
Una ley financiera es un modelo o función matemática ($F(z)$) que permite cuantificar la variación del valor del dinero en el tiempo. Se utiliza para proyectar capitales a un momento determinado $p$. Dependiendo de la dirección de la proyección, se distinguen dos tipos [4]:
*   **Leyes de capitalización:** Proyectan el capital hacia el futuro ($t < p$), sumando intereses [5].
*   **Leyes de descuento:** Proyectan el capital hacia el pasado o presente ($t > p$), restando el descuento [5].

#### 16.1.1.3. Operación financiera
Una operación financiera se define como el intercambio no simultáneo de capitales entre dos partes: prestamista (quien entrega la prestación o primer capital) y prestatario (quien entrega la contraprestación) [6], [7]. Para que la operación sea viable, debe existir **equilibrio financiero**, lo que significa que el valor de la prestación y la contraprestación deben ser equivalentes ($ \approx $) bajo una ley financiera y un punto de comparación pactados [8], [9].

#### 16.1.1.4. Características comerciales: tantos efectivos y tantos efectivos anuales (TAE)
Las operaciones financieras suelen conllevar gastos adicionales o características comerciales (comisiones, impuestos, gastos de gestión) que rompen la equivalencia estricta derivada del tanto pactado inicialmente [10].
*   **Tanto efectivo:** Es la tasa que realmente equilibra los capitales entregados y recibidos teniendo en cuenta todos los flujos (prestación, contraprestación y gastos) [11].
*   **TAE (Tasa Anual Equivalente):** Es una referencia normalizada por el Banco de España que permite comparar el coste o rendimiento real de productos financieros anualizando el tanto efectivo y considerando las comisiones y plazos [12], [13].

## 16.2. Leyes simples

### 16.2.1. Capitalización, descuento simple, tantos equivalentes y sustitución de capitales
Las leyes simples se caracterizan porque los intereses generados no se acumulan al capital para generar nuevos intereses en periodos siguientes; es decir, el interés es proporcional al capital inicial y al tiempo [14], [15]. Se utilizan habitualmente en operaciones a corto plazo (menos de un año) [16].

### 16.2.2. Capitalización simple a tanto vencido
En la capitalización simple, el montante final ($M$) se obtiene sumando al capital inicial ($C$) los intereses generados. La fórmula fundamental es:
$$ M = C \cdot (1 + i \cdot n) $$
Donde $i$ es el tanto de interés y $n$ la duración. La función es lineal respecto al tiempo ($1 + in$) [14], [15].

### 16.2.3. Descuento simple a tanto vencido
Conocido también como descuento racional o matemático. Se calcula sobre el capital inicial (valor actual). Es la operación inversa a la capitalización simple. El valor actual $C_0$ de un capital $C_n$ disponible en el futuro se determina dividiendo por el factor de capitalización:
$$ C_0 = \frac{C_n}{(1 + i \cdot n)} $$
Esto permite determinar el valor presente eliminando los intereses que se habrían generado [17], [18].

### 16.2.4. Descuento simple a tanto anticipado
Conocido como descuento comercial. En este caso, los intereses (o descuento) se calculan sobre el valor nominal (el capital final o futuro) y se pagan por adelantado. La ley financiera se expresa como:
$$ A(t, p) = 1 - d \cdot z $$
Donde $d$ es el tanto de descuento. El valor efectivo ($V$) de un nominal ($N$) se calcula como $V = N(1 - d \cdot n)$ [17], [18].

### 16.2.5. Tantos equivalentes
En capitalización simple, el tanto de interés ($i$) y el tanto de descuento ($d$) no son numéricamente iguales para una misma operación, aunque produzcan el mismo resultado financiero. La relación de equivalencia entre ambos (para un periodo unitario) es:
$$ d = \frac{i}{1 + i} \quad \text{o} \quad i = \frac{d}{1 - d} $$
Esto indica que el tipo de interés siempre es numéricamente mayor que el tipo de descuento equivalente [19], [20].

### 16.2.6. Sustitución de capitales: vencimiento común y vencimiento medio
La sustitución de capitales implica reemplazar un conjunto de capitales por otro único (o diferente conjunto) que sea financieramente equivalente [21].
*   **Vencimiento común:** Es el momento $t$ en el que un capital único $C$ es equivalente a la suma de varios capitales $C_1, C_2, \dots$ basándose en una ley financiera [22], [21].
*   **Vencimiento medio:** Es un caso particular del vencimiento común donde la cuantía del capital único es igual a la suma aritmética de las cuantías de los capitales a sustituir ($C = \sum C_i$). Se busca el punto de tiempo donde se cumple el equilibrio financiero bajo esta condición [21].

## 16.3. Operaciones a corto plazo

### 16.3.1. Descuentos efectos comerciales
Es una operación típica de corto plazo donde una entidad financiera anticipa el importe de un efecto (letra de cambio, pagaré) antes de su vencimiento, deduciendo los intereses (descuento) y comisiones [23], [24].
*   **Efectivo:** Es el valor que recibe el cliente tras restar al Nominal el descuento y otros gastos. Se usa la ley de descuento comercial simple: $E = N(1 - n \cdot d) - \text{Gastos}$ [25].

#### 16.3.1.1. Pago mediante Forfait
Aunque las fuentes no detallan la definición específica de "Forfait" bajo este epígrafe, en el contexto del temario de operaciones a corto plazo y descuento comercial [26], se refiere a una modalidad de descuento a tanto alzado o precio fijo acordado para la operación, simplificando el cálculo de costes financieros en operaciones comerciales [23].

#### 16.3.1.2. Letra de resaca
Dentro del descuento de efectos comerciales [26], si el efecto resulta impagado al vencimiento, surgen mecanismos de recuperación. La letra de resaca es un instrumento utilizado para cobrar el importe de una letra impagada más los gastos de protesto y recargos, girando una nueva letra. Se basa en los principios de valoración de deudas pendientes en operaciones de corto plazo descritos en las leyes de descuento [23], [24].

### 16.3.2. Liquidación de cuenta corriente de débito y de crédito
Las cuentas corrientes son operaciones de soporte con prestación y contraprestación múltiple [27]. Se liquidan mediante el método de números comerciales o hamburgués, calculando intereses sobre los saldos mantenidos durante los días que permanecen vigentes [23], [26].

#### 16.3.2.1. Cuenta corriente de débito
Se refiere a cuentas donde el titular deposita fondos (operación pasiva para el banco). Los intereses se generan a favor del cliente sobre los saldos acreedores [27], [26].

#### 16.3.2.2. Cuenta corriente de crédito
Conocidas como cuentas de crédito. Permiten al titular disponer de fondos hasta un límite concedido (operación activa para el banco). El cliente paga intereses por los saldos deudores (dinero dispuesto) y, habitualmente, una comisión sobre el saldo no dispuesto o sobre el máximo excedido [23], [28].

### 16.3.3. Operaciones con letras del tesoro

#### 16.3.3.1. Concepto
Las Letras del Tesoro son activos de Deuda Pública a corto plazo emitidos al descuento. Son operaciones financieras simples donde el inversor compra el título por un precio ($P$) inferior a su valor Nominal ($N$) que recibirá al vencimiento [29].

#### 16.3.3.2. Funcionamiento
La rentabilidad se obtiene por la diferencia entre el precio de compra (prestación) y el nominal recibido al vencimiento (contraprestación) [30], [31].
*   **Fecha de liquidación:** Momento de pago del precio.
*   **Fecha de vencimiento:** Momento de cobro del nominal.
El cálculo de rentabilidad utiliza la ley de capitalización simple (año civil de 360 o 365 días según convención) [30].

## 16.4. Leyes compuestas

### 16.4.1. Capitalización y descuentos compuestos

#### 16.4.1.1. Capitalización

##### 16.4.1.1.1. Concepto
La capitalización compuesta se caracteriza por ser acumulativa: los intereses generados en cada periodo se suman al capital inicial para generar nuevos intereses en los periodos siguientes [17]. Es la ley utilizada para valorar operaciones a largo plazo y realizar análisis de equivalencia financiera dinámica [32], [33].

##### 16.4.1.1.2. Operación
La fórmula fundamental que relaciona el capital final ($M$) con el inicial ($C$) tras $n$ periodos a un tanto $i$ es:
$$ M = C \cdot (1 + i)^n $$
El factor $(1+i)^n$ es el factor de capitalización compuesto. A diferencia de la simple, el crecimiento del capital no es lineal, sino exponencial [32], [33].

#### 16.4.1.2. Descuentos Compuestos

##### 16.4.1.2.1. Concepto
Es la operación inversa a la capitalización compuesta. Se utiliza para traer capitales futuros al momento presente (actualización), manteniendo la lógica de interés acumulativo (en sentido inverso) [18].

##### 16.4.1.2.2. Operación
El valor actual ($C_0$) de un capital futuro ($C_n$) se obtiene despejando de la fórmula de capitalización:
$$ C_0 = C_n \cdot (1 + i)^{-n} $$
Se utiliza para valorar flujos de caja futuros, como en el cálculo del VAN (Valor Actual Neto) [34], [21].

## 16.5. Valoración de rentas. Rentas constantes

### 16.5.1. Tipos de rentas constantes

#### 16.5.1.1. Concepto
Una renta financiera es un conjunto de capitales con vencimientos equidistantes en el tiempo. Si todos los capitales tienen la misma cuantía ($C_1 = C_2 = \dots = C$), se denomina renta constante [35].

### 16.5.2. Rentas constantes: temporales–pospagables

#### 16.5.2.1. Concepto
Son aquellas en las que los pagos (términos de la renta) se realizan al final de cada periodo (ej. vencimiento de mes o año) y tienen una duración finita [36].

#### 16.5.2.2. Operación
El Valor Actual ($V_0$) se calcula sumando los valores actualizados de cada pago. La fórmula de la anualidad pospagable ($a_{\overline{n}|i}$) es:
$$ V_0 = C \cdot \frac{1 - (1+i)^{-n}}{i} $$
[37], [38].

### 16.5.3. Rentas constantes: temporales–prepagables

#### 16.5.3.1. Concepto
Son rentas donde los capitales se hacen efectivos al principio de cada periodo (ej. alquileres que se pagan por adelantado) [39].

#### 16.5.3.2. Operación
Se obtienen multiplicando el valor de la renta pospagable por el factor de capitalización de un periodo $(1+i)$, ya que cada pago se adelanta un periodo respecto a la pospagable.
$$ \ddot{a}_{\overline{n}|i} = a_{\overline{n}|i} \cdot (1+i) $$
[40], [41].

### 16.5.4. Rentas constantes: temporales–diferidas

#### 16.5.4.1. Concepto
Son rentas cuyo primer pago o vencimiento se produce tras un periodo de carencia o espera ($d$ periodos antes de comenzar la renta normal) [42], [43].

#### 16.5.4.2. Operación
El valor actual se calcula obteniendo el valor de la renta inmediata y descontándolo por los periodos de diferimiento:
$$ V_0 = V_{\text{inmediato}} \cdot (1+i)^{-d} $$
[44], [43].

### 16.5.5. Rentas constantes: temporales–anticipadas

#### 16.5.5.1. Concepto
En la clasificación general, se refiere a aquellas valoradas en un momento posterior a la finalización de la renta (valor final) o rentas cuyos pagos se realizan al comienzo del intervalo (sinónimo de prepagable en algunos contextos, pero aquí se distingue como "anticipadas" en el sentido de valoración futura según el temario oficial en relación a [43]). Basado en [43], se tratan relaciones de valor final.

#### 16.5.5.2. Operación
El valor final ($S_n$) de una renta constante se obtiene capitalizando el valor actual o sumando los montantes de cada pago:
$$ S_{\overline{n}|i} = C \cdot \frac{(1+i)^n - 1}{i} $$
[37], [45].

### 16.5.6. Rentas constantes: perpetuas

#### 16.5.6.1. Concepto
Son rentas cuya duración es ilimitada, es decir, el número de términos tiende a infinito ($n \to \infty$) [42].

#### 16.5.6.2. Operación
El valor actual de una renta perpetua pospagable unitaria se simplifica al límite de la fórmula temporal:
$$ V_0 = \frac{C}{i} $$
No tiene sentido calcular el valor final, pues tiende a infinito [46], [47].

## 16.6. Valoración de rentas. Rentas variables

### 16.6.1. Renta variable en progresión geométrica

#### 16.6.1.1. Temporal

##### 16.6.1.1.1. Concepto
Los términos de la renta varían siguiendo una progresión geométrica, multiplicándose por una razón constante $q$ (o $1+g$ donde $g$ es la tasa de crecimiento) en cada periodo [48].

##### 16.6.1.1.2. Operación
El valor actual depende de la relación entre la razón de la progresión ($q$) y el factor de actualización. Si la razón $q \neq 1+i$, la suma es finita y calculable mediante fórmula específica que combina el primer pago, la razón $q$ y el tipo de interés $i$ [40].

#### 16.6.1.2. Perpetua

##### 16.6.1.2.1. Concepto
Renta variable geométrica con duración infinita. Solo es valorable si la razón de crecimiento $q$ es menor que $1+i$ [47].

##### 16.6.1.2.2. Operación
El valor actual se simplifica considerablemente:
$$ V_0 = \frac{C_1}{i - g} $$
(Asumiendo $q = 1+g$) [40].

### 16.6.2. Renta variable en progresión aritmética

#### 16.6.2.1. Temporal

##### 16.6.2.1.1. Concepto
Los términos varían sumando una cantidad constante $d$ (diferencia) en cada periodo respecto al anterior ($C_2 = C_1 + d$, etc.) [48], [49].

##### 16.6.2.1.2. Operación
El valor actual se descompone en una parte fija (renta constante del primer término) y una parte variable que depende de la diferencia $d$ y una renta unitaria aritmética [50].

#### 16.6.2.2. Perpetua

##### 16.6.2.2.1. Concepto
Renta aritmética con número infinito de términos [46].

##### 16.6.2.2.2. Operación
Se calcula el límite cuando $n \to \infty$ de la fórmula temporal. Se compone del valor actual de la renta perpetua del primer término más el valor actual de la perpetuidad de la diferencia [51].

## 16.7. Valoración de rentas. Rentas fraccionadas

### 16.7.1. Renta constante fraccionada

#### 16.7.1.1. Concepto
Ocurre cuando la frecuencia de los pagos es distinta a la frecuencia del tipo de interés base (generalmente anual). Por ejemplo, pagos mensuales con un tipo anual. Implica dividir el periodo en sub-periodos $m$ [38], [52].

#### 16.7.1.2. Operación
Se utilizan tantos equivalentes ($i_m$ o $J_m$). Se debe homogeneizar el tiempo y el tanto. El valor actual se calcula usando el tipo de interés fraccionado correspondiente a la frecuencia de pago [53], [33].

### 16.7.2. Renta variable en progresión geométrica fraccionada

#### 16.7.2.1. Concepto
Los pagos son sub-periódicos (ej. mensuales) y varían geométricamente.

#### 16.7.2.2. Operación
Se combina la lógica de la renta geométrica con la equivalencia de tantos fraccionados ($i^{(m)}$), ajustando la razón de variación a la frecuencia de pago [47].

### 16.7.3. Renta variable en progresión aritmética fraccionada

#### 16.7.3.1. Concepto
Pagos fraccionados que varían mediante una diferencia constante en cada sub-periodo.

#### 16.7.3.2. Operación
Se aplica la fórmula de renta aritmética utilizando el interés del sub-periodo y el número total de sub-periodos ($n \cdot m$) [47].

### 16.7.4. Renta perpetua fraccionada

#### 16.7.4.1. Concepto
Pagos infinitos con frecuencia superior a la anual.

#### 16.7.4.2. Operación
Se calcula utilizando el tipo de interés nominal ($J_m$) o el fraccionado ($i_m$) en el denominador, aplicando el límite al infinito [46].

### 16.7.5. Renta fraccionada no uniforme

#### 16.7.5.1. Concepto
Rentas donde los pagos fraccionados no siguen una ley de variación uniforme simple (ni puramente geométrica ni puramente aritmética en todos los niveles) o varían en bloques.

#### 16.7.5.2. Operación
Se valoran generalmente agrupando términos o convirtiéndolos en rentas anuales equivalentes para simplificar el cálculo, o sumando los valores actuales individuales si no hay patrón [54].

## 16.8. Préstamos

### 16.8.1. Sistema americano

#### 16.8.1.1. Concepto
Método de amortización donde el prestatario paga periódicamente solo los intereses generados por el principal. El capital prestado ($C_0$) se devuelve íntegramente en un único pago al final de la operación [55], [56].

#### 16.8.1.2. Operación
*   **Cuota periódica:** Solo intereses ($I = C_0 \cdot i$).
*   **Última cuota:** Intereses más el capital total ($I + C_0$).
A menudo se asocia con la constitución de un fondo (Sinking Fund) para acumular el capital final necesario [57], [58].

### 16.8.2. Sistema francés

#### 16.8.2.1. Concepto
También llamado sistema de **cuotas constantes**. El prestatario paga una cantidad fija (término amortizativo) al final de cada periodo, que incluye una parte de interés y una parte de amortización de capital [55], [59].

#### 16.8.2.2. Operación
El término amortizativo ($a$) se calcula mediante la equivalencia financiera:
$$ C_0 = a \cdot a_{\overline{n}|i} \rightarrow a = \frac{C_0 \cdot i}{1 - (1+i)^{-n}} $$
A medida que pasa el tiempo, la parte de interés de la cuota disminuye (al bajar la deuda viva) y la parte de amortización de capital aumenta [60], [61].

### 16.8.3. Préstamo a tipo variable y cuotas de amortización constante

#### 16.8.3.1. Concepto
Préstamos donde el tipo de interés se revisa periódicamente según un índice de referencia (como el Euribor). El sistema descrito en el temario ("cuotas de amortización constante") se refiere al **Método Italiano** o de cuota de amortización capital constante, aunque aplicado a entornos de tipo variable [55], [62].

#### 16.8.3.2. Operación
*   La cuota de amortización de capital ($A$) es fija: $A = C_0 / n$.
*   La cuota de interés ($I_k$) varía en cada periodo según el capital vivo restante y el tipo de interés vigente en ese momento ($i_k$).
*   El término amortizativo total ($a_k$) es variable: $a_k = A + I_k$ [63], [64].

***

# Resumen de 3 Puntos Clave

1.  **Fundamentos y Equivalencia:** Las operaciones financieras se basan en el intercambio de capitales en diferentes momentos del tiempo. Para que sean viables, deben cumplir el principio de **equivalencia financiera**, donde el valor de la prestación y la contraprestación se igualan bajo una ley financiera (simple o compuesta) acordada.
2.  **Leyes Financieras:** La **capitalización simple** se utiliza para operaciones a corto plazo (crecimiento lineal), mientras que la **capitalización compuesta** es la norma para el largo plazo y la valoración de rentas, caracterizándose por el carácter acumulativo de los intereses (crecimiento exponencial).
3.  **Amortización de Préstamos:** Existen diversos métodos para devolver un capital ajeno. Destacan el **sistema francés** (pagos totales constantes, con interés decreciente y amortización creciente) y el **sistema americano** (pago periódico solo de intereses y devolución del capital al final).
<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-3 mb-8">
        <span class="text-blue-500 font-mono text-xs shrink-0 self-start sm:self-auto mt-1 sm:mt-0">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-lg sm:text-xl break-words leading-tight">Esquema Conceptual Módulo A16</h3>
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

    </div>
</div>
