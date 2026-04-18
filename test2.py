total = 0
for i in range(3):
    for j in range(2):
        total += 1
print(total)

for i in range(3):
    for j in range(2):
        print("Hi")

try:
    x = int("hello")
except ValueError:
    print("A")
except TypeError:
    print("B")
except Exception:
    print("C")

try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Success")

try:
    x = 10 / 0
except ZeroDivisionError:
    print("A")
finally:
    print("B")


count = 0
for i in range(3):
    for j in range(3):
        if i == j:
            count += 1
print(count)


def info():
    return "Alice", 30


def info():
    return "Alice", 30

data = info()
print(data)

def say_hello(name="User"):
    return f"Hello, {name}"

print(say_hello())

def divide(a, b):
    return a / b, a % b

result = divide(10, 3)
print(result)

# Define a function order_summary(item, quantity=1, price=10.0, discount=0) that returns the total cost after applying
# the discount.
def order_summary(item, quantity = 1, price = 10.0, discount = 0):
    total_cost = price * quantity - discount
    return total_cost
print(order_summary(1, 3, 10, .2))

# Create a function called calculate_total that takes one required argument price and one optional argument tax_rate
# with a default value of 0.08. The function should return the total price including tax.
def calculate_total(price, tax_rate = 0.08):
    total_price = price + tax_rate
    return total_price
print(calculate_total(10, ))

# Write a function build_profile(**info) that constructs and returns a sentence like ‘Hi, I’m Tina, a 22 year old
# Information Technology student’.
# Call the function using keyword arguments: name, age and major.
def build_profile(**info):
    sentence = f"Hi, I'm {info["name"]}, a {info["age"]} year old {info["major"]} student."
    return sentence
print(build_profile(name = "Tina", age = 22, major = "Information Technology"))

# The random module must be imported to be used
import random
# Assigning a value (rand_num) for a random number between 1 and 10
rand_num = random.randint(1, 10)
# Printing random number
print(f"Output: {rand_num}")

# The random module must be imported to be used
import random
# Creating a list of strings
animals = ["fish", "mouse", "lion", "bear"]
# Assigning a value (random_animal) for a random element to be chosen within the list of strings [animals]
random_animal = random.choice(animals)
# Printing random animal
print(f"Output: {random_animal}")

# Creating a list of strings
animals = ["fish", "mouse", "lion", "bear"]
# Shuffling list of strings to output a random element
random.shuffle(animals)
# Printing list in a random order
print(f"Output: {animals}")

#random.randrange(100) is interpreted as randrange(start=0,stop=100,step=1). A random value between 1-99 is printed
print(random.randrange(100))
