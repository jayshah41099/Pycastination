def monthly_payment(Principal, Down_payment, Interest, Term):
    P = float(Principal - Down_payment)
    R = float((Interest/100)/12)
    N = float(Term * 12)
    # loan amount(P) is principal after down payment
    # R is interest rate for every month in float
    # N is loan term in months
    M = P * (R * ((1 + R) ** N)) / (((1 + R) ** N) - 1)

    # calulating first year interset and principal for each month and for first year
    Monthly_Principal = M - (P * R)
    Monthly_Interest = M - Monthly_Principal
    yearly_Interest = Monthly_Interest * 12
    yearly_Principal = Monthly_Principal * 12

    return M, Monthly_Principal, Monthly_Interest, yearly_Interest, yearly_Principal


def main():
    Principal = int(input("Enter your total house purchase amount: "))
    Down = int(input("Enter your down payment amount (not the percentage): "))
    Interest = float(input("Enter the loan interest rate (e.g. 3.44% = 3.44): "))
    Term = int(input("Enter the loan term(in years, e.g., 30 years = 30): "))
    Month_payment, Month_Principal, Month_Interest, year_Interest, year_Principal = monthly_payment(Principal, Down, Interest, Term)
    print(" your Monthly payment for first year is: \t%.2f" % round(Month_payment, 2))
    print(" Out of your montly payment amount goes towards principal is: \t%.2f" % round(Month_Principal, 2))
    print(" Out of your montly payment amount goes towards interest is: \t%.2f" % round(Month_Interest, 2))
    print(" Toatl principal paid for the first year is: \t%.2f" % round(year_Principal, 2))
    print(" Toatl interest paid for the first year is: \t%.2f" % round(year_Interest, 2))

if __name__ == '__main__':
    main()