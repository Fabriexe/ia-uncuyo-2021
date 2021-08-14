# IA FUNDAMENTOS FILOSOFICOS

Los filósofos definen la hipótesis de la IA débil como la afirmación de que es posible que las máquinas actúen con inteligencia, la hipótesis de la IA fuerte consiste en la afirmación de que las máquinas sí piensan realmente

## IA Débil

Algunos filósofos han intentado demostrar que la IA es imposible; que las máquinas no
tendrán la posibilidad de actuar inteligentemente.
En esencia,la IA consiste en la búsqueda del mejor programa agente en una arquitectura dada. Con
esta formulación, la IA es posible por definición: para cualquier arquitectura digital de
k bits de almacenamiento existirán exactamente 2k programas agente y todo lo que habrá que hacer para encontrar el mejor es enumerarlos y probar todos ellos. Esto podría
no ser viable para una k grande, pero los filósofos abordan más la teoría que la práctica.Sin
embargo, los filósofos están interesados en el problema de comparar dos arquitecturas,
la humana y la de la máquina. Además, ellos por tradición han formulado la pregunta
de la siguiente manera: «¿Pueden pensar las máquinas?»
Alan Turing sugirió que en vez de preguntar si las máquinas pueden pensar, deberíamos
preguntar si las máquinas pueden aprobar un test de inteligencia conductiva conocido como el Test de Turing. La prueba se realiza para que el programa
mantenga una conversación durante cinco minutos con un interrogador Éste tiene que averiguar si la conversación se
está llevando a cabo con un programa o con una persona; si el programa engaña al
interlocutor un 30 por ciento del tiempo, este pasará la prueba. Turing conjeturó que, haciael año 2000, un computador con un almacenamiento de 109 unidades podría llegar a programarse lo suficientemente bien como para pasar esta prueba, pero no estaba en lo cierto.  
Turing también examinó una gran gama de posibles objeciones ante la posibilidad
de las máquinas inteligentes, incluyendo virtualmente aquellas que han aparecido medio siglo después de que apareciera este artículo. Examinaremos algunas de ellas.  

### El argumento de incapacidad

El «argumento de incapacidad» afirma que «una máquina nunca puede hacer X». Como
ejemplos de X:
>Ser amable, tener recursos, ser guapo, simpático, tener iniciativas, tener sentido del
humor, distinguir lo correcto de lo erróneo, cometer errores, enamorarse, disfrutar con
las fresas con nata, hacer que otra persona también se enamore, aprender de la experiencia,
utilizar palabras de forma adecuada, ser el tema de su propio pensamiento, tener tanta
diversidad de comportamientos como el hombre, hacer algo realmente nuevo.

Actualmente hacen muchas cosas que anteriormente eran sólo del dominio humano. Los programas juegan a la ajedrez, a las damas y a otros juegos, inspeccionan piezas de las líneas de
producción, comprueban la ortografía en los documentos de los procesadores de texto,
conducen coches y helicópteros, diagnostican enfermedades, y hacen otros cientos de
tareas tan bien o mejor que los hombres. Los computadores han hecho pequeños pero
significativos descubrimientos.  
Paul Meehl  estudió
los procesos de la toma de decisiones de expertos formados en tareas subjetivas como
predecir el éxito de un alumno en un programa de formación, o la reincidencia de un delincuente Desde el año 1999, el Educational Testing Serviceha utilizado un programa automatizado para calificar millones depreguntas de redacciones en el examen GMAT. Este programa concuerda con los examinadores en un 97 por ciento, aproximadamente al mismo nivel de concordancia entre dos personas (Burstein et al., 2001).  
Es evidente que los computadores pueden hacer muchas cosas tan bien o mejor que
el ser humano, incluso cosas que las personas creen que requieren mucha intuición y entendimiento humano. Por supuesto, esto no significa que los computadores utilicen la
intuición y el entendimiento para realizar estas tareas,También es cierto, desde luego, que existen todavía muchas tareas en donde los computadores no sobresalenincluida la tarea de Turing de mantener una conversación abierta.

