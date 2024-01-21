""" Hyperskill: Last Pencil
Stage 3/5:  Working on the gameplay 
Difficulty: Easy
Track:      Python Core
Author:     Rixyn
Completed:  2024-01-17
"""

def print_pencils(pencils):
    return "|" * pencils

num_pencils = int(input("How many pencils would you like to use: "))
turn_name = input("Who will be the first (John, Jack): ")
print(print_pencils(num_pencils))

while True:
    turn = int(input(f"{turn_name}'s turn: "))
    if turn > num_pencils or turn < 1:
        print("Invalid input")
        continue
    num_pencils -= turn
    if num_pencils == 0:
        # print(f"{turn_name} won!")
        break
    print(print_pencils(num_pencils))
    turn_name = "Jack" if turn_name == "John" else "John"