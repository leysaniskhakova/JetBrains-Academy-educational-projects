import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment", type= int)
parser.add_argument("--principal", type= int)
parser.add_argument("--periods", type= int)
parser.add_argument("--interest", type= float)
args = parser.parse_args()

monthly_payment = args.type
credit_principal = args.principal
count_of_periods = args.periods
credit_interest = args.interest
payment = args.payment


def nomimal(credit_interest):
    return credit_interest / (12 * 100)

def bases(count_of_periods, nominal_interest):
    xbase = math.pow((1 + nominal_interest), count_of_periods)
    return nominal_interest * xbase / (xbase - 1)

def overpayment(credit_principal, pay):
    overpayment = int(abs(credit_principal - pay))
    print(f'Overpayment = {overpayment}')

def annuity_monthly_payment(credit_principal, base, count_of_periods):
    annuity_payment = math.ceil(credit_principal * base)
    print(f'Your annuity payment = {annuity_payment}!')
    pay = annuity_payment * count_of_periods
    overpayment(credit_principal, pay)

def differentiated_monthly_payment(credit_principal, count_of_periods, nominal_interest):
    pay = 0
    for month in range(1, count_of_periods + 1):
        differentiated_payment = math.ceil(credit_principal / count_of_periods +\
                                 nominal_interest * (credit_principal - (credit_principal * (month - 1))/ count_of_periods))
        pay += differentiated_payment
        print(f'Month {month}: paid out {differentiated_payment}')
    print()
    overpayment(credit_principal, pay)

def creditprincipal(payment, base, count_of_periods):
    principal = math.floor(payment / base)
    print(f'Your credit principal = {principal}!')
    pay = payment * count_of_periods
    overpayment(principal, pay)

def number_of_months(credit_principal, payment, nominal_interest):
    periods = math.ceil(math.log(payment / (payment - nominal_interest * credit_principal), 1 + nominal_interest))
    year = periods // 12
    months = periods % 12
    if year == 0:
        if months == 1:
            print('You need 1 month to repay this credit!')
        else:
            print(f'You need {months} months to repay this credit!')
    elif months == 0:
        if year == 1:
            print('You need 1 year to repay this credit!')
        else:
            print(f'You need {year} years to repay this credit!')
    else:
        print(f'You need {year} years and {months} months to repay this credit!')
    pay = payment * periods
    overpayment(credit_principal, pay)


if monthly_payment == "annuity" and credit_principal and count_of_periods and credit_interest:
    if credit_principal < 0 or count_of_periods < 0 or credit_interest < 0:
        print("Incorrect parameters.")
    else:
        nominal_interest = nomimal(credit_interest)
        base = bases(count_of_periods, nominal_interest)
        annuity_monthly_payment(credit_principal, base, count_of_periods)
elif monthly_payment == "diff" and credit_principal and count_of_periods and credit_interest:
    if credit_principal < 0 or count_of_periods < 0 or credit_interest < 0:
        print("Incorrect parameters.")
    else:
        nominal_interest = nomimal(credit_interest)
        differentiated_monthly_payment(credit_principal, count_of_periods, nominal_interest)
elif monthly_payment and payment and count_of_periods and credit_interest:
    if payment < 0 or count_of_periods < 0 or credit_interest < 0:
        print("Incorrect parameters.")
    else:
        nominal_interest = nomimal(credit_interest)
        base = bases(count_of_periods, nominal_interest)
        creditprincipal(payment, base, count_of_periods)
elif monthly_payment != "diff" and credit_principal and payment and credit_interest:
    if credit_principal < 0 or payment < 0 or credit_interest < 0:
        print("Incorrect parameters.")
    else:
        nominal_interest = nomimal(credit_interest)
        number_of_months(credit_principal, payment, nominal_interest)
else:
    print("Incorrect parameters.")