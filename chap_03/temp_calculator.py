# Exercise 5: Write a program which prompts the user for a Celsius temperature, 
# convert the temperature to Fahrenheit, and print out the converted temperature.

# Prompt the user to enter temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit using the formula:
# Fahrenheit = (Celsius * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# Display the result
print("Temperature in Fahrenheit:", fahrenheit)