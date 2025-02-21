# Pandas for Data Science

* [1. Introduction](#1-introduction)
* [2. Pandas Data Structures](#2-pandas-data-structures)
* [3. Dropping](#3-dropping)
* [4. Asking for Help](#4-asking-for-help)
* [5. Sort and Rank](#5-sort-and-rank)
* [6. Input/Output](#6-inputoutput)
* [7. Selection](#7-selection)
* [8. Retrieving Series/DataFrame Information](#8-retrieving-seriesdataframe-information)
* [9. Applying Functions](#9-applying-functions)
* [10. Data Alignment](#10-data-alignment)

---

## 1. Introduction
The Pandas library is built on NumPy and provides easy-to-use data structures and data analysis tools for the Python programming language. 

Use the following import convention:
```python
import pandas as pd
```

## 2. Pandas Data Structures
**Series:** A one-dimensional labeled array capable of holding any data type:
```python
s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])
```
**DataFrame:** A two-dimensional labeled data structure with columns of potentially different types:
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
Getting:
```python
s['b'] # Get one element
df[1:] # Get subset of a DataFrame
```
Selecting, Boolean Indexing & Setting.
```python
# ---- By Position ----
df.iloc[[0], [0]] # Select single value 
df.iat([0], [0]) # Select single value 

# ---- By Label -----
df.loc[[0], ['Country']] # Select single value 
df.at([0], ['Country']) # Select single value 

# ---- By Label/Position -----
df.ix[2] # Select single row of subset of rows
df.ix[:, 'Capital'] # Select a single column of subset of columns
df.ix[1, 'Capital'] # Select rows and columns

# ---- Boolean Indexing -----
s[~(s > 1)] # Series s where value is not > 1
s[(s < -1) | (s > 2)] # s where value is < -1 OR > 2
df[df['Population'] < 1_200_000_000] # Use filter to adjust DataFrame

# ---- Setting -----
s['a'] = 6 # Set index a of Series s to 6
```

## 8. Retrieving Series/DataFrame Information
Basic Information:
```python
df.shape # (rows, columns)
df.index # Describe index
df.columns # Describe columns
df.info() # Info on DataFrame
df.count() # Number of non-NA values
```
Summary:
```python
df.sum() # Sum of values
df.cumsum() # Cumulative sum of values
df.min() # Minimum value
df.max() # Maximum value
df.idxmin() # Index of the minimum value
df.idxmax() # Index of the maximum value
```

## 9. Applying Functions
```python
f = lambda x: x*2
df.apply(f) # Apply function
df.applymap(f) # Apply function element-wise
```

## 10. Data Alignment
Internal Data Alignment:
```python
# NA values are introduced in the indices that don't overlap
s3 = pd.Series([7, -2, 3], index=['a', 'c', 'd'])
s + s3
# a     10.0
# b     NaN
# c     5.0
# d     7.0
```
Arithmetic Operations with Fill Methods
```python
# You can also do the internal data alignment yourself with the help of the fill methods:
s.add(s3, fill_value=0)
# a    10.0
# b    -5.0
# c    5.0
# d    7.0
s.sub(s3, fill_value=2)
s.div(s3, fill_value=4)
s.mul(s3, fill_value=3)
```

---

##### _Source: [Datacamp](https://media.datacamp.com/legacy/image/upload/v1676302204/Marketing/Blog/Pandas_Cheat_Sheet.pdf)_

