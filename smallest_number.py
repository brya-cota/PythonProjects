'''
Brya Cota
CSC101
3/4/26
This program accepts three numbers as input and determines the smallest among them.
'''

# Prompt the user to enter three integer numbers. Use the input() function and convert to the appropriate data type.
number_1 = float(input("Enter a number: "))
number_2 = float(input("Enter another number: "))
number_3 = float(input("Enter one more number: "))

# Use conditional statements to find the smallest of the three numbers.
# Print the smallest number in a clear message like: "The smallest number is: X"

if number_1 < number_2:
    if number_1 < number_3:
        print(f'The smallest number is: {number_1}')
    else:
        print(f'The smallest number is: {number_3}')
elif number_2 < number_1:
    if number_2 < number_3:
        print(f'The smallest number is: {number_2}')
else:
    print(f'The smallest number is: {number_3}')