def print_board(board):
    """
    Prints the current state of the Tic-Tac-Toe board.

    Args:
    board (list of list of str): The game board to print, a 3x3 matrix.
    """
    for row in board:
        # Join the elements of the row with ' | ' and print it
        print(" | ".join(row))
        # Print a separator line
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
    # Check rows for a win
    for row in board:
        if all([spot == player for spot in row]):
            return True
    # Check columns for a win
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals for a win
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
        # If there is any empty spot, it's not a draw
        if any([spot == " " for spot in row]):
            return False
    return True

def tic_tac_toe():
    """
    Main function to play the Tic-Tac-Toe game.
    """
    # Initialize the game board, a 3x3 matrix filled with spaces
    board = [[" " for _ in range(3)] for _ in range(3)]
    # Define the players, 'X' and 'O'
    players = ["X", "O"]
    # Start with the first player's turn
    turn = 0
    
    while True:
        # Print the current state of the board
        print_board(board)
        # Determine the current player
        player = players[turn % 2]
        print(f"Player {player}'s turn")
        
        try:
            # Prompt the player to enter row and column
            row, col = map(int, input("Enter row and column (0, 1, or 2): ").split())
            # Check if the chosen spot is already taken
            if board[row][col] != " ":
                print("Spot already taken. Try again.")
                continue
        except (ValueError, IndexError):
            # Handle invalid input
            print("Invalid input. Please enter row and column as two numbers (0, 1, or 2).")
            continue
        
        # Place the player's mark on the board
        board[row][col] = player
        
        # Check if the current player has won
        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        # Check if the game is a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch to the next player's turn
        turn += 1

if __name__ == "__main__":
    # Start the game
    tic_tac_toe()
