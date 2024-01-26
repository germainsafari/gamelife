import random
import json

class Cell:
    def __init__(self, alive=False):
        self.alive = alive

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell() for _ in range(cols)] for _ in range(rows)]

    def generate_random_board(self, num_living_cells):
        for _ in range(num_living_cells):
            row, col = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
            self.cells[row][col].alive = True

    def generate_random_board_density(self, density):
        num_living_cells = int(self.rows * self.cols * density)
        self.generate_random_board(num_living_cells)

    def generate_board_from_string(self, board_string):
        for i, row in enumerate(board_string.split('\n')):
            for j, char in enumerate(row):
                if char == '1':
                    self.cells[i][j].alive = True

    def __eq__(self, other):
        return all(self.cells[i][j].alive == other.cells[i][j].alive
                   for i in range(self.rows) for j in range(self.cols))

    def __str__(self):
        return '\n'.join(''.join('1' if cell.alive else '0' for cell in row) for row in self.cells)

class Game:
    def __init__(self):
        self.board = None

    def initialize_board(self, rows, cols, density):
        self.board = Board(rows, cols)
        self.board.generate_random_board_density(density)

    def simulate(self, steps):
        for step in range(steps):
            print(f"Step {step + 1}:\n{self.board}")
            new_board = Board(self.board.rows, self.board.cols)

            for i in range(self.board.rows):
                for j in range(self.board.cols):
                    live_neighbors = self.count_live_neighbors(i, j)
                    if self.board.cells[i][j].alive:
                        new_board.cells[i][j].alive = live_neighbors in [2, 3]
                    else:
                        new_board.cells[i][j].alive = live_neighbors == 3

            if self.board == new_board:
                print("Stable configuration reached. Simulation stopped.")
                break

            self.board = new_board

    def count_live_neighbors(self, row, col):
        live_neighbors = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < self.board.rows and 0 <= j < self.board.cols and (i != row or j != col):
                    live_neighbors += int(self.board.cells[i][j].alive)
        return live_neighbors

    def save_game_state(self, file_path):
        game_state = {
            'rows': self.board.rows,
            'cols': self.board.cols,
            'cells': [[int(cell.alive) for cell in row] for row in self.board.cells]
        }

        with open(file_path, 'w') as file:
            json.dump(game_state, file)

    def load_game_state(self, file_path):
        with open(file_path, 'r') as file:
            game_state = json.load(file)

        self.board = Board(game_state['rows'], game_state['cols'])
        self.board.cells = [[Cell(alive=bool(cell)) for cell in row] for row in game_state['cells']]

if __name__ == "__main__":
    game = Game()
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    density = float(input("Enter the population density (0-1): "))
    game.initialize_board(rows, cols, density)
    steps = int(input("Enter the number of simulation steps: "))
    game.simulate(steps)

    # Save game state to a file
    file_path = input("Enter the file path to save the game state: ")
    game.save_game_state(file_path)

    # Load game state from a file
    loaded_game = Game()
    loaded_file_path = input("Enter the file path to load the game state: ")
    loaded_game.load_game_state(loaded_file_path)
    loaded_game.simulate(steps)
