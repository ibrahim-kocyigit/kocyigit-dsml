# Pandas for Data Science

* [1. Introduction](#1-introduction)
* [2. Pandas Data Structures](#2-pandas-data-structures)
* [3. Dropping](#3-dropping)
* [4. Asking for Help](#4-asking-for-help)
* [5. Sort and Rank](#5-sort-and-rank)
* [6. Input/Output](#6-inputoutput)
* [7. Selection](#7-selection)
* []()
* []()
* []()
* []()

---

## 1. Introduction
The Pandas library is built on NumPy and provides easy-to-use data structures and data analysis tools for the Python programming language. 

Use the following import convention:
```python
import pandas as pd
```

## 2. Pandas Data Structures
* **Series:** A one-dimensional labeled array capable of holding any data type.
```python
s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])
```
* **DataFrame:** A two-dimensional labeled data structure with columns of potentially different types.
```python
df = pd.DataFrame({
    'Country': ['Belgium', 'India', 'Brazil'],
    'Capital': ['Brussels', 'New Delhi', 'Brasilia'],
    'Population': [11_190_846, 1_303_171_035, 207_847_528]
})
```

## 3. Dropping
```python
s.drop(['a', 'c']) # Drop values from rows (axis=0)
df.drop('Country', axis=1) # Drop values from columns (axis=1)
```

## 4. Asking for Help
```python
help(pd.Series.loc)
```

## 5. Sort and Rank
```python
df.sort_index() # Sort by labels along an axis
df.sort_values(by='Country') # Sort by the values along an axis
df.rank() # Assign ranks to entries 
```

## 6. Input/Output
Read and Write to CSV:
```python
pd.read_csv('file.csv', header=None, nrows=5)
df.to_csv('myDataFrame.csv')
```
Read and Write to Excel:
```python
pd.read_excel('file.xlsx')
df.to_excel('dir/myDataFrame.xlsx',  sheet_name='Sheet1')

# Read multiple sheets from the same file
xlsx = pd.ExcelFile('file.xls')
df = pd.read_excel(xlsx,  'Sheet1')
```
Read and Write to SQL Query or Database Table:
```python
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')
pd.read_sql(SELECT * FROM my_table;, engine)
pd.read_sql_table('my_table', engine)
pd.read_sql_query(SELECT * FROM my_table;', engine)

# (read_sql()is a convenience wrapper around read_sql_table() and read_sql_query())
df.to_sql('myDf', engine)
```

## 7. Selection
```python
# ---- GETTING ----
s['b'] # Get one element
df[1:] # Get subset of a DataFrame

# ---- SELECTING, BOOLEAN INDEXING, AND SETTING ----
# --- By Position
df.iloc[[0], [0]] # Select single value by row & column 
df.iat([0], [0])

# --- By Label
df.loc[]
```

## 8. Section
```python

```

## 9. Section
```python

```

## 10. Section
```python

```

---

##### _Source: [Datacamp](https://media.datacamp.com/legacy/image/upload/v1676302204/Marketing/Blog/Pandas_Cheat_Sheet.pdf)_

