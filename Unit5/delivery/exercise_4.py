import math

rows = 6
columns = 6
ini = 0
end = 0
total = rows * columns

def create_board():
    board = []
    for _ in range (rows):
        aux = [0] * columns
        board.append(aux) 
    return board

def is_valid(row1, column1, row2, column2):
    abs1 = abs(row2 - row1)
    abs2 = abs(column2 - column1)
    return (((abs1 == 1) and (abs2 == 2)) or ((abs1 == 2) and (abs2 == 1)))

def print_board(board):
    for i in range (len(board)):
        print(board[i], end = "\n")

def movement(board, row, column, cont):
    if (cont >= rows * columns):
        print_board(board)
        return True
    for i in range (rows):
        for j in range (columns):
            if (is_valid(row, column, i, j) and (board[i][j] == 0)):
                board[i][j] = "x"
                exito = movement(board, i, j, cont + 1)
                board[i][j] = 0  
                if (exito):
                    print("Movement to", i, ",", j , "\n")
                    return True       

board = create_board()
board[ini][end] = "X"
movement(board, ini, end, 1)