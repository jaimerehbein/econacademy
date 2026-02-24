# M8: Economía industrial

## Tema 1: Fundamentos Teóricos y el Paradigma Estructura-Conducta-Desempeño

### Subtema 1.1: Definición y Evolución del Campo
La Organización Industrial (OI) se define como la rama de la microeconomía que profundiza en el estudio de la estructura y el funcionamiento de los mercados, poniendo especial énfasis en las interacciones estratégicas entre las empresas y en cómo la política pública influye sobre estos elementos [1]. A diferencia del modelo de competencia perfecta, que asume a los agentes como tomadores de precios, la OI se centra en el análisis de mercados imperfectos donde las empresas poseen poder de mercado, entendido como la capacidad de fijar precios por encima del costo marginal [2]. Históricamente, la disciplina ha evolucionado desde el paradigma **Estructura-Conducta-Desempeño (ECD)**, popularizado por Joe Bain y la Escuela de Harvard en los años 50, hacia la **Nueva Organización Industrial (NOI)**, la cual utiliza la teoría de juegos para modelar decisiones estratégicas complejas [3, 4].

El paradigma ECD postula una causalidad unidireccional: la estructura del mercado (concentración, barreras de entrada, diferenciación) determina la conducta de las empresas (políticas de precios, publicidad, I+D), lo que a su vez dicta el desempeño del mercado (eficiencia, rentabilidad, progreso técnico) [5]. Sin embargo, este enfoque ha sido criticado y refinado, reconociendo que la conducta también puede alterar la estructura (por ejemplo, mediante precios predatorios o fusiones) y que existen variables exógenas y políticas públicas que afectan todo el sistema. En la actualidad, el análisis se ha vuelto más riguroso matemáticamente, integrando modelos de equilibrio parcial y teoría de juegos para explicar fenómenos como la colusión tácita y la disuasión de entrada, superando las regresiones lineales simples de corte transversal que caracterizaban a los estudios empíricos iniciales [6].

### Subtema 1.2: Eficiencia y Bienestar Social
El análisis normativo en economía industrial se fundamenta en el concepto de **eficiencia**, generalmente desglosada en eficiencia asignativa y eficiencia productiva. La eficiencia asignativa se logra cuando el precio se iguala al costo marginal ($P = CMg$), maximizando el excedente total (la suma del excedente del consumidor y el beneficio del productor) [7, 8]. Cualquier desviación de esta igualdad, típica en monopolios y oligopolios, genera una pérdida irrecuperable de eficiencia o costo social, representada gráficamente por el triángulo de Harberger [9, 10]. Por otro lado, la eficiencia productiva implica minimizar los costos para un nivel dado de producción. Existe un debate académico persistente, impulsado por la Escuela de Chicago (notablemente Demsetz), que sugiere que la concentración de mercado puede ser resultado de una mayor eficiencia productiva de ciertas firmas y no necesariamente de prácticas anticompetitivas [11].

La medición del bienestar se complica al introducir consideraciones dinámicas. Schumpeter argumentó que cierto grado de poder de mercado (monopolio temporal) podría ser necesario para incentivar la innovación y la eficiencia dinámica, una tensión que es central en el diseño de políticas de patentes y defensa de la competencia [12]. Formalmente, el excedente total ($W$) se define como la integral de la función de demanda inversa menos el costo total: $W = \int_{0}^{Q} P(x)dx - CT(Q)$ [13]. La maximización de esta función respecto a la cantidad $Q$ confirma la condición de primer orden de precio igual a costo marginal, sirviendo como *benchmark* para evaluar las distorsiones de mercado provocadas por el poder de mercado y la regulación [14].

## Tema 2: Monopolio y Poder de Mercado

### Subtema 2.1: Maximización y el Índice de Lerner
El monopolista, al enfrentar toda la demanda del mercado, internaliza el efecto de su producción sobre el precio. Su problema de maximización de beneficios, $\max \pi(Q) = P(Q)Q - C(Q)$, lleva a la condición de primer orden donde el ingreso marginal ($IM$) iguala al costo marginal ($CMg$) [15, 16]. Dado que la curva de demanda tiene pendiente negativa, el $IM$ siempre es menor que el precio, lo que resulta en un equilibrio donde $P > CMg$. La magnitud de esta distorsión se mide a través del **Índice de Lerner** ($L$), definido como $L = \frac{P - CMg}{P} = \frac{1}{|\varepsilon|}$, donde $\varepsilon$ es la elasticidad-precio de la demanda [17, 18]. Esta ecuación fundamental revela que el poder de mercado es inversamente proporcional a la elasticidad de la demanda; cuanto más inelástica sea la demanda, mayor será el margen que el monopolista puede fijar sobre sus costos.

