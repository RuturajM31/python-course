import seaborn as sns
import matplotlib.pyplot as plt

# 1. 📈 Line Plot (Trend Analysis)

x = [1, 2, 3, 4, 5]
y = [10, 12, 15, 13, 18]

sns.lineplot(x=x, y=y)
plt.title("Line Plot")
plt.show()


# 2. 📊 Bar Plot (Category Comparison)

categories = ["A", "B", "C"]
values = [10, 25, 15]

sns.barplot(x=categories, y=values)
plt.title("Bar Plot")
plt.show()

# 5. 📦 Histogram (Distribution)

# Used to show data distribution

data = np.random.normal(50, 10, 100)

sns.histplot(data, bins=10, kde=True)
plt.title("Histogram with KDE")
plt.show()

# 6. 📦 Box Plot (Outliers & Spread)

# Used to detect outliers and spread.
import numpy as np
data = np.random.randn(100)

sns.boxplot(data=data)
plt.title("Box Plot")
plt.show()

# 7. 🔥 Heatmap (Correlation / Matrix Data)

matrix = np.random.rand(5, 5)

sns.heatmap(matrix, annot=True, cmap="coolwarm")
plt.title("Heatmap")
plt.show()

# 8. 🎻 Violin Plot (Distribution Shape)

# Combines box plot + KDE.

data = np.random.normal(60, 15, 200)

sns.violinplot(data=data)
plt.title("Violin Plot")
plt.show()

# 9. 🔗 Scatter Plot (Relationships)

# Used to show relationships between variables.

x = np.random.rand(50)
y = np.random.rand(50)

sns.scatterplot(x=x, y=y)
plt.title("Scatter Plot")
plt.show()

# 10. 📊 Pair Plot (Multi-variable Analysis)

# Used to visualize relationships between multiple variables.

df = sns.load_dataset("iris")

sns.pairplot(df, hue="species")
plt.show()