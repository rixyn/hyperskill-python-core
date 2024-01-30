""" Hyperskill: Last Pencil
Stage 4/5:  Fair play
Difficulty: Easy
Track:      Python Core
Author:     Rixyn
Completed:  2024-01-17
"""


def print_pencils(pencils):
    return "|" * pencils


while True:
    try:
        num_pencils = int(input("How many pencils would you like to use: "))
    except (TypeError, ValueError):
        print("The number of pencils should be numeric")
        continue
    num_pencils = int(num_pencils)
    if num_pencils < 1:
        print("The number of pencils should be positive")
        continue
    else:
        break


while True:
    turn_name = input("Who will be the first (John, Jack): ")
    if turn_name not in ["John", "Jack"]:
        print("Choose between 'John' and 'Jack'")
        continue
    else:
        print(print_pencils(num_pencils))
        break


while True:
    acceptable_turns = [1, 2, 3]

    try:
        turn = int(input(f"{turn_name}'s turn!  "))
    except (TypeError, ValueError):
        print("Possible values: '1', '2' or '3'")
        continue
    if turn not in acceptable_turns:
        print("Possible values: '1', '2' or '3'")
        continue
    elif turn > num_pencils:
        print("Too many pencils taken")
        continue
    else:
        num_pencils -= turn

    if num_pencils == 0:
        winner = "Jack" if turn_name == "John" else "John"
        print(f"{winner} won!")
        break
    print(print_pencils(num_pencils))
    turn_name = "Jack" if turn_name == "John" else "John"