Una extensión crítica de este modelo básico es el monopolio multiproducto. Cuando una empresa produce bienes sustitutos o complementarios, la regla de fijación de precios se ajusta para considerar las elasticidades cruzadas ($\varepsilon_{ij}$). Si los bienes son sustitutos, la empresa tenderá a fijar precios más altos que si fueran independientes para mitigar la canibalización; si son complementarios, podría fijar precios más bajos para estimular la demanda conjunta [19, 20]. Formalmente, la condición de primer orden para el producto $i$ incorpora un término que ajusta por el efecto en el beneficio de los otros productos $j$: $\frac{P_i - C'_i}{P_i} = \frac{1}{\varepsilon_{ii}} - \sum_{j \neq i} \frac{(P_j - C'_j) D_j \varepsilon_{ij}}{R_i \varepsilon_{ii}}$ [19].

### Subtema 2.2: La Conjetura de Coase y Bienes Duraderos
El análisis del monopolio se complejiza significativamente cuando se consideran bienes duraderos. Ronald Coase planteó la hipótesis de que un monopolista de bienes duraderos compite contra sus propias ventas futuras. Si los consumidores son racionales y anticipan que el monopolista bajará el precio en el futuro para capturar a los consumidores con menor valoración (discriminación intertemporal), pospondrán su compra [21, 22]. En el límite, si el monopolista puede ajustar precios instantáneamente, pierde todo su poder de mercado y el precio converge al costo marginal competitivo inmediatamente; esto se conoce como la **Conjetura de Coase** [22, 23].

Para mitigar este problema de credibilidad y compromiso, el monopolista puede adoptar estrategias como el arrendamiento (leasing) en lugar de la venta, la obsolescencia programada, o compromisos contractuales de no bajar precios (cláusulas de "nación más favorecida") [24, 25]. El modelo formal de dos periodos demuestra que, sin compromiso, el precio del primer periodo debe ser menor que el precio de monopolio estático para compensar la expectativa de reducción futura. Si $\delta$ es el factor de descuento, a medida que $\delta \to 1$ (periodos muy cortos), el beneficio del monopolista tiende a cero, validando la intuición de Coase de que la durabilidad del bien erosiona el poder de mercado [26, 27].

## Tema 3: Modelos de Oligopolio Estático

### Subtema 3.1: Competencia en Cantidades (Cournot)
El modelo de Cournot es fundamental para entender mercados donde las empresas deciden simultáneamente la cantidad a producir, y el precio de mercado ajusta la oferta a la demanda. Bajo este modelo, cada empresa asume que la cantidad de su rival es fija y maximiza su beneficio en función de su propia producción, lo que deriva en funciones de reacción [28, 29]. Para un duopolio con demanda lineal $P = a - b(q_1 + q_2)$ y costo marginal constante $c$, la función de reacción de la empresa 1 es $q_1 = \frac{a - c - bq_2}{2b}$ [28]. El equilibrio de Nash se encuentra en la intersección de estas funciones de reacción.

Una propiedad clave del modelo de Cournot es que el resultado se sitúa entre el monopolio y la competencia perfecta. A medida que el número de empresas ($N$) aumenta, el margen precio-costo disminuye y converge al nivel competitivo cuando $N \to \infty$ [30, 31]. Analíticamente, el índice de Lerner en Cournot para una empresa $i$ está dado por $L_i = \frac{s_i}{|\varepsilon|}$, donde $s_i$ es la cuota de mercado [32]. Esto implica que las empresas con mayor participación de mercado tienen mayores márgenes, y que el poder de mercado agregado está relacionado con el Índice Herfindahl-Hirschman (HHI), estableciendo un vínculo formal entre estructura (concentración) y desempeño (márgenes) [33].

