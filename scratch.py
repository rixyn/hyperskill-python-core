import math
import argparse


def calculate_annuity_payment(principal, periods, interest):
    i = interest / (12 * 100)
    payment = principal * (i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1)
    return math.ceil(payment)


def calculate_principal(payment, periods, interest):
    i = interest / (12 * 100)
    principal = payment / ((i * pow(1 + i, periods)) /
                           (pow(1 + i, periods) - 1))
    return round(principal)


def calculate_periods(principal, payment, interest):
    i = interest / (12 * 100)
    periods = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
    return periods


def calculate_diff_payments(principal, periods, interest):
    i = interest / (12 * 100)
    total_payment = 0
    for m in range(1, periods + 1):
        diff_payment = math.ceil(
            principal / periods + i * (principal - (principal * (m - 1)) / periods))
        total_payment += diff_payment
        print(f"Month {m}: payment is {diff_payment}")
    return total_payment


def format_periods(periods):
    years = periods // 12
    months = periods % 12
    year_str = f"{years} {'year' if years == 1 else 'years'}" if years > 0 else ""
    month_str = f"{months} {'month' if months == 1 else 'months'}" if months > 0 else ""
    return f"{year_str} and {month_str}" if year_str and month_str else f"{year_str}{month_str}"


def main():
    parser = argparse.ArgumentParser(description="Loan Calculator")
    parser.add_argument(
        "--type", choices=["annuity", "diff"], help="type of payment: 'annuity' or 'diff'")
    parser.add_argument("--payment", type=float, help="the payment amount")
    parser.add_argument("--principal", type=float, help="loan principal")
    parser.add_argument("--periods", type=int,
                        help="number of months needed to repay the loan")
    parser.add_argument("--interest", type=float,
                        help="loan interest rate without a percent sign")
    args = parser.parse_args()

    # Validation of parameters
    if (args.type is None or args.interest is None or
        (args.type == "diff" and args.payment is not None) or
        (args.principal is not None and args.principal < 0) or
        (args.periods is not None and args.periods < 0) or
        (args.payment is not None and args.payment < 0) or
            (args.interest is not None and args.interest < 0)):
        print("Incorrect parameters")
        return

    if args.type == "annuity":
        if args.principal is None:
            principal = calculate_principal(
                args.payment, args.periods, args.interest)
            print(f"Your loan principal = {principal}!")
            overpayment = int(args.payment * args.periods - principal)
        elif args.payment is None:
            payment = calculate_annuity_payment(
                args.principal, args.periods, args.interest)
            print(f"Your annuity payment = {payment}!")
            overpayment = int(payment * args.periods - args.principal)
        elif args.periods is None:
            periods = calculate_periods(
                args.principal, args.payment, args.interest)
            formatted_periods = format_periods(periods)
            print(f"It will take {formatted_periods} to repay this loan!")
            overpayment = int(args.payment * periods - args.principal)
        print(f"Overpayment = {overpayment}")

    elif args.type == "diff":
        total_payment = calculate_diff_payments(
            args.principal, args.periods, args.interest)
        overpayment = int(total_payment - args.principal)
        print(f"Overpayment = {overpayment}")


if __name__ == '__main__':
    main()
