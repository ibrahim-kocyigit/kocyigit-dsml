# Python Basics Cheat Sheet

## Core Concepts

**1. Comments**

* **Description:** Lines of text ignored by the Python interpreter.
* **Syntax:** `# This is a comment`
* **Example:**
    ```python
    # This is a comment
    ```

**2. Variable Assignment**

* **Description:** Assigns a value to a variable.
* **Syntax:** `variable_name = value`
* **Example:**
    ```python
    name = "John"  # assigning John to variable name
    x = 5  # assigning 5 to variable x
    ```

**3. Data Types**

* **Description:** Basic data types in Python.
* **Types:**
    * Integer (`int`): Whole numbers (e.g., 7).
    * Float (`float`): Decimal numbers (e.g., 12.4).
    * Boolean (`bool`): True or False values.
    * String (`str`): Text (e.g., "John").
* **Example:**
    ```python
    x = 7  # Integer Value
    y = 12.4  # Float Value
    is_valid = True  # Boolean Value
    is_valid = False  # Boolean Value
    F_Name = "John"  # String Value
    ```

**4. Python Operators**

* **Description:** Symbols used to perform operations.
* **Types:**
    * Addition (`+`): Adds two values.
    * Subtraction (`-`): Subtracts one value from another.
    * Multiplication (`*`): Multiplies two values.
    * Division (`/`): Divides one value by another (returns a float).
    * Floor Division (`//`): Divides one value by another (returns an integer quotient).
    * Modulo (`%`): Returns the remainder of a division.
* **Example:**
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

* **Description:** Combines (concatenates) strings.
* **Syntax:** `concatenated_string = string1 + string2`
* **Example:**
    ```python
    result = "Hello" + " John"
    ```

**2. Indexing**

* **Description:** Accesses a character at a specific index.
* **Example:**
    ```python
    my_string = "Hello"
    char = my_string[0]
    ```

**3. Slicing**

* **Description:** Extracts a portion of a string.
* **Syntax:** `substring = string_name[start:end]`
* **Example:**
    ```python
    my_string = "Hello"
    substring = my_string[0:5]
    ```

**4. `len()`**

* **Description:** Returns the length of a string.
* **Syntax:** `len(string_name)`
* **Example:**
    ```python
    my_string = "Hello"
    length = len(my_string)
    ```

**5. `lower()`**

* **Description:** Converts a string to lowercase.
* **Example:**
    ```python
    my_string = "Hello"
    lowercase_text = my_string.lower()
    ```

**6. `upper()`**

* **Description:** Converts a string to uppercase.
* **Example:**
    ```python
    my_string = "Hello"
    uppercase_text = my_string.upper()
    ```

**7. `strip()`**

* **Description:** Removes leading/trailing whitespace.
* **Example:**
    ```python
    my_string = " Hello "
    trimmed = my_string.strip()
    ```

**8. `replace()`**

* **Description:** Replaces substrings.
* **Example:**
    ```python
    my_string = "Hello"
    new_text = my_string.replace("Hello", "Hi")
    ```

**9. `split()`**

* **Description:** Splits a string into a list based on a delimiter.
* **Example:**
    ```python
    my_string = "apple,banana,orange"
    split_text = my_string.split(",")
    ```

## Output

**1. `print()`**

* **Description:** Prints a message or variable to the console.
* **Example:**
    ```python
    print("Hello, world")
    a = 1
    b = 2
    print(a + b)
    ```