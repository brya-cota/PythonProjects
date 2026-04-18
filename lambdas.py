'''
Brya Cota
In this activity, the program will practice lambda syntax by converting simple functions, then apply
lambdas with map(), filter(), sorted(). I have converted regular functions into lambda expressions, starting
with simple syntax practice, then using them with built-in functions.
'''

# Square a Number
# def square(x):
# """Return the square of x"""
# return x ** 2

squared_lambda = lambda x: x ** 2

# Add Two Numbers
# def add_numbers(a, b):
# """Add two numbers together"""
# return a + b
addnums_lambda = lambda a, b: a + b

# Check If Positive
# def is_positive(num):
# """Check if number is positive"""
# return num > 0

posi_lambda = lambda num: num > 0

# Get First Character
# def first_char(text):
# """Return the first character of a string"""
# return text[0]

first_char_lambda = lambda text: text[0]

# Double A Number
# def double(x):
#     """Double a number"""
#     return x * 2
# Use with map() to double all numbers in: [1, 2, 3, 4, 5]
# Expected result: [2, 4, 6, 8, 10]

nums = [1,2,3,4,5]
double_lambda = list(map(lambda x: x * 2, nums))

# Filter Even Numbers
# def is_even(num):
#     """Check if number is even"""
#     return num % 2 == 0
# Use with filter() on: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected result: [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
is_even_lambda = list(filter(lambda num: num % 2 == 0, numbers))

# Sort By Length
# def get_length(word):
#     """Get the length of a word"""
#     return len(word)
# Use with sorted() to sort by length: ["cat", "elephant", "dog", "bird"]
# Expected result: ["cat", "dog", "bird", "elephant"]
word_list = ["cat", "elephant", "dog", "bird"]
get_length_lambda = sorted(word_list, key=lambda x: len(x))

#Square all numbers using map() with a direct lambda (Not storing the lambda inside a variable)
list(map(lambda x: x ** 2, nums))

#Filter numbers greater than 5 using filter() with a direct lambda (Not storing the lambda inside a variable)
number_direct = [1, 8, 3, 12, 5, 9, 2]
list(filter(lambda x: x > 5, number_direct))


print("=== LAMBDA PRACTICE ACTIVITY ===\n")

print(f"PART 1: Basic Lambda Conversions\nsquare(5) = {squared_lambda(5)}\nadd_numbers(3,7) = {addnums_lambda(3,7)}"
      f"\nis_positive(-5) = {posi_lambda(-5)}\nfirst_char('hello') = {first_char_lambda('hello')}")
print(f"")

print(f"PART 2: Using Lambdas with Built-in Functions\nDouble with map():\nOriginal: {nums}\n"
      f"Doubled: {double_lambda}\n\nFilter evens:\nOriginal: {numbers}\nEven numbers: {is_even_lambda}")

print(f"\nSort by length: \nOriginal: {word_list}\nSorted by length: {get_length_lambda}")

print(f"\nPART 3: Direct Lambda Usage: \nSquared numbers: {list(map(lambda x: x * 2, nums))}\nNumbers > 5: "
      f"{list(filter(lambda x: x > 5, number_direct))}")
