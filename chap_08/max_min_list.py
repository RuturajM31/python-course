# Create an empty list to store all the numbers entered by the user
numbers = []

while True:
    # Ask the user to enter a number
    user_input = input("Enter a number: ")

    # If the user types "done", stop the loop
    if user_input.lower() == "done":
        break

    try:
        # Convert the input into a float (decimal number allowed)
        num = float(user_input)

        # Add the number to the list
        numbers.append(num)

    except ValueError:
        # If input is not a number, show an error message
        print("Invalid input. Please enter a number or 'done'.")

# After the loop ends, check if the list is not empty
if numbers:
    # Find and print the maximum value in the list
    print("Maximum:", max(numbers))

    # Find and print the minimum value in the list
    print("Minimum:", min(numbers))
else:
    # If no numbers were entered, show this message
    print("No numbers were entered.")