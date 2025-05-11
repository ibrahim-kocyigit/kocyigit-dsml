# ---------------------------- Assignment Operators ---------------------------- #
var = 10
var += 1  # var = var + 1
var -= 1  # var = var - 1
var *= 1  # var = var * 1
var /= 1  # var = var / 1
var //= 1  # var = var // 1
var %= 1  # var = var % 1


# ---------------------------- Arithmetic Operators ---------------------------- #
# From highest to lowers precedence:
print(2**3)  # Exponent -> 8
print(22 % 8)  # Modulus/Remainder -> 6
print(22 // 8)  # Integer division -> 2
print(8 / 2)  # Division -> 4.0
print(3 * 3)  # Multiplication -> 9
print(5 - 2)  # Subtraction -> 3
print(5 + 2)  # Addition -> 7


# ---------------------------- Comparison Operators ---------------------------- #
"""
==	Equal to
!=	Not equal to
<	Less than
>	Greater Than
<=	Less than or Equal to
>=	Greater than or Equal to
"""

print("Hello" == "hello")  # -> False
print(42 == 42.0)  # -> True
print(42 == "42")  # -> False


# ----------------------------- Boolean Operators ----------------------------- #
print(True and True)  # -> True
print(True and False)  # -> False
print(False and True)  # -> False
print(False and False)  # -> False

print(True or True)  # -> True
print(True or False)  # -> True
print(False or True)  # -> True
print(False or False)  # -> False

print(not True)  # -> False
print(not False)  # -> True

# `or` operator returns the first True value
print("hi" or "hey")  # -> 'hi'
print(0 == 3 or "Hello")  # -> "Hello"

# `and` operator evaluates the second argument only if the first argument is True
print(0 != 3 and "Hi there!")  # -> "Hi there!"
print("Hello everyone!" or "What's up?")  # -> "Hello everyone!"


# ----------------------------- is & in Operators ------------------------------ #
# `is` is the identity operator. returns 'True' if both are the same objects
print(dict is dict)  # -> True

# `in` is the membership operator. Tells if a value is contained within a list or another sequence
exam_scores = [34, 46, 67]
print(34 in exam_scores)  # -> True


# ------------------------------ Ternary Operator ------------------------------ #
# Allows us to quickly define a conditional
def is_adult(age):
    return True if age >= 18 else False


is_adult(15)  # -> False
is_adult(25)  # -> True
