import random

def print_board(board):
    """
    Prints the current state of the Tic-Tac-Toe board.

    Args:
    board (list of list of str): The game board to print, a 3x3 matrix.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    """
    Checks if the specified player has won the game.

    Args:
    board (list of list of str): The game board.
    player (str): The player to check, either 'X' or 'O'.

    Returns:
    bool: True if the player has won, False otherwise.
    """
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    """
    Checks if the game is a draw (i.e., the board is full and there is no winner).

    Args:
    board (list of list of str): The game board.

    Returns:
    bool: True if the game is a draw, False otherwise.
    """
    for row in board:
        if any([spot == " " for spot in row]):
            return False
    return True

def find_best_move(board, player):
    """
    Finds the best move for the AI player.

    Args:
    board (list of list of str): The game board.
    player (str): The AI player, either 'X' or 'O'.

    Returns:
    tuple: The row and column of the best move.
    """
    opponent = 'X' if player == 'O' else 'O'

    # Check for possible winning move
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                board[r][c] = player
                if check_win(board, player):
                    return (r, c)
                board[r][c] = " "

    # Check for possible blocking move
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                board[r][c] = opponent
                if check_win(board, opponent):
                    return (r, c)
                board[r][c] = " "

    # Choose a random corner if available
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    random.shuffle(corners)
    for r, c in corners:
        if board[r][c] == " ":
            return (r, c)

    # Choose the center if available
    if board[1][1] == " ":
        return (1, 1)

    # Choose a random side if available
    sides = [(0, 1), (1, 0), (1, 2), (2, 1)]
    random.shuffle(sides)
    for r, c in sides:
        if board[r][c] == " ":
            return (r, c)

    # Choose a random move as a fallback
    empty_spots = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    if empty_spots:
        return random.choice(empty_spots)

def tic_tac_toe():
    """
    Main function to play the Tic-Tac-Toe game.
    """
    while True:
        # Initialize the game board, a 3x3 matrix filled with spaces
        board = [[" " for _ in range(3)] for _ in range(3)]
        players = ["X", "O"]
        turn = 0
        
        # Choose game mode
        mode = input("Enter '1' for single player mode, '2' for multiplayer mode: ").strip()
        
        while True:
            print_board(board)
            player = players[turn % 2]
            
            if mode == '1' and player == 'O':
                row, col = find_best_move(board, player)
                board[row][col] = player
            else:
                print(f"Player {player}'s turn")
                try:
                    row, col = map(int, input("Enter row and column (0, 1, or 2): ").split())
                    if board[row][col] != " ":
                        print("Spot already taken. Try again.")
                        continue
                except (ValueError, IndexError):
                    print("Invalid input. Please enter row and column as two numbers (0, 1, or 2).")
                    continue
                board[row][col] = player
            
            if check_win(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            
            turn += 1

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    tic_tac_toe()
