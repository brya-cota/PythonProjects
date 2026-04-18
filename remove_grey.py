'''
Brya Cota
3/6/26
This program removes the gray component from RGB color values by identifying and subtracting the minimum value from all
three color components within an RGB.

Computer graphics represent colors using the RGB color model, where each color is composed of three sub-components:
Red (R): Intensity of red light (0-255)
Green (G): Intensity of green light (0-255)
Blue (B): Intensity of blue light (0-255)
'''

# Prompt the user to read three integer values, for red, green and blue components
red = int(input("Enter RGB Components:\n"))
green = int(input(""))
blue = int(input(""))

# Find the smallest of the three input values (this is the gray component) using conditional statements
# Subtract this smallest value from each of the three RGB components

if red < green and red < blue:
        green = green - red
        blue = blue - red
        red = red - red
elif blue < green and blue < red:
        red = red - blue
        green = green - blue
        blue = blue - blue
else:
    blue = blue - green
    red = red - green
    green = green - green

# Print the adjusted RGB values on one line, separated by spaces.
print(f"\nOutput:\n{red} {green} {blue}")
