# ============================================
# PYTHON ITERATION & LOOPING – ALL IN ONE FILE
# ============================================

# --------------------------------------------
# 1. UPDATING VARIABLES (Increment / Decrement)
# --------------------------------------------
print("\n--- 1. Updating Variables ---")

x = 0  # initialization (you must define before using)
print("Initial x:", x)

x = x + 1  # increment → add 1 to current value
print("After increment:", x)

x = x - 1  # decrement → subtract 1
print("After decrement:", x)

# NOTE:
# x = x + 1 means:
# take old value → add 1 → store back in x


# --------------------------------------------
# 2. WHILE LOOP (Countdown)
# --------------------------------------------
print("\n--- 2. While Loop (Countdown) ---")

n = 5  # iteration variable (controls loop)

while n > 0:  # loop runs while condition is True
    print(n)
    n = n - 1  # IMPORTANT: change value so loop can stop

print("Blastoff!")

# NOTE:
# If you don't update n → infinite loop
# Always ask: "what changes each loop?"


# --------------------------------------------
# 3. INFINITE LOOP + BREAK
# --------------------------------------------
print("\n--- 3. Infinite Loop with Break ---")

# This loop runs forever until "done" is entered
while True:
    text = input("Enter something (type 'done' to stop): ")

    if text == "done":
        break  # exit loop immediately

    print("You typed:", text)

print("Exited loop successfully.")

# NOTE:
# while True = always running
# break = manual stop condition


# --------------------------------------------
# 4. CONTINUE (Skip Iteration)
# --------------------------------------------
print("\n--- 4. Continue Example ---")

while True:
    line = input("> ")

    # Skip lines starting with '#'
    if line.startswith("#"):
        continue  # skip this iteration and go to next

    if line == "done":
        break

    print("Processed:", line)

print("Done with filtering input.")

# NOTE:
# continue = skip current loop step
# break = exit loop completely


# --------------------------------------------
# 5. FOR LOOP (Definite Loop)
# --------------------------------------------
print("\n--- 5. For Loop ---")

friends = ["Joseph", "Glenn", "Sally"]

for friend in friends:  # iteration variable = friend
    print("Happy New Year:", friend)

print("Done with greetings.")

# NOTE:
# for loop automatically goes through each item
# no need to manually update counter


# --------------------------------------------
# 6. COUNTING LOOP
# --------------------------------------------
print("\n--- 6. Counting Items ---")

numbers = [3, 41, 12, 9, 74, 15]

count = 0  # counter variable (start from 0)

for num in numbers:
    count = count + 1  # increase by 1 each loop

print("Count:", count)

# NOTE:
# used to count how many items exist


# --------------------------------------------
# 7. SUMMING LOOP (Accumulator)
# --------------------------------------------
print("\n--- 7. Summing Values ---")

total = 0  # accumulator (stores running sum)

for num in numbers:
    total = total + num  # add each number

print("Total:", total)

# NOTE:
# accumulator = keeps adding values
# very common in data analysis


# --------------------------------------------
# 8. FIND MAXIMUM
# --------------------------------------------
print("\n--- 8. Find Maximum ---")

largest = None  # means "no value yet"

for num in numbers:
    if largest is None or num > largest:
        largest = num  # update if bigger value found

print("Largest:", largest)

# NOTE:
# largest = "biggest value seen so far"
# None helps handle first value safely


# --------------------------------------------
# 9. FIND MINIMUM
# --------------------------------------------
print("\n--- 9. Find Minimum ---")

smallest = None  # "no value yet"

for num in numbers:
    if smallest is None or num < smallest:
        smallest = num  # update if smaller value found

print("Smallest:", smallest)

# NOTE:
# same logic as max, but reversed comparison


# --------------------------------------------
# 10. CUSTOM FUNCTION (Reusable Logic)
# --------------------------------------------
print("\n--- 10. Custom Function ---")

def find_min(values):
    smallest = None

    for value in values:
        if smallest is None or value < smallest:
            smallest = value

    return smallest


result = find_min(numbers)
print("Minimum using function:", result)

# NOTE:
# function = reusable block of code
# avoids repeating logic again and again


# ============================================
# END SUMMARY (IMPORTANT CONCEPTS)
# ============================================

"""
Key Takeaways (Simple Version):

1. Always initialize variables before updating
2. while loop → runs based on condition
3. for loop → runs over list items
4. break → stops loop completely
5. continue → skips current iteration
6. counter → counts items (count = count + 1)
7. accumulator → adds values (total = total + value)
8. None → means "no value yet" (used in min/max)

Think like this:
- Loop = repetition
- Variable = memory
- Update = progress
"""