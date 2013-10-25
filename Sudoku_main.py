def main():

    # Initialise Sudoku
    sudoku = [[[0, [col+1]] for col in range(9)] for row in range(9)]

    print "\nWelcome to the Sudoku solver.\n\n"

    # Start program, this will only exit if the user enters 0.
    while True:
        printMainOptions()

        # Get the input int value from the user
        try:
            cmd = int(raw_input("\n"))

            # Make sure the value entered is in the bounds
            if cmd < 0 or cmd > 5:
                print "\nPlease enter a number from 0 to 5.\n"
                continue

        # Only allow integer values to be entered
        except ValueError:
            print "\nPlease enter a number from 0 to 5.\n"
            continue


        # User options
        if cmd == 0:
            break

        elif cmd == 1:
            printSudoku(sudoku)

        elif cmd == 2:
            solveSudoku(sudoku)

        elif cmd == 3:
            enterValueMode(sudoku)

        elif cmd == 4:
            clearSudoku(sudoku)

        elif cmd == 5:
            loadEasy(sudoku)


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




# Loads an easy Sudoku into the program
def loadEasy(sudoku):
    d = [i+1 for i in range(9)]

    r1 = [[2, d], [8, d], [6, d], [0, d], [0, d], [1, d], [0, d], [9, d], [0, d]]
    r2 = [[3, d], [0, d], [0, d], [2, d], [0, d], [7, d], [0, d], [0, d], [0, d]]
    r3 = [[0, d], [0, d], [5, d], [9, d], [0, d], [0, d], [6, d], [0, d], [0, d]]
    r4 = [[0, d], [0, d], [7, d], [0, d], [1, d], [4, d], [2, d], [3, d], [0, d]]
    r5 = [[0, d], [3, d], [0, d], [0, d], [0, d], [0, d], [0, d], [1, d], [0, d]]
    r6 = [[0, d], [2, d], [8, d], [6, d], [9, d], [0, d], [5, d], [0, d], [0, d]]
    r7 = [[0, d], [0, d], [1, d], [0, d], [0, d], [5, d], [3, d], [0, d], [0, d]]
    r8 = [[0, d], [0, d], [0, d], [1, d], [0, d], [9, d], [0, d], [0, d], [2, d]]
    r9 = [[0, d], [4, d], [0, d], [3, d], [0, d], [0, d], [1, d], [8, d], [9, d]]

    sudoku[0] = r1
    sudoku[1] = r2
    sudoku[2] = r3
    sudoku[3] = r4
    sudoku[4] = r5
    sudoku[5] = r6
    sudoku[6] = r7
    sudoku[7] = r8
    sudoku[8] = r9

    printSudoku(sudoku)


# Print the Sudoku to the command line
def printSudoku(sudoku):
    print " _ _ _ _ _ _ _ _ _ _ _ _ "

    for row in range(9):
        s = "| "

        for col in range(3):
            if sudoku[row][col][0] != 0:
                s += str(sudoku[row][col][0]) + " "
            else:
                s += ". "

        s += "| "

        for col in range(3, 6):
            if sudoku[row][col][0] != 0:
                s += str(sudoku[row][col][0]) + " "
            else:
                s += ". "

        s += "| "

        for col in range(6, 9):
            if sudoku[row][col][0] != 0:
                s += str(sudoku[row][col][0]) + " "
            else:
                s += ". "

        s+= "|"

        print s

        if row == 2 or row == 5:
            print "--------+-------+--------"

    print "-------------------------\n"



# Change to the mode where you can enter values into the Sudoku
def enterValueMode(sudoku):
    while True:
        printEnterOptions()

        # Get the input int value from the user
        try:
            cmd = int(raw_input("\n"))

            # Make sure the value entered is in the bounds
            if cmd < 0 or cmd > 6:
                print "\nPlease enter a number from 0 to 6.\n"
                continue

        # Only allow integer values to be entered
        except ValueError:
            print "\nPlease enter a number from 0 to 6.\n"
            continue

        if cmd == 0:
            break

        elif cmd == 1:
            enterValue(sudoku)

        elif cmd == 2:
            clearValue(sudoku)

        elif cmd == 3:
            enterRow(sudoku)

        elif cmd == 4:
            enterColumn(sudoku)

        elif cmd == 5:
            clearRow(sudoku)

        elif cmd == 6:
            clearColumn(sudoku)



# Give option to insert a value into the Sudoku
def enterValue(sudoku):
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

    sudoku[row][col][0] = num
    printSudoku(sudoku)



# Give option to clear a value in the Sudoku
def clearValue(sudoku):
    val = raw_input("\nEnter a coordinate to clear, of the form \"[row][col]\":\n\n")

    if len(val) != 6:
        print "\nIncorrect format. Here is an example: "
        print "    [1][9] will clear the very bottom left corner"

        return

    try:
        row = int(val[1:2])
        row -= 1

        col = int(val[4:5])
        col -= 1

    except ValueError:
        print "\nIncorrect format. Here is an example: "
        print "    [1][9] will clear the very bottom left corner"

        return

    sudoku[row][col][0] = 0
    printSudoku(sudoku)


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
        row.append([nums[col], []])

    sudoku[rowInd] = row

    printSudoku(sudoku)


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
        col.append([nums[row], []])


    for row in range(9):
        sudoku[row][colInd] = col[row]

    printSudoku(sudoku)


# Give option to clear a row
def clearRow(sudoku):
    val = raw_input("\nEnter the row to clear: ")

    if len(val) != 1:
        print "\nIncorrect format. Just enter a number"
        return

    try:
        row = int(val) - 1

    except:
        print "\nIncorrect format. Just enter a number"
        return


    for col in range(9):
        sudoku[row][col][0] = 0

    printSudoku(sudoku)


# Give option to clear a row
def clearColumn(sudoku):
    val = raw_input("\nEnter the column to clear: ")

    if len(val) != 1:
        print "\nIncorrect format. Just enter a number"
        return

    try:
        col = int(val) - 1

    except:
        print "\nIncorrect format. Just enter a number"
        return


    for row in range(9):
        sudoku[row][col][0] = 0

    printSudoku(sudoku)



# Clears all cells in the Sudoku
def clearSudoku(sudoku):
    for y in range(9):
        for x in range(9):
            sudoku[x][y][0] = 0

    printSudoku(sudoku)


# Get the column with the input index
def getColumn(sudoku, col):
    ret = []

    for row in range(9):
        ret.append(sudoku[row][col-1])

    return ret


# Commands that will be printed in the main loop
def printMainOptions():
    print "\n|---------------|"
    print "|   Main Menu   |"
    print "|---------------|\n"
    print "0: Exit Program"
    print "1: Print Sudoku"
    print "2: Solve Sudoku"
    print "3: Enter values into Sudoku"
    print "4: Clear Sudoku"
    print "5: Load an easy Sudoku"



# Commands that will be printed in the value entering loop
def printEnterOptions():
    print "\n|------------------------|"
    print "|   Change Values Menu   |"
    print "|------------------------|\n"
    print "0: Go back"
    print "1: Enter a value"
    print "2: Clear a value"
    print "3: Enter a row"
    print "4: Enter a column"
    print "5: Clear a row"
    print "6: Clear a column"


if __name__ == '__main__':
    main()