# Python Strings – Complete Important Functions (Revision File with Notes)

# -------------------------------------------------
# 1. String Creation
# -------------------------------------------------
# Strings are sequences of characters enclosed in quotes
text = "Python"
print("String:", text)


# -------------------------------------------------
# 2. Indexing & Negative Indexing
# -------------------------------------------------
# Access characters using position (0-based index)
text = "Python"
print(text[0])   # P
print(text[-1])  # n


# -------------------------------------------------
# 3. Slicing
# -------------------------------------------------
# Extract parts of a string
text = "Python"
print(text[0:3])   # Pyt
print(text[::-1])  # reverse string


# -------------------------------------------------
# 4. Length
# -------------------------------------------------
# Returns number of characters
text = "Python"
print(len(text))


# -------------------------------------------------
# 5. Case Conversion Methods
# -------------------------------------------------
text = "hello World"

print(text.upper())       # HELLO WORLD
print(text.lower())       # hello world
print(text.title())       # Hello World
print(text.capitalize())   # Hello world
print(text.casefold())     # aggressive lowercase (for comparisons)


# -------------------------------------------------
# 6. Whitespace Handling
# -------------------------------------------------
text = "   hello python   "

print(text.strip())   # remove both sides
print(text.lstrip())  # left side
print(text.rstrip())  # right side


# -------------------------------------------------
# 7. Find, Index, Count
# -------------------------------------------------
text = "hello python"

print(text.find("p"))     # returns index or -1
print(text.index("p"))    # same but error if not found
print(text.count("l"))    # count occurrences


# -------------------------------------------------
# 8. Replace
# -------------------------------------------------
text = "I like Java"
print(text.replace("Java", "Python"))


# -------------------------------------------------
# 9. Startswith / Endswith
# -------------------------------------------------
text = "Python programming"

print(text.startswith("Py"))  # True
print(text.endswith("ing"))   # True


# -------------------------------------------------
# 10. Split & Join
# -------------------------------------------------
sentence = "I love Python"
words = sentence.split()
print(words)

print("-".join(words))


# -------------------------------------------------
# 11. Check Methods
# -------------------------------------------------
text1 = "Python"
text2 = "123"
text3 = "Python123"

print(text1.isalpha())  # letters only
print(text2.isdigit())  # numbers only
print(text3.isalnum())  # letters + numbers
print("   ".isspace()) # only spaces


# -------------------------------------------------
# 12. Alignment Methods
# -------------------------------------------------
text = "Python"

print(text.center(10, "*"))  # **Python**
print(text.ljust(10, "-"))   # Python----
print(text.rjust(10, "-"))   # ----Python


# -------------------------------------------------
# 13. zfill (Zero Padding)
# -------------------------------------------------
num = "42"
print(num.zfill(5))  # 00042


# -------------------------------------------------
# 14. Partition / rpartition
# -------------------------------------------------
text = "I love Python programming"

print(text.partition("Python"))   # splits into 3 parts
print(text.rpartition(" "))       # split from right


# -------------------------------------------------
# 15. Prefix / Suffix Removal
# -------------------------------------------------
text = "www.google.com"

print(text.removeprefix("www."))
print(text.removesuffix(".com"))


# -------------------------------------------------
# 16. Replace using translate
# -------------------------------------------------
text = "hello world"

mapping = str.maketrans("hel", "HEW")
print(text.translate(mapping))


# -------------------------------------------------
# 17. String Formatting
# -------------------------------------------------
name = "Alice"
age = 25

print(f"My name is {name} and age is {age}")
print("My name is {} and age is {}".format(name, age))


# -------------------------------------------------
# 18. Membership Operator
# -------------------------------------------------
text = "Python"

print("P" in text)     # True
print("z" in text)     # False


# -------------------------------------------------
# 19. ASCII Conversion
# -------------------------------------------------
print(ord("A"))  # character to ASCII
print(chr(65))    # ASCII to character


# -------------------------------------------------
# 20. Reverse String
# -------------------------------------------------
text = "Python"
print(text[::-1])


# -------------------------------------------------
# 21. Comparison (lexicographical)
# -------------------------------------------------
print("apple" < "banana")  # True


# -------------------------------------------------
# 22. Useful Trick: Loop through string
# -------------------------------------------------
text = "Python"

for char in text:
    print(char)
