# ------------------------------- Complex Numbers ------------------------------- #
num = 2 + 3j
num2 = complex(2, 3)  # same as above

type(num)  # -> complex

print(num.real)  # -> 2.0
print(num.imag)  # -> 3.0


# ----------------------------- Built-in Functions ----------------------------- #
abs(-5.5)  # -> 5.5
round(5.49)  # -> 5
round(5.49, 1)  # 5.5


# -------------------------------- Enumerations -------------------------------- #
# Enum is a set of symbolic names (members) bound to unique values
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED)  # -> Color.RED
print(Color.BLUE.value)  # -> 3
print(Color(2))  # -> Color
print(Color["BLUE"])  # -> Color.BLUE

Color.GREEN.value = 1  # Won't work!

print(list(Color))  # -> [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]
print(len(Color))  # -> 3
