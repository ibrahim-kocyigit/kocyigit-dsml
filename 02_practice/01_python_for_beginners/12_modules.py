# ----------------------------------- Basics ----------------------------------- #
# Every Python file is a module

from utils import add  # importing add() from utils.py
from utils import subtract as minus  # importing subtract() from utils.py but as 'minus'

add(2, 4)  # -> 6
minus(4, 2)  # -> 2

# We can create folders to use as modules as long as we put empty __init__.py files in it

from my_modules import calculator
from my_modules.calculator import subtract

calculator.add(3, 5)  # -> 8
subtract(3, 3)  # -> 0


# --------------------------- Python Standard Library -------------------------- #
# Python standard library has many helpful modules such as:
# math for math utilities
# json to work with JSON
# re for regular expressions
# datetime to work with dates
# sqlite3 to use SQLite
# os for Operating System utilities
# random for random number generation
# statistics for statistics utilities
# requests to perform HTTP network requests
# http to create HTTP servers
# urllib to manage URLs

import math

print(math.pi)  # 3.141592653589793
print(math.sqrt(9))  # 3.0
