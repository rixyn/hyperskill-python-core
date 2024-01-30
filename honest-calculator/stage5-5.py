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
    return (True if (num > -10 and num < 10 and num.is_integer()) else False)


def main():
    accepted_operations = ["+", "-", "*", "/"]
    memory = float(0)
    loop_status = True

    while loop_status == True:

        if loop_status == False:
            break

        print(msg_0)
        calc = input()
        x, oper, y = calc.split()

        try:
            if x == "M":
                x = memory
            if y == "M":
                y = memory
            x, y = float(x), float(y)
        except ValueError:
            print(msg_1)
            continue

        if oper not in accepted_operations:
            print(msg_2)
            continue

        check(x, y, oper)

        if oper == "+":
            result = x + y
            print(result)
        elif oper == "-":
            result = x - y
            print(result)
        elif oper == "*":
            result = x * y
            print(result)
        elif oper == "/" and y != 0:
            result = x / y
            print(result)
        else:
            print(msg_3)
            continue

        while True:

            if loop_status == False:
                break

            print(msg_4)
            answer = input()

            if answer == "y" or answer == "Y":  # new loop starts here
                if is_one_digit(result):
                    msg_index = 10
                    while True:
                        print(globals()["msg_" + str(msg_index)])
                        new_answer = input()
                        if new_answer == "y" or new_answer == "Y":
                            if msg_index < 12:
                                msg_index += 1
                                continue
                            else:
                                memory = result
                        elif new_answer == "n" or new_answer == "N":
                            pass
                        else:
                            continue
                        break
                else:
                    memory = result
            elif answer == "n" or answer == "N":
                pass
            else:
                continue

            while True:

                print(msg_5)
                answer = input()

                if answer == "y" or answer == "Y":
                    break
                elif answer == "n" or answer == "N":
                    loop_status = False
                    break
                else:
                    continue
            break


if __name__ == '__main__':
    main()
