msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else "undefined"
}

memory = 0

while True:
    try:
        print(msg_0)
        calc = input()
        x, oper, y = calc.split()
        x = memory if x == "M" else float(x)
        y = memory if y == "M" else float(y)
    except ValueError:
        print(msg_1)
        continue
    if oper in operations:
        result = operations[oper](x, y)
        if result == "undefined":
            print(msg_3)
            continue
        else:
            print(result)
            while True:
                print(msg_4)
                answer = input().lower()
                if answer == "y":
                    memory = result
                    break
                elif answer == "n":
                    break
                else:
                    continue
            while True:
                print(msg_5)
                answer = input().lower()
                if answer == "y":
                    break
                elif answer == "n":
                    exit(0)
                else:
                    continue
    else:
        print(msg_2)
        continue
