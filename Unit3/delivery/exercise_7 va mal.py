def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end = "   ")
        print("\n")

def transposed_matrix(matrix): 
    return transposed(matrix, 0, len(matrix) - 1, 0, len(matrix) - 1)

def transposed(matrix, iniRow, endRow, iniColumn, endColumn):
    #print(iniRow, iniColumn, endRow, endColumn)
    if iniRow < endRow:
        if (len(matrix) % 2) == 0:
            mediumRow = (iniRow + endRow)//2
            mediumColumn = (iniColumn + endColumn)//2
            transposed(matrix, iniRow, mediumRow, iniColumn, mediumColumn) #arriba izquierda
            transposed(matrix, iniRow, mediumRow, mediumColumn + 1, endColumn) #arriba derecha
            transposed(matrix, mediumRow + 1, endRow, iniColumn, mediumColumn) #abajo izquierda
            transposed(matrix, mediumRow + 1, endRow, mediumColumn + 1, endColumn) #abajo derecha
            swap_quadrants(matrix, mediumRow + 1, iniColumn, iniRow, mediumColumn + 1, endRow - mediumRow)
        else:
            mediumRow = (iniRow + endRow)//2
            mediumColumn = (iniColumn + endColumn)//2
            transposed(matrix, iniRow, mediumRow - 1, iniColumn, mediumColumn - 1) #arriba izquierda
            transposed(matrix, iniRow, mediumRow - 1, mediumColumn + 1, endColumn) #arriba derecha
            transposed(matrix, mediumRow + 1, endRow, iniColumn, mediumColumn - 1) #abajo izquierda
            transposed(matrix, mediumRow + 1, endRow, mediumColumn + 1, endColumn) #abajo derecha
            swap_row_column(matrix, mediumRow, mediumRow)
            swap_quadrants(matrix, mediumRow + 1, iniColumn, iniRow, mediumColumn + 1, endRow - mediumRow)
    return matrix

def swap_quadrants(matrix, iniRowA, iniColumnA, iniRowB, iniColumnB, dimension):
    for i in range(dimension):
        for j in range(dimension):
            matrix[iniRowA + i][iniColumnA + j], matrix[iniRowB + i][iniColumnB + j] =  matrix[iniRowB + i][iniColumnB + j], matrix[iniRowA + i][iniColumnA + j]
            #aux = matrix[iniRowA + i][iniColumnA + j]
            #matrix[iniRowA + i][iniColumnA + j] = matrix[iniRowB + i][iniColumnB + j]
            #matrix[iniRowB + i][iniColumnB + j] = aux
    return matrix

def swap_row_column(matrix, row, column):
    for i in range(len(matrix)):
        matrix[row][i], matrix[i][column] = matrix[i][column], matrix[row][i]
    return matrix

matrix5 = [[0, 1, 1, 1, 0],
           [1, 0, 0, 1, 0],
           [0, 1, 1, 1, 1],
           [1, 0, 0, 1, 1],
           [1, 1, 0, 0, 0]]

matrix52 = [[7, 1, 1, 1, 3],
            [8, 0, 0, 2, 0],
            [9, 1, 1, 4, 5],
            [2, 3, 0, 6, 1],
            [9, 1, 2, 4, 0]]
 
matrix4 = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

matrix10 = [[0, 0, 0, 1, 1, 0, 1, 0, 1, 0],
           [1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
           [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
           [0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
           [1, 1, 0, 1, 0, 1, 0, 0, 1, 0],
           [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
           [1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
           [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
           [1, 1, 1, 0, 1, 0, 0, 1, 1, 0],
           [0, 0, 1, 1, 0, 0, 1, 0, 0, 1]]

matrix8 = [[0, 0, 0, 1, 1, 0, 1, 0],
           [1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 1, 1, 1, 0],
           [0, 0, 1, 0, 1, 1, 1, 0],
           [0, 0, 1, 0, 1, 1, 1, 0],
           [0, 0, 1, 0, 1, 1, 1, 0],
           [0, 0, 1, 0, 1, 1, 1, 0],
           [0, 0, 1, 0, 1, 1, 1, 0]]

print("\nMatriz original\n")
print_matrix(matrix52)
print("Matriz traspuesta\n")
print_matrix(transposed_matrix(matrix52))