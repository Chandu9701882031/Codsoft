def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    turns = 0

    while turns < 9:
        print_board(board)
        row = int(input(f"Player {player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {player}, enter column (0, 1, 2): "))

        if board[row][col] != " ":
            print("This position is already taken. Try again.")
            continue

        board[row][col] = player
        turns += 1

        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        player = "O" if player == "X" else "X"

    if turns == 9:
        print_board(board)
        print("It's a draw!")

tic_tac_toe()