### La objeción matemática
ciertas
cuestiones matemáticas, en principio, no pueden ser respondidas por sistemas formales
concretos. El teorema de la incompletitud de Gödel es el ejemplo más conocido en este respecto. En resumen, para cualquier sistema axiomático formal F lo suficientemente potente como para hacer aritmética, es posible construir una
«sentencia Gödel» G(F) con las propiedades siguientes:
- G(F) es una sentencia de F, pero no se puede probar dentro de F.
- Si F es consistente, entonces G(F) es verdadero.    

Filósofos como J. R. Lucas (1961) han afirmado que este teorema demuestra que las máquinas son mentalmente inferiores a los hombres, porque las máquinas son sistemas formales limitados por el teorema de la incompletitud, es decir no pueden establecer la
verdad de su propia sentencia Gödel, mientras que los hombres no tienen dicha limitación.  
El teorema de la incompletitud de Gödel se aplica sólo a sistemas
formales que son lo suficientemente potentes como para realizar aritmética.  
Un agente no debería avergonzarse de no poder establecer la verdad de una sentencia aunque otros agentes sí puedan.  
De manera mucho más importante, aunque reconozcamos que los
computadores tienen limitaciones sobre lo que pueden demostrar, no existen evidencias
de que los hombres sean inmunes ante esas limitaciones. Es realmente sencillo demostrar con rigor que un sistema formal no puede hacer X, y afirmar entonces que los hombres pueden hacer X utilizando sus propios métodos informales, sin dar ninguna evidencia,se sabe que los
hombres son inconsistentes. Esto es verdadero para el razonamiento diario, pero también es verdadero para un pensamiento matemático cuidadoso. Un ejemplo muy conocido es el problema del mapa de cuatro colores.  
### El argumento de la informalidad

Turing mediante su «argumento de la informalidad del comportamiento». Esta
afirmación consiste en que el comportamiento humano es demasiado complejo para poder captarse mediante un simple juego de reglas y que debido a que los computadores
no pueden nada más que seguir un conjunto (juego) de reglas, no pueden generar un comportamiento tan inteligente como el de los hombres. En IA la incapacidad de capturarlo todo en un conjunto de reglas lógicas se denomina problema de cualificación.  
Dreyfus y Dreyfus (1986) proponen un proceso de adquisición de pericia en cinco etapas, comenzando con un procesamiento basado en reglas,pasan en efecto de ser críticos a la IA
a ser teóricos de IA, ya que proponen una arquitectura de redes neurales organizadas en una biblioteca de casos extensa, pero señalan algunos problemas.
Entre estos problemas se incluyen los siguientes:  
1. No se puede lograr una generalización buena de ejemplos sin un conocimiento
básico. Afirman que no se sabe cómo incorporar el conocimiento básico en el
proceso de aprendizaje de las redes neuronales. Sin embargo, esas técnicas dependen de la disponibilidad
previa de conocimiento de forma explícita en los algoritmos de aprendizaje, algo
que niegan vigorosamente.
2. El aprendizaje de redes neuronales es una forma de aprendizaje supervisado, que requiere la identificación anterior de las entradas relevantes y las salidas correctas. Por tanto, afirman que no puede funcionar autónomamente sin la ayuda de un entrenador humano.
3. Los algoritmos de aprendizaje no funcionan bien con muchas funciones, si
seleccionamos un subgrupo de éstas, «no existe una forma conocida de añadir
funciones nuevas, si el conjunto actual demuestra ser inadecuado para tener en
cuenta los hechos aprendidos».
4. El cerebro es capaz de dirigir sus sensores para buscar la información relevante
y procesarla para extraer aspectos relevantes para la situación actual. Sin embargo,
afirman que «Actualmente, los detalles de este mecanismo ni se entienden y ni
siquiera se hipotetizan para guiar la investigación en la IA»

