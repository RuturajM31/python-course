# NumPy Explained Simply 🚀 (Beginner + Advanced Notes)

## What is NumPy?

:contentReference[oaicite:0]{index=0} is a core Python library used for:

- fast numerical computing
- arrays and matrices
- statistics
- data science & machine learning

👉 It is much faster than normal Python lists because it uses optimized C-based operations.

```python
import numpy as np
```

---

# PART 1 – Beginner Concepts

---

## 1. Creating Arrays

### Idea
A NumPy array is like a Python list, but:
- faster
- more memory efficient
- supports math operations directly

```python
a = np.array([10, 20, 30, 40, 50])
```

### Key properties

| Property | Meaning |
|---|---|
| `dtype` | data type |
| `shape` | dimensions |

```python
print(a.dtype)
print(a.shape)
```

Example output:
```
int64
(5,)
```

👉 `(5,)` means 1D array with 5 elements

---

## 2. arange() and linspace()

### np.arange()

Creates numbers with a step size:

```python
np.arange(0, 10, 2)
```

Output:
```
[0 2 4 6 8]
```

Syntax:
```python
np.arange(start, stop, step)
```

---

### np.linspace()

Creates evenly spaced values:

```python
np.linspace(0, 1, 6)
```

Output:
```
[0.  0.2 0.4 0.6 0.8 1. ]
```

Syntax:
```python
np.linspace(start, stop, number_of_values)
```

---

## 3. 2D Arrays (Matrices)

```python
m = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
```

Access elements:

```python
m[1,2]
```

Result:
```
6
```

👉 indexing starts at 0:
- row 1 → second row
- column 2 → third column

---

## 4. Slicing

Extract parts of arrays:

```python
a[2:6]
```

👉 elements from index 2 to 5

```python
a[::2]
```

👉 every second element

```python
a[-3:]
```

👉 last 3 elements

---

## 5. Vectorized Operations

One of NumPy’s biggest advantages.

```python
a * 2
a ** 2
np.sqrt(a)
```


::contentReference[oaicite:1]{index=1}


👉 operations apply to every element automatically (no loops needed)

---

## 6. Boolean Indexing

Filter arrays using conditions:

```python
noten[noten <= 2.0]
```

👉 keeps only values that satisfy the condition

---

## 7. Statistics

```python
d.min()
d.max()
d.mean()
d.std()
np.median(d)
```

### Mean formula:
:contentReference[oaicite:2]{index=2}

### Standard deviation:
:contentReference[oaicite:3]{index=3}

---

## 8. reshape()

Change shape without changing data:

```python
a.reshape(3,4)
```

👉 1D → 2D transformation

Constraint:
- total number of elements must stay the same

---

## 9. Random Numbers

```python
np.random.randint(1, 7, size=20)
```

👉 simulates dice rolls

### Reproducibility:
```python
np.random.seed(42)
```

---

## 10. np.where()

Simple conditional logic:

```python
np.where(temp >= 20, "warm", "cold")
```

Meaning:

```
if condition is true → "warm"
else → "cold"
```

---

# PART 2 – Advanced NumPy Concepts

---

## 11. Broadcasting

Automatically expands arrays to match shapes:

```python
M + v
```

👉 vector added to every row of matrix

---

## 12. Matrix Multiplication

```python
A @ B
```

:contentReference[oaicite:4]{index=4}

- `@` → matrix multiplication  
- `*` → element-wise multiplication  

---

## 13. Linear Algebra

### Transpose
```python
M.T
```

### Determinant
:contentReference[oaicite:5]{index=5}

### Inverse
:contentReference[oaicite:6]{index=6}

Used in:
- physics
- machine learning
- optimization

---

## 14. Eigenvalues & Eigenvectors

```python
np.linalg.eig(M)
```

Core equation:
:contentReference[oaicite:7]{index=7}

👉 vector direction stays the same, only scaling changes

Used in:
- PCA
- data reduction
- ML models

---

## 15. Linear Regression

Goal: find best-fit line


::contentReference[oaicite:8]{index=8}


- m = slope
- b = intercept

NumPy solves it using:

```python
np.linalg.lstsq()
```

---

## 16. argsort()

Returns sorting order (indices):

```python
np.argsort(punkte)
```

👉 useful for ranking systems

---

## 17. Vectorization (Performance)

### Slow:
```python
for x in data:
```

### Fast:
```python
np.where(...)
```

👉 NumPy is faster because it runs optimized C code internally

---

## 18. Stacking Arrays

### Vertical stacking
```python
np.vstack([a,b])
```

### Horizontal stacking
```python
np.hstack([a,b])
```

---

## 19. Correlation

:contentReference[oaicite:9]{index=9}

Values:
- 1 → strong positive relation
- 0 → no relation
- -1 → strong negative relation

---

## 20. Save & Load Data

```python
np.save("file.npy", data)
np.load("file.npy")
```

Also CSV:

```python
np.savetxt("file.csv", data, delimiter=",")
```

---

# Summary 🧠

| Concept | Meaning |
|---|---|
| Arrays | fast data structure |
| Broadcasting | automatic shape matching |
| Vectorization | fast operations without loops |
| Slicing | extract parts of data |
| Boolean indexing | filtering |
| reshape | change shape |
| linalg | linear algebra |
| random | simulation data |

---

# Why NumPy matters

NumPy is the foundation of:

- Pandas
- Scikit-learn
- TensorFlow
- PyTorch

👉 Without NumPy, modern data science in Python would not exist.

---

# Final takeaway

> NumPy = fast arrays + mathematical power + data science foundation
```