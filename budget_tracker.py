"""
Brya Cota
CSC101
2/16/26

This program will calculate the total expenses by summing up the food, rent, and entertainment expenses, then
calculate the remaining budget by subtracting the total expenses from the monthly budget.
"""
monthly_budget = float(input("Enter your Total Monthly Budget: "))
food_expenses = float(input("Enter your Food Expenses: "))
rent_expenses = float(input("Enter your Rent Expenses: "))
entertainment_expenses = float(input("Enter your Entertainment Expenses: "))

# Calculate the total expenses by summing up the food, rent, and entertainment expenses
total_expenses = food_expenses + rent_expenses + entertainment_expenses

# Calculate the remaining budget by subtracting the total expenses from the monthly budget.
money_left = monthly_budget - total_expenses

# Display the budget summary, including the total budget, total expenses, and remaining budget, formatted to two decimal places.
print("----- Budget Summary -----")
print(f"Total Monthly Budget: ${monthly_budget:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${money_left:.2f}")


# To format float numbers to two decimal places in Python by using an f string formatter, or format specifier: (:2f).
# You ensure the program handles numeric input correctly when using the input() function by type casting to an integer or float value.
# It's useful to use variables to store user input so we can re-use and/or change the stored values later.