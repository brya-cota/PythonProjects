'''
Brya Cota
CSC101
4/21/26
In this activity I'll demonstrate how to write a list of numbers toa text file using Python, read those numbers
from the file, and then calculate the average of the numbers read from the file
'''

# Part1: Writing to a file
# Create a list of numbers, e.g., [45, 78, 102, 56, 89].
numbers = [45,78,102,56,89]

# Open a file named numbers.txt in write mode.
file = open("numbers.txt", "w")

# Write each number to the file on a new line.
for num in numbers:
    file.write(str(num) + "\n")

# Close the file
file.close()

# Part2: Reading from a file
# Open the file numbers.txt in read mode.
file = open("numbers.txt", "r")

# Read all the numbers from the file.
# Convert the strings read from the file into integers.
total = 0
for num in file:
    num = int(num)
    # Calculate the sum and the average of these numbers.
    total += num
#print(f"Total:{total}")

# Display the numbers and the average
avg = total / len(numbers)
print(f"Average: {avg}")

# Close the file
file.close()

# Part3: Using the with statement
# Repeat part1 and part2 using the with statement.
# Open a file named numbers.txt in write mode.
with open("numbers.txt", "w") as file:
    # Write each number to the file on a new line - must convert integers back to string
    for num in numbers:
        file.write(f"{num}\n")

# Reading from a file
# Open the file numbers.txt in read mode.
total = 0
with open("numbers.txt", "r") as file:
    # Read and process each line
    for num in file:
        # Convert the strings read from the file into integers.
        num = int(num)
        total += num
    # Calculate the sum and the average of these numbers.
    # Display the numbers and the average
avg = total / len(numbers)
print(f"Average using 'with': {avg}")