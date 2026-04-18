'''
Brya Cota
CSC101
3/14/26
This program will focus on Using for loops to read through a list, Random number generation, and Calculating the average temperature
'''
# Import the random module at the beginning of your program
import random

# Create an empty list called sensor_readings to store temperature data
sensor_readings = []

# Use a for loop with range(10) to simulate 10 temperature readings
for temp_readings in range(10):
    # Generate a random integer between 18 and 35 (inclusive) using random.randint(18, 35)
    rand_num = random.randint(18, 35)
    # Append each generated reading to the sensor_readings list
    sensor_readings.append(rand_num)

# Variable to store the sensor number (1-10)
display_sensor = 0

# Iterate through the sensor_readings list. Display the sensor number with the corresponding elements (temperatures)
# inside the list [sensor_readings]
for sensor in sensor_readings:
    display_sensor += 1
    print(f"Sensor {display_sensor}: {sensor}°C")

# Variable to hold the sum of the temperatures
temp_sum = 0
# Calculate the sum of the temperatures manually using a for loop
for total in sensor_readings:
    temp_sum += total

# Then calculate the average and display it with one decimal place, e.g.: Average Temperature: 25.4°C
temp_avg = temp_sum / len(sensor_readings) #10
print(f"\nAverage Temperature: {temp_avg:.1f}°C")
