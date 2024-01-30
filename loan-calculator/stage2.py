""" Hyperskill: Loan Calculator Project
Stage 2/4:  Dreamworld
Difficulty: Medium
Track:      Python Core
Author:     Rixyn
Completed:  2024-01-16
"""

import math


def payment(principal, periods, interest=0):
    return principal / periods + interest * principal


def last_payment(principal, payment, periods):
    return principal - (periods - 1) * payment


def main():
    principal = int(input("Enter the loan principal: "))
    option = input("""What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment: """)
    if option == "m":
        payment = int(input("Enter the monthly payment: "))
        periods = math.ceil(principal / payment)
        print(
            f"It will take {periods} {'months' if periods > 1 else 'month'} to repay the loan")
    elif option == "p":
        periods = int(input("Enter the number of months: "))
        payment = math.ceil(principal / periods)
        last = last_payment(principal, payment, periods)
        if last != payment:
            print(
                f"Your monthly payment = {payment} and the last payment = {last}")
        else:
            print(f"Your monthly payment = {payment}")
    else:
        print("Invalid option")


if __name__ == '__main__':
    main()
