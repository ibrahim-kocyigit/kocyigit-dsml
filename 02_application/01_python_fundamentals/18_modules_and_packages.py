import os

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
# - Imports the entire module. Access contents with `module_name.member`.
import math

print(f"The square root of 81 is: {math.sqrt(81)}")
print(f"The value of Pi is: {math.pi}")

# --- `from module_name import member` ---
# - Imports a specific function, class, or variable directly into the current namespace.
from random import choice, randint

print(f"\nA random number between 1 and 100: {randint(1, 100)}")
print(f"A random choice from a list: {choice(['apple', 'banana', 'cherry'])}")

# --- `import module_name as alias` ---
# - Imports a module with a shorter, more convenient name (an alias).
# - This is extremely common in Data Science (e.g., `import numpy as np`).
import datetime as dt

print(f"\nThe current date and time is: {dt.datetime.now()}")
print("-" * 30)


# =======================================
# 3. CREATING AND USING A CUSTOM PACKAGE
# =======================================
# - We'll create a simple package called `my_ds_tools` in its own folder.

# --- Step 1: Create the package structure programmatically ---
PACKAGE_NAME = "my_ds_tools"
os.makedirs(PACKAGE_NAME, exist_ok=True)

# Create the __init__.py file to make the folder a package
with open(os.path.join(PACKAGE_NAME, "__init__.py"), "w") as f:
    pass  # This file can be empty

# Create a module for string utilities
string_utils_path = os.path.join(PACKAGE_NAME, "string_utils.py")
with open(string_utils_path, "w") as f:
    f.write("def clean_text(text):\n")
    f.write('    """Removes whitespace and converts to lowercase."""\n')
    f.write("    return text.strip().lower()\n\n")
    f.write("def count_chars(text):\n")
    f.write('    """Counts characters in a string."""\n')
    f.write("    return len(text)\n")

# Create a module for math utilities
math_utils_path = os.path.join(PACKAGE_NAME, "math_utils.py")
with open(math_utils_path, "w") as f:
    f.write("def average(numbers):\n")
    f.write('    """Calculates the average of a list of numbers."""\n')
    f.write("    if not numbers: return 0\n")  # handle empty list
    f.write("    return sum(numbers) / len(numbers)\n")

print(f"--- Created a package named '{PACKAGE_NAME}' ---")


# --- Step 2: Import from our custom package ---
from my_ds_tools import string_utils
from my_ds_tools.math_utils import average

# Use the imported module and function
raw_text = "  Some Text To Clean Up  "
cleaned = string_utils.clean_text(raw_text)
print(f"\nOriginal text: '{raw_text}'")
print(f"Cleaned text: '{cleaned}'")
print(f"Character count of cleaned text: {string_utils.count_chars(cleaned)}")

data_points = [10, 20, 30, 40, 50]
avg = average(data_points)
print(f"\nThe average of {data_points} is: {avg}")
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

# --- Let's add this block to our math_utils.py file ---
with open(math_utils_path, "a") as f:  # Re-open in append mode
    f.write("\n# The following block runs only when this script is executed directly\n")
    f.write("if __name__ == '__main__':\n")
    f.write('    print("Running math_utils.py as a script.")\n')
    f.write("    test_data = [1, 2, 3]\n")
    f.write('    print(f"Testing average function: {average(test_data)}")\n')

print("--- Running our `math_utils.py` module directly ---")
# os.system() lets us run a command line command from Python
# We can see the output of the __main__ block this way.
os.system(f"python {math_utils_path}")

print("\nNote that when we imported `average` earlier, the test code did not run.")
print("-" * 30)

print("This concludes the Python Fundamentals phase!")
