'''
Brya Cota
CSC101
3/15/26
This program implements a basic password protection system. The program should continuously prompt the user for a
password until they enter the correct one, then display a welcome message.
'''

# Define a hardcoded password as a string variable
password = "Py$th56_On"

# Use a while loop to repeatedly prompt for password input
continue_validation = True
attempts = 3 # Add a counter to track and display the number of failed attempts Limit the user to 3 attempts, then lock them out.


# Use a while loop to repeatedly prompt for password input
while continue_validation:
    user_input = input(f"Please enter the password: ")
# Use conditional statements to check if the entered password is correct.
    if user_input == password:
        print("Welcome! Thank you for entering your password!")
        continue_validation = False
    elif attempts == 0:
        print("**Account locked** Try again later.")
        continue_validation = False
    elif user_input != password:
        print(f"Wrong password. Try again. You have {attempts} attempts left.")
        attempts -= 1

