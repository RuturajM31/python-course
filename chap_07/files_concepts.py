# 📁 File Handling in Python (open() and file concepts)

# File handling allows Python to create, read, write, and manage files.

# 🔹 1. open() function
# Used to open a file and return a file object.

# Syntax:
# open(file, mode)

f = open("data.txt", "r")  # opens file in read mode

# -------------------------------------------------------

# 🔹 2. File modes

# "r" → Read (default, file must exist)
# "w" → Write (overwrites file or creates new)
# "a" → Append (adds data at end)
# "x" → Create file (error if exists)
# "b" → Binary mode (images/videos)
# "t" → Text mode (default)

# -------------------------------------------------------

# 🔹 3. Reading files

# Read full file
f = open("data.txt", "r")
content = f.read()
print(content)
f.close()

# Read line by line
f = open("data.txt", "r")
for line in f:
    print(line)
f.close()

# Read all lines into list
f = open("data.txt", "r")
lines = f.readlines()
print(lines)
f.close()

# -------------------------------------------------------

# 🔹 4. Writing files

# Overwrite file (w mode)
f = open("data.txt", "w")
f.write("Hello World")
f.close()  # ⚠️ deletes old content

# Append file (a mode)
f = open("data.txt", "a")
f.write("\nNew line added")
f.close()

# -------------------------------------------------------

# 🔹 5. Best practice: with open()

# Automatically closes file (recommended)
with open("data.txt", "r") as f:
    content = f.read()
    print(content)

# -------------------------------------------------------

# 🔹 6. File pointer (seek & tell)

f = open("data.txt", "r")

# Current position
print(f.tell())

# Move pointer to start
f.seek(0)

f.close()

# -------------------------------------------------------

# 🔹 7. Full example

with open("example.txt", "w") as f:
    f.write("Hello Python")

with open("example.txt", "r") as f:
    print(f.read())

# -------------------------------------------------------

# 🔹 8. Python 2 (obsolete - NOT for Python 3)

# f = file("data.txt", "r")  # ❌ not supported in Python 3

# -------------------------------------------------------

# 🚀 Summary
# - Use open() for file handling
# - Use "r", "w", "a" modes depending on need
# - Prefer "with open()" for safety
# - Always close file if not using "with"
# - file() is deprecated (Python 2 only)