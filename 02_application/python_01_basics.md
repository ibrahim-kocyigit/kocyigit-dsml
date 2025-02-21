# Python Basics

* [1. Accessing Help and Getting Object Types](#1-accessing-help-and-getting-object-types)
* [2. Importing Packages](#2-importing-packages)
* [3. The Working Directory](#3-the-working-directory)
* [4. Operators](#4-operators)
* [5. Getting Started With Lists](#5-getting-started-with-lists)
* [6. Getting Started With Dictionaries](#6-getting-started-with-dictionaries)
* [7. NumPy Arrays](#7-numpy-arrays)
* [8. Math Functions and Methods](#8-math-functions-and-methods)
* [9. Getting Started with Characters and Strings](#9-getting-started-with-characters-and-strings)
* [10. Getting Started with DataFrames](#10-getting-started-with-dataframes)

---

## 1. Accessing Help and Getting Object Types
```python
1 + 1 # Everything after the hash symbol is ignored by Python
help(max) # Display the documentation for the max function
type('a') # Get the type of an object - this returns 'str'
```

## 2. Importing Packages
Python packages are a collection of useful tools developed by the open-source community. They extend the capabilities of the python language. To install a new package (for example, pandas), you can go to your command prompt and type in pip install pandas. Once a package is installed, you can import it as follows:
```python
import pandas # Import a package without an alias
import pandas as pd # Import a package with an alias
from pandas import DataFrame # Import an object from a package
```

## 3. The Working Directory
The working directory is the default file path that python reads or saves files into. An example of the working directory is C://file/path . The os library or the pathlib library (more modern, and more Pythonic than os) is needed to set and get the working directory.
```python
import os # Import the operating system package
from pathlib import Path # Import the Path class from the pathlib library

os.getcwd() # Get the current directory
os.setcwd("new/working/directory") # Set the working directory to a new file path

current_dir = Path.cwd() # Get the current directory
```

## 4. Operators
```python
# ---- ARITHMETIC OPERATORS ----
102 + 37 # Add two numbers with +
102 - 37 # Subtract a number with -
4 * 6 # Multiply two numbers with *
22 / 7 # Divide a number by another with /
22 // 7 # Integer divide a number with //
3 ** 4 # Raise to the power of with //
22 % 7 # Get the remainder after division with %

# ---- ASSIGNMENT OPERATOR ----
a = 5    # Assign a value to a
x[0] = 1 # Change the value of an item in a list

# ---- NUMERIC COMPARISON OPERATORS ----
3 == 3 # Test for equality with ==
3 != 3 # Test for inequality with !=
3 > 1 # Test greater than with >
3 >= 3 # Test greater than or equal to with >=
3 < 4 # Test less than with <
3 <= 4 # Test less than or equal to with <=

# ---- LOGICAL OPERATORS ----
~(2 == 2) # Logical NOT with ~
(1 != 1) & (1 < 1) # Logical AND with &
(1 != 1) | (1 < 1) # Logical OR with |
(1 != 1) ^ (1 < 1) # Logical XOR with ^
```

## 5. Getting Started With Lists
A list is an ordered and changeable sequence of elements. It can hold integers, characters, floats, strings, and even objects.
```python
# ---- Creating Lists ----
x = [1, 3, 2]

# --- LIST FUNCTIONS AND METHODS ----
x.sorted(x) # Return a sorted copy of the list e.g., [1, 2, 3]
x.sort() # Sorts the list in-place (replaces x)
reversed(x) # Reverse the order of elements in x e.g., [3, 2, 1]
x.reversed() # Reverse the list in-place
x.count(2) # Count the number of element 2 in the list

# ---- SELECTING LIST ELEMENTS ----
x = ['a', 'b', 'c', 'd', 'e'] # Defining the list
x[0] # Select the 0th element in the list
x[-1] # Select the last element in the list
x[1:3] # Select 1st (inclusive) to 3rd (exclusive)
x[2:] # Select the 2nd to the end
x[:3] # Select 0th to 3rd (exclusive)
x[0:5:2] # Select every other element from the 0th to the 5th (exclusive)

# ---- CONCATENATING LISTS ----
x = [1, 3, 6] # Define the x list
y = [10, 15, 21] # Define the y list
x + y # Returns [1, 3, 6, 10, 15, 21]
3 * x # Returns [1, 3, 6, 1, 3, 6, 1, 3, 6]
```


## 6. Getting Started With Dictionaries
A dictionary stores data values in key-value pairs. That is, unlike lists which are indexed by position, dictionaries are indexed by their keys, the names of which must be unique.
```python
# ---- CREATING DICTIONARIES ----
x = {'a': 1, 'b': 'Hello', 'c': True}

# ---- DICTIONARY FUNCTIONS AND METHODS ----
x.keys() # Get the keys of a dictionary, returns dict_keys(['a', 'b', 'c'])
x.values() # Get the values of a dictionary, returns dict_values([1, 'Hello', True])

# ---- SELECTING DICTIONARY ELEMENTS ----
x['a'] # Get a value from a dictionary by specifying the key
```

## 7. NumPy Arrays
NumPy is a python package for scientific computing. It provides multidimensional array objects and efficient operations on them. To import NumPy, you can run this Python code: `import numpy as np`
```python
# Convert a python list to a NumPy array:
np.array([1, 2, 3]) # Returns array([1, 2, 3])

# Return a sequence from start (inclusive) to end (exclusive)
np.arange(1, 5) # Returns array([1, 2, 3, 4])

# Return a stepped sequence from start (inclusive) to end (exclusive)
np.arange(1, 5, 2) # Returns array([1, 3])

# Repeat values n times
np.repeat([1, 3, 6], 3) # Returns array([1, 1, 1, 3, 3, 3, 6, 6, 6])

# Repeat values n times
np.tile([1, 3, 6], 3) # Returns array([1, 3, 6, 1, 3, 6, 1, 3, 6])
```

## 8. Math Functions and Methods
All functions take an array as the input.
```python
np.log(x) # Calculate logarithm
np.exp(x) # Calculate exponential
np.max(x) # Get maximum value
np.min(x) # Get minimum value
np.sum(x) # Calculate sum
np.mean(x) # Calculate mean
np.quantile(x, q) # Calculate q-th quantile
np.round(x, n) # Round to n decimal places
np.var(x) # Calculate variance
np.std(x) # Calculate standard deviation
```

## 9. Getting Started with Characters and Strings
```python
# Create a string with double or single quotes
string = "DataCamp"

# Embed a quote in string with the escape character \
"He said, \"DataCamp\""

# Create multi-line strings with triple quotes
"""
A Frame of Data
Tidy, Mine, Analyze It
Now You Have Meaning
Citation: https://mds-book.github.io/haikus.html
"""

string[0] # Get the character at a specific position
string[0:2] # Get a substring from starting position (inclusive) to ending index (exclusive)

# ---- COMBINING AND SPLITTING STRINGS ---
"Data" + "Framed" # Concatenate strings with +, this returns "DataFramed"
3 * "data " # Repeat strings with *, this returns "data data data "
"beekepers".split("e") # Split a string on a delimiter, returns ['b', '', 'k', '', 'p', 'rs']

# ---- MUTATE STRINGS ----
string = "Jack and Jill" # Define string
string.upper() # Convert a string to uppercase, returns "JACK AND JILL"
string.lower() # Convert a string to lowercase, returns "jack and jill"
string.title() # Convert a string to title case, returns "Jack And Jill"
string.replace('J', 'P') # Replaces matches of a substring with another, returns "Pack and Pill"
```

## 10. Getting Started with DataFrames
Pandas is a fast and powerful package for data analysis and manipulation in python. To import the package, you can use `import pandas as pd`. 
* A pandas DataFrame is a structure that contains two-dimensional data stored as rows and columns. 
* A pandas series is a structure that contains one-dimensional data
```python
# ---- CREATING DATAFRAMES ----
# Create a DataFrame from a dictionary
pd.DataFrame({
    'a': [1, 2, 3],
    'b': np.array[4, 4, 6],
    'c': ['x', 'x', 'y']
})

# Create a DataFrame from a list of dictionaries
pd.DataFrame([
    {'a': 1, 'b': 4, 'c': 'x'},
    {'a': 2, 'b': 4, 'c': 'x'},
    {'a': 3, 'b': 6, 'c': 'y'},
])

# ---- SELECTING DATAFRAME ELEMENTS ----
# Select a row, column or element from a dataframe. Remember: all positions are counted from zero, not one.

df.iloc[3] # Select the 3rd row
df.['col_name'] # Select one column by name
df[['col_1', 'col_2']] # Select multiple columns by name
df.iloc[:, 2] # Select all rows, 2nd column
df.iloc[3, 2] # Select the element in the 3rd row, 2nd column
df.iloc[::2,:] # Select all the columns for every other row

# ---- MANIPULATING DATAFRAMES ----
pd.concat([df1, df2]) # Concatenate DataFrames vertically
pd.concat([df1, df2], axis="columns") # Concatenate DataFrames horizontally
df.query('logical_condition') # Get rows matching a condition
df.drop(columns=['col_1', 'col_2']) # Drop columns by name
df.rename(columns={'old_name':'new_name'}) # Rename columns
df['new_column'] = df['existing_column'] * 2 # Add a new column
df.assign(temp_f = 9/5 * df['temp_c'] + 32) # Add a new column
df.mean() # Calculate the mean of each column
df.agg(aggregation_function) # Apply an aggregation function to all columns
df.drop_duplicates() # Get unique rows
df.sort_values(by='col_name') # Sort by values in a column (ascending=True by default)
df.nlargest(n, 'col_name') # Get rows with largest values in a column.
```

---

##### _Source: [Datacamp](https://media.datacamp.com/legacy/image/upload/v1694526244/Marketing/Blog/Python_Basics_Cheat_Sheet-updated.pdf)_
