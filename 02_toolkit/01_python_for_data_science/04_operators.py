# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. Arithmetic Operators
# 2. Assignment Operators
# 3. Comparison Operators
# 4. Logical Operators
# 5. Identity Operators
# 6. Membership Operators
# 7. Bitwise Operators


# =======================================
# 1. ARITHMETIC OPERATORS
# =======================================
# - Used with numeric values to perform common mathematical operations.

a = 10
b = 3

print(f"Addition (a + b): {a + b}")  # 13
print(f"Subtraction (a - b): {a - b}")  # 7
print(f"Multiplication (a * b): {a * b}")  # 30
print(f"Exponentiation (a ** b): {a**b}")  # 1000

print(f"Division (a / b): {a / b}")  # 3.333... (always returns a float)
print(f"Floor Division (a // b): {a // b}")  # 3 (discards fraction, returns int)
print(f"Modulus (a % b): {a % b}")  # 1 (remainder of division)


# =======================================
# 2. ASSIGNMENT OPERATORS
# =======================================
# - Used to assign values to variables.
# - Compound operators perform an operation and assignment in one step.
x = 5  # Simple assignment
print(f"Initial x: {x}")  # "Initial x: 5"

x += 2  # Equivalent to x = x + 2
print(f"x += 2: {x}")  # "x += 2: 7"

x -= 3  # Equivalent to x = x - 3
print(f"x -= 3: {x}")  # "x -= 3: 4"

x *= 4  # Equivalent to x = x * 4
print(f"x *= 4: {x}")  # "x *= 4: 16"


# =======================================
# 3. COMPARISON OPERATORS
# =======================================
# - Used to compare two values.
# - The result is always a Boolean value: True or False.

val1 = 10
val2 = 20

print(f"val1 == val2: {val1 == val2}")  # False (Equal)
print(f"val1 != val2: {val1 != val2}")  # True (Not equal)
print(f"val1 > val2: {val1 > val2}")  # False (Greater than)
print(f"val1 <= val2: {val1 <= val2}")  # True (Less than or equal to)


# =======================================
# 4. LOGICAL OPERATORS
# =======================================
# - Used to combine conditional statements.
# - Operate on Boolean values (True, False).

is_raining = True
is_sunny = False

# - `and`: True only if BOTH operands are True.
print(f"Raining AND Sunny: {is_raining and is_sunny}")  # False

# - `or`: True if AT LEAST ONE operand is True.
print(f"Raining OR Sunny: {is_raining or is_sunny}")  # True

# - `not`: Inverts the Boolean value.
print(f"NOT Raining: {not is_raining}")  # False


# =======================================
# 5. IDENTITY OPERATORS
# =======================================
# - Used to compare the memory locations of two objects, not just their values.
# - `is`: True if variables point to the same object in memory.
# - `is not`: True if variables point to different objects.

# Note: Python may cache small integers, so they can have the same ID.
list_a = [1, 2, 3]
list_b = [1, 2, 3]  # A different object in memory with the same content
list_c = list_a  # Points to the exact same object as list_a

print(f"list_a == list_b: {list_a == list_b}")  # True (values are the same)
print(f"list_a is list_b: {list_a is list_b}")  # False (different objects in memory)
print(f"list_a is list_c: {list_a is list_c}")  # True (same object in memory)


# =======================================
# 6. MEMBERSHIP OPERATORS
# =======================================
# - Used to test if a sequence is present in an object.
# - `in`: True if a value is found in the sequence.
# - `not in`: True if a value is NOT found in the sequence.

my_course = "Python for Data Science"
my_list = [10, 20, 30, 40]

print(f"'Data' in my_course: {'Data' in my_course}")  # True
print(f"'Java' in my_course: {'Java' in my_course}")  # False
print(f"50 not in my_list: {50 not in my_list}")  # True
print(f"20 in my_list: {20 in my_list}")  # True


# =======================================
# 7. BITWISE OPERATORS
# =======================================
# - Used to perform operations on integers at the binary level.
# - Less common in high-level data science tasks but useful in specific domains.
# - Examples: & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), >> (right shift)

# Example: 6 in binary is 0110, 3 in binary is 0011
print(f"6 & 3: {6 & 3}")  # Binary 0110 & 0011 = 0010, which is 2
print(f"6 | 3: {6 | 3}")  # Binary 0110 | 0011 = 0111, which is 7


# --- End of File ---
