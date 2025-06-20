# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. Dictionary Basics
# 2. Accessing Elements
# 3. Adding & Updating Pairs
# 4. Removing Pairs
# 5. Iterating Over Dictionaries
# 6. Dictionary Views & Membership


# =======================================
# 1. DICTIONARY BASICS
# =======================================
# - A dictionary is a mutable collection of key-value pairs.
# - As of Python 3.7+, dictionaries are ordered by insertion.
# - Created with curly braces `{}`. Syntax: `{'key': 'value'}`.
# - Keys must be unique and of an immutable type (e.g., string, number, tuple).
# - Values can be of any data type and can be duplicated.

# An empty dictionary
empty_dict = {}

# A simple dictionary
student = {"name": "Jane Doe", "age": 22, "major": "Computer Science", "gpa": 3.8}


# =======================================
# 2. ACCESSING VALUES
# =======================================
# - Access the value associated with a key.

# --- Square Bracket Notation `[]` ---
# - Direct access. Fast but raises a `KeyError` if the key does not exist.
print(f"Student's Name: {student['name']}")

# --- `.get(key, default)` Method ---
# - Safer way to access values
# - Returns `None` if the key is not found, preventing an error.
# - You can provide a default value to be returned instead of `None`.
print(f"Student's GPA: {student.get('gpa')}")
print(f"Student's Minor: {student.get('minor')}")  # Returns None, no error
print(f"Student's Minor (with default): {student.get('minor', 'Not Specified')}")


# =======================================
# 3. ADDING & UPDATING PAIRS
# =======================================
# - Dictionaries are mutable, so you can easily add, update, or remove pairs.

# --- Add a new key-value pair ---
student["graduation_year"] = 2025
print(f"\nAdded graduation year: {student}")

# --- Update an existing value ---
student["gpa"] = 3.9
print(f"Updated GPA: {student}")

# --- `.update()` Method ---
# - Merges another dictionary or an iterable of key-value pairs.
more_info = {"is_international": False, "major": "Data Science"}
student.update(more_info)
print(f"After update: {student}")


# =======================================
# 4. REMOVING PAIRS
# =======================================
# - Various ways to remove key-value pairs.


# --- `del` keyword ---
# - Removes a specific key-value pair. Raises `KeyError` if key is not found.
# del student['is_international']

# --- `.pop(key, default)` ---
# - Removes a key and returns its value. Safer against KeyErrors if default is provided.
gpa_value = student.pop("gpa")
print(f"\nRemoved GPA value: {gpa_value}")
print(f"Dict after pop: {student}")

# --- `.popitem()` ---
# - Removes and returns the last inserted key-value pair (LIFO).
last_item = student.popitem()
print(f"Popped last item: {last_item}")
print(f"Dict after popitem: {student}")


# =======================================
# 5. ITERATING OVER DICTIONARIES
# =======================================
# - Common patterns for looping through dictionary contents.

config = {"host": "localhost", "port": 8080, "user": "admin"}
print("\n--- Iterating through a dictionary ---")

# --- Loop through keys (default) ---
print("Keys:")
for k in config:  # same as `for k in config.keys():`
    print(f"  - {k}")

# --- Loop through values ---
print("Values:")
for v in config.values():
    print(f"  - {v}")

# --- Loop through key-value pairs (most common) ---
print("Items (key-value pairs):")
for key, value in config.items():
    print(f"  - {key}: {value}")


# =======================================
# 6. DICTIONARY VIEWS & MEMBERSHIP
# =======================================
# - `.keys()`, `.values()`, `.items()` return dynamic "view" objects, not lists.
# A view reflects changes made to the dictionary
# The `in` operator checks for the presence of a KEY

print("\n--- Membership testing ---")
# Check if a KEY exists
print(f"Is 'port' a key in config? {'port' in config}")  # True
print(f"Is 'password' a key in config? {'password' in config}")  # False

# To check for a value, you must use the `.values()` view
print(f"Is 8080 a value in config? {8080 in config.values()}")  # True


# --- End of File ---