## IA FUERTE

Muchos filósofos han afirmado que una máquina que pasa el Test de Turing no quiere
decir que esté realmente pensando, sería solamente una simulación de la acción de
pensar. De nuevo esta objeción fue prevista por Turing, y cita unas palabras del Profesor Geoffrey Jefferson (1949):  
>Hasta que una máquina pueda escribir un soneto o componer un concierto porque sienta los pensamientos y las emociones, y no porque haya una lluvia de símbolos, podría
reconocer que la máquina iguala al cerebro, es decir, no sólo escribirlo sino que sepa que
lo ha hecho.    

Esto es lo que Turing llama el argumento de la consciencia, la máquina tiene que ser
consciente de sus propias acciones y estados mentales. Aunque la consciencia sea un tema
importante, el punto de vista clave de Jefferson se relaciona realmente con la fenomenología, o el estudio de la experiencia directa, es decir, la máquina tiene que sentir emociones realmente. Otros se centran en la intencionalidad, esto es, en la cuestión de si
las creencias, deseos y otras representaciones supuestas de la máquina son de verdad algo
que pertenece al mundo real.  
Turing mantiene que la cuestión no está
bien definida al decir, «¿Pueden pensar las máquinas?». No obstante, Turing dice que «En vez de
argumentar constantemente sobre este punto de vista, es usual mantener la convención
educada de que todos pensamos».  
Turing reconoce que la cuestión de la conciencia (consciencia) es difícil, pero niega que
sea relevante para la práctica de la IA, nos interesa crear programas que
se comporten de forma inteligente y no en si alguien los declara reales o simulados.  
En 1848, Frederick Wöhler sintetizó urea artificial por primera vez. Este fue un hecho
importante porque probó que la química orgánica y la inorgánica se podían unir, cuestión discutida muy fuertemente.Los químicos reconocieron que la urea artificial era urea, porque tenía todas las propiedades físicas
adecuadas.  
Podemos concluir diciendo que en algunos casos el comportamiento de un artefacto es importante, aunque en otros sea el pedigrí del artefacto lo que importa. Lo importante en cada caso parece ser una cuestión de convención. Sin embargo para las mentes
artificiales, no existe una convención, y tenemos que depender de las intuiciones.Todo depende de la teoría de los estados y los procesos mentales.  
La teoría del __funcionalismo__ dice que un estado mental es cualquier condición causal
inmediata entre la entrada y la salida. Bajo la teoría funcionalista, dos sistemas con
procesos causales isomórficos tendrían los mismos estados mentales. Por tanto, un
programa informático podría tener los mismos estados mentales que una persona.  
En contraste, la teoría del naturalismo biológico dice que los estados mentales son
características emergentes de alto nivel originadas por procesos neurológicos de bajo
nivel en las neuronas, y lo que importa son las propiedades de las
neuronas. Así pues, los estados mentales no se pueden duplicar justo en la base de algún
programa necesitaríamos que el programa se ejecutara en una arquitectura con la
misma potencia causal que las neuronas.  
Para investigar estos dos puntos de vista examinaremos uno de los problemas más
antiguos de la filosofía de la mente, y retomaremos tres experimentos pensados.

### El problema de mente-cuerpo

