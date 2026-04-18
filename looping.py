'''
Brya Cota
CSC101
3/12/26
This program will calculate the sum of the squares of integers in user-specified range using a for loop and a while loop.
'''

# Prompts the user for a starting number (start) and an ending number (end)
start_number = int(input("Please enter the starting number: "))
end_number = int(input("Please enter the ending number: "))
print(f"Start number: {start_number}")
print(f"End number: {end_number}\n")

# Calculate the sum of squares of all integers from start to end (inclusive) using: A for loop & A while loop
# Store the results in separate variables (e.g,, while_sum and for_sum)
for_sum = 0
for num in range(start_number, end_number + 1):
    num_squared = num ** 2
    for_sum += num_squared
print(f"For Loop sum: {for_sum}")

while_sum = 0
num = start_number
while num != end_number + 1:
    num_squared = num ** 2
    while_sum += num_squared
    num += 1
print(f"While Loop sum: {while_sum}")