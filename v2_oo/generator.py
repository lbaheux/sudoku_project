import random
from board import SudokuBoard

class SudokuGenerator:
    def __init__(self):
        self.board = SudokuBoard([[0 for _ in range(9)]for _ in range(9)]) # Grille 9x9 remplie de 0


    def fill_grid(self):
        """Remplit la grille avec des nombres valides"""
        
        for row in range(9):
            for col in range(9):
                if self.board.grid[row][col] == 0:
                    numbers = list(range(1, 10))
                    random.shuffle(numbers)
                    for num in numbers:
                        if self.board.is_valid(row, col, num):
                            self.board.grid[row][col] = num
                            if self.fill_grid():
                                return True
                            self.board.grid[row][col] = 0
                    return False
                    
        return True
    
    def generate_full_board(self):
        """Retourne une grille de Sudoku complète et valide"""
        self.fill_grid()
        #print(self.board.grid)
        return self.board
                

