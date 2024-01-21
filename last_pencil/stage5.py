""" Hyperskill: Last Pencil
Stage 5/5:  The right strategy
Difficulty: Easy
Track:      Python Core
Author:     Rixyn
Completed:  2024-01-17
"""

import random


def print_pencils(pencils):
    return "|" * pencils


def bot_turn(pencils):
    if pencils % 4 == 0:
        return 3
    elif pencils % 4 == 3:
        return 2
    elif pencils % 4 == 2:
        return 1
    else:
        return random.randint(1, min(3, pencils))


while True:
    try:
        num_pencils = int(input("How many pencils would you like to use: "))
        if num_pencils < 1:
            raise ValueError
        break
    except ValueError:
        print("The number of pencils should be positive and numeric")


while True:
    turn_name = input("Who will be the first (John, Jack): ")
    if turn_name in ["John", "Jack"]:
        break
    else:
        print("Choose between 'John' and 'Jack'")


while num_pencils > 0:
    print(print_pencils(num_pencils))
    if turn_name == "Jack":
        turn = bot_turn(num_pencils)
        print(f"Jack's turn:\n{turn}")
    else:
        while True:
            try:
                turn = int(input(f"{turn_name}'s turn! "))
                if turn in [1, 2, 3]:
                    if turn > num_pencils:
                        print("Too many pencils taken")
                    else:
                        break
                else:
                    print("Possible values: '1', '2', '3'")
            except ValueError:
                print("Possible values: '1', '2', '3'")
    num_pencils -= turn
    if num_pencils == 0:
        winner = "Jack" if turn_name == "John" else "John"
        print(f"{winner} won!")
        break
    turn_name = "Jack" if turn_name == "John" else "John"
