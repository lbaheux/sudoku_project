from board import SudokuBoard
from generator import SudokuGenerator

# Génération d'une grille complète
generator = SudokuGenerator()
board = generator.generate_full_board()

print("grille générée:")
board.display()