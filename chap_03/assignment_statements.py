# Exercise 4: Assume that we execute the following assignment statements:

# Assign integer value to variable width
width = 17

# Assign floating-point value to variable height
height = 12.0


# Integer (floor) division: result is rounded DOWN to nearest whole number
# 17 // 2 = 8
print("width // 2 =", width // 2, "Type:", type(width // 2))


# Floating-point division: result will always be a float
# 17 / 2.0 = 8.5
print("width / 2.0 =", width / 2.0, "Type:", type(width / 2.0))


# One operand is float → result is float
# 12.0 / 3 = 4.0
print("height / 3 =", height / 3, "Type:", type(height / 3))


# Order of operations (BODMAS/PEMDAS):
# Multiplication first → 2 * 5 = 10
# Then addition → 1 + 10 = 11
print("1 + 2 * 5 =", 1 + 2 * 5, "Type:", type(1 + 2 * 5))

