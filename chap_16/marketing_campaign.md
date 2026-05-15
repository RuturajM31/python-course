# 📊 Marketing Campaign Analysis (End-to-End Data Science Project)

## 🧠 Project Overview

This project analyzes a real-world marketing campaign dataset containing 2,240 customers. The goal is to understand customer behavior, identify high-value segments, and evaluate campaign effectiveness using data analysis and RFM segmentation.

---

# 🎯 Business Objective

The analysis focuses on answering three key business questions:

1. **Who are the customers?** (Demographics)
2. **What do they buy?** (Spending behavior)
3. **How do they respond to marketing campaigns?** (Campaign effectiveness)

The final outcome is a **customer segmentation model** that helps improve marketing targeting and ROI.

---

# 📦 Dataset Overview

* **Rows:** 2240 customers
* **Columns:** 26 features
* **Type:** CRM marketing dataset

### Key Feature Groups:

#### 👤 Customer Profile

* Year_Birth
* Income
* Kidhome
* Teenhome

#### 🛒 Product Spending

* Wines, Fruits, Meat, Fish, Sweets, Gold Products

#### 📈 Purchase Channels

* Web, Store, Catalog purchases
* Web visits per month

#### 🎯 Campaign Response

* Response (target variable)
* AcceptedCmp1–5

---

# 🚨 Data Loading Issue (Important Learning Point)

Initially, the dataset failed to load correctly because it used a **semicolon (;) separator instead of a comma**.

### ❌ Incorrect attempts:

```python
pd.read_csv(file_path)
pd.read_csv(file_path, sep="\t")
```

### ✅ Correct solution:

```python
df = pd.read_csv(file_path, sep=";")
```

👉 This fixed the dataset structure and enabled proper analysis.

---

# 🧹 Data Cleaning Steps

## 1. Handling Missing Values

Only the `Income` column had missing values (~1.1%).

```python
df["Income"] = df["Income"].fillna(df["Income"].median())
```

👉 Median was used because income is skewed.

---

## 2. Removing Irrelevant Columns

* Z_CostContact
* Z_Revenue

These columns had constant values and no analytical value.

---

## 3. Feature Engineering

### Age Creation

```python
df["Age"] = 2026 - df["Year_Birth"]
```

### Total Spending (Key KPI)

```python
df["Total_Spend"] = (
    df["MntWines"] + df["MntFruits"] + df["MntMeatProducts"] +
    df["MntFishProducts"] + df["MntSweetProducts"] + df["MntGoldProds"]
)
```

### Purchase Frequency

```python
df["Frequency"] = (
    df["NumWebPurchases"] + df["NumStorePurchases"] + df["NumCatalogPurchases"]
)
```

---

# 📊 Exploratory Data Analysis (EDA)

## 💰 Income Distribution

* Average income: ~52,000
* Slight right skew

## 🛒 Spending Behavior

* Wine is the highest spending category
* Meat is second highest
* Fruits and sweets are low

## 🛍️ Channel Behavior

* Store purchases > Web purchases
* Web visits are relatively high

👉 Insight: Customers browse online but prefer buying offline

---

## 🎯 Campaign Response Rate

* Only ~15% of customers responded

👉 Insight: Campaign targeting is inefficient and needs segmentation

---

# 📈 Data Visualization Summary

Key plots used:

* Income distribution (histogram)
* Total spending distribution
* Purchase channels comparison (bar chart)
* Campaign response distribution
* Segment analysis charts

---

# 🧩 RFM Segmentation Model

RFM stands for:

* **Recency** → How recently a customer purchased
* **Frequency** → How often they purchase
* **Monetary** → How much they spend

---

## 🔴 Recency Score

```python
df["Recency_Score"] = pd.qcut(df["Recency"], 5, labels=[5,4,3,2,1]).astype(int)
```

## 🔵 Frequency Score

```python
df["Frequency_Score"] = pd.qcut(df["Frequency"], 5, labels=[1,2,3,4,5]).astype(int)
```

## 🟢 Monetary Score

```python
df["Monetary_Score"] = pd.qcut(df["Total_Spend"], 5, labels=[1,2,3,4,5]).astype(int)
```

---

## 🧠 Final RFM Score

```python
df["RFM_Score"] = (
    df["Recency_Score"] +
    df["Frequency_Score"] +
    df["Monetary_Score"]
)
```

---

## 🧩 Customer Segments

| Segment             | Description                         |
| ------------------- | ----------------------------------- |
| Champions           | High value, highly active customers |
| Loyal Customers     | Regular and stable buyers           |
| Potential Customers | Growth opportunity segment          |
| At Risk             | Low engagement customers            |

---

# 📊 Business Insights

## 🎯 1. Campaign Performance is Low

Only ~15% response rate → targeting is inefficient.

## 🎯 2. Revenue is Concentrated

A small group of customers contributes most of the revenue.

## 🎯 3. Offline Shopping Dominates

Store purchases exceed online purchases.

## 🎯 4. Wine is the Key Product Driver

Wine dominates customer spending behavior.

---

# 🚀 Final Conclusion

This project demonstrates a complete data analytics workflow:

✔ Data cleaning and preprocessing
✔ Feature engineering
✔ Exploratory data analysis
✔ Business insight extraction
✔ RFM-based customer segmentation

The final output enables **data-driven marketing strategies**, improving targeting, retention, and campaign efficiency.

---

# 💡 Outcome