El __problema mente-cuerpo__ cuestiona cómo se relacionan los estados y los procesos mentales con los estados y los procesos del cuerpo.  
Para la primera dificultad nos
remontaremos a René Descartes, quien abordó el tema de cómo un alma inmortal interactúa con un cuerpo mortal, y concluyó diciendo que el alma y el cuerpo son dos tipos
de cosas diferentes, una teoría __dualista__. La teoría __monista__, frecuentemente llamada __materialismo__, mantiene que no existen cosas tales como almas inmateriales, sino sólo objetos materiales.  
El materialista se debe enfrentar por lo menos con dos obstáculos serios. El primer
problema es el de la __libertad de elección__: ¿Cómo puede ser que una mente puramente
física, cuyas transformaciones están regidas por las leyes de la física, conserve todavía
el libre albedrío? La mayoría de los filósofos consideran que este problema necesita una
reconstitución cuidadosa de nuestra noción ingenua de libertad de elección. El segundo problema tiene que ver con el
tema general de la conciencia. Para simplificar, por qué se siente algo cuando se tienen ciertos estados cerebrales, mientras que probablemente no se siente nada al tener otros
estados físicos.  
Para empezar a responder estas cuestiones, necesitamos formas de hablar sobre los
estados del cerebro a niveles más abstractos que las configuraciones específicas de todos los átomos del cerebro de una persona en particular en un momento concreto.  
Casi todo el mundo cree que si tomamos un cerebro y sustituimos los
átomos de carbono por un nuevo conjunto de átomos de carbono
, el estado mental nose verá afectado.  

Ahora vamos a examinar una clase en particular de estado mental: las __actitudes
proposicionales__ , conocidas también como
__estados intencionales__. Estos son estados tales como creer, conocer, desear, temer, y otros
más que se relacionan con algunos aspectos del mundo exterior. Por otro lado, anteriormente, hemos argumentado que los
estados mentales son estados del cerebro, y de aquí que los estados mentales de identidad o no-identidad se deberían determinar permaneciendo completamente «dentro de la
cabeza», sin hacer referencia al mundo real. Para examinar este dilema retomaremos el
experimento del pensamiento que intenta separar a los estados intencionales de sus objetos externos.

### El experimento del cerebro en una cubeta
Imagínese que al nacer le extraen el cerebro de su cuerpo y lo colocan en una cubeta. Esta cubeta mantiene su cerebro y le permite crecer y
desarrollarse. Al mismo tiempo, su cerebro recibe unas señales electrónicas de un
simulador informático que pertenece a un mundo totalmente ficticio, y las señales motoras de su cerebro son interceptadas y utilizadas para modificar la simulación cuando
sea adecuado
.A continuación, el estado del cerebro podría tener el estado mental _MueroPor (Yo, Hamburguesa)_ aunque no tenga un cuerpo con el que sentir hambre ni sentido del gusto para experimentarlo, y puede que tampoco haya hamburguesas en el mundo
real. En ese caso, ¿sería el mismo estado mental que el del cerebro en un cuerpo?  
Una forma de resolver el dilema es decir que el contenido de los estados mentales
puede ser interpretado desde dos puntos de vista diferentes. La visión del «contenido
extenso» interpreta el dilema desde el punto de vista de un observador omnisciente desde
fuera con acceso a la situación completa.__El contenido estrecho__ sólo tiene en cuenta
el punto de vista subjetivo interno, y bajo este punto de vista todas las creencias serían
las mismas.  
Ahora vamos a entrar
en la esfera de __qualia__, o de las experiencias intrínsecas. Suponga que mediante algún accidente del cableado
retinal o neuronal la persona X experimenta en rojo el color que la persona Y percibe como
verde, y viceversa. Entonces cuando ambas vean las luces del semáforo actuarán de la
misma manera, pero la experiencia que tienen será de alguna manera diferente. Ambas
pueden reconocer que el nombre de su experiencia es «la luz es roja», pero las experiencias se sienten de diferente manera.  

### El experimento de la prótesis cerebral

Connsiste en sustituir gradualmente todas las neuronas de la cabeza de alguien con mecanismos electrónicos y a continuación invertir el proceso para retornar al sujeto a su estado biológico normal.  
Por definición del experimento, el comportamiento externo del sujeto no debe sufrir ningún cambio en comparación con lo que se
observaría si la operación no se llevase a cabo.  
Patricia Churchland señala que los argumentos funcionalistas que operan a
nivel de neurona también pueden funcionar al nivel de cualquier unidad funcional más
grande, un grupo de neuronas, un módulo mental, un lóbulo, una hemisfera, o todo el
cerebro. Eso significa que si se acepta la noción de que el experimento de prótesis del
cerebro muestra que el cerebro de sustitución es consciente, deberíamos también creer
que la consciencia se mantiene cuando el cerebro entero se sustituye por un circuito que
hace corresponder la entrada con la salida mediante una tabla de búsqueda.

