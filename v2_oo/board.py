class SudokuBoard:
    def __init__(self, grid):
        self.grid = grid

    
    def is_valid(self, row, col, num):
        """Vérifie si num peut être placé à (row, col)"""

        if num in self.grid[row]:
            return False
        
        for i in range(9):
            if self.grid[i][col] == num:
                return False
        
        # Vérifie le bloc 3*3
        start_row = 3 * (row // 3)
        start_col = 3 * (col // 3)

        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
        
        return True
    

    def solve(self):
        """Résolution de la grille"""

        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0: # Case vide
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.grid[row][col] = num
                            if self.solve():
                                return True
                            self.grid[row][col] = 0
                    
                    return False # Aucun chiffre ne convient
        return True # Toutes les cases sont remplies
    

    def display(self):
        """Affiche la grille avec encadrement extérieur et séparateurs des blocs 3x3, sans enumerate"""
        horizontal_border = "+-------+-------+-------+"
        print(horizontal_border)
        i = 0
        for row in self.grid:
            print("|", end=" ")
            j = 0
            for num in row:
                print(str(num) if num != 0 else ".", end=" ")
                j += 1
                if j % 3 == 0:
                    print("|", end=" ")
            print()
            i += 1
            if i % 3 == 0:
                print(horizontal_border)


                            

