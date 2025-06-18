# =======================================
# 1. TUPLE BASICS
# =======================================
# - A tuple is an immutable, ordered sequence of items.
# - "Immutable" means it cannot be changed after creation.
# - "Ordered" means items maintain a stable position (index).
# - Created with parentheses `()`.
# - Often used for fixed collections of items, like coordinates or database records.

# An empty tuple
empty_tuple = ()

# A tuple of integers
numbers = (1, 2, 3, 4, 5)

# A tuple with mixed data types
mixed_tuple = (1, "hello", 3.14, True)

# Creating a tuple with a single item requires a trailing comma
# to distinguish it from a number in parentheses.
single_item_tuple = (42,)
not_a_tuple = 42  # This is just the integer 42

# Parentheses are often optional (this is called "tuple packing")
packed_tuple = 10, 20, "thirty"
print(f"Packed tuple: {packed_tuple}")


# =======================================
# 2. ACCESSING ELEMENTS (INDEXING & SLICING)
# =======================================
# - Works exactly the same as with lists.
# - Use an integer index `[index]` to get a single element.
# - Use slicing `[start:stop:step]` to get a new sub-tuple.

point = (10, 20, 30)  # Represents an (x, y, z) coordinate
print(f"X coordinate: {point[0]}")
print(f"Y coordinate: {point[1]}")

# Slicing
# Gets items from index 0 up to (but not including) index 2
xy_coordinates = point[0:2]
print(f"XY coordinates: {xy_coordinates}")


# =======================================
# 3. IMMUTABILITY IN ACTION
# =======================================
# - You cannot change, add, or remove elements after a tuple is created.
# - Attempting to do so will result in a `TypeError`.

rgb_color = (255, 128, 0)  # An orange color
# rgb_color[0] = 200  # This line would raise a TypeError: 'tuple' object does not support item assignment
# rgb_color.append(1) # This would raise an AttributeError: 'tuple' object has no attribute 'append'


# =======================================
# 4. TUPLE METHODS
# =======================================
# - Because they are immutable, tuples have very few methods.

# - `.count(value)`: Returns the number of times a value appears.
# - `.index(value)`: Returns the index of the first occurrence of a value.
grades = ("A", "C", "B", "B", "A", "B")
print(f"\nNumber of 'B' grades: {grades.count('B')}")
print(f"First occurrence of 'A': {grades.index('A')}")


# =======================================
# 5. TUPLE UNPACKING
# =======================================
# - A powerful feature to assign the items of a tuple to multiple variables at once.
# - The number of variables must match the number of items in the tuple.
# - Commonly used when a function returns multiple values (it often returns them as a tuple).

record = ("John Doe", 34, "john.doe@email.com")

# Unpacking the tuple into separate variables
name, age, email = record

print(f"\nName: {name}")
print(f"Age: {age}")
print(f"Email: {email}")


# =======================================
# 6. WHY USE TUPLES?
# =======================================
# 1. Data Integrity: Protects your data from accidental changes.
#    config = ("192.168.1.1", 8080)

# 2. Performance: Can be slightly faster to create and process than lists.

# 3. Dictionary Keys: Tuples can be used as keys in a dictionary because
#    they are immutable. Lists cannot.
location_data = {
    ("New York", "NY"): 8.4,
    ("Los Angeles", "CA"): 3.9,
}
print(f"\nPopulation of New York: {location_data[('New York', 'NY')]} million")


# =======================================
# 7. LENGTH AND MEMBERSHIP
# =======================================
# - `len()`: Gets the number of items in a tuple.
# - `in` / `not in`: Checks if a value exists in a tuple.
# - These work the same as with lists.

permissions = ("read", "write", "execute")
print(f"\nNumber of permissions: {len(permissions)}")
print(f"Does user have 'write' permission? {'write' in permissions}")
print(f"Does user have 'admin' permission? {'admin' in permissions}")
