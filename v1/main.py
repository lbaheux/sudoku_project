from sudoku import solve

def print_board(board):
    """Affiche la grille dans la console"""
    
    i = 0
    for row in board:
        line = []

        j = 0
        for num in row:
            if num != 0:
                line.append(str(num))
            else:
                line.append(".")

            j += 1
            if j % 3 == 0 and j < 9:
                line.append("|")
        
        print(" ".join(line))

        i += 1

        if i % 3 == 0 and i < 9:
            print("-" * 21) # ligne de tirets pour séparer les blocs


# Grille partiellement remplie
board = [
    [5, 1, 7, 6, 0, 0, 0, 3, 4],
    [2, 8, 9, 0, 0, 4, 0, 0, 0],
    [3, 4, 6, 2, 0, 5, 0, 9, 0],
    [6, 0, 2, 0, 0, 0, 0, 1, 0],
    [0, 3, 8, 0, 0, 6, 0, 4, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 7, 8],
    [7, 0, 3, 4, 0, 0, 5, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print("Grille initiale :")
print_board(board)

if solve(board):
    print("\nGrille résolue :")
    print_board(board)
else:
    print("Pas de solution trouvée.")