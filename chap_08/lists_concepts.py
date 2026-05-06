# 📚 LIST SUMMARY IN PYTHON

# -------------------------------------------------------
# 🔹 1. Concept of a Collection
# A list is a collection of multiple items in a single variable.
# It can store different data types.

my_list = [1, 2, 3, "apple", True]

# -------------------------------------------------------
# 🔹 2. Lists and definite loops
# We use loops to go through each element in a list.

for item in my_list:
    print(item)

# -------------------------------------------------------
# 🔹 3. Indexing and lookup
# Lists use index positions starting from 0.

print(my_list[0])   # first element
print(my_list[-1])  # last element

# -------------------------------------------------------
# 🔹 4. List mutability
# Lists can be changed after creation.

my_list[1] = 100
print(my_list)

# -------------------------------------------------------
# 🔹 5. Useful functions

nums = [10, 5, 20, 3]

print(len(nums))   # number of elements
print(min(nums))   # smallest value
print(max(nums))   # largest value
print(sum(nums))   # sum of all elements

# -------------------------------------------------------
# 🔹 6. Slicing lists
# Extract part of a list.

print(nums[0:2])   # first two elements
print(nums[:3])    # from start to index 2
print(nums[1:])    # from index 1 to end

# -------------------------------------------------------
# 🔹 7. List methods

nums.append(50)     # add element at end
nums.remove(5)      # remove value 5
print(nums)

# -------------------------------------------------------
# 🔹 8. Sorting lists

nums.sort()         # ascending order
print(nums)

nums.sort(reverse=True)  # descending order
print(nums)

# -------------------------------------------------------
# 🔹 9. Splitting strings into lists

text = "apple banana mango"
words = text.split()   # splits by space
print(words)

# -------------------------------------------------------
# 🔹 10. Using split to parse strings

csv_data = "John,25,Germany"
parts = csv_data.split(",")
print(parts)

# -------------------------------------------------------
# 🚀 SUMMARY
# - Lists store multiple values
# - They are ordered and changeable (mutable)
# - Indexing starts at 0
# - Common operations: append, remove, sort, slicing
# - split() converts strings into lists