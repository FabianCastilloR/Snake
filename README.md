# Snake

En el código inicial se encontraban funciones para:
- Controlar la serpiente.
- Asignar un color predefinido a la serpiente y a la comida.
- Ganar puntos al tomar la comida y hacer crecer a la serpiente.
- La comida permanece estática, y al ser tomada por el jugador se cambia a un lugar aleatorio dentro del plano.
- Perder si la serpiente toca algún borde, y cambiar el color de la cabeza.

En el código modificado se agregó:
- Hacer dinámica a la comida, logrando que permaneciera dentro del plano (Modificado por Fabián Castillo Rodríguez. Se implementó al crear un vector de movimiento para la comida que cambiara aleatoriamente entre dar un paso a la derecha, izquierda, arriba y abajo, y detectar cuando estuviera en las esquinas para que de un paso hacia el lado contrario de dicho borde).
- Cambiar el color de la serpiente y la comida a uno diferente en cada nueva partida (Modificado por Sergio Adolfo Sanoja Hernández. Se implementó al crear una lista de cinco colores diferentes y crear dos variables que tomaran aleatoriamente el valor de alguno de los colores contenidos en la lista, después se comprobaba que no tuvieran el mismo color y se le asignaba una variable al color de la serpiente y otra al de la comida).

Además, se comentó todo el código para hacerlo más entendible para programadores externos y personas con poco conocimiento de programación.
