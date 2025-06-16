"""
Key Concepts:
- Dynamic typing (no explicit type declaration)
- Mutable and immutable objects
- Common data types in data workflows
- Type conversion
- Variable naming conventions
"""

# ====================
# 1. Basic Data Types
# ====================
# Numeric types (fundamental in data science)
int_example = 42  # Integer (whole number)
float_example = 3.14150  # Floating point (decimal)
complex_example = 2 + 3j

# Boolean (essential for conditions and masking)
bool_true = True
bool_false = False

# Text type
string_example = "Data Science"  # also used for categorical data representation

# NoneType (often used as placeholder)
null_value = None


# ====================
# 2. Type Checking
# ====================
print(type(int_example))  # -> <class 'int'>
print(isinstance(float_example, float))  # -> True


# ====================
# 3. Type Conversion
# ====================
# Common in data cleaning/preprocessing

str_to_int = int("100")  # "100" -> 100
int_to_float = float(42)  # 42 -> 42.0
float_to_str = str(3.14)  # 3.14 -> "3.14"

# Dangerous conversions (data science watchout)
# int("3.14") -> ValueError
# float("abc") -> ValueError


# ====================
# 4. Variable Naming
# ====================
# PEP8 conventions (Python standard)
good_name = "clear"  # Descriptive
bad_name = "x"  # Non-Descriptive


# ====================
# 5. Special Cases
# ====================
# Large numbers (readability)
big_num = 1_000_000  # same as 1000000

# Multiple assignment
x, y, z = 1, 2, 3

# Swapping (no temp variable needed)
x, y = y, z  # Common in algorithms


# ====================
# 6. Memory Management
# ====================
# id() shows memory address
print(id(x))  # Unique identifier for the object

# Same value may have same id (implementation detail)
a = 256
b = 256
print(a is b)  # True for small integers (-5 to 256)


# ====================
# 7. Mutable vs. Immutable
# ====================
"""
Immutable (can't change after creation):
- int, float, bool, str, tuple

Mutable (can change):
- list, dict, set
"""


# Example of immutability
s = "data"
# s[0] = "D" # -> TypeError (strings are immutable)


# ====================
# 8. Practical DS Examples
# ====================
# Type conversion during data cleaning
dirty_data = "123.45"
clean_float = float(dirty_data)  # Common ETL operation

# Boolean masking preparation
is_outlier = False  # Will be used in filtering later

# Placeholder for missing data
missing_value = None  # Often replaced with np.nan later
