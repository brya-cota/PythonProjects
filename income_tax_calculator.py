'''
Brya Cota
4/1/26
This program will compute the income tax owed by a user based on their, wages, taxable interest,
unemployment compensation, filing status and taxes already withheld.
'''

# Implement the function Adjusted Gross Income (AGI), calc_AGI() that takes wages, interest and unemployment as
# input. Calculates and returns the AGI by adding the wages, interest, and unemployment compensation. (Hint:
# Use the abs() built-in function that returns the absolute value of a number).
def calc_agi(wages, interest, unemployment):
    agi = abs(wages + interest + unemployment)
    return agi

# Implement function, get_deduction(status) that returns the deduction based on the following criteria:
# 0 - $6,000
# 1 - $12,000
# 2 - $24,000
# All others - $6,000
def get_deduction(status):
    if status == 0:
        deduction = 6000
        return deduction
    elif status == 1:
        deduct = 12000
        return deduct
    elif status == 2:
        deduction = 24000
        return deduction
    else:
        deduction = 6000
        return deduction

# Implement a function, calc_taxable(agi, deduction), that takes agi and deduction as input and calculates and
# returns the taxable income (agi - deduction). If the result is negative, set to 0.
def calc_taxable(agi, deduction):
    taxable_income = agi - deduction
    if taxable_income < 0:
        taxable_income = 0
    return taxable_income

# Implement function, calc_tax() that takes status and taxable income as input and calculates tax based on the criteria below:
# Round the result using round().
def calc_tax(status, taxable_income):
    tax = 0
    # Independent or Single deductions - based on income range and corresponding tax formula
    if status == 0 or status == 1:
        if 0 <= taxable_income <= 10000:
            tax = .10 * taxable_income
        elif 10001 <= taxable_income <= 40000:
            tax = 1000 + .12 * (taxable_income - 10000)
        elif 40001 <= taxable_income <= 85000:
            tax = 4600 + .22 * (taxable_income - 40000)
        else:
            tax = 14500 + .24 * (taxable_income - 85000)

    # Married deductions - based on income range and corresponding tax formula
    if status == 2:
        if 0 <= taxable_income <= 20000:
            tax = .10 * taxable_income
        if 20001 <= taxable_income <= 80000:
            tax = 2000 + .12 * (taxable_income - 20000)
        else:
            9200 + .22 * (taxable_income - 80000)
    return round(tax)
# Implement a function, calc_tax_due(tax, withheld), that takes tax and withheld tax as input and returns the calculated
# tax due (tax - withheld). If withheld tax is less than 0, set to 0.
def calc_tax_due(tax, withheld):
    if withheld < 0:
        withheld = 0
    return tax - withheld

# In the main() function of the code, prompt the user to enter the wages (integer), taxable interest (integer),
# unemployment compensation (integer), filing status (0- Independent, 1 - Single, 2 - Married) and taxes withheld (integer).
def main():
    wages = int(input("Enter wages: "))
    interest = int(input("Enter interest: "))
    unemployment_comp = int(input("Enter unemployment: "))
    filing_status = int(input("Enter filing status 0- Independent, 1 - Single, 2 - Married: "))
    taxes_withheld = int(input("Enter taxes withheld: "))

    # Calling each function in main() and assigning variables to the functions output
    agi = calc_agi(wages, interest, unemployment_comp)
    deduction = get_deduction(filing_status)
    taxable = calc_taxable(agi, deduction)
    tax = calc_tax(filing_status, taxable)
    tax_due = calc_tax_due(tax, taxes_withheld)

    print(f"AGI: ${agi}")
    print(f"Deduction: ${deduction}")
    print(f"Taxable Income: ${taxable}")
    print(f"Federal Tax: ${tax}")
    print(f"Tax Due: ${tax_due}")

main()
