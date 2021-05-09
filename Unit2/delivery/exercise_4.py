import math

def PrimAlgorithm(matrix):
    '''
    OBJ: implementation of Prim Algorithm
    '''
    minDistance = [0]
    nearestNode = [0] 
    T = []
    knownNodes = []
    for i in range(1, len(matrix)):
        nearestNode.append(0)
        minDistance.append(matrix[i][0])
    for i in range(len(matrix) - 1):
        min = math.inf
        for j in range(1, len(matrix)):
            if (0 <= minDistance[j] < min and j not in knownNodes):
                min = minDistance[j]
                k = j
        T.append([nearestNode[k] + 1, k + 1])
        knownNodes.append(k)
        for j in range(1, len(matrix)):
            if (matrix[j][k] < minDistance[j]):
                minDistance[j] = matrix[j][k]
                nearestNode[j] = k
    return T

w = math.inf
matrix = [[0, w, 4, w, 5, 1, w],
          [w, 0, 3, 6, 2, w, w],
          [4, 3, 0, 5, w, w, 1],
          [w, 6, 5, 0, 9, w, 7],
          [5, 2, w, 9, 0, w, 5],
          [1, w, w, w, w, 0, 3],
          [w, w, 1, 7, 5, 3, 0]]

print(PrimAlgorithm(matrix))