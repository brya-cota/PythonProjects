"""
Brya Cota
CSC101
3/26/26
This program will generate various shapes using nested for loops based on the size that the user enters.
"""

print("===AI Pattern Training Data Generator===")

generate_another = True
while generate_another:
    print("Please choose the pattern you'd like to generate.")
    print("1. Checkerboard \n2. Right Diagonal Stripes \n3. Solid Triangle \n4. Dimond Outline \n5. Quit")
    choice = int(input("Enter your pattern choice(1-5): "))

# Quitting the program upon user request
    if choice == 5:
        break

# If user doesn't want to stop playing, then we ask for the size they prefer
    size = int(input("Enter the size of the pattern: "))

# checkerboard pattern
    if choice == 1:
        for i in range(size):
            for j in range(size):
                #stars alternate, only even numbers are printed as a star
                if (i+j) % 2 == 0:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

# rightDiagonalStripes
    if choice == 2:
        for i in range(size):
            for j in range(size):
                #first diagonal line starting from upper right down left
                if i == j:
                    print("*", end="")
                #second diagonal line starting from top left down right
                elif i + j == size - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

# solidTriangle
    if choice == 3:
        for i in range(size):
            for j in range(i):
                print("*", end="")
            print()

#dimondOutline
    if choice == 4:
    #top half leading spaces
        for i in range(size):
            for j in range(size - i - 1):
                print(" ", end="")

        #printing stars and creating hallow portion for top half
            for j in range(i * 2 + 1):
                if j == 0 or j == 2*i:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

    #bottom half leading spaces
        for i in range(size - 2, -1, -1):
            for j in range(size - i - 1):
                print(" ", end="")

        #printing stars for bottom and creating hallow portion for bottom half
            for j in range(i * 2 + 1):
                if j == 0 or j == 2*i:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

#asking the user if they want to play again
play_again = input("Are you sure you want to quit? (Y/N): ").lower()
if play_again != "y":
    print("Thanks for playing!")
    generate_another = False


