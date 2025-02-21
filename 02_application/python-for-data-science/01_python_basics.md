# Python Basics

* [1. Accessing Help and Getting Object Types](#1-accessing-help-and-getting-object-types)
* [2. Importing Packages](#2-importing-packages)
* [3. The Working Directory](#3-the-working-directory)
* [4. Operators](#4-operators)
* [5. Getting Started With Lists](#5-getting-started-with-lists)
* []()
* []()
* []()
* []()
* []()


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
# ---- Arithmetic Operators ----
#-------------------------------
102 + 37 # Add two numbers with +
102 - 37 # Subtract a number with -
4 * 6 # Multiply two numbers with *
22 / 7 # Divide a number by another with /
22 // 7 # Integer divide a number with //
3 ** 4 # Raise to the power of with //
22 % 7 # Get the remainder after division with %

# ---- Assignment Operator ----
a = 5    # Assign a value to a
x[0] = 1 # Change the value of an item in a list

# ---- Numeric Comparison Operators ----
3 == 3 # Test for equality with ==
3 != 3 # Test for inequality with !=
3 > 1 # Test greater than with >
3 >= 3 # Test greater than or equal to with >=
3 < 4 # Test less than with <
3 <= 4 # Test less than or equal to with <=

# ---- Logical Operators ----
~(2 == 2) # Logical NOT with ~
(1 != 1) & (1 < 1) # Logical AND with &
(1 != 1) | (1 < 1) # Logical OR with |
(1 != 1) ^ (1 < 1) # Logical XOR with ^
```

## 5. Getting Started With Lists
A list is an ordered and changeable sequence of elements. It can hold integers, characters, floats, strings, and even objects.
```python
# --- Creating Lists
x = [1, 2, 3]

# --- List Functions and Methods
x.sorted(x) # Return a sorted copy of the list e.g., [1, 2, 3]

```


---

## Title
Exp
```python

```

---

_Source: [Datacamp](https://media.datacamp.com/legacy/image/upload/v1694526244/Marketing/Blog/Python_Basics_Cheat_Sheet-updated.pdf)_
