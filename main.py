# Import statement for the built in random package that is used by the computer to play the game
import random
# Import statement for the built in os package to clear the terminal when required
import os

# Main array which is modified to play the game
mainBoard = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

# Greetings and instructions on how to play the game
os.system('cls')
print("Welcome to Tic Tac Toe")
print("How to play?\nThis is a tic tac toe game played in the terminal so you cannot use your mouse\nHence the main playing board is in a grid of 9 x 9 and to enter your input enter the row and column number\nThe index starts from 0")
start = input("Do you wish to start? (Y/N) : ")

# Takes input from the player if they want to play or not
if start.lower() == 'n':
    os.system('cls')
    print("Very Well See Ya later!")
elif start.lower() == 'y':

    # Function to print an array in a 3 X 3 grid
    def printBoard(board):
        os.system('cls')
        for row in board:
            print(' | '.join(*zip(*row)))

    printBoard(mainBoard)

    gameOver = 0

    # Function that makes the computer play tic tac toe

    def computerTurn():
        compStatus = True

        while compStatus:
            row = random.randrange(0, 3)
            column = random.randrange(0, 3)

            if not any('_' in x for x in mainBoard):
                compStatus = False
            elif mainBoard[row][column] == '_':
                compStatus = False
                return [row, column]
            else:
                compStatus = True

    # Checks if the player has won the game

    def winCheckPlayer(board):
        if (board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O') or (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O') or (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O') or (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O') or (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O') or (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O') or (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
            printBoard(mainBoard)
            print("PLAYER WON!")
            global gameOver
            gameOver = 2

    # Checks if the computer has won the game

    def winCheckComp(board):
        if (board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X') or (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X') or (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X') or (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X') or (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X') or (board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X') or (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
            printBoard(mainBoard)
            print("YOU LOST!")
            global gameOver
            gameOver = 2

    # Main game loop
    while (gameOver < 1):

        userRowInput = int(input("Enter row: "))
        userColumnInput = int(input("Enter column: "))
        if userRowInput > 2 or userColumnInput > 2:
            print("Please enter index in the range 0 - 2")
        elif mainBoard[userRowInput][userColumnInput] != '_':
            print("That place is already occupied")
        else:
            mainBoard[userRowInput][userColumnInput] = 'O'
            winCheckPlayer(mainBoard)
            if gameOver == 2:
                break
            compMove = computerTurn()
            if not any('_' in x for x in mainBoard):
                printBoard(mainBoard)
                print("Game Over")
                gameOver = 2
            else:
                mainBoard[compMove[0]][compMove[1]] = 'X'
                winCheckComp(mainBoard)
                if gameOver == 2:
                    break
                printBoard(mainBoard)
else:
    print("Please enter Y (For Yes) or N (For No)")
