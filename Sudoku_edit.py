# ------------------------------------------------------------ #
# ------------------------------------------------------------ #
# -------- Functions for editing values in the Sudoku -------- #
# ------------------------------------------------------------ #
# ------------------------------------------------------------ #



import Sudoku_main as main

# Change to the mode where you can enter values into the Sudoku
def enterValueMode(sudoku):
    while True:
        printEnterOptions()

        # Get the input int value from the user
        try:
            cmd = int(raw_input("\n"))

            # Make sure the value entered is in the bounds
            if cmd < 0 or cmd > 3:
                print "\nPlease enter a number from 0 to 3.\n"
                continue

        # Only allow integer values to be entered
        except ValueError:
            print "\nPlease enter an integer from 0 to 3.\n"
            continue

        if cmd == 0:
            break

        elif cmd == 1:
            enterValue(sudoku)

        elif cmd == 2:
            enterRow(sudoku)

        elif cmd == 3:
            enterColumn(sudoku)



# Give option to insert a value into the Sudoku
def enterValue(sudoku):
    print "0 will clear the cell, 1-9 will insert a number"
    val = raw_input("\nEnter a coordinate and a value of the form \"[row][col] = number\":\n\n")

    if len(val) != 10:
        print "\nIncorrect format. Here is an example: "
        print "    [1][9] = 5 will put a 5 in the very bottom left corner"

        return

    try:
        row = int(val[1:2])
        row -= 1

        col = int(val[4:5])
        col -= 1

        num = int(val[-1])

    except ValueError:
        print "\nIncorrect format. Here is an example: "
        print "    [1][9] = 5 will put a 5 in the very bottom left corner"

    sudoku[row][col] = num
    main.printSudoku(sudoku)



# Give option to enter a row into the sudoku
def enterRow(sudoku):
    val = raw_input("\nEnter row, of the form: \"1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]\"\nPut a 0 for a blank square.\n\n")

    if len(val) != 31:
        print "\nIncorrect format. Here is an example: "
        print "    1 = [2, 5, 0, 0, 0, 6, 7, 8, 0] will put those values in the first row"

        return

    try:
        rowInd = int(val[0:1]) - 1

        nums = map(int, val[5:-1].split(","))

    except ValueError:
        print "\nIncorrect format ERROR. Here is an example: "
        print "    1 = [2, 5, 0, 0, 0, 6, 7, 8, 0] will put those values in the first row"

        return

    row = []

    for col in range(9):
        row.append(nums[col])

    sudoku[rowInd] = row

    main.printSudoku(sudoku)



# Give option to enter a column into the sudoku
def enterColumn(sudoku):
    val = raw_input("\nEnter column, of the form: \"colNum = [1, 2, ... , 9]\"\nPut a 0 for a blank square.\n\n")

    if len(val) != 31:
        print "\nIncorrect format. Here is an example: "
        print "    1 = [2, 5, 0, 0, 0, 6, 7, 8, 0] will put those values in the first column"

        return

    try:
        colInd = int(val[0:1]) - 1

        nums = map(int, val[5:-1].split(","))

    except ValueError:
        print "\nIncorrect format ERROR. Here is an example: "
        print "    1 = [2, 5, 0, 0, 0, 6, 7, 8, 0] will put those values in the first row"

        return

    col = []

    for row in range(9):
        col.append(nums[row])


    for row in range(9):
        sudoku[row][colInd] = col[row]

    main.printSudoku(sudoku)




# Clears all cells in the Sudoku
def clearSudoku(sudoku):
    for y in range(9):
        for x in range(9):
            sudoku[x][y] = 0

    main.printSudoku(sudoku)



# Commands that will be printed in the value entering loop
def printEnterOptions():
    print "\n|------------------------|"
    print "|   Change Values Menu   |"
    print "|------------------------|\n"
    print "0: Go back"
    print "1: Enter a value"
    print "2: Enter a row"
    print "3: Enter a column"
