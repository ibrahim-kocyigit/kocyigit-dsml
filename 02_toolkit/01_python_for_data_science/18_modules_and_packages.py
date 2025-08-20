# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. What are Modules and Packages?
# 2. Using Built-in and Third-party Modules
# 3. Creating and Using a Custom Package
# 4. The `if __name__ == '__main__':` Block


# =======================================
# 1. WHAT ARE MODULES AND PACKAGES?
# =======================================
# - Module: A single Python file (`.py`) containing functions, classes, and variables.
# - Package: A directory containing multiple modules. It must contain a file named `__init__.py` (can be empty).
# - Why? To organize code, promote reusability, and prevent naming conflicts.


# =======================================
# 2. USING BUILT-IN AND THIRD-PARTY MODULES
# =======================================
# - Python has a vast Standard Library of modules.
# - The syntax for using them is the same as for your own modules.

# --- `import module_name` ---
# - Imports the entire module. Access contents with `module_name.member`
import math

print(f"The square root of 81 is: {math.sqrt(81)}")
print(f"The value of Pi is {math.pi}")

# --- `from module_name import member` ---
# - Imports a specific function, class, or variable directly into the current namespace.
from random import choice, randint

print(f"A random number between 1 and 100: {randint(1, 100)}")
print(f"A random choice from a list: {choice(['apple', 'banana', 'cherry'])}")

# --- `import module_name as alias` ---
# - Imports a module with a shorter, more convenient name (an alias).
# - This is extremely common in Data Science (e.g. `import numpy as np`).
import datetime as dt

print(f"\nThe current date and time is {dt.datetime.now()}")
print("-" * 30)


# =======================================
# 3. CREATING AND USING A CUSTOM PACKAGE
# =======================================
# - To use your own modules, you first need to create the files and folders.
# - In the same directory as this script, create the following structure:

# my_ds_tools/
# ├── __init__.py
# ├── string_utils.py
# └── math_utils.py

# --- Step 1: Create the `__init__.py` file ---
# This file can be completely empty. Its presence tells Python that
# `my_ds_tools` is a package, allowing you to import from it.

# --- Step 2: Create the `string_utils.py` module ---
# --- Place the following code inside `my_ds_tools/string_utils.py` ---
"""
def clean_text(text):
    \"\"\"Removes whitespace and converts to lowercase.\"\"\"
    return text.strip().lower()

def count_chars(text):
    \"\"\"Counts characters in a string.\"\"\"
    return len(text)
"""

# --- Step 3: Create the `math_utils.py` module ---
# --- Place the following code inside `my_ds_tools/math_utils.py` ---
"""
def average(numbers):
    \"\"\"Calculates the average of a list of numbers.\"\"\"
    if not numbers: return 0 # handle empty list
    return sum(numbers) / len(numbers)
"""

# --- Step 4: Import from our custom package ---
# Now that the files are created, we can import from them in this script.
print("--- Importing from a custom package ---")
from my_ds_tools import string_utils
from my_ds_tools.math_utils import average

# Use the imported module and function
raw_text = "   Some Text To Clean Up    "
cleaned = string_utils.clean_text(raw_text)
print(f"\nOriginal text: '{raw_text}'")
print(f"Cleaned text: '{cleaned}'")
print(f"Character count of cleaned text: {string_utils.count_chars(cleaned)}")

data_points = [10, 20, 30, 40, 50]
avg = average(data_points)
print(f"\nThe average of {data_points} is {avg}")
print("-" * 30)


# =======================================
# 4. THE `if __name__ == '__main__':` BLOCK
# =======================================
# - This is a crucial idiom in Python.
# - `__name__` is a special built-in variable.
#   - When a file is run directly, its `__name__` is set to "__main__".
#   - When a file is imported as a module, its `__name__` is set to its filename.
# - This block allows you to write code that ONLY RUNS when the file is executed directly,
#   not when it's imported. It's perfect for tests or demonstrations of the module's functions.

# --- To see this in action, add the following block to the END of your `math_utils.py` file ---
"""
# The following block runs only when this script is executed directly
if __name__ == '__main__':
    print("\\n--- Running math_utils.py as a script ---")
    test_data = [1, 2, 3]
    print(f"Testing average function: {average(test_data)}")
"""

# Now, if you run `python my_ds_tools/math_utils.py` from your terminal,
# you will see the test output. But when you import `average` (as we did above),
# that test code does not run.


# --- End of File ---