### Subtema 3.2: Competencia en Precios (Bertrand)
El modelo de Bertrand asume que las empresas compiten eligiendo precios para un producto homogéneo. La conclusión clásica, conocida como la **Paradoja de Bertrand**, es que incluso con solo dos empresas, la competencia feroz lleva el precio al nivel del costo marginal ($P = CMg$), eliminando los beneficios económicos [34, 35]. Esto ocurre porque, si una empresa fija un precio superior al costo marginal, la rival tiene incentivos para subcotizarla ligeramente (undercutting) y capturar todo el mercado, desatando una guerra de precios [36, 37].

Sin embargo, este resultado es muy sensible a los supuestos. La paradoja se resuelve (es decir, los precios suben por encima del costo marginal) si se introducen restricciones de capacidad (modelo de Edgeworth) o diferenciación de productos [38, 39]. En el modelo de **Kreps y Scheinkman**, se demuestra que si las empresas eligen primero capacidad y luego compiten en precios, el resultado reproduce el equilibrio de Cournot, lo que sugiere que Cournot es una forma reducida adecuada para industrias donde la capacidad es una decisión de largo plazo y los precios de corto plazo [40].

### Subtema 3.3: Liderazgo y Stackelberg
El modelo de Stackelberg introduce una dinámica secuencial donde una empresa ("Líder") decide su cantidad antes que la otra ("Seguidora"). El líder anticipa la función de reacción del seguidor e incorpora esta información en su propia maximización [41]. Matemáticamente, si la demanda es $P = 100 - (q_L + q_S)$, el líder maximiza $\pi_L = (100 - q_L - R_S(q_L))q_L - C(q_L)$, donde $R_S$ es la función de reacción de Cournot del seguidor.

Este modelo suele arrojar un beneficio mayor para el líder y menor para el seguidor en comparación con el equilibrio de Cournot, debido a la ventaja del primer movimiento ("first-mover advantage") [42]. El líder produce más y el seguidor menos, resultando en una cantidad total mayor y un precio menor, lo que incrementa el bienestar social respecto a Cournot [42]. Este marco es esencial para analizar mercados con asimetrías claras, como una empresa dominante establecida frente a nuevos entrantes o competidores periféricos [43].

## Tema 4: Diferenciación de Productos

### Subtema 4.1: Diferenciación Horizontal (Hotelling y Salop)
La diferenciación horizontal aborda situaciones donde, a igualdad de precios, los consumidores discrepan sobre qué producto es preferible debido a gustos variados o localización. El modelo de la **Ciudad Lineal de Hotelling** representa a los consumidores distribuidos en un segmento [44] y a las empresas eligiendo ubicación y precios. La utilidad del consumidor depende del precio y del costo de transporte (lineal o cuadrático) hasta la empresa [45]. Con costos de transporte cuadráticos, se evitan discontinuidades en la demanda y se demuestra que las empresas tienden a diferenciarse al máximo (ubicándose en los extremos) para suavizar la competencia en precios [46].

Una extensión es el modelo de la **Ciudad Circular de Salop**, útil para analizar la entrada de empresas en el largo plazo. Aquí, las empresas se distribuyen en un círculo para evitar la competencia directa. El equilibrio muestra un *trade-off* entre costos fijos de entrada y costos de transporte agregados: el mercado libre tiende a generar un número de empresas (variedad) excesivo en comparación con el óptimo social, debido a que las empresas entrantes no internalizan el efecto de "robo de negocio" sobre sus rivales [47, 48].

### Subtema 4.2: Diferenciación Vertical (Shaked y Sutton)
La diferenciación vertical ocurre cuando todos los consumidores concuerdan en que un producto es superior a otro (mayor calidad), pero difieren en su capacidad o disposición a pagar por esa calidad [49]. El modelo de Shaked y Sutton muestra que, incluso con costos de producción nulos para la calidad, solo un número limitado de empresas puede coexistir en el mercado con beneficios positivos, una propiedad conocida como "finitud natural" [50].

A diferencia de la diferenciación horizontal, donde el mercado puede fragmentarse infinitamente al crecer la demanda, en la diferenciación vertical la competencia de precios entre productos de alta y baja calidad puede expulsar a los de baja calidad si la diferencia de precios no compensa la diferencia de calidad. Esto explica la alta concentración en industrias donde la inversión en calidad (publicidad, I+D) es un costo hundido endógeno [51].

## Tema 5: Colusión y Juegos Dinámicos

