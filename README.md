El juego de la vida de Conway
Descripción del Proyecto

Este proyecto consiste en la implementación del Juego de la Vida de Conway utilizando Python y programación orientada a objetos.

El Juego de la Vida es una simulación basada en una cuadrícula donde cada celda puede estar viva o muerta. Dependiendo de la cantidad de vecinos vivos que tengan alrededor, las celdas cambian de estado en cada generación siguiendo una serie de reglas simples.

El objetivo principal de esta tarea fue aplicar conceptos como:

Programación orientada a objetos
Manejo de matrices
Simulación de sistemas dinámicos
Visualización gráfica
Medición de rendimiento
Estructura del Proyecto
Tarea_1_Game_Of_Life/

- main.py
- game_of_life.py
- patterns.py
- visualization.py
- benchmark.py
- README.md
Explicación de los Archivos
main.py

Archivo principal desde donde se ejecuta el programa y se muestran las opciones del menú.

juego_de_la_vida.py

Contiene la clase GameOfLifey toda la lógica del juego, incluyendo las reglas y actualización del tablero.

patrones.py

Incluye patrones clásicos como:

Planeador
Intermitente
Sapo
visualización.py

Se encarga de mostrar la simulación gráficamente utilizando matplotlib.

benchmark.py

Realiza pruebas de rendimiento y genera gráficas del tiempo de ejecución.

Requisitos

Instalar Python 3 y matplotlib.

pip install matplotlib
Cómo Ejecutar

Ejecutar el siguiente comando dentro de la carpeta del proyecto:

python main.py
Opciones del Programa
1 - Tablero Aleatorio
2 - Glider
3 - Blinker
4 - Toad
5 - Benchmark
Reglas del Juego
Una celda viva con menos de 2 vecinos vivos muere.
Una celda viva con más de 3 vecinos vivos muere.
Una celda viva con 2 o 3 vecinos vivos sobreviven.
Una celda muerta con exactamente 3 vecinos vivos revive.
Rendimiento

El programa realiza pruebas utilizando diferentes tamaños de parrilla para medir el tiempo de ejecución y analizar cómo aumenta el costo computacional conforme crece el número de celdas.

También se generan gráficas normales y log-log para observar el comportamiento del algoritmo.

Herramientas Utilizadas:
- Python 3
- Matplotlib
- Programación Orientada a Objetos

Conclusiones

Este proyecto permitió comprender mejor cómo reglas simples pueden generar comportamientos complejos dentro de una simulación.

Además, ayudó a reforzar conceptos importantes relacionados con programación orientada a objetos, simulación, visualización gráfica y análisis de rendimiento.
