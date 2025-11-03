print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")

#Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
#If the bmi is under 18.5 (not including), print out "underweight"
#If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
#If the bmi is 25 (including) or over, print out "overweight"

weight = 85
height = 1.85
print(input("What is your bmi "))
bmi = weight / (height ** 2)
if bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("underweight")