This analysis transforms raw customer data into actionable business intelligence, enabling better marketing decisions and customer segmentation strategies.
# 📊 Marketing Campaign Analysis (End-to-End Data Science Project)

## 🧠 Project Overview

This project analyzes a real-world marketing campaign dataset containing 2,240 customers. The goal is to understand customer behavior, identify high-value segments, and evaluate campaign effectiveness using data analysis and RFM segmentation.

---

# 🎯 Business Objective

The analysis focuses on answering three key business questions:

1. **Who are the customers?** (Demographics)
2. **What do they buy?** (Spending behavior)
3. **How do they respond to marketing campaigns?** (Campaign effectiveness)

The final outcome is a **customer segmentation model** that helps improve marketing targeting and ROI.

---

# 📦 Dataset Overview

* **Rows:** 2240 customers
* **Columns:** 26 features
* **Type:** CRM marketing dataset

### Key Feature Groups:

#### 👤 Customer Profile

* Year_Birth
* Income
* Kidhome
* Teenhome

#### 🛒 Product Spending

* Wines, Fruits, Meat, Fish, Sweets, Gold Products

#### 📈 Purchase Channels

* Web, Store, Catalog purchases
* Web visits per month

#### 🎯 Campaign Response

* Response (target variable)
* AcceptedCmp1–5

---

# 🚨 Data Loading Issue (Important Learning Point)

Initially, the dataset failed to load correctly because it used a **semicolon (;) separator instead of a comma**.

### ❌ Incorrect attempts:

```python
pd.read_csv(file_path)
pd.read_csv(file_path, sep="\t")
```

### ✅ Correct solution:

```python
df = pd.read_csv(file_path, sep=";")
```

👉 This fixed the dataset structure and enabled proper analysis.

---

# 🧹 Data Cleaning Steps

## 1. Handling Missing Values

Only the `Income` column had missing values (~1.1%).

```python
df["Income"] = df["Income"].fillna(df["Income"].median())
```

👉 Median was used because income is skewed.

---

## 2. Removing Irrelevant Columns

* Z_CostContact
* Z_Revenue

These columns had constant values and no analytical value.

---

## 3. Feature Engineering

### Age Creation

```python
df["Age"] = 2026 - df["Year_Birth"]
```

### Total Spending (Key KPI)

```python
df["Total_Spend"] = (
    df["MntWines"] + df["MntFruits"] + df["MntMeatProducts"] +
    df["MntFishProducts"] + df["MntSweetProducts"] + df["MntGoldProds"]
)
```

### Purchase Frequency

```python
df["Frequency"] = (
    df["NumWebPurchases"] + df["NumStorePurchases"] + df["NumCatalogPurchases"]
)
```

---

# 📊 Exploratory Data Analysis (EDA)

## 💰 Income Distribution

* Average income: ~52,000
* Slight right skew

## 🛒 Spending Behavior

* Wine is the highest spending category
* Meat is second highest
* Fruits and sweets are low

## 🛍️ Channel Behavior

* Store purchases > Web purchases
* Web visits are relatively high

👉 Insight: Customers browse online but prefer buying offline

---

## 🎯 Campaign Response Rate

* Only ~15% of customers responded

👉 Insight: Campaign targeting is inefficient and needs segmentation

---

# 📈 Data Visualization Summary

Key plots used:

* Income distribution (histogram)
* Total spending distribution
* Purchase channels comparison (bar chart)
* Campaign response distribution
* Segment analysis charts

---

# 🧩 RFM Segmentation Model

RFM stands for:

* **Recency** → How recently a customer purchased
* **Frequency** → How often they purchase
* **Monetary** → How much they spend

---

## 🔴 Recency Score

```python
df["Recency_Score"] = pd.qcut(df["Recency"], 5, labels=[5,4,3,2,1]).astype(int)
```

## 🔵 Frequency Score

```python
df["Frequency_Score"] = pd.qcut(df["Frequency"], 5, labels=[1,2,3,4,5]).astype(int)
```

## 🟢 Monetary Score

```python
df["Monetary_Score"] = pd.qcut(df["Total_Spend"], 5, labels=[1,2,3,4,5]).astype(int)
```

---

## 🧠 Final RFM Score

```python
df["RFM_Score"] = (
    df["Recency_Score"] +
    df["Frequency_Score"] +
    df["Monetary_Score"]
)
```

---

## 🧩 Customer Segments

| Segment             | Description                         |
| ------------------- | ----------------------------------- |
| Champions           | High value, highly active customers |
| Loyal Customers     | Regular and stable buyers           |
| Potential Customers | Growth opportunity segment          |
| At Risk             | Low engagement customers            |

---

# 📊 Business Insights

## 🎯 1. Campaign Performance is Low

Only ~15% response rate → targeting is inefficient.

## 🎯 2. Revenue is Concentrated

A small group of customers contributes most of the revenue.

## 🎯 3. Offline Shopping Dominates

Store purchases exceed online purchases.

## 🎯 4. Wine is the Key Product Driver

Wine dominates customer spending behavior.

---

# 🚀 Final Conclusion

This project demonstrates a complete data analytics workflow:

✔ Data cleaning and preprocessing
✔ Feature engineering
✔ Exploratory data analysis
✔ Business insight extraction
✔ RFM-based customer segmentation

The final output enables **data-driven marketing strategies**, improving targeting, retention, and campaign efficiency.

---

# 💡 Outcome

This analysis transforms raw customer data into actionable business intelligence, enabling better marketing decisions and customer segmentation strategies.
