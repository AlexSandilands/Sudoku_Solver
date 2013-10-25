import Sudoku_solver as solver
import Sudoku_edit as editor

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
            solver.solveSudoku(sudoku)

        elif cmd == 3:
            editor.enterValueMode(sudoku)

        elif cmd == 4:
            editor.clearSudoku(sudoku)

        elif cmd == 5:
            loadEasy(sudoku)



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



if __name__ == '__main__':
    main()