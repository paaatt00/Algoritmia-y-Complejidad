import numpy as np

def createMatrix(row, column):
    matrix = [] # matrix made from row*columns and filled by 0. 
    for _ in range(column):
        aux = [0]*row
        matrix.append(aux)
    return matrix

def transposed(matrix):
    if (len(matrix) ==2 ) and len(matrix[0]) == 2: # if it is 2x2
        aux = matrix[1][0]
        matrix[1][0] = matrix[0][1]
        matrix[0][1] = aux
        return matrix
    elif len(matrix) < 4 and len(matrix[0] < 4): # if it is less than 4x4
        tmatrix = createMatrix(len(matrix),len(matrix[0]))
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                tmatrix[i][j] = matrix[j][i]
        return tmatrix
    else:
        if len(matrix) % 2 == 0: # even
            matrix1 = transposed(matrix[0:(len(matrix)//2), 0:(len(matrix)//2)])
            matrix2 = transposed(matrix[0:len(matrix)//2, ((len(matrix)//2)):len(matrix)])
            matrix3 = transposed(matrix[((len(matrix)//2)):len(matrix), 0:len(matrix)//2])
            matrix4 = transposed(matrix[((len(matrix)//2)):len(matrix), ((len(matrix)//2)):len(matrix)])
            tmatrix1 = np.hstack((matrix1, matrix3)) # adds matrix1 and 3 horizontally by the right side
            tmatrix2 = np.hstack((matrix2, matrix4)) # adds matrix2 and 4 horizontally by the right side
            matrixSolution = np.vstack((tmatrix1,tmatrix2)) # adds both resultant matrix vertically
        else: # odd
            matrix1 = transposed(matrix[0:(len(matrix)//2) + 1, 0:(len(matrix)//2) + 1])
            matrix2 = transposed(matrix[0:len(matrix)//2 + 1, ((len(matrix)//2) + 1):len(matrix)])
            matrix3 = transposed(matrix[((len(matrix)//2) + 1):len(matrix), 0:len(matrix)//2 + 1])
            matrix4 = transposed(matrix[((len(matrix)//2) + 1):len(matrix), ((len(matrix)//2) + 1):len(matrix)])
            tmatrix1 = np.hstack((matrix1, matrix3))
            tmatrix2 = np.hstack((matrix2, matrix4))
            matrixSolution = np.vstack((tmatrix1,tmatrix2))
        return matrixSolution
               
# TRIALS
matrix5 = [[0, 1, 1, 0, 1],
           [1, 0, 0, 1, 0],
           [0, 1, 1, 1, 1],
           [1, 0, 0, 1, 1],
           [1, 1, 0, 0, 0]]
matrix5 = np.array(matrix5)
print('5x5 original matrix:\n', matrix5)
print('5x5 transposed matrix:\n', transposed(matrix5))


matrix10=[[0, 0, 0, 1, 1, 0, 1, 0, 1, 0],
          [1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
          [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
          [0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
          [1, 1, 0, 1, 0, 1, 0, 0, 1, 0],
          [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
          [1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
          [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
          [1, 1, 1, 0, 1, 0, 0, 1, 1, 0],
          [0, 0, 1, 1, 0, 0, 1, 0, 0, 1]]
matrix10 = np.array(matrix10)
print('10x10 original matrix:\n', matrix10)
print('10x10 transposed matrix:\n', transposed(matrix10))