msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else "undefined"
}
memory = float(0)


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def is_one_digit(num):
    return num > -10 and num < 10 and num.is_integer()


def main():

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

        if oper not in operations:
            print(msg_2)
            continue
        else:
            check(x, y, oper)
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
                        if is_one_digit(result):  # New loop starts here
                            msg_index = 10
                            while True:
                                print(globals()["msg_" + str(msg_index)])
                                answer = input().lower()
                                if answer == "y":
                                    if msg_index < 12:
                                        msg_index += 1
                                        continue
                                    else:
                                        memory = result
                                    break
                                elif answer == "n":
                                    break
                                else:
                                    continue
                        else:
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
                        # loop_status = False
                        exit(0)
                    else:
                        continue


if __name__ == '__main__':
    main()
