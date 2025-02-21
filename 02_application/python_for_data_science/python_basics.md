# Python Basics Cheat Sheet

## Core Concepts

**1. Comments**
Lines of text ignored by the Python interpreter.
```python
# This is a comment
```

**2. Variable Assignment**
Assigns a value to a variable.
```python
name = "John"  # assigning John to variable name
x = 5  # assigning 5 to variable x
```

**3. Data Types**
Basic data types in Python.
* Integer (`int`): Whole numbers (e.g., 7).
* Float (`float`): Decimal numbers (e.g., 12.4).
* Boolean (`bool`): True or False values.
* String (`str`): Text (e.g., "John").
```python
x = 7  # Integer Value
y = 12.4  # Float Value
is_valid = True  # Boolean Value
is_valid = False  # Boolean Value
F_Name = "John"  # String Value
```

**4. Python Operators**
Symbols used to perform operations.
* Addition (`+`): Adds two values.
* Subtraction (`-`): Subtracts one value from another.
* Multiplication (`*`): Multiplies two values.
* Division (`/`): Divides one value by another (returns a float).
* Floor Division (`//`): Divides one value by another (returns an integer quotient).
* Modulo (`%`): Returns the remainder of a division.
```python
x = 9
y = 4
result_add = x + y  # Addition
result_sub = x - y  # Subtraction
result_mul = x * y  # Multiplication
result_div = x / y  # Division
result_fdiv = x // y  # Floor Division
result_mod = x % y  # Modulo
```

## String Manipulation

**1. Concatenation**
Combines (concatenates) strings.
```python
result = "Hello" + " John"
```

**2. Indexing**
Accesses a character at a specific index.
```python
my_string = "Hello"
char = my_string[0]
```

**3. Slicing**
Extracts a portion of a string.
```python
my_string = "Hello"
substring = my_string[0:5]
```

**4. `len()`**
Returns the length of a string.
```python
my_string = "Hello"
length = len(my_string)
```

**5. `lower()`**
Converts a string to lowercase.
```python
my_string = "Hello"
lowercase_text = my_string.lower()
```

**6. `upper()`**
Converts a string to uppercase.
```python
my_string = "Hello"
uppercase_text = my_string.upper()
```

**7. `strip()`**
Removes leading/trailing whitespace.
```python
my_string = " Hello "
trimmed = my_string.strip()
```

**8. `replace()`**
Replaces substrings.
```python
my_string = "Hello"
new_text = my_string.replace("Hello", "Hi")
```

**9. `split()`**
Splits a string into a list based on a delimiter.
```python
my_string = "apple,banana,orange"
split_text = my_string.split(",")
```

## Output

**1. `print()`**
Prints a message or variable to the console.
```python
print("Hello, world")
a = 1
b = 2
print(a + b)
```