### Subtema 5.1: Sostenibilidad de la Colusión Tácita
La colusión se analiza mediante la teoría de juegos repetidos (superjuegos). El **Teorema del Pueblo (Folk Theorem)** establece que si las empresas valoran suficientemente el futuro (factor de descuento $\beta$ alto), es posible sostener precios de monopolio mediante estrategias de gatillo (*trigger strategies*) [52, 53]. Estas estrategias implican cooperar mientras los rivales cooperen, pero revertir al equilibrio de Nash (competencia dura) permanentemente o por un tiempo determinado si alguien se desvía (hace trampa).

La condición de estabilidad para la colusión es $V_{col} \geq V_{desvio}$, lo que se traduce en $\frac{\pi_m}{1-\beta} \geq \pi_d + \frac{\beta \pi_c}{1-\beta}$, donde $\pi_m, \pi_d, \pi_c$ son los beneficios de monopolio (colusión), desvío y competencia (castigo) respectivamente. Resolviendo para $\beta$, se obtiene un umbral crítico: la colusión es sostenible si $\beta \geq \frac{\pi_d - \pi_m}{\pi_d - \pi_c}$ [54]. Factores como el número reducido de empresas, la simetría de costos, la transparencia del mercado y la frecuencia de interacción facilitan la colusión al reducir este umbral o facilitar el monitoreo [55].

### Subtema 5.2: Guerras de Precios y Monitoreo Imperfecto
En la realidad, la demanda fluctúa y las acciones de los rivales no siempre son observables perfectamente. El modelo de **Green y Porter (1984)** explica las guerras de precios no como un colapso de la colusión, sino como parte del equilibrio en un entorno de incertidumbre [56]. Si una empresa observa una caída en su demanda, no sabe si se debe a un shock de mercado (baja demanda general) o a que un rival ha bajado precios secretamente.

Para mantener los incentivos, el cartel debe entrar en una fase de castigo (guerra de precios) cada vez que el precio de mercado cae por debajo de cierto umbral ("precio de gatillo"), aunque esto ocurra por causas exógenas [57]. Esto resulta en periodos alternados de altos precios (colusión) y bajos precios (castigo). Rotemberg y Saloner (1986) añaden que la tentación de desviarse es mayor en periodos de alta demanda (booms), por lo que los carteles podrían necesitar bajar precios en los auges para evitar la ruptura, lo que resulta contraintuitivo [58].

## Tema 6: Barreras a la Entrada y Comportamiento Estratégico

### Subtema 6.1: Precios Límite y Depredación
Las empresas establecidas pueden comportarse estratégicamente para disuadir la entrada. El modelo de **precios límite** sugiere que un incumbente puede fijar un precio inferior al de monopolio para señalar a potenciales entrantes que sus costos son bajos (información asimétrica), haciendo que la entrada parezca no rentable [59, 60]. Milgrom y Roberts formalizaron esto como un equilibrio de señalización, donde una empresa eficiente sacrifica beneficios a corto plazo para separar su tipo de una empresa ineficiente y disuadir la entrada [61].

La **depredación de precios** implica fijar precios por debajo del costo (generalmente costo variable medio, según la regla Areeda-Turner) para expulsar rivales y luego subir precios [62]. Aunque la Escuela de Chicago argumentó que la depredación es irracional (es más barato fusionarse que incurrir en pérdidas para ambos), modelos modernos de teoría de juegos (reputación, "bolsillo profundo") demuestran que puede ser un equilibrio racional si sirve para construir una reputación de agresividad que disuada futuras entradas en múltiples mercados [63, 64].

### Subtema 6.2: Mercados Desafiables y Costos Hundidos
La teoría de los **Mercados Desafiables (Contestable Markets)** de Baumol, Panzar y Willig postula que si no existen costos hundidos (sunk costs) y la entrada/salida es ultralibre, la amenaza de entrada potencial es suficiente para disciplinar a un monopolista, obligándolo a fijar precios iguales al costo medio y obteniendo beneficios cero, incluso con una sola empresa en el mercado [65].

Sin embargo, la presencia de costos hundidos (inversiones irrecuperables) actúa como una barrera de entrada formidable. Sutton introduce el concepto de **costos hundidos endógenos** (publicidad, I+D), que son decididos por las empresas. En industrias con costos hundidos endógenos, un aumento en el tamaño del mercado no fragmenta la estructura industrial (como en competencia perfecta), sino que eleva la inversión en estos costos, manteniendo la concentración alta y elevando las barreras para nuevos competidores [66, 67].

