import math
import argparse

loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

# write your code here

parser = argparse.ArgumentParser()

parser.add_argument('--type')
parser.add_argument('--payment', type=float)
parser.add_argument('--principal', type=float)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
args = parser.parse_args()

inputs = [args.type, args.interest, args.periods, args.principal, args.payment]


if args.type == "diff":
    if args.interest is None:
        print("Incorrect parameters.")
    else:
        p = args.principal
        n = args.periods
        i = args.interest
        i /= 1200

        total_payment = 0
        for m in range(1, n + 1):
            d = (p/n) + i * (p - (p * (m - 1)) / n)
            print(f'Month {m} : payment is {math.ceil(d)}')
            total_payment += math.ceil(d)
        overpayment = total_payment - p
        print(f'Overpayment={overpayment}')

elif args.type == "annuity":
    if args.interest is None:
        print("Incorrect parameters.")
    elif args.principal is None:
        a = args.payment
        n = args.periods
        i = args.interest
        i /= 1200

        p = a / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
        print(f'Your loan principal = {p}!')
        a = math.ceil(p * i * (math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
        total_payment = a * n
        overpayment = total_payment - p
        print(f'Overpayment={overpayment}')

    elif args.periods is None:
        p = args.principal
        a = args.payment
        i = args.interest
        i /= 1200

        n = math.ceil(math.log((a / (a - i * p)), i + 1))
        years = n // 12
        months = n % 12
        if years == 0:
            print(f'It will take {months} months to repay this loan!')
        elif months == 0:
            print(f'It will take {years} years to repay this loan!')
        else:
            print(f'It will take {years} years and {months} months to repay this loan!')
        total_payment = a * n
        overpayment = total_payment - p
        print(f'Overpayment={overpayment}')

    elif args.payment is None:
        p = args.principal
        n = args.periods
        i = args.interest
        i /= 1200

        a = math.ceil(p * i * (math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
        print(f'Your annuity payment = {a}!')
        total_payment = a * n
        overpayment = total_payment - p
        print(f'Overpayment={overpayment}')
