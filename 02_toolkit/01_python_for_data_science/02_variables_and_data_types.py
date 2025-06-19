# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. Variables
# 2. Built-in Data Types - Numeric
# 3. Built-in Data Types - Sequence
# 4. Built-in Data Types - Dictionary
# 5. Built-in Data Types - Set
# 6. Built-in Data Types - Boolean
# 7. Built-in Data Types - None
# 8. Type Checking & Conversion


# =======================================
# 1. VARIABLES
# =======================================
# - Containers for storing data values.
# - Created when you first assign a value to them.
# - Python is dynamically typed; variable type is determined at runtime.
# - Can be reassigned to data of a different type.

# Example of variable assignment and dynamic typing
variable_x = 100  # x is an integer
print(variable_x)

variable_x = "Now I'm a string."  # x is now a string
print(variable_x)


# =======================================
# 2. BUILT-IN DATA TYPES - NUMERIC
# =======================================
# - `int`: Whole numbers, positive or negative, without decimals.
# - `float`: Numbers with a decimal point.
# - `complex`: Numbers with a real and imaginary part (e.g., 3 + 5j).

integer_number = 42
float_number = 3.14159
complex_number = 3 + 5j

# You can use underscores for readability in large numbers
large_integer = 1_000_000


# =======================================
# 3. BUILT-IN DATA TYPES - SEQUENCE
# =======================================
# - Ordered collections of items, accessible by index

# --- Strings (`str`) ---
# - Immutable sequence of characters.
# - Enclosed in single ('') or double ("") quotes.
# - (Detailed manipulation in the next lesson).
my_string = "Hello, Python!"

# --- Lists (`list`) ---
# - Mutable, ordered sequence of items.
# - Can contain items of different data types.
# - Defined with square brackets `[]`.
my_list = [1, "apple", 3.5, True]
my_list.append("new_item")  # Lists are mutable (can be changed)

# --- Tuples (`tuple`) ---
# - Immutable, ordered sequence of items.
# - Once created, cannot be changed.
# - Defined with parentheses `()`.
my_tuple = (1, "apple", 3.5, True)
# my_tuple.append("new_item") # This would raise an AttributeError


# =======================================
# 4. BUILT-IN DATA TYPES - DICTIONARY
# =======================================
# - `dict`: Unordered (in older Python versions) collection of key-value pairs.
# - Keys must be unique and immutable (e.g., string, number, tuple)
# - Mutable; values can be changed.
# - Defined with curly braces `{}`.

my_dictionary = {
    "name": "Ibrahim",
    "age": 41,
    "courses": ["Data Science", "Machine Learning"],
}

my_dictionary["age"] = 42  # Dictionaries are mutable


# =======================================
# 5. BUILT-IN DATA TYPES - SET
# =======================================
# - `set`: Mutable, unordered collection of unique items.
# - No duplicate elements are allowed.
# - Defined with curly braces `{}` or `set()` function.

my_set = {1, 2, 3, 4, 4, 5}  # Duplicates are automatically removed
print(my_set)  # -> {1, 2, 3, 4, 5}
my_set.add(6)  # Sets are mutable

# --- Frozenset (`frozenset`) ---
# - Immutable version of a set.
my_frozen_set = frozenset({1, 2, 3, 4})
# my_frozen_set.add(5) # This would raise an AttributeError


# =======================================
# 6. BUILT-IN DATA TYPES - BOOLEAN
# =======================================
# - `bool`: Represents one of two values: True or False.
# - Often the result of comparison operations.
is_active = True
has_permission = False
is_greater = 10 > 5  # Evaluates to True


# =======================================
# 7. BUILT-IN DATA TYPES - NONE
# =======================================
# - `NoneType`: Has only one value: None.
# - Used to signify the absence of a value or a null value.
no_value = None


# =======================================
# 8. TYPE CHECKING & CONVERSION
# =======================================
# - `type()`: Built-in function to check the type of a variable.
# - Type Conversion (Casting): Convert between compatible data types

number_string = "123"
print(type(number_string))  # <class 'str'>

# Convert string to integer
number_int = int(number_string)
print(type(number_int))  # <class 'int'>

# Convert integer to float
number_float = float(number_int)
print(type(number_float))  # <class 'float'>

# Convert a list to a tuple
list_to_convert = [1, 2, 3]
converted_tuple = tuple(list_to_convert)
print(type(converted_tuple))  # <class 'tuple'>


# --- End of File ---
