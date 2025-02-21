# Python Basics Cheat Sheet

## Core Concepts

**1. Comments**
```python
# This is a comment
```

**2. Variable Assignment**
```python
name = "John"  # assigning John to variable name
x = 5  # assigning 5 to variable x
```

**3. Basic Data Types**
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
* Addition (`+`): Adds two values.
* Subtraction (`-`): Subtracts one value from another.
* Multiplication (`*`): Multiplies two values.
* Division (`/`): Divides one value by another (returns a float).
* Floor Division (`//`): Divides one value by another (returns an integer quotient).
* Modulo (`%`): Returns the remainder of a division.
```python
x = 9
y = 4
result_add = x + y  # Addition (13)
result_sub = x - y  # Subtraction (5)
result_mul = x * y  # Multiplication (36)
result_div = x / y  # Division (2.25)
result_fdiv = x // y  # Floor Division (2)
result_mod = x % y  # Modulo (1)
```

## String Manipulation

**1. Concatenation**
```python
result = "Hello" + " John" # "Hello John"
```
**2. Indexing**
```python
my_string = "Hello"
char = my_string[0] # 'H'
```
**3. Slicing**
```python
my_string = "Hello"
substring = my_string[0:5] # "Hello"
```
**4. Length**
```python
my_string = "Hello"
length = len(my_string) # 5
```

**5. To Lowercase**
```python
my_string = "Hello"
lowercase_text = my_string.lower() # "hello"
```

**6. To Uppercase**
```python
my_string = "Hello"
uppercase_text = my_string.upper() # "HELLO"
```

**7. Removing leading/trailing whitespace**
```python
my_string = " Hello "
trimmed = my_string.strip() # "Hello"
```

**8. Replacing substrings**
```python
my_string = "Hello"
new_text = my_string.replace("Hello", "Hi") # "Hi"
```

**9. Splitting a string into a list based on a delimiter**
```python
my_string = "apple,banana,orange"
split_text = my_string.split(",") # ['apple', 'banana', 'orange']
```

## Output

**1. Printing to the console**
```python
print("Hello, world") # prints "Hello, world"
a = 1
b = 2
print(a + b) # prints 3
```
