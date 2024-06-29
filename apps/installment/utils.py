from decimal import Decimal, getcontext

def calculate_annuity_payment(P, monthly_rate, months):

    getcontext().prec = 28

    P = Decimal(P)
    r = Decimal(monthly_rate) / Decimal(100)
    n = Decimal(months)

    A = P * r * (1 + r) ** n / ((1 + r) ** n - 1)

    return int(A)
