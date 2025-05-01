# ----- Math Operators (From highest to lowers precedence) ----- #

2**3  # Exponent -> 8
22 % 8  # Modulus/Remainder -> 6
22 // 8  # Integer division -> 2
8 / 2  # Division -> 4.0
3 * 3  # Multiplication -> 9
5 - 2  # Subtraction -> 3
5 + 2  # Addition -> 7


# --------------- Augmented Assignment Operators --------------- #

var = 10
var += 1  # var = var + 1
var -= 1  # var = var - 1
var *= 1  # var = var * 1
var /= 1  # var = var / 1
var //= 1  # var = var // 1
var %= 1  # var = var % 1


# --------------------- Test of Emptiness ---------------------- #
a = [1, 2, 3]

# Bad way:
if len(a) > 0:
    print("The list is not empty!")

# Good way:
if a:  # If a were empty, this was going to evaluate to "False"
    print("The list is not empty!")
