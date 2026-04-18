"""
Brya Cota
CSC101
2/15/28
This program focuses on essential Python programming concepts: variables,
input/output operations like print() and input() and basic operators.
"""
# Create variables to store the information below
# Your full name as a string
# Today’s temperature as an integer
# Cost of coffee as a float
# Freshman status as a boolean variable

name = "Brya Cota"
todays_temp = 64
coffee_cost = 5.20
freshman_status = False

# Display all four variables in a single statement. Implement the sep parameter to include "..." between each value
print(name, todays_temp, coffee_cost, freshman_status, sep="...")

#Create a series of print statements that display the info on the same line using the end parameter
print(f"My name is {name}.", end=" ")
print(f"The temperature today is {todays_temp} degrees.", end=" ")
print(f"A cup of coffee costs ${coffee_cost:.2f}.", end=" ")
print(f"Freshman status: {freshman_status}.")

# Print the data type of each variable
print("name data type is:", type(name))
print("todays_temp data type is:", type(todays_temp))
print("coffee_cost data type is:", type(coffee_cost))
print("freshman_status data type is:", type(freshman_status))

# Perform a series of arithmetic operations after prompting the user for 2 numbers
user_input = int(input("Hi, please enter a whole number. "))
user_input2 = int(input("Please enter a second whole number. "))
print(user_input + user_input2)
print(user_input - user_input2)
print(user_input * user_input2)
print(user_input / user_input2)
print(user_input % user_input2)
print(user_input ** user_input2)





