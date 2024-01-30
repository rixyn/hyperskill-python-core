import random

game_pieces = "XO_"


def check_win(board):
    # Check for winning conditions in rows, columns, and diagonals
    for line in board + list(zip(*board)) + [[board[i][i] for i in range(3)], [board[i][2-i] for i in range(3)]]:
        if len(set(line)) == 1 and line[0] in "XO":
            print(f"{line[0]} wins")  # Announce the winner
            return True

    # Check for a draw (no empty cells left)
    if all(cell != "_" for row in board for cell in row):
        print("Draw")
        return True
    return False


def check_turn_input(usr_input):
    try:
        # Split the input into coordinates and convert to integers
        new_input = [int(coordinate) for coordinate in usr_input.split()]
        # Check for valid input (two coordinates, each between 1 and 3)
        if len(new_input) != 2 or any(not 1 <= n <= 3 for n in new_input):
            raise ValueError
    except ValueError:
        # Handle invalid input
        print("Invalid input. Coordinates should be two numbers from 1 to 3.")
        return None
    return [n - 1 for n in new_input]  # Adjust for zero-based indexing


def print_board(board):
    # Print the current state of the board
    print("---------")
    for row in board:
        print(f"| {' '.join(cell.replace('_', ' ') for cell in row)} |")
    print("---------")


def make_computer_move(board):
    # Find all empty cells on the board
    empty_cells = [(r, c) for r in range(3)
                   for c in range(3) if board[r][c] == "_"]
    if empty_cells:
        row, col = random.choice(empty_cells)  # Choose a random empty cell
        board[row][col] = "O"  # Place the computer's move
    else:
        print("No empty spots.")
    return board


def is_cell_free(coords, board):
    # Check if the selected cell is empty
    row, col = coords
    return board[row][col] == "_"


def main():
    current_turn = "X"  # Start with player X
    board = [["_"] * 3 for _ in range(3)]  # Initialize an empty board

    while True:
        if current_turn == "X":
            print_board(board)  # Display the board
            usr_input = input("Enter the coordinates: ")
            # Validate and parse user input
            coords = check_turn_input(usr_input)
            if coords and is_cell_free(coords, board):
                board[coords[0]][coords[1]] = current_turn  # Make the move
                if check_win(board):  # Check for a win or draw after the move
                    break
                current_turn = "O"  # Switch turns
            else:
                print("Invalid move or cell occupied. Try again.")
        else:
            # Computer's turn
            print('Making move level "easy"')
            board = make_computer_move(board)  # Make a move for the computer
            print_board(board)  # Display the board
            if check_win(board):  # Check for a win or draw after the move
                break
            current_turn = "X"  # Switch turns


if __name__ == "__main__":
    main()
