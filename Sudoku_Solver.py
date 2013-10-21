def main():

    # Initialise Sudoku
    sudoku = [[0 for col in range(9)] for row in range(9)]

    print "\nWelcome to the Sudoku solver.\n\n"

    # Start program, this will only exit if the user enters 0.
    while True:
        printMainOptions()

        # Get the input int value from the user
        try:
            cmd = int(raw_input("\n"))

            # Make sure the value entered is in the bounds
            if cmd < 0 or cmd > 4:
                print "\nPlease enter a number from 0 to 4.\n"
                continue

        # Only allow integer values to be entered
        except ValueError:
            print "\nPlease enter a number from 0 to 4.\n"
            continue


        # User options
        if cmd == 0:
            break

        elif cmd == 1:
            printSudoku(sudoku)

        elif cmd == 3:
            enterValueMode(sudoku)

        elif cmd == 4:
            clearSudoku(sudoku)



# Algorithm to solve the Sudoku
def solveSudoku(sudoku):


# Print the Sudoku to the command line
def printSudoku(sudoku):
    print " _ _ _ _ _ _ _ _ _ _ _ _ "

    for row in range(9):
        s = "| "

        for col in range(3):
            if sudoku[row][col] != 0:
                s += str(sudoku[row][col]) + " "
            else:
                s += "  "

        s += "| "

        for col in range(3, 6):
            if sudoku[row][col] != 0:
                s += str(sudoku[row][col]) + " "
            else:
                s += "  "

        s += "| "

        for col in range(6, 9):
            if sudoku[row][col] != 0:
                s += str(sudoku[row][col]) + " "
            else:
                s += "  "

        s+= "|"

        print s

        if row == 2 or row == 5:
            print "-------------------------"

    print "-------------------------\n"



# Change to the mode where you can enter values into the Sudoku
def enterValueMode(sudoku):
    while True:
        printEnterOptions()

        # Get the input int value from the user
        try:
            cmd = int(raw_input("\n"))

            # Make sure the value entered is in the bounds
            if cmd < 0 or cmd > 4:
                print "\nPlease enter a number from 0 to 2.\n"
                continue

        # Only allow integer values to be entered
        except ValueError:
            print "\nPlease enter a number from 0 to 2.\n"
            continue

        if cmd == 0:
            break

        elif cmd == 1:
            enterValue(sudoku)

        elif cmd == 2:
            clearValue(sudoku)



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

    sudoku[row][col] = num
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

    sudoku[row][col] = 0
    printSudoku(sudoku)



# Clears all cells in the Sudoku
def clearSudoku(sudoku):
    for y in range(9):
        for x in range(9):
            sudoku[x][y] = 0

    printSudoku(sudoku)



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



# Commands that will be printed in the value entering loop
def printEnterOptions():
    print "\n|------------------------|"
    print "|   Change Values Menu   |"
    print "|------------------------|\n"
    print "0: Go back"
    print "1: Enter a value"
    print "2: Clear a value"



if __name__ == '__main__':
    main()