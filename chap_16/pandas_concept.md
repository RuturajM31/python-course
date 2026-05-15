# Pandas Revision Notes

## What is Pandas?

Pandas is a Python library used for:

* Data analysis
* Data cleaning
* Data manipulation
* Working with tables and time-series data

Pandas mainly provides two important data structures:

1. **Series** → One-dimensional labeled data
2. **DataFrame** → Two-dimensional table (rows and columns)

---

# 1. Importing Pandas

```python
import pandas as pd
```

`pd` is the standard alias used for pandas.

---

# 2. Pandas Series

A Series is like a single column of data.

## Create a Series

```python
import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)
```

## Series with Custom Index

```python
s = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
print(s)
```

## Access Elements

```python
print(s['a'])
print(s[0])
```

---

# 3. Pandas DataFrame

A DataFrame is a table with rows and columns.

## Create DataFrame from Dictionary

```python
import pandas as pd

students = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [21, 22, 23],
    'Marks': [85, 90, 88]
}

_df = pd.DataFrame(students)
print(_df)
```

## Create DataFrame from List

```python
data = [
    ['Alice', 21],
    ['Bob', 22]
]

_df = pd.DataFrame(data, columns=['Name', 'Age'])
print(_df)
```

---

# 4. Reading Files

## Read CSV File

```python
_df = pd.read_csv('data.csv')
```

## Read Excel File

```python
_df = pd.read_excel('data.xlsx')
```

## Read JSON File

```python
_df = pd.read_json('data.json')
```

---

# 5. Writing Files

## Save to CSV

```python
_df.to_csv('output.csv', index=False)
```

## Save to Excel

```python
_df.to_excel('output.xlsx', index=False)
```

---

# 6. Viewing Data

## Display First Rows

```python
_df.head()
```

Default shows first 5 rows.

## Display Last Rows

```python
_df.tail()
```

## Check Shape

```python
_df.shape
```

Returns:

```python
(rows, columns)
```

## Column Names

```python
_df.columns
```

## Data Types

```python
_df.dtypes
```

## Summary Information

```python
_df.info()
```

## Statistical Summary

```python
_df.describe()
```

---

# 7. Selecting Data

## Select Single Column

```python
_df['Name']
```

## Select Multiple Columns

```python
_df[['Name', 'Marks']]
```

## Select Row using loc

`loc` uses labels.

```python
_df.loc[0]
```

## Select Row using iloc

`iloc` uses index positions.

```python
_df.iloc[0]
```

## Select Specific Rows and Columns

```python
_df.loc[0:2, ['Name', 'Marks']]
```

```python
_df.iloc[0:2, 0:2]
```

---

# 8. Filtering Data

## Filter Rows

```python
_df[_df['Marks'] > 85]
```

## Multiple Conditions

```python
_df[(_df['Marks'] > 85) & (_df['Age'] > 21)]
```

## Using OR Condition

```python
_df[(_df['Marks'] > 85) | (_df['Age'] > 21)]
```

---

# 9. Sorting Data

## Sort by One Column

```python
_df.sort_values('Marks')
```

## Sort Descending

```python
_df.sort_values('Marks', ascending=False)
```

## Sort by Multiple Columns

```python
_df.sort_values(['Age', 'Marks'])
```

---

# 10. Adding and Modifying Columns

## Add New Column

```python
_df['Grade'] = ['A', 'A+', 'A']
```

## Create Column using Calculation

```python
_df['Bonus'] = _df['Marks'] + 5
```

## Modify Existing Column

```python
_df['Marks'] = _df['Marks'] + 2
```

---

# 11. Removing Data

## Drop Column

```python
_df.drop('Bonus', axis=1)
```

## Drop Multiple Columns

```python
_df.drop(['Bonus', 'Grade'], axis=1)
```

## Drop Row

```python
_df.drop(0)
```

## Delete Permanently

```python
_df.drop('Bonus', axis=1, inplace=True)
```

---

# 12. Handling Missing Values

## Detect Missing Values

```python
_df.isnull()
```

## Count Missing Values

```python
_df.isnull().sum()
```

## Remove Missing Values

```python
_df.dropna()
```

## Fill Missing Values

```python
_df.fillna(0)
```

## Fill with Mean

```python
_df['Marks'].fillna(_df['Marks'].mean())
```

---

# 13. Duplicate Handling

## Check Duplicates

```python
_df.duplicated()
```

## Remove Duplicates

```python
_df.drop_duplicates()
```

---

# 14. GroupBy Operations

Used for aggregation and analysis.

## Group By Column

```python
_df.groupby('Grade')['Marks'].mean()
```

## Multiple Aggregations

```python
_df.groupby('Grade')['Marks'].agg(['mean', 'max', 'min'])
```

---

# 15. Merge and Join

## Merge DataFrames

```python
pd.merge(df1, df2, on='ID')
```

## Left Join

```python
pd.merge(df1, df2, on='ID', how='left')
```

## Right Join

```python
pd.merge(df1, df2, on='ID', how='right')
```

## Inner Join

```python
pd.merge(df1, df2, on='ID', how='inner')
```

## Outer Join

```python
pd.merge(df1, df2, on='ID', how='outer')
```

---

# 16. Concatenation

## Combine Rows

```python
pd.concat([df1, df2])
```

## Combine Columns

```python
pd.concat([df1, df2], axis=1)
```

---

# 17. Apply Functions

## Apply Function on Column

```python
_df['Marks'].apply(lambda x: x + 5)
```

## Apply Custom Function

```python
def grade(marks):
    if marks > 90:
        return 'A+'
    return 'A'

_df['Grade'] = _df['Marks'].apply(grade)
```

---

# 18. String Operations

## Convert to Lowercase

