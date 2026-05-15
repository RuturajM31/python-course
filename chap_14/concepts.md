# Python OOP Concepts (Simple Explanation)

# 1. Class = Blueprint / Template

A **class** is like a blueprint for creating objects.

Example:
- Blueprint of a car
- Blueprint of a house

In Python:

```python
class PartyAnimal:
```

This creates a class called `PartyAnimal`.

It describes:
- what data objects will store
- what actions objects can perform

---

# 2. Attribute = Variable inside a class

Attributes store data about an object.

Example:

```python
x = 0
name = ""
```

Here:
- `x` stores the party count
- `name` stores the person's name

Think of attributes as:
> information the object remembers

---

# 3. Method = Function inside a class

A method is a function that belongs to a class.

Example:

```python
def party(self):
```

This method increases the party count.

```python
self.x = self.x + 1
```

---

# 4. Object = Real instance created from a class

Objects are actual things created from the class.

Example:

```python
s = PartyAnimal("Sally")
j = FootballFan("Jim")
```

Now:
- `s` is an object
- `j` is another object

Both are created using class blueprints.

---

# 5. Constructor = Runs automatically when object is created

Constructor in Python:

```python
def __init__(self, nam):
```

This runs automatically when an object is created.

Example:

```python
s = PartyAnimal("Sally")
```

Python automatically calls:

```python
__init__
```

Inside constructor:

```python
self.name = nam
```

This stores the name inside the object.

---

# 6. self = Current object

`self` means:
> this current object

For Sally:
- `self.name` = Sally

For Jim:
- `self.name` = Jim

`self` helps Python know which object is being used.

---

# 7. Inheritance = Reusing another class

Inheritance allows one class to use properties and methods from another class.

Example:

```python
class FootballFan(PartyAnimal):
```

This means:

> `FootballFan` inherits from `PartyAnimal`

So `FootballFan` automatically gets:
- attributes
- methods
- constructor

from `PartyAnimal`.

---

# Complete Example with Inheritance

```python
class PartyAnimal:

    # Attributes
    x = 0
    name = ""

    # Constructor
    def __init__(self, nam):
        self.name = nam
        print(self.name, "constructed")

    # Method
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)


# Inherited Class
class FootballFan(PartyAnimal):

    # New attribute
    points = 0

    # New method
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)


# Create PartyAnimal object
s = PartyAnimal("Sally")
s.party()

# Create FootballFan object
j = FootballFan("Jim")
j.party()
j.touchdown()
```

---

# Understanding the Inheritance

## Parent Class

```python
class PartyAnimal:
```

This is the main/base class.

It contains:
- name
- x
- constructor
- party()

---

## Child Class

```python
class FootballFan(PartyAnimal):
```

This class inherits from `PartyAnimal`.

So `FootballFan` can already use:

```python
j.party()
```

even though `party()` was not written again inside `FootballFan`.

---

# Step-by-Step Execution

---

## Step 1: Create Sally

```python
s = PartyAnimal("Sally")
```

Constructor runs automatically.

Output:

```python
Sally constructed
```

---

## Step 2: Sally parties

```python
s.party()
```

`x` increases from 0 → 1

Output:

```python
Sally party count 1
```

---

## Step 3: Create Jim

```python
j = FootballFan("Jim")
```

Even though `FootballFan` has no constructor,
it inherits the constructor from `PartyAnimal`.

Output:

```python
Jim constructed