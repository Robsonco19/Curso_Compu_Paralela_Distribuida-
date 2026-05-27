import time
import matplotlib.pyplot as plt

from game_of_life import GameOfLife


def run_benchmark():

    sizes = [32, 64, 128, 256, 512, 1024]

    execution_times = []

    # -------------------------------------------------

    for size in sizes:

        print()
        print("Probando tablero:", size, "x", size)

        game = GameOfLife(size, size)

        start_time = time.perf_counter()

        # Ejecutar 10 generaciones
        for i in range(10):

            game.step()

        end_time = time.perf_counter()

        average_time = (end_time - start_time) / 10

        execution_times.append(average_time)

        print("Tiempo promedio:", average_time)

    # -------------------------------------------------
    # Crear lista de número de celdas
    # -------------------------------------------------

    cells = []

    for size in sizes:

        cells.append(size * size)

    # -------------------------------------------------
    # Gráfica normal
    # -------------------------------------------------

    plt.figure(figsize=(8, 5))

    plt.plot(cells, execution_times, marker='o')

    plt.xlabel("Número de celdas")
    plt.ylabel("Tiempo promedio")

    plt.title("Tiempo vs Tamaño de Entrada")

    plt.grid(True)

    plt.show()

    # -------------------------------------------------
    # Gráfica log-log
    # -------------------------------------------------

    plt.figure(figsize=(8, 5))

    plt.loglog(cells, execution_times, marker='o')

    plt.xlabel("Número de celdas (log)")
    plt.ylabel("Tiempo (log)")

    plt.title("Gráfica Log-Log")

    plt.grid(True)

    plt.show()