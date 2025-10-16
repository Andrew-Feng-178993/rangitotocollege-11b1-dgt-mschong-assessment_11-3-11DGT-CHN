"""board = { "-", "-", "-",
          "-", "-", "-",
          "-", "-", "-" }
currentPlayer = "X"
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def playerInput(board):
    inp = int(input("Enter a number from 1 to 9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("A player is already in that position!")





while gameRunning:
    printBoard(board)
    playerInput(board)

      """
def print_board(board):
    """Prints the tic-tac-toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    """Check if the given player has won."""
    # rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_board_full(board):
    """Return True if board is full (no empty spaces)."""
    return all(cell != " " for row in board for cell in row)


def get_move(player):
    """Prompt the player to enter a move (row, col)."""
    while True:
        move = input(f"Player {player}, enter your move as row,col (0-2): ")
        parts = move.split(",")
        if len(parts) != 2:
            print("Invalid format. Use row,col.")
            continue
        try:
            r = int(parts[0].strip())
            c = int(parts[1].strip())
        except ValueError:
            print("Invalid numbers. Try again.")
            continue
        if r < 0 or r > 2 or c < 0 or c > 2:
            print("Out of bounds. Use values 0,1,2.")
            continue
        return r, c


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        r, c = get_move(current_player)
        if board[r][c] != " ":
            print("That spot is already taken. Try again.")
            continue
        board[r][c] = current_player
        
        # Check for win
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"
    
    print("Game over.")


if __name__ == "__main__":
    main()
