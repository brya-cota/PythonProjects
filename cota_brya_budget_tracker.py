'''
Brya Cota
CSC101
04/10/2026
This program is a comprehensive budget tracking system that demonstrates modules, advanced function parameters,
scope management, and error handling.
'''

# Required imports
import datetime
import math

# Global scope variables
monthly_budget = 0.0   # Total budget for the current month
expenses = []          # List of expense dictionaries
income = []            # List of income dictionaries

# Args:
    # amount (float or int): Must be >= 0
    # currency (str): Default "USD"
def set_monthly_budget(amount, currency="USD"):
    # Set the monthly budget with validation.
    global monthly_budget
    # ValueError: If amount is negative
    try:
        amount < 0
    except ValueError:
        print("Please enter a positive amount")

    # TypeError: If amount is not a number
    try:
        amount == str
    except TypeError:
        print("Please enter a valid amount")
    # Returns:
    monthly_budget = amount
    # str: Confirmation message with formatted amount and currency
    return f"Your monthly budget is ${monthly_budget:.2f} {currency}"

def add_expense(amount, category="miscellaneous", description="", date=None):
    # Add an expense entry.
    expense_entry = {
        "amount": float(amount),
        "category": str(category),
        # Description (str): Optional
        "description": (description),
        "date": datetime.date
    }
    # Category (str): Converted to lowercase
    category = category.lower()

    # Args:
    # Amount (float or int): Must be > 0
    try:
        amount < 0
    except ValueError:
        print("Please enter a positive amount")
    try:
        amount == str
    except TypeError:
        print("Please enter a valid amount")
    # Date (datetime.date or str): If None → today. If str → must be "YYYY-MM-DD"
    if date is None:
        date = datetime.date.today()
    elif date is str:
        try:
            date = datetime.date.strftime(date, "%Y-%m-%d")
        except ValueError:
            print("Please enter a valid date format")

    # Adding an expense entry to our global list expenses[]
    expenses.append(expense_entry)

    # Returns:
    return f"Added expense: {amount:.2f} in {category} on {date}"
    pass

def add_income(amount, source="salary", date=None):
    # Add an income entry.
    income_entry = {
        "amount": float(amount),
        "source": str(source),
        "date": datetime.date
    }
    # Same rules as add_expense for amount and date.
    try:
        amount < 0
    except ValueError:
        print("Please enter a positive amount")
    try:
        amount == str
    except TypeError:
        print("Please enter a valid amount")
        # Date (datetime.date or str): If None → today. If str → must be "YYYY-MM-DD"
    if date is None:
        date = datetime.date.today()
    elif date is str:
        try:
            date = datetime.date.strftime(date, "%Y-%m-%d")
        except ValueError:
            print("Please enter a valid date format")

    # Adding an income entry to global list income[]
    income.append(income_entry)

    # Returns:
    return f"Added income: {amount:.2f} from {source} on {date}"
    pass

def get_remaining_budget():
    # Summing 'amount' values (float) in the list of dictionaries (expenses)
    expenses_amounts = sum(exp_amt["amount"] for exp_amt in expenses)
    remaining_budget = monthly_budget - expenses_amounts

    # Returns:
    return f"Your remaining budget is ${remaining_budget:.2f}"
    pass

def analyze_spending(**filters):
    # Return spending summary based on filters.
    filtered = expenses

    # Valid filter keys:
    # Category (str)
    if 'category' in filters:
        filtered = list(filter(lambda x: x['category'].lower() == filters['category'].lower(), filtered))

    # Start_date (date or "YYYY-MM-DD")
    if 'start_date' in filters:
        st_date = datetime.datetime.strptime(filters['start_date'], "%Y-%m-%d")
        filtered = list(filter(lambda x: x['date'] == filters['st_date'], filtered))

    # End_date (date or "YYYY-MM-DD")
    if 'end_date' in filters:
        ed_date = datetime.datetime.strptime(filters['end_date'], "%Y-%m-%d")
        filtered = list(filter(lambda x: x['date'] == filters['ed_date'], filtered))

    # Min_amount (float)
    if 'min_amount' in filters:
        filtered = list(filter(lambda x: x['amount'] < filters['min_amount'], filtered))

    # Max_amount (float)
    if 'max_amount' in filters:
        filtered = list(filter(lambda x: x['amount'] > filters['max_amount'], filtered))

    # Returns:
    # dict with:
    # 'count': int
    # 'total': float (2 decimals)
    # 'average': float (2 decimals or 0.0 if no items)
    count = len(filtered)
    total = sum(filt_amt['amount'] for filt_amt in filtered)
    average = total / count

    analyzed_spending = {
        "count" : count,
        "total" : round(total,2),
        "average" : round(average,2)
    }
    return analyzed_spending
    pass

def get_spending_report(*categories):
    spending_report = {}
    total = 0

    # Args:
    # *categories: One or more category names (case-insensitive)
    for category in categories:
        for expense in expenses:
            if expense['category'].lower == category.lower():
                total += expense['amount']

    # Returns:
    # dict: {category: total_spent} for requested categories
    # Include categories even if total is 0.0
    spent = {
        "total" : round(total,2),
    }
    return spent
    pass

if __name__ == "__main__":
    print(set_monthly_budget(2500))
    print(add_expense(75.50, "Food", "Lunch", "2025-08-10"))
    print(add_expense(150.00, "food", "Groceries"))
    print("Remaining budget:", get_remaining_budget())
    print("Food spending:", analyze_spending(category="food"))
