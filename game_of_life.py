import random


class GameOfLife:

    def __init__(self, rows, cols, initial_state=None):

        self.rows = rows
        self.cols = cols

        # Si existe un estado inicial
        if initial_state is not None:

            self.board = initial_state

        # Crear tablero aleatorio
        else:

            self.board = []

            for i in range(rows):

                row = []

                for j in range(cols):

                    value = random.randint(0, 1)

                    row.append(value)

                self.board.append(row)

    # -------------------------------------------------

    def get_state(self):

        return self.board

    # -------------------------------------------------

    def count_neighbors(self, row, col):

        neighbors = 0

        for i in range(-1, 2):

            for j in range(-1, 2):

                # Ignorar la misma celda
                if i == 0 and j == 0:
                    continue

                new_row = row + i
                new_col = col + j

                # Verificar límites
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols:

                    neighbors += self.board[new_row][new_col]

        return neighbors

    # -------------------------------------------------

    def step(self):

        # Crear nuevo tablero vacío
        new_board = []

        for i in range(self.rows):

            row = []

            for j in range(self.cols):

                row.append(0)

            new_board.append(row)

        # Aplicar reglas
        for i in range(self.rows):

            for j in range(self.cols):

                neighbors = self.count_neighbors(i, j)

                # Celda viva
                if self.board[i][j] == 1:

                    # Soledad o sobrepoblación
                    if neighbors < 2 or neighbors > 3:

                        new_board[i][j] = 0

                    # Supervivencia
                    else:

                        new_board[i][j] = 1

                # Celda muerta
                else:

                    # Reproducción
                    if neighbors == 3:

                        new_board[i][j] = 1

        # Actualizar tablero
        self.board = new_board

    # -------------------------------------------------

    def run(self, steps):

        for i in range(steps):

            self.step()