### La habitación china

Este se
debe a John Searle, quien describe un sistema hipotético que claramente está ejecutando un programa y que pasa la prueba de Turing, pero que igualmente y de manera clara no entiende ninguna entrada ni salida. Su conclusión es que
ejecutar el programa adecuado no es una condición suficiente para ser una mente.  
El sistema se compone de un hombre, que solamente entiende inglés, y que está equipado con un libro de reglas escrito en inglés y varias pilas de papel, algunas en blanco
y algunas con inscripciones indescifrables.El sistema se encuentra dentro de una habitación con una apertura al exterior. A través
de la apertura se van deslizando los papeles con símbolos indescifrables. El hombre encuentra los símbolos correspondientes en el libro de reglas y sigue las instrucciones.Finalmente las instrucciones harán que un símbolo o más sean transcritos a un trozo de papel que se pasa
otra vez al mundo exterior.  
La persona que está en la habitación no entiende
el chino. El libro de reglas y las pilas de papel, que son sólo trozos de
papel no entienden el chino. Por consiguiente no está habiendo comprensión del chino.
_De aquí que, según dice Searle, ejecutar el programa adecuado no genera necesariamente entendimiento._  
El objetivo del argumento de la habitación china es refutar la IA fuerte,
es decir la afirmación de que ejecutar la clase adecuada de programa da como resultado necesariamente una mente. Searle apela a la intuición, no a la prueba: sólo hay que observar la habitación; ¿qué hay en ella que sea una mente? Sin embargo, se podría hacer el mismo argumento sobre el cerebro: observe el conjunto de
células, que funcionan ciegamente según las leyes de la Bioquímica ¿Qué hay ahí que sea una mente? ¿Por qué un trozo de cerebro puede ser una
mente mientras que un trozo de hígado no puede serlo?

## La ética y los riesgos de desarrollar la Inteligencia Artificial

