board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def checkWinner(board, player):
    # horizontal
    if (board[0] == board[1] == board[2] == player or
        board[3] == board[4] == board[5] == player or
        board[6] == board[7] == board[8] == player):
        return True
    # vertical
    if (board[0] == board[3] == board[6] == player or
        board[1] == board[4] == board[7] == player or
        board[2] == board[5] == board[8] == player):
        return True
    # diagonal
    if (board[0] == board[4] == board[8] == player or
        board[2] == board[4] == board[6] == player):
        return True
    return False

def isBoardFull(board):
    return "-" not in board

def playerInput(board):
    while True:
        try:
            inp = input(f"Player {currentPlayer}, enter your move as x,y (0-2, column,row): ")
            x, y = map(int, inp.split(","))
            if x < 0 or x > 2 or y < 0 or y > 2:
                print("Values must be 0, 1, or 2.")
                continue
            index = y * 3 + x
            if board[index] == "-":
                board[index] = currentPlayer
                break
            else:
                print("That spot is already taken!")
        except:
            print("Invalid input, try again!")

while gameRunning:
    printBoard(board)
    playerInput(board)
    
    if checkWinner(board, currentPlayer):
        printBoard(board)
        print(f"Player {currentPlayer} wins!")
        break
    if isBoardFull(board):
        printBoard(board)
        print("It's a draw!")
        break
    
    currentPlayer = "O" if currentPlayer == "X" else "X"

print("Game over.")
