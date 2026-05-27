from game_of_life import GameOfLife

from patterns import create_glider
from patterns import create_blinker
from patterns import create_toad

from visualization import animate_game

from benchmark import run_benchmark


# -------------------------------------------------

print()
print("====================================")
print("      CONWAY'S GAME OF LIFE")
print("====================================")
print()

print("1 - Tablero Aleatorio")
print("2 - Glider")
print("3 - Blinker")
print("4 - Toad")
print("5 - Benchmark")
print()

option = input("Seleccione una opción: ")

# -------------------------------------------------
# TABLERO ALEATORIO
# -------------------------------------------------

if option == "1":

    rows = int(input("Ingrese número de filas: "))
    cols = int(input("Ingrese número de columnas: "))

    game = GameOfLife(rows, cols)

    animate_game(game, 200)

# -------------------------------------------------
# GLIDER
# -------------------------------------------------

elif option == "2":

    pattern = create_glider()

    game = GameOfLife(3, 3, pattern)

    animate_game(game, 100)

# -------------------------------------------------
# BLINKER
# -------------------------------------------------

elif option == "3":

    pattern = create_blinker()

    game = GameOfLife(3, 3, pattern)

    animate_game(game, 100)

# -------------------------------------------------
# TOAD
# -------------------------------------------------

elif option == "4":

    pattern = create_toad()

    game = GameOfLife(2, 4, pattern)

    animate_game(game, 100)

# -------------------------------------------------
# BENCHMARK
# -------------------------------------------------

elif option == "5":

    run_benchmark()

# -------------------------------------------------

else:

    print()
    print("Opción inválida")