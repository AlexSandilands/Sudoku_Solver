# Algorithm to solve the Sudoku
def solveSudoku(sudoku):
    change = False

    print "Start"

    while True:

        # print "Top of while"

        # Iterate through
        for row in range(9):
            for col in range(9):

                # print "Top of first for"

                if sudoku[row][col][0] == 0:
                    continue

                curCol = getColumn(sudoku, col)
                curRow = sudoku[row]


                for i in range(9):
                    # print "Top of second for"

                    if curCol[i][0] in sudoku[row][col][1]:
                        # print "Change from col"
                        sudoku[row][col][1].remove(curCol[i][0])
                        change = True

                    if curRow[i][0] in sudoku[row][col][1]:
                        # print "Change from row"
                        sudoku[row][col][1].remove(curRow[i][0])
                        change = True


                if len(sudoku[row][col][1]) == 1:
                    print "Value was changed"
                    sudoku[row][col][0] = sudoku[row][col][1][0]
                    sudoku[row][col][1] = []
                    change = True


        if not change:
            break



# Get the column with the input index
def getColumn(sudoku, col):
    ret = []

    for row in range(9):
        ret.append(sudoku[row][col-1])

    return ret