```python
_df['Name'].str.lower()
```

## Convert to Uppercase

```python
_df['Name'].str.upper()
```

## String Length

```python
_df['Name'].str.len()
```

## Replace Text

```python
_df['Name'].str.replace('Alice', 'Anna')
```

---

# 19. Date and Time Operations

## Convert to Datetime

```python
_df['Date'] = pd.to_datetime(_df['Date'])
```

## Extract Year

```python
_df['Date'].dt.year
```

## Extract Month

```python
_df['Date'].dt.month
```

## Extract Day

```python
_df['Date'].dt.day
```

---

# 20. Pivot Tables

## Create Pivot Table

```python
pd.pivot_table(
    _df,
    values='Marks',
    index='Grade',
    aggfunc='mean'
)
```

---

# 21. Indexing

## Set Index

```python
_df.set_index('Name')
```

## Reset Index

```python
_df.reset_index()
```

---

# 22. Renaming Columns

```python
_df.rename(columns={'Marks': 'Score'})
```

---

# 23. Value Counts

Count frequency of values.

```python
_df['Grade'].value_counts()
```

---

# 24. Unique Values

## Get Unique Values

```python
_df['Grade'].unique()
```

## Count Unique Values

```python
_df['Grade'].nunique()
```

---

# 25. Query Method

```python
_df.query('Marks > 85')
```

---

# 26. Important Pandas Functions

| Function       | Purpose                    |
| -------------- | -------------------------- |
| head()         | First rows                 |
| tail()         | Last rows                  |
| info()         | Dataset information        |
| describe()     | Statistical summary        |
| shape          | Number of rows and columns |
| columns        | Column names               |
| dtypes         | Data types                 |
| isnull()       | Detect missing values      |
| fillna()       | Fill missing values        |
| dropna()       | Remove missing values      |
| groupby()      | Group data                 |
| merge()        | Combine datasets           |
| concat()       | Concatenate datasets       |
| sort_values()  | Sort data                  |
| value_counts() | Count values               |

---

# 27. Common Interview Questions

## Difference Between loc and iloc

| loc                | iloc                   |
| ------------------ | ---------------------- |
| Uses labels        | Uses integer positions |
| Includes end index | Excludes end index     |

Example:

```python
_df.loc[0]
_df.iloc[0]
```

---

## Difference Between Series and DataFrame

| Series          | DataFrame        |
| --------------- | ---------------- |
| One-dimensional | Two-dimensional  |
| Single column   | Multiple columns |

---

## Difference Between merge and concat

| merge               | concat                 |
| ------------------- | ---------------------- |
| Database-style join | Simple combination     |
| Uses common keys    | Stacks rows or columns |

---

# 28. Performance Tips

* Use vectorized operations instead of loops
* Use `category` datatype for repeated text values
* Avoid unnecessary copies of DataFrames
* Use `inplace=True` carefully
* Use `loc` and `iloc` efficiently

---

# 29. Best Practices

* Always inspect data using `head()` and `info()`
* Handle missing values before analysis
* Use meaningful column names
* Keep code readable and clean
* Save cleaned datasets separately

---

# 30. Mini Practice Example

```python
import pandas as pd

# Create DataFrame
students = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Marks': [85, 90, 88, 92],
    'Age': [21, 22, 23, 21]
}

_df = pd.DataFrame(students)

# View data
print(_df.head())

# Filter students
high_scores = _df[_df['Marks'] > 88]
print(high_scores)

# Average marks
average = _df['Marks'].mean()
print(average)

# Sort data
sorted_df = _df.sort_values('Marks', ascending=False)
print(sorted_df)
```

---

# 31. Quick Revision Cheat Sheet

## Data Loading

```python
pd.read_csv()
pd.read_excel()
```

## Data Inspection

```python
_df.head()
_df.info()
_df.describe()
```

## Selection

```python
_df['column']
_df.loc[]
_df.iloc[]
```

## Filtering

```python
_df[_df['Marks'] > 50]
```

## Missing Values

```python
_df.isnull()
_df.fillna()
_df.dropna()
```

## Aggregation

```python
_df.groupby()
_df.mean()
_df.sum()
```

## Combining Data

```python
pd.merge()
pd.concat()
```

---

# 32. Recommended Learning Path

1. Learn Series and DataFrame
2. Practice selection and filtering
3. Learn cleaning techniques
4. Practice groupby and aggregation
5. Learn merging and joins
6. Work on real datasets
7. Practice interview questions

---

# 33. Real-World Use Cases of Pandas

* Business reporting
* Data cleaning
* Financial analysis
* Marketing analytics
* Machine learning preprocessing
* Dashboard data preparation
* CSV and Excel automation

---

# 34. Common Errors

## KeyError

Happens when a column name does not exist.

```python
_df['Salary']
```

## Solution

Check available columns:

```python
print(_df.columns)
```

---

## SettingWithCopyWarning

Occurs when modifying a sliced DataFrame.

Better approach:

```python
_df.loc[_df['Marks'] > 90, 'Grade'] = 'A+'
```

---

# 35. Useful Aggregation Functions

```python
_df['Marks'].mean()
_df['Marks'].sum()
_df['Marks'].max()
_df['Marks'].min()
_df['Marks'].count()
_df['Marks'].std()
```

---

# 36. Memory Optimization

## Check Memory Usage

```python
_df.memory_usage()
```

## Convert Data Type

```python
_df['Grade'] = _df['Grade'].astype('category')
```

---

# 37. Final Revision Notes

Remember these core concepts:

* DataFrame basics
* Selection using `loc` and `iloc`
* Filtering and sorting
* Missing value handling
* GroupBy and aggregation
* Merge and concat
* String and datetime operations
* File handling

Pandas is best learned through practice with real datasets.
