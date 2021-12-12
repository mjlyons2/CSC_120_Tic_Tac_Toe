from board import printBoard
from implement_one import playerInput
from implement_one import checkWin

gameRunning = True
winner = None
currentPlayer = "X"
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

while gameRunning == True:

    printBoard(board)
    playerInput(board, currentPlayer)

    if currentPlayer == "X":
        checkWin(board, currentPlayer)
        currentPlayer = "O"

    elif currentPlayer == "O":
        checkWin(board, currentPlayer)
        currentPlayer = "X"