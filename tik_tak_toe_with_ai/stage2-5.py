import random

game_pieces = "XO_"


def check_win(current_board):
    first_row = current_board[0]
    second_row = current_board[1]
    third_row = current_board[2]
    if len(set(first_row)) == 1:
        if first_row[0] == "X":
            print("X wins")
            return True
        elif first_row[0] == "O":
            print("O wins")
            return True
    elif len(set(second_row)) == 1:
        if second_row[0] == "X":
            print("X wins")
            return True
        elif second_row[0] == "O":
            print("O wins")
            return True
    elif len(set(third_row)) == 1:
        if third_row[0] == "X":
            print("X wins")
            return True
        elif third_row[0] == "O":
            print("O wins")
            return True
    elif len(set([first_row[0], second_row[0], third_row[0]])) == 1:
        if first_row[0] == "X":
            print("X wins")
            return True
        elif first_row[0] == "O":
            print("O wins")
            return True
    elif len(set([first_row[1], second_row[1], third_row[1]])) == 1:
        if first_row[1] == "X":
            print("X wins")
            return True
        elif first_row[1] == "O":
            print("O wins")
            return True
    elif len(set([first_row[2], second_row[2], third_row[2]])) == 1:
        if first_row[2] == "X":
            print("X wins")
            return True
        elif first_row[2] == "O":
            print("O wins")
            return True
    elif len(set([first_row[0], second_row[1], third_row[2]])) == 1:
        if first_row[0] == "X":
            print("X wins")
            return True
        elif first_row[0] == "O":
            print("O wins")
            return True
    elif len(set([first_row[2], second_row[1], third_row[0]])) == 1:
        if first_row[2] == "X":
            print("X wins")
            return True
        elif first_row[2] == "O":
            print("O wins")
            return True
    elif ("_" not in first_row) and ("_" not in second_row) and ("_" not in third_row):
        print("Draw")
        return True
    else:
        return False


def check_first_turn(usr_input):
    num_x = 0
    num_o = 0
    for cell in usr_input:
        if cell == "X":
            num_x += 1
        if cell == "O":
            num_o += 1
    if num_x <= num_o:
        return True
    else:
        return False


def check_initial_input(usr_input):
    if len(usr_input) != 9:
        print("Input needs to be nine (9) cells.  Try again.")
        return False
    for cell in usr_input:
        if cell not in game_pieces:
            print("Improper game pieces.  Try again.")
            return False
    return True


def check_turn_input(usr_input):
    check_input = usr_input.split()
    try:
        new_input = [int(coordinate) for coordinate in check_input]
    except Exception:
        print("You should enter numbers!")
        return False
    if len(check_input) != 2:
        print("You should only enter two (2) coordinates. Try again.")
        return False
    elif (0 < new_input[0] > 3) or (0 < new_input[1] > 3):
        print("Coordinates should be from 1 to 3!")
        return False
    else:
        usr_coordinates = [new_input[0] - 1, new_input[1] - 1]
        return usr_coordinates


def print_board(current_board):
    first_row = current_board[0]
    second_row = current_board[1]
    third_row = current_board[2]
    print("---------")
    print(f"| {' '.join(first_row).replace('_', ' ')} |")
    print(f"| {' '.join(second_row).replace('_', ' ')} |")
    print(f"| {' '.join(third_row).replace('_', ' ')} |")
    print("---------")


def make_computer_move(board):
    empty_cells = []

    # Find all the empty cells on the board
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "_":
                empty_cells.append((row, col))

    # Choose a random empty cell
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"
        return board
    else:
        print("No empty spots.")


def check_board(new_coords, current_board):
    column = new_coords[0]
    row = new_coords[1]
    first_row = current_board[0]
    second_row = current_board[1]
    third_row = current_board[2]
    if column == 0:
        if first_row[row] != "_":
            return False
        else:
            return True
    elif column == 1:
        if second_row[row] != "_":
            return False
        else:
            return True
    elif column == 2:
        if third_row[row] != "_":
            return False
        else:
            return True


def main():
    current_turn = "X"
    current_board = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
    ]
    while True:
        # print(f"{current_turn}'s turn.")
        if current_turn == "X":
            print_board(current_board)
            usr_input = input("Enter the coordinates: ")
            if not check_turn_input(usr_input):
                continue
            else:
                new_coords = check_turn_input(usr_input)
                if not check_board(new_coords, current_board):
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    current_board[new_coords[0]][new_coords[1]] = current_turn
                    print_board(current_board)
                    if check_win(current_board):
                        break
                    else:
                        print("Game not finished")
                        current_turn = "O"
                        continue
        else:
            print('Making move level "easy"')
            current_board = make_computer_move(current_board)
            print_board(current_board)
            if check_win(current_board):
                break
            else:
                current_turn = "X"
                continue


if __name__ == "__main__":
    main()
