# Exercise 1: Read numbers until "done"
# Print total, count, and average

total = 0      # accumulator (sum of numbers)
count = 0      # counter (how many valid numbers)

while True:
    user_input = input("Enter a number: ")

    if user_input == "done":
        break  # stop loop

    try:
        num = float(user_input)  # convert input to number
    except:
        print("Invalid input")
        continue  # skip to next iteration

    total = total + num   # add number to total
    count = count + 1     # increase count

# After loop ends
if count > 0:
    average = total / count
    print(total, count, average)
else:
    print("No valid numbers entered")