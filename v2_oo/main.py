from board import SudokuBoard
from generator import SudokuGenerator

# Génération d'une grille complète
generator = SudokuGenerator()
board = generator.generate_full_board()

print("grille générée:")
board.display()


"""
board = SudokuBoard(grid)
print("Grille initiale :")
board.display()

if board.solve():
    print("\nGrille résolue :")
    board.display()
else:
    print("Pas de solution trouvée.")
"""

