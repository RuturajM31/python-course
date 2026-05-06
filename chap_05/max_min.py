# Exercise 2: Read numbers and find min and max

largest = None   # will store the biggest number entered
smallest = None  # will store the smallest number entered

while True:  # infinite loop until user types "done"
    user_input = input("Enter a number: ")

    if user_input == "done":
        break  # exit the loop

    try:
        num = float(user_input)  # convert input to a number
    except:
        print("Invalid input")   # handle non-numeric input
        continue                 # skip this iteration and ask again

    # -------------------------
    # Update largest value
    # -------------------------
    # If largest is still None (first valid input),
    # OR current number is greater than stored largest,
    # then update largest
    if largest is None or num > largest:
        largest = num

    # -------------------------
    # Update smallest value
    # -------------------------
    # If smallest is still None (first valid input),
    # OR current number is smaller than stored smallest,
    # then update smallest
    if smallest is None or num < smallest:
        smallest = num

# -------------------------
# After loop ends
# -------------------------
if largest is not None and smallest is not None:
    # If at least one valid number was entered
    print("Maximum:", largest)  # biggest number found
    print("Minimum:", smallest) # smallest number found
else:
    # If user never entered any valid numbers
    print("No valid numbers entered")