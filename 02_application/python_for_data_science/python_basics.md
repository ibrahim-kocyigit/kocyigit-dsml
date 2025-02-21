# Python Basics

* [1. Accessing Help and Getting Object Types](#1-accessing-help-and-getting-object-types)
* [2. Importing Packages](#2-importing-packages)
* [3. The Working Directory](#3-the-working-directory)
* [4. Operators](#4-operators)
* [5. Getting Started With Lists](#5-getting-started-with-lists)
* [6. Getting Started With Dictionaries](#6-getting-started-with-dictionaries)
* [7. Getting Started with Characters and Strings](#7-getting-started-with-characters-and-strings)

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
**Arithmetic Operators**
```python
102 + 37 # Add two numbers with +
102 - 37 # Subtract a number with -
4 * 6 # Multiply two numbers with *
22 / 7 # Divide a number by another with /
22 // 7 # Integer divide a number with //
3 ** 4 # Raise to the power of with //
22 % 7 # Get the remainder after division with %
```
**Assignment Operator**
```python
a = 5    # Assign a value to a
x[0] = 1 # Change the value of an item in a list
```
**Numeric Comparison Operators**
```python
3 == 3 # Test for equality with ==
3 != 3 # Test for inequality with !=
3 > 1 # Test greater than with >
3 >= 3 # Test greater than or equal to with >=
3 < 4 # Test less than with <
3 <= 4 # Test less than or equal to with <=
```
**Logical Operators**
```python
~(2 == 2) # Logical NOT with ~
(1 != 1) & (1 < 1) # Logical AND with &
(1 != 1) | (1 < 1) # Logical OR with |
(1 != 1) ^ (1 < 1) # Logical XOR with ^
```

## 5. Getting Started With Lists
A list is an ordered and changeable sequence of elements. It can hold integers, characters, floats, strings, and even objects.

**Creating Lists**
```python
x = [1, 3, 2]
```
**List Functions and Methods**
```python
x.sorted(x) # Return a sorted copy of the list e.g., [1, 2, 3]
x.sort() # Sorts the list in-place (replaces x)
reversed(x) # Reverse the order of elements in x e.g., [3, 2, 1]
x.reversed() # Reverse the list in-place
x.count(2) # Count the number of element 2 in the list
```
**Selecting List Elements**
```python
x = ['a', 'b', 'c', 'd', 'e'] # Defining the list
x[0] # Select the 0th element in the list
x[-1] # Select the last element in the list
x[1:3] # Select 1st (inclusive) to 3rd (exclusive)
x[2:] # Select the 2nd to the end
x[:3] # Select 0th to 3rd (exclusive)
x[0:5:2] # Select every other element from the 0th to the 5th (exclusive)
```
**Concatenate Lists**
```python
x = [1, 3, 6] # Define the x list
y = [10, 15, 21] # Define the y list
x + y # Returns [1, 3, 6, 10, 15, 21]
3 * x # Returns [1, 3, 6, 1, 3, 6, 1, 3, 6]
```


## 6. Getting Started With Dictionaries
A dictionary stores data values in key-value pairs. That is, unlike lists which are indexed by position, dictionaries are indexed by their keys, the names of which must be unique.

**Creating Dictionaries**
```python
x = {'a': 1, 'b': 'Hello', 'c': True}
```
**Dictionary Functions and Methods**
```python
x.keys() # Get the keys of a dictionary, returns dict_keys(['a', 'b', 'c'])
x.values() # Get the values of a dictionary, returns dict_values([1, 'Hello', True])
```
**Selecting Dictionary Elements**
```python
x['a'] # Get a value from a dictionary by specifying the key
```

## 7. Getting Started with Characters and Strings
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
```
**Combining and Splitting Strings**
```python
"Data" + "Framed" # Concatenate strings with +, this returns "DataFramed"
3 * "data " # Repeat strings with *, this returns "data data data "
"beekepers".split("e") # Split a string on a delimiter, returns ['b', '', 'k', '', 'p', 'rs']
```
**Mutate Strings**
```python
string = "Jack and Jill" # Define string
string.upper() # Convert a string to uppercase, returns "JACK AND JILL"
string.lower() # Convert a string to lowercase, returns "jack and jill"
string.title() # Convert a string to title case, returns "Jack And Jill"
string.replace('J', 'P') # Replaces matches of a substring with another, returns "Pack and Pill"
```

---

##### _Source: [Datacamp](https://media.datacamp.com/legacy/image/upload/v1694526244/Marketing/Blog/Python_Basics_Cheat_Sheet-updated.pdf)_