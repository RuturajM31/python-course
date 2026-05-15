# 📊 Seaborn Charts – Notebook Examples

This document contains ready-to-run Seaborn chart examples for Jupyter Notebook practice.

---

# 1. 📈 Line Plot (Trend Analysis)

```python
import seaborn as sns
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 12, 15, 13, 18]

sns.lineplot(x=x, y=y)
plt.title("Line Plot")
plt.show()
```

---

# 2. 📊 Bar Plot (Category Comparison)

```python
import seaborn as sns
import matplotlib.pyplot as plt

categories = ["A", "B", "C", "D"]
values = [5, 15, 10, 20]

sns.barplot(x=categories, y=values)
plt.title("Bar Plot")
plt.show()
```

---

# 3. 📦 Histogram (Distribution)

```python
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(50, 15, 200)

sns.histplot(data, bins=15, kde=True)
plt.title("Histogram + KDE")
plt.show()
```

---

# 4. 📦 Box Plot (Outliers Detection)

```python
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(100)

sns.boxplot(data=data)
plt.title("Box Plot")
plt.show()
```

---

# 5. 🎻 Violin Plot (Distribution Shape)

```python
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(60, 10, 200)

sns.violinplot(data=data)
plt.title("Violin Plot")
plt.show()
```

---

# 6. 🔥 Heatmap (Matrix Visualization)

```python
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

matrix = np.random.rand(5, 5)

sns.heatmap(matrix, annot=True, cmap="coolwarm")
plt.title("Heatmap")
plt.show()
```

---

# 7. 🔗 Scatter Plot (Relationship)

```python
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(50)
y = np.random.rand(50)

sns.scatterplot(x=x, y=y)
plt.title("Scatter Plot")
plt.show()
```

---

# 8. 📊 Pair Plot (Multi-variable Analysis)

```python
import seaborn as sns

df = sns.load_dataset("iris")

sns.pairplot(df, hue="species")
plt.show()
```

---

# 9. 📊 Count Plot (Category Frequency)

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.countplot(x="day", data=tips)
plt.title("Count Plot")
plt.show()
```

---

# 10. 📊 Cat Plot (Flexible Categorical Plot)

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.catplot(x="day", y="total_bill", kind="bar", data=tips)
plt.show()
```

---

# 🚀 Summary

These charts cover the most important Seaborn visualizations:

* Line → trends
* Bar → comparison
* Histogram → distribution
* Box/Violin → spread & outliers
* Heatmap → matrix relationships
* Scatter → correlation
* Pairplot → multi-variable analysis
* Catplot → categorical analysis

---

# ✅ End of Notebook Examples
