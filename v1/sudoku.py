def is_valid(board, row, col, num):
    """Vérifie si num peut être placé a la position (row, col)"""

    # Vérifie la ligne
    if num in board[row]:
        return False
    
    # Vérifie la colonne
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Vérifie le carré 3*3
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

def solve(board):
    """Résolution de la grille de sudoku"""

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0: # Case vide
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        
                        board[row][col] = 0
                return False # Aucun chiffre ne convient
    return True # Toutes les cases remplies