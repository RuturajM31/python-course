# Python Strings – Quick Revision Notes

## 1. What is a String?

A **string** is a sequence of characters enclosed in quotes.

```python
name = "Alice"
city = 'Berlin'
```

You can use:

* Single quotes: 'Hello'
* Double quotes: "Hello"
* Triple quotes for multi-line strings:

```python
text = '''Hello
World'''
```

---

## 2. String Indexing

Strings are indexed (starting from 0).

```python
text = "Python"
# P  y  t  h  o  n
# 0  1  2  3  4  5
```

* Positive indexing: left → right
* Negative indexing: right → left

```python
text[-1]  # 'n'
text[0]   # 'P'
```

---

## 3. String Slicing

Extract part of a string.

```python
text = "Python"

text[0:3]   # 'Pyt'
text[2:5]   # 'tho'
text[:4]    # 'Pyth'
text[2:]    # 'thon'
text[:]     # full string
```

Format:

```python
string[start:end:step]
```

---

## 4. String Length

```python
len("Python")  # 6
```

---

## 5. String Immutability

Strings cannot be changed after creation.

```python
text = "Hello"
# text[0] = 'h'  ❌ Not allowed
```

You must create a new string instead.

---

## 6. String Concatenation

Combine strings using `+`

```python
"Hello" + " World"
```

Repeat strings using `*`

```python
"Hi" * 3  # 'HiHiHi'
```

---

## 7. Common String Methods

### Case Methods

```python
"hello".upper()   # 'HELLO'
"HELLO".lower()   # 'hello'
"hello".title()   # 'Hello'
"hello".capitalize() # 'Hello'
```

### Search Methods

```python
"python".find("t")     # index of 't'
"python".count("p")    # count occurrences
```

### Replace

```python
"I like Java".replace("Java", "Python")
```

### Check Methods

```python
"abc".isalpha()
"123".isdigit()
"abc123".isalnum()
```

### Whitespace

```python
"  hello  ".strip()   # removes spaces
"  hello".lstrip()    # left strip
"hello  ".rstrip()     # right strip
```

---

## 8. Splitting and Joining

### Split string into list

```python
"a,b,c".split(",")   # ['a', 'b', 'c']
```

### Join list into string

```python
",".join(['a','b','c'])  # 'a,b,c'
```

---

## 9. String Formatting

### f-strings (recommended)

```python
name = "Alice"
age = 25

f"My name is {name} and age is {age}"
```

### format()

```python
"My name is {}".format("Alice")
```

---

## 10. Escape Characters

```python
\n  # new line
\t  # tab
\\  # backslash
\"  # double quote
```

Example:

```python
print("Hello\nWorld")
```

---

## 11. Useful Tricks

### Reverse string

```python
text[::-1]
```

### Check substring

```python
"py" in "python"  # True
```

---

## 12. Summary

* Strings are immutable sequences of characters
* Use slicing for extraction
* Use methods for transformation
* Use f-strings for formatting
