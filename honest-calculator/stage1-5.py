msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"


while True:
    try:
        print(msg_0)
        calc = input()
        x, oper, y = calc.split()
        x, y = float(x), float(y)
    except ValueError:
        print(msg_1)
        continue
    if oper in ["+", "-", "*", "/"]:
        break
    else:
        print(msg_2)
        continue
