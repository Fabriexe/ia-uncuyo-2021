# EJERCICIO 1

Para un sudoku de 9x9  

**Variables**: Las 81 celdas.  
**Dominio**:{1,2,3,4,5,6,7,8,9}
**Restricciones**: Usamos un operador que verifique que todos los elementos sean diferentes.  
La restriccion la tenesmos que hacer en la misma fila, columna y cuadricula de 3x3 por ende tendria que verificar todas las filas, todas las columnas y todas las cuadriculas de 3x3.  

# EJERCICIO 2

Al aplicar WA=red y V=blue se encola para la revisión las variables cuyo dominio se puede ver afectado al aplicar la arco consistencia, la lista nos quedaria con NT{green,blue}, NSW{red,green} y SA{green}.  
Al desencolar llegariamos con SA o NT, en los cuales al aplicarle la arco consistencia se elimina {green} del dominio de SA, quedando sin ninguna asignacion posible

# EJERCICIO 3

Por la estructura del árbol en la cual cada variable se conecta mediante una restriccion, los arcos son considerados 1 vez. Por ende si tenemos una cantidad A de aristas a revisar y una cantidad V de valores en el dominio, podemos llegar a considerar a cada 1 de los valores por cada 1 de las aristas, llegando a una complejidad de V*A

# EJERCICIO 4

La reduccion de la complejidad esta en no encolar nuevamente las aristas que ya tienen un resultado consistente en la asignacion de su valor