## Tema 7: Relaciones Verticales y Restricciones

### Subtema 7.1: Doble Marginalización
Cuando un monopolista productor vende a un monopolista minorista, surge el problema de la **doble marginalización**. Ambos agregan su propio margen de beneficio ($mark-up$), resultando en un precio final al consumidor ($P_m$) mayor que el precio de monopolio integrado ($P_I$) y una cantidad menor ($Q_m < Q_I$) [68]. Esto es perjudicial tanto para las empresas (menores beneficios conjuntos) como para los consumidores.

Si el productor fija el precio mayorista $r$, el minorista maximiza $\pi_D = (P - r)Q$. La condición de primer orden del minorista genera una demanda derivada para el productor. La integración vertical o la imposición de restricciones verticales, como la **Fijación de Precios de Reventa (RPM)** (específicamente precios máximos) o tarifas en dos partes, puede resolver esta externalidad vertical, restaurando el precio y cantidad del monopolio integrado y mejorando la eficiencia [69, 70].

### Subtema 7.2: Exclusividad y Free-Riding
Las restricciones verticales también abordan externalidades horizontales entre distribuidores, como el problema del **free-riding** en servicios de preventa. Si un minorista invierte en exhibición y asesoramiento (aumentando la demanda del producto), pero los consumidores pueden informarse allí y luego comprar en un minorista de descuento que no invierte, el primer minorista dejará de prestar el servicio [71].

