game_pieces = "XO_"


def check_win(board):
    rows = board
    cols = [[row[i] for row in board] for i in range(3)]
    diags = [[board[i][i]
              for i in range(3)], [board[i][2-i] for i in range(3)]]

    for line in rows + cols + diags:
        if len(set(line)) == 1 and line[0] in "XO":
            print(f"{line[0]} wins")
            return True

    if all(cell != "_" for row in board for cell in row):
        print("Draw")
        return True
    return False


def check_first_turn(usr_input):
    return usr_input.count("X") <= usr_input.count("O")


def check_initial_input(usr_input):
    if len(usr_input) != 9:
        print("Input needs to be nine (9) cells. Try again.")
        return False
    if any(cell not in game_pieces for cell in usr_input):
        print("Improper game pieces. Try again.")
        return False
    return True


def check_turn_input(usr_input):
    try:
        new_input = [int(coordinate) for coordinate in usr_input.split()]
        if len(new_input) != 2 or any(not 1 <= n <= 3 for n in new_input):
            raise ValueError
    except ValueError:
        print("Invalid input. Coordinates should be two numbers from 1 to 3.")
        return False
    return [n - 1 for n in new_input]


def print_board(current_board):
    print("---------")
    for row in current_board:
        print(f"| {' '.join(cell.replace('_', ' ') for cell in row)} |")
    print("---------")
    return check_win(current_board)


def check_board(new_coords, current_board):
    return current_board[new_coords[0]][new_coords[1]] == "_"


def main():
    while True:
        board = input("Enter the cells: ")
        if not check_initial_input(board):
            continue
        break

    current_board = [list(board[i:i+3]) for i in range(0, 9, 3)]
    print_board(current_board)
    current_turn = "X" if check_first_turn(board) else "O"

    while True:
        print(f"{current_turn}'s turn.")
        usr_input = input("Enter the coordinates: ")
        new_coords = check_turn_input(usr_input)
        if not new_coords or not check_board(new_coords, current_board):
            print("Invalid move. Try again.")
            continue

        current_board[new_coords[0]][new_coords[1]] = current_turn
        if print_board(current_board):
            break
        current_turn = "O" if current_turn == "X" else "X"


if __name__ == "__main__":
    main()