Si es más probable que los efectos de la tecnología de la IA sean más negativos que positivos, sería responsabilidad moral de los
trabajadores en su campo redirigir su investigación. Todos los
científicos e ingenieros se enfrentan a consideraciones éticas de cómo deberían actuar
en el trabajo.Sin embargo, la IA parece que expone problemas nuevos
yendo más allá de, por ejemplo, construir puentes que no se desmoronen:
-_Las personas podrían perder sus trabajos por la automatización._ La economía
industrial moderna ha llegado a depender en general de los computadores, y selecciona
programas de IA en particular. Se podría decir que miles de trabajadores han sido
desplazados por estos programas de IA.Hasta ahora, la automatización por medio de la tecnología de
la IA ha creado más trabajos de los que ha eliminado, y ha creado puestos de trabajo más
interesantes y mejor pagados. Ahora que el programa IA canónico es un «agente inteligente» diseñado para ayudar a un hombre, la pérdida de trabajo preocupa menos que cuando la IA se centraba en los sistemas expertos diseñados para sustituir a los hombres.
-_Las personas podrían tener demasiado (o muy poco) tiempo de ocio._ las personas que trabajan en las industrias muy relacionadas con el conocimiento han descubierto que forman parte de un sistema computerizado integrado que funciona 24 horas al día; para mantenerlo se han visto forzados a trabajar durante más horas.
En una economía industrial, las recompensas son aproximadamente proporcionales al tiempo invertido; trabajar el 10 por ciento más llevaría a producir un incremento del 10 por
ciento en los ingresos. En una economía de la información marcada por la comunicación
de un ancho de banda alto y por una reproducción fácil de la propiedad intelectual existe una gran recompensa por ser ligeramente mejor que la competencia;
trabajar un 10 por ciento más podría significar un 100 por 100 de incremento en los ingresos. De forma que todos se sienten más presionados por trabajar más fuerte. La IA 
incrementa el ritmo de la innovación tecnológica y contribuye así a esta tendencia general, pero la IA también mantiene la promesa de permitirnos ahorrar tiempo y permitir que
nuestros agentes automatizados hagan las cosas por un tiempo.
-_Las personas podrían perder su sentido de ser únicas._ Uno de los argumentos principales de Weizenbaum es que
la investigación en IA hace posible la idea de que los hombres sean autómatas, una idea
que produce pérdida de autonomía o incluso de humanidad.La IA,
aunque sea una materia de gran éxito, quizá sea por lo menos amenazante para las
suposiciones morales de la sociedad del siglo XXI al igual que la teoría de la evolución
lo fue para los del siglo XIX.
-_Las personas podrían perder algo de sus derechos privados._ Weizenbaum también
señaló que la tecnología del reconocimiento de voz podría llevar a una intercepción
extensa de cableados, y de aquí a la pérdida de las libertades civiles.Algunas personas reconocen
que la computerización conduce a la pérdida de privacidad, el consejero
delegado de Sun Microsystems, Scott McNealy ha dicho que «De cualquier forma tenemos privacidad cero. Hay que superarlo». Otros no están de acuerdo.El
juez Louis Brandeis en 1890 escribió que «La privacidad es el derecho más completo y
extenso de todos... el derecho de la personalidad de uno mismo»
-_La utilización de sistemas de IA podría llevar a la pérdida de responsabilidad._
-_El éxito de la IA podría significar el fin de la raza humana._ Casi cualquier tecnología tiene el potencial de hacer daño si se encuentra en las manos equivocadas, pero con
la IA y la robótica, tenemos el problema nuevo de que las manos equivocadas podrían
pertenecer a dicha tecnología.  
Hans Moravec predice que los robots
se igualarán a la inteligencia humana en 50 años y a continuación la excederán:
>De manera bastante rápida podríamos quedar desplazados y fuera de la existencia. No
estoy tan alarmado como muchos otros por esta última posibilidad, ya que considero que
las máquinas del futuro son nuestra progenie, «hijos de mente» construidos a nuestra imagen y semejanza, es decir, nosotros mismos pero en una forma más potente. Al igual que
los hijos biológicos de generaciones anteriores, representarán la mejor esperanza de la
humanidad para un futuro a largo plazo. Nos corresponde a nosotros ofrecerles todas las
ventajas, y cómo retirarnos cuando ya no podamos contribuir. (Moravec, 2000.)

Ray Kurzweil,predice que hacia el año 2099
existirá «una fuerte tendencia hacia una fusión del pensamiento humano en el mundo de
la inteligencia de la máquina que las especies humanas crearon inicialmente. Ya no existe una distinción clara entre los hombres y los computadores». Existe incluso una palabra nueva, __trashumanismo__, que se refiere al movimiento social real que ansía este futuro.

## Conclusión

Con respecto a la IA débil se argumenta muy bien ya que, si una maquina llegara _"pensar"_ no sentiría emociones que son en la gran mayoria la que nos lleva a decidir algo, no es la misma decision sobre un tema cuando uno esta feliz, triste, cansado,etc.  
Con respecto a la IA fuerte los problemas de la filosofía de la mente, hablan de un hipotetico caso de que si pudiera tener conciencia y a la vez lo niegan, y la frase que mas me quedo es la de Searle de _"ejecutar el programa adecuado no genera necesariamente entendimiento"_.  
Con respecto a los riesgos son algunos, pero creo que hay mas ganancias que riesgos al largo plazo.  
[Enlance del mapa](https://www.mindomo.com/mindmap/fundamentos-filosficos-de-la-inteligencia-artificial-33d838d1fb974221adf08790c324d250)


