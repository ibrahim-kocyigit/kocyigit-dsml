"""
Key Concepts:
- Arithmetic operators (matrix operations precursor)
- Comparison operators (filtering data)
- Logical operators (conditional execution)
- Membership operators (checking for values)
- Identity operators (memory efficiency checks)
- Operator precedence (critical for complex expressions)
"""

# ====================
# 1. Arithmetic Operators
# ====================
# Fundamental for numerical computing
a, b = 10, 3

print("Addition:", a + b)  # 13 (also works for lists/strings concatenation)
print("Subtraction:", a - b)  # 7
print("Multiplication:", a * b)  # 30 (also string repetition: "a"*3 → "aaa")
print("Division:", a / b)  # 3.333... (always returns float)
print("Floor Division:", a // b)  # 3 (returns int, drops remainder)
print("Modulo:", a % b)  # 1 (remainder, useful for hashing)
print("Exponent:", a**b)  # 1000 (powers, common in feature engineering)


# ====================
# 2. Comparison Operators
# ====================
# Essential for data filtering and conditions
print("\nComparison Operators:")
print("Equal:", a == b)  # False
print("Not Equal:", a != b)  # True
print("Greater Than:", a > b)  # True
print("Less Than:", a < b)  # False
print("Greater/Equal:", a >= b)  # True
print("Less/Equal:", a <= b)  # False

# Chained comparisons (readable range checks)
x = 5
print(1 < x < 10)  # True (equivalent to 1 < x and x < 10)


# ====================
# 3. Logical Operators
# ====================
# Used in conditional statements and masking
print("\nLogical Operators:")
print("AND:", True and False)  # False (both must be True)
print("OR:", True or False)  # True (either can be True)
print("NOT:", not True)  # False (inverts)


# Short-circuit evaluation ...
# ... avoids unnecessary computations ...
def check():
    print("Called!")
    return True


False and check()  # check() never executes (short-circuited)


# ... also checks conditions before dangerous operations
x = 0
x != 0 and y / x > 1  # Won't divide by zero if x is 0


# ====================
# 4. Membership Operators
# ====================
# Checking for presence in data structures
data = [10, 20, 30, 40]

print("\nMembership Operators:")
print("In:", 20 in data)  # True
print("Not In:", 50 not in data)  # True

# Works with strings (substring checks)
print("sub" in "data science")  # False


# ====================
# 5. Identity Operators
# ====================
# Checking memory location (vs value comparison)
lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
lst3 = lst1

print("\nIdentity Operators:")
print("is:", lst1 is lst2)  # False (different objects)
print("is:", lst1 is lst3)  # True (same object)
print("is not:", lst1 is not lst2)  # True

# Common pitfall with immutable types
x = 256
y = 256
print(x is y)  # True (Python caches small integers)


# ====================
# 6. Bitwise Operators
# ====================
# Used in hashing and low-level optimizations
print("\nBitwise Operators:")
print("AND:", 0b1100 & 0b1010)  # 0b1000 (8)
print("OR:", 0b1100 | 0b1010)  # 0b1110 (14)
print("XOR:", 0b1100 ^ 0b1010)  # 0b0110 (6)
print("Shift Left:", 1 << 3)  # 8 (multiply by 2^3)
print("Shift Right:", 8 >> 2)  # 2 (divide by 2^2)


# ====================
# 7. Operator Precedence
# ====================
# Critical for complex expressions
result = 5 + 3 * 2**2 / 4 - 1  # Evaluates as: 5 + ((3 * (2 ** 2)) / 4) - 1
print("\nOperator Precedence Result:", result)  # 7.0

# Recommended: Use parentheses for clarity
clear_result = 5 + ((3 * (2**2)) / 4) - 1


# ====================
# 8. Walrus Operator (:=)
# ====================
# Assignment within expressions
if (n := len(data)) > 3:
    print(f"List has {n} elements (>=3)")  # -> "List has 4 elements (>=3)"

# Useful in while loops and comprehensions


# ====================
# 9. DS-Specific Examples
# ====================
# Conditional feature engineering
temperature = 28
is_summer = True
air_con = (temperature > 25) and is_summer  # Becomes a feature (True)

# Data validation
valid = (len(data) > 0) and (None not in data)

# Efficient membership testing
features = {"age", "income", "education"}
required = {"age", "education", "email"}
missing = required - features

print(list(missing))  # -> ['email']
