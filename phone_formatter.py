"""
Brya Cota
CSC101
2/16/26
This program will show you how to manipulate integers and extract specific parts using mathematical operations.
Use the % (modulus) and // (integer division) operators to format a 10-digit phone number.
"""

# Ask the user for their phone number
phone_number = int(input("Enter a 10-digit phone number: "))

# Since we only want the first 3 numbers, we'll divide phone_number by 10*7 to isolate the first 3 digits.
area_code = phone_number // 10000000
#print(area_code)

# To obtain the prefix, we'll need to discard the last 4 digits, discard the first 3 digits, and extract the middle (or next)
# 3 digits.
prefix = phone_number // 10000 % 1000
#print(prefix)

# Isolate the last 4 digits or line number.
line_number = phone_number % 10000
#print(line_number)

print(f"({area_code}) {prefix}-{line_number}")