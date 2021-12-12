from board import printBoard
def playerInput(board, currentPlayer):
    location = int(input("Enter a number 1-9: "))
    if location >= 1 and location <= 9 and board[location-1] == "-":
        board[location-1] = currentPlayer
    elif location > 9:
        print("This isn't a square")
        printBoard(board)
        playerInput(board, currentPlayer)
    else:
        print("This square is already taken")
        printBoard(board)
        playerInput(board, currentPlayer)

def checkWin(board, currentPlayer):

    #horizontal wins
    if board[0] == currentPlayer and board[1] == currentPlayer and board[2] == currentPlayer:
        print(currentPlayer + " has won!")
        printBoard(board)
        quit()

    elif board[3] == currentPlayer and board[4] == currentPlayer and board[5] == currentPlayer:
        print(currentPlayer + " has won!")
        printBoard(board)
        quit()

    elif board[6] == currentPlayer and board[7] == currentPlayer and board[8] == currentPlayer:
        print(currentPlayer + " has won!")
        printBoard(board)
        quit()

    #vertical wins
    elif board[0] == currentPlayer and board[3] == currentPlayer and board[6] == currentPlayer:
        print(currentPlayer + " has won!")
        printBoard(board)
        quit()

    elif board[1] == currentPlayer and board[4] == currentPlayer and board[7] == currentPlayer:
        print(currentPlayer + " has won!")
        printBoard(board)
        quit()

    elif board[2] == currentPlayer and board[5] == currentPlayer and board[8] == currentPlayer:
        print(currentPlayer + " has won!")
        printBoard(board)
        quit()

    #diagonal wins
    elif board[0] == currentPlayer and board[4] == currentPlayer and board[8] == currentPlayer:
        print(currentPlayer + " has won!")
        printBoard(board)
        quit()

    elif board[6] == currentPlayer and board[4] == currentPlayer and board[2] == currentPlayer:
        print(currentPlayer + " has won!")
        printBoard(board)
        quit()

    #draw
    elif not any("-" in s for s in board) == True:
        print("Draw!")
        printBoard(board)
        quit()

    #pass
    else:
        pass
