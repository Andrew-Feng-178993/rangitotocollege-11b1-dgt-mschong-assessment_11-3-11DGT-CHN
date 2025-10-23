"""my Tic Tac Toe Game."""

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
scores = {}
gameRunning = True

def printBoard(board):
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def checkWinner(board, mark):
    if (board[0] == board[1] == board[2] == mark or
        board[3] == board[4] == board[5] == mark or
        board[6] == board[7] == board[8] == mark or
        board[0] == board[3] == board[6] == mark or
        board[1] == board[4] == board[7] == mark or
        board[2] == board[5] == board[8] == mark or
        board[0] == board[4] == board[8] == mark or
        board[2] == board[4] == board[6] == mark):
        return True
    return False

def isBoardFull(board):
    return "-" not in board

def playerInput(board, player_name, mark):
    while True:
        try:
            inp = input(f"{player_name} ({mark}), enter your move as x,y (1-3, column,row): ")
            x, y = map(int, inp.split(","))
            if x < 1 or x > 3 or y < 1 or y > 3:
                print("Values must be 1, 2, or 3.")
                continue
            index = (y - 1) * 3 + (x - 1)
            if board[index] == "-":
                board[index] = mark
                break
            else:
                print("That spot is already taken!")
        except:
            print("Invalid input, try again!")

print("WELCOME TO ANDREW'S TIC TAC TOE GAME!!!\n")

player1 = input("Enter name for Player 1: ")
symbol1 = input(f"{player1}, choose your symbol: ")
player2 = input("Enter name for Player 2: ")
symbol2 = input(f"{player2}, choose your symbol (must be different from {symbol1}): ")

while symbol2 == symbol1:
    print("That symbol is already taken. Choose a different one.")
    symbol2 = input(f"{player2}, choose your symbol: ")

scores[player1] = 0
scores[player2] = 0

while gameRunning:
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    currentPlayer = player1
    currentMark = symbol1

    while True:
        printBoard(board)
        playerInput(board, currentPlayer, currentMark)
        if checkWinner(board, currentMark):
            printBoard(board)
            print(f"{currentPlayer} wins this round!")
            scores[currentPlayer] += 1
            break
        if isBoardFull(board):
            printBoard(board)
            print("It's a draw!")
            break
        if currentPlayer == player1:
            currentPlayer = player2
            currentMark = symbol2
        else:
            currentPlayer = player1
            currentMark = symbol1

    print(f"Scores: {player1} = {scores[player1]}, {player2} = {scores[player2]}")
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print()
        print("FINAL SCORES:")
        print(f"{player1}: {scores[player1]}")
        print(f"{player2}: {scores[player2]}")
        print("Thanks for playing!")
        break
