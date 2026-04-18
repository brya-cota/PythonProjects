from itertools import accumulate

length = 5
width = 2
total_perimeter = length * width

print(total_perimeter)

# Write Python code that takes name and grade as input and prints a message:
# 	“Alice has an A grade.”

#name = input("What is your name? ").title()
#grade = input("What is your grade? ").upper()
#print(f"{name} has an {grade} grade")

# Write python code that defines a variable, total and assign it a value of 5,
# double the value in the variable total and print the output.
variable_total = 5
variable_total *= 2
print(variable_total)

x = 7
y = 3
print(x % y)

print("5" + "10")
print(5 + 10 * 2)

a = 10
b = 3
c = a // b
print(c)
d = a % b
print(d)
print(c + d)
(print(type(None)))

x = 5
y = 2.0
z = x + y
print(type(z), z)

#Create two string variables first_name and last_name.
# Concatenate them into a single variable called full_name with a space in between and print it.
first_name = "Zoe"
last_name = "Gaston"
full_name = first_name + " " + last_name
print(full_name)

'''
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
'''

#  Write a while loop that calculates the sum of even numbers from 2 to 20.
count = 0
total = 0
while count <= 25:
    if count % 2 == 0:
        total += count
    count += 1
print(total)

# Use a for loop with an accumulator to multiply all numbers in a list: [2, 3, 4, 5] (i.e., calculate the product).
nums = [2, 3, 4, 5]
#accumulator
total = 1
for num in nums:
    total *= num
print(total)

# Write a program using a loop that counts how many times the letter "a" appears in the string "Banana Apple Mango".
fruits = "Banana Apple Mango"
index = 0
for letter_a in fruits:
    if letter_a == "a" or letter_a =="A":
        index += 1
print(index)

c = 0
while c < 3:
    print(c, "Hello")
    c += 1

for letter in "Hi":
    print(letter)

word = "loop"
vowel_count = 0
for char in word:
    if char in "aeiou":
        vowel_count += 1
print(vowel_count)

for i in range(2):
    for j in range(3):
        print(i,j)


for i in range(4):
    for j in range(3):
        print(f"i={i}, j={j}")

# Write a nested loop to display the list in matrix format
data = [[2,4],[6,8],[10,12]]
for row in data:
    for value in row:
        print(value, end=" ")
    print()

# Using nested loops, generate the following pattern. (3 pts)
'''
*
* *
* * *
* * * *
'''
for i in range(4):
    for j in range(i+1):
        print("*", end=" ")
    print()

# Write nested loops using range() to print this pattern:
'''
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
'''
for i in range(3):
    for j in range(5,0,-1):
        print(j, end=" ")
    print()

# Modify this code to catch both ValueError and ZeroDivisionError separately
            # num = int(input("Enter a number: "))
            # result = 100 / num
            # print(result)

# try:
#     num = int(input("Enter a number: "))
#     result = 100 / num
#     print(result)
# except ValueError:
#     print("Please enter a valid number")
# except ZeroDivisionError:
#     print("Cannot divide by zero")


'''
Creates a list of 5 items. (create your own list of items)
Asks the user to enter an index number (0–4).
Tries to access and print the item at that index.
Use try, except, else, and finally to handle errors and display messages properly. '''

my_list = [2,4,6,8,10]

try:
    index = int(input("Enter an index number (0-4): "))
    print(my_list[index])
except IndexError:
    print("Index out of range")
except ValueError:
    print("Please enter a valid index number")
else:
    print("Thank you for entering a valid index value!")
finally:
    print("Program has ran. The end.")

'''
Accumulator Pattern
# Sum all numbers in a list
numbers = [1, 2, 3, 4, 5]
total = 0  # Accumulator
for num in numbers:
    total += num
print(f"Sum: {total}")
Counter Pattern
# Count specific items
text = "Hello World"
count = 0  # Counter
for char in text:
    if char == 'l':
        count += 1
print(f"Found {count} letter 'l's")

'''