Para corregir esta falla de mercado, el fabricante puede imponer territorios exclusivos o fijación de precios mínimos de reventa, eliminando la competencia en precios entre minoristas y forzándolos a competir en calidad de servicio [72]. Sin embargo, estas prácticas también pueden tener efectos anticompetitivos, como el cierre de mercado (*foreclosure*) a productores rivales mediante contratos de exclusividad, elevando los costos de los rivales (*raising rivals' costs*) [73, 74].

## Tema 8: Organización Industrial Empírica (NEIO)

### Subtema 8.1: Estimación de Poder de Mercado
La Nueva Organización Industrial Empírica (NEIO) busca estimar el poder de mercado sin observar directamente los costos marginales, los cuales son raramente conocidos. El enfoque de **Bresnahan-Lau** consiste en estimar simultáneamente una función de demanda y una relación de oferta que incluye un "parámetro de conducta" ($\theta$) [75, 76].

La relación de oferta se especifica como $P = CMg + \theta \cdot \frac{Q}{\partial Q / \partial P}$. Si $\theta = 0$, el mercado es competitivo ($P=CMg$); si $\theta = 1$, es un monopolio o cartel perfecto; valores intermedios indican oligopolio de Cournot u otras formas de competencia imperfecta [77]. La identificación econométrica de $\theta$ requiere variables exógenas que roten la curva de demanda (desplazadores) para trazar la relación de oferta y distinguirla de cambios en costos [78].

### Subtema 8.2: Técnicas de Estimación
Los métodos modernos utilizan modelos estructurales de elección discreta (como Logit o BLP - Berry, Levinsohn y Pakes) para estimar demandas de productos diferenciados. Estos modelos permiten calcular elasticidades cruzadas y simular efectos de fusiones sin asumir formas funcionales restrictivas [79].

Otro enfoque es el análisis no paramétrico o de preferencia revelada, que busca bounds (límites) sobre el comportamiento sin especificar formas funcionales completas [80]. Además, se estudian funciones de producción y fronteras estocásticas para medir la ineficiencia técnica y las economías de escala, cruciales para determinar si un mercado es un monopolio natural [81].

## Tema 9: Regulación y Política de Competencia

### Subtema 9.1: Regulación del Monopolio Natural
El monopolio natural surge cuando la subaditividad de costos hace que una sola empresa sea más eficiente que varias [82]. La regulación óptima ("Primer Mejor") de $P=CMg$ genera pérdidas si hay costos medios decrecientes [83]. Por ello, se utilizan soluciones de "Segundo Mejor" como los **Precios de Ramsey-Boiteux**, donde los precios se elevan por encima del costo marginal inversamente a la elasticidad de la demanda ($\frac{P_i - C'_i}{P_i} = \frac{k}{\varepsilon_i}$) para cubrir el déficit con la menor distorsión posible [84, 85].

En la práctica, la regulación ha transitado desde la Tasa de Retorno (que induce el **efecto Averch-Johnson** de sobrecapitalización por el incentivo de inflar la base de capital [86]) hacia mecanismos de incentivos de alto poder como el **Price-Cap** (IPC-X), que incentiva la eficiencia al permitir que la empresa retenga los ahorros de costos temporalmente [87].

### Subtema 9.2: Política Antitrust y Fusiones
La política de competencia tiene dos pilares: la sanción de conductas anticompetitivas (carteles, abuso de posición dominante) y el control de fusiones [88]. En el análisis de fusiones, el objetivo es prevenir un aumento significativo del poder de mercado. El análisis comienza definiendo el **Mercado Relevante** utilizando el test del monopolista hipotético (SSNIP) y calculando las cuotas de mercado [89].

Se evalúan los efectos unilaterales (la empresa fusionada sube precios unilateralmente) y coordinados (facilita la colusión tácita). Un *trade-off* fundamental, formalizado por Oliver Williamson, es la comparación entre la pérdida de eficiencia asignativa (aumento de precios/pérdida de peso muerto) y la ganancia en eficiencia productiva (reducción de costos/sinergias) que la fusión podría generar [90]. Si las eficiencias son suficientemente grandes, pueden compensar el daño a los consumidores, justificando la aprobación de la fusión ("Efficiency Defense") [91].

---

## Puntos Clave

1.  **Poder de Mercado y Eficiencia:** La existencia de poder de mercado (capacidad de fijar $P > CMg$) es la falla central que estudia la OI, generando ineficiencia asignativa (pérdida de bienestar social) que justifica la intervención regulatoria o antitrust, aunque en contextos dinámicos (Schumpeter) puede incentivar la innovación.
2.  **Interacción Estratégica:** Los modelos de oligopolio (Cournot, Bertrand, Stackelberg) demuestran que el resultado del mercado depende críticamente de la variable estratégica (cantidad vs. precio), el timing de las decisiones y la diferenciación del producto; Bertrand con productos homogéneos lleva a resultados competitivos, mientras que Cournot y la diferenciación preservan márgenes positivos.
3.  **Barreras y Disuasión:** La estructura de mercado no es estática; las empresas establecidas pueden manipularla estratégicamente creando barreras endógenas (publicidad, capacidad excedente, proliferación de marcas) o utilizando precios límite y predatorios para disuadir la entrada y proteger sus rentas monopólicas.
4.  **Problemas de Información y Regulación:** La regulación de monopolios naturales enfrenta asimetrías de información fundamentales; mecanismos modernos como el *Price-Cap* o la competencia por el mercado (subastas de franquicias) buscan alinear los incentivos de la empresa con el bienestar social, mitigando ineficiencias como el efecto Averch-Johnson.
5.  **Identificación Empírica:** La NEIO permite medir el poder de mercado real ($\theta$) mediante la estimación estructural de oferta y demanda, superando las limitaciones del paradigma ECD al no inferir conducta directamente de la concentración, sino estimando parámetros de comportamiento a partir de datos observables.
<!-- VISUAL_ENRICHMENT -->
<div class="my-16">
    <div class="flex items-center gap-3 mb-8">
        <span class="text-teal-500 font-mono text-xs">[DIAGRAMA]</span>
        <h3 class="text-white font-bold text-xl">Esquema Conceptual Módulo M8</h3>
    </div>
    <div class="bg-black/30 p-2 md:p-6 rounded-2xl border border-white/5 overflow-x-auto">
        
        <pre class="mermaid bg-transparent flex justify-center">
graph LR
    A[Fundamentos Teóricos] --> B(Aplicación Práctica)
    B --> C{Análisis Crítico}
    C -->|Evaluación| D[Validación Empírica]
    C -->|Revisión| E[Ajuste de Modelo]
    
    classDef default fill:#111827,stroke:#14b8a6,stroke-width:1px,color:#d1d5db
    classDef decision fill:#134e4a,stroke:#14b8a6,stroke-width:2px,color:#fff
    class C decision
        </pre>

    </div>
</div>
