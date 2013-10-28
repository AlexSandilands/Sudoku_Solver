# ------------------------------------------------------------ #
# ------------------------------------------------------------ #
# ------------- Functions for solving the Sudoku ------------- #
# ------------------------------------------------------------ #
# ------------------------------------------------------------ #



# Algorithm to solve the Sudoku
def solveSudoku(sudoku):
    # Iterate through every cell
    for row in range(9):
        for col in range(9):

            # If there is a blank cell, start guessing
            if sudoku[row][col] == 0:

                # Check every value from 1-9
                for test in range(1, 10):

                    if isValid(sudoku, row, col, test):
                        # If the guessed value was valid, stick it in the cell
                        sudoku[row][col] = test

                        # If it was the last cell, then the algorithm is done
                        if isFull(sudoku):
                            return sudoku

                        # Otherwise recursively call the solve algorithm with
                        # the guessed value in place
                        step = solveSudoku(sudoku)

                        # If the recursive call returns a full sudoku it was a
                        # correct guess.
                        if isFull(step):
                            return step

                        # Otherwise the guess didn't work, so clear the cell
                        # and continue guessing
                        else:
                            sudoku[row][col] = 0
                            continue

                # If none of the guesses were valid return an incomplete sudoku
                return sudoku




# Checks if the val can be placed in the cell: [row, col]
# without breaking any constraints
def isValid(sudoku, row, col, val):
    # Get the box that the row is in
    for r in range(1, 4):
        if row < r*3:
            rMin = r*3 - 3
            rMax = r*3
            break

    # Get the box that the col is in
    for c in range(1, 4):
        if col < c*3:
            cMin = c*3 - 3
            cMax = c*3
            break

    # Check if the val is in the box that row, col is in
    for r in range(rMin, rMax):
        for c in range(cMin, cMax):
            if sudoku[r][c] == val:
                return False

    # Check if the val is in the column: col
    if val in [ sudoku[r][col] for r in range(9)]:
        return False

    # Check if the val is in the row: row
    if val in sudoku[row]:
        return False

    return True



# Checks if the sudoku has any empty cells
def isFull(sudoku):
    for row in range(9):
        if 0 in sudoku[row]:
            return False

    return True
