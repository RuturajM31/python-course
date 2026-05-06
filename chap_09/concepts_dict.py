"""
TOPIC: Python Dictionaries & Collections (Study Notes in Code Form)
"""

# --------------------------------------------
# 1. WHAT IS A COLLECTION?
# --------------------------------------------
# A collection stores multiple values in one variable.
# Examples: list, tuple, dictionary, set

# --------------------------------------------
# 2. LISTS VS DICTIONARIES
# --------------------------------------------

# List: ordered, indexed, allows duplicates
my_list = ["apple", "banana", "apple"]

# Dictionary: key-value pairs, fast lookup, unordered (hashing)
my_dict = {
    "name": "Ali",
    "age": 20
}

# --------------------------------------------
# 3. DICTIONARY CONSTANTS
# --------------------------------------------
# Dictionaries use curly braces {}
# Format: {key: value}

student = {
    "id": 101,
    "grade": "A"
}

# --------------------------------------------
# 4. MOST COMMON USE CASE (WORD COUNT)
# --------------------------------------------
text = "apple banana apple orange apple"

word_count = {}

for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1  # uses get()

print("Word Count:", word_count)

# --------------------------------------------
# 5. USING get() METHOD
# --------------------------------------------
# Prevents KeyError if key does not exist

print(word_count.get("apple", 0))   # returns value or 0 if missing

# --------------------------------------------
# 6. HASHING & LACK OF ORDER
# --------------------------------------------
# Dictionaries use hashing → fast access, but no guaranteed order

# --------------------------------------------
# 7. WRITING DICTIONARY LOOPS
# --------------------------------------------

# Loop through keys
for key in student:
    print("Key:", key, "Value:", student[key])

# Loop through key-value pairs
for key, value in student.items():
    print(key, value)

# --------------------------------------------
# 8. SNEAK PEEK: TUPLES
# --------------------------------------------
# Tuples are ordered and immutable (cannot change)

my_tuple = (1, 2, 3)

# --------------------------------------------
# 9. SORTING DICTIONARIES
# --------------------------------------------

# Sort by keys
sorted_items = sorted(word_count.items())
print("Sorted by key:", sorted_items)

# Sort by values
sorted_by_value = sorted(word_count.items(), key=lambda x: x[1])
print("Sorted by value:", sorted_by_value)