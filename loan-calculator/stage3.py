""" Hyperskill: Loan Calculator Project
Stage 3/4:  Annuity payment
Difficulty: Medium
Track:      Python Core
Author:     Rixyn
Completed:  2024-01-16
"""

import math
import argparse


def calculate_payment(principal, periods, interest):
    i = interest / (12 * 100)
    payment = principal * (i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1)
    return math.ceil(payment)


def calculate_principal(payment, periods, interest):
    i = interest / (12 * 100)
    principal = payment / ((i * pow(1 + i, periods)) /
                           (pow(1 + i, periods) - 1))
    return principal


def calculate_periods(principal, payment, interest):
    i = interest / (12 * 100)
    periods = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
    return periods


def format_periods(periods):
    years = periods // 12
    months = periods % 12
    year_str = f"{years} {'year' if years == 1 else 'years'}" if years > 0 else ""
    month_str = f"{months} {'month' if months == 1 else 'months'}" if months > 0 else ""
    return f"{year_str} and {month_str}" if year_str and month_str else f"{year_str}{month_str}"


def main():
    parser = argparse.ArgumentParser(description="Loan Calculator")
    parser.add_argument("--payment", type=float, help="the payment amount")
    parser.add_argument("--principal", type=float, help="loan principal")
    parser.add_argument("--periods", type=int,
                        help="number of months needed to repay the loan")
    parser.add_argument("--interest", type=float,
                        help="loan interest rate without a percent sign")
    args = parser.parse_args()

    if args.interest is None:
        print("Interest rate is required.")
        return

    if args.principal is None:
        principal = calculate_principal(
            args.payment, args.periods, args.interest)
        print(f"Your loan principal = {principal:.0f}!")
    elif args.payment is None:
        payment = calculate_payment(
            args.principal, args.periods, args.interest)
        print(f"Your monthly payment = {payment:.0f}!")
    elif args.periods is None:
        periods = calculate_periods(
            args.principal, args.payment, args.interest)
        formatted_periods = format_periods(periods)
        print(f"It will take {formatted_periods} to repay this loan!")


if __name__ == '__main__':
    main()
