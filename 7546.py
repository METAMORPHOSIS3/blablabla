# Import Random module for generating random numbers
import random

# Function to draw the board
def draw_board():
    # Create a 3x3 grid of underscores
    print("  1 | 2 | 3")
    print("  ---------")
    print("  4 | 5 | 6")
    print("  ---------")
    print("  7 | 8 | 9")

# Function to get user input and check if it's a valid move
def get_user_input(row, col):
    # Ask the user for their move
    move = input("Enter row and column (1-9): ")
    # Check if the move is valid
    if not validate_move(row, col, move):
        # If the move is invalid, prompt the user again
        return get_user_input(row, col)
    else:
        # If the move is valid, return the move
        return move

# Function to validate a move
def validate_move(row, col, move):
    # Check if the move is outside the bounds of the board
    if move < 1 or move > 9:
        return False
    # Check if the move is a diagonal move
    if abs(row - move) == abs(col - move):
        return False
    # Check if the move is a horizontal or vertical move
    elif abs(row - move) == 1 or abs(col - move) == 1:
        return True
    else:
        return False

# Main game loop
while True:
    # Draw the board
    draw_board()

    # Get the user's move
    move = get_user_input(randint(0, 2), randint(0, 2))

    # Update the board with the user's move
    if validate_move(randint(0, 2), randint(0, 2), move):
        # If the move is valid, update the board and display the new state
        print("O has been placed in", move[0], move[1])
        # Update the board
        board[move[0]][move[1]] = "X"
        # Display the updated board
        draw_board()
    else:
        # If the move is invalid, display an error message and prompt the user again
        print("Invalid move. Try again.")

# Game over checks
if len([i for i in board if i != "_"]) == 9:
    print("Game over! O has won.")
elif len([i for i in board if i == "_"]) == 9:
    print("Game over! X has won.")
else:
    print("The game is still ongoing.")