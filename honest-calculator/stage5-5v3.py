messages = ["Enter an equation", "Do you even know what numbers are? Stay focused!", "Yes ... an interesting math operation. You've slept through all classes, haven't you?", "Yeah... division by zero. Smart move...",
            "Do you want to store the result? (y / n):", "Do you want to continue calculations? (y / n):", " ... lazy", " ... very lazy", " ... very, very lazy", "You are", "Are you sure? It is only one digit! (y / n)", "Don't be silly! It's just one number! Add to the memory? (y / n)", "Last chance! Do you really want to embarrass yourself? (y / n)"]
operations = {"+": lambda x, y: x + y, "-": lambda x, y: x - y,
              "*": lambda x, y: x * y, "/": lambda x, y: x / y if y != 0 else "undefined"}
memory = 0.0


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += messages[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += messages[7]
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += messages[8]
    if msg != "":
        print(messages[9] + msg)


def is_one_digit(num):
    return -10 < num < 10 and num.is_integer()


def main():
    global memory
    while True:
        try:
            print(messages[0])
            x, oper, y = input().split()
            x = memory if x == "M" else float(x)
            y = memory if y == "M" else float(y)
        except ValueError:
            print(messages[1])
            continue
        if oper not in operations:
            print(messages[2])
            continue
        check(x, y, oper)
        result = operations[oper](x, y)
        if result == "undefined":
            print(messages[3])
            continue
        print(result)
        if input(messages[4]).lower() == "y":
            if is_one_digit(result):
                for i in range(10, 13):
                    if input(messages[i]).lower() == "n":
                        break
                else:
                    memory = result
            else:
                memory = result
        if input(messages[5]).lower() == "n":
            break


if __name__ == '__main__':
    main()
