msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."

# accepted_operations = ["+", "-", "*", "/"]

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else "undefined"
}

while True:
    try:
        print(msg_0)
        calc = input()
        x, oper, y = calc.split()
        x, y = float(x), float(y)
    except ValueError:
        print(msg_1)
        continue
    # if oper not in accepted_operations:
    #     print(msg_2)
    #     continue
    # if oper == "+":
    #     print(x + y)
    #     break
    # elif oper == "-":
    #     print(x - y)
    #     break
    # elif oper == "*":
    #     print(x * y)
    #     break
    # elif oper == "/" and y != 0:
    #     print(x / y)
    #     break
    # else:
    #     print(msg_3)
    #     continue
    if oper in operations:
        result = operations[oper](x, y)
        if result == "undefined":
            print(msg_3)
            continue
        else:
            print(result)
            break
    else:
        print(msg_2)
        continue