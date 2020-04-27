ROW = 9
COL = 9

def printBoard(board):
    for i in range(ROW):
        for j in range(COL):
            print(str(board[i][j]), end=" ")

        print() 
    print()


# Checks if it's possible to add number in current row, returns true if possible, false if not
def checkRow(board, number, row):
    for i in range(COL):
        if board[row][i] == number:
            return False
    
    return True


# Checks if it's possible to add number in current column, returns true if possible, false if not
def checkCol(board, number, col):
    for i in range(ROW):
        if board[i][col] == number:
            return False

    return True


# Checks subgrid, returns true if possible, false if not
def checkSubgrid(board, number, row, col):
    row_index = (row // 3) * 3 
    col_index = (col // 3) * 3

    for i in range(row_index, row_index+3):
        for j in range(col_index, col_index+3):
            if board[i][j] == number:
                return False

    return True



# Checks if a position is valid, return True if valid, False if not
def isValidPosition(board, number, row, col):
    return checkCol(board, number, col) and checkRow(board, number, row) and checkSubgrid(board, number, row, col)


# Returns False if it finds empty grid, return True otherwise
def checkForEmptyCell(board):
    for i in range(ROW):
        for j in range(COL):
            if board[i][j] == "-":
                return False

    return True


# Returns coords to first valid position
def coordsEmptyCell(board):
    for i in range(ROW):
        for j in range(COL):
            if board[i][j] == "-":
                return (i, j)


def solve(board):
    if checkForEmptyCell(board):
        return True
    
    coords = coordsEmptyCell(board)
    row_index = coords[0]
    col_index = coords[1]
    for i in range(1, 10):
        if isValidPosition(board, i, row_index, col_index):
            board[row_index][col_index] = i
            if solve(board):
                return True

            board[row_index][col_index] = "-"
    return False