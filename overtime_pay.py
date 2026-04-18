'''
Brya Cota
CSC101
3/6/26
This program will calculate normal hours worked and any overtime worked to add up your pay for this week.
'''

# Ask user how many hours they worked this week
hours = int(input("How many hours did you work this week? "))

# Variables to represent normal pay with normal hours and overtime pay with overtime hours
normal_working_hours = 40
pay = 20
overtime_pay = 30
overtime_hours = hours - normal_working_hours

# Conditionals to check if the worker gets over time pay or not
if hours == normal_working_hours:
    pay_check = pay * normal_working_hours
elif hours > normal_working_hours:
    pay_check = (pay * normal_working_hours) + (overtime_hours * overtime_pay)
else:
    pay_check = pay * normal_working_hours

# Printing the total pay check amount
print(f"You earned ${pay_check} this week.")