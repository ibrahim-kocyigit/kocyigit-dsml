# --------------------------------- Variables ---------------------------------- #
name = "Beau"
age = 39
pi = 3.14
my_name = "Ibrahim"
NAME = "Constant"

# cannot start with a number
1st_name = "Ibrahim" # SyntaxError: invalid decimal literal

# cannot use Python keywords as variables

if = "ibrahim" # -> SyntaxError: invalid syntax 


# ------------------------- Expressions and Statements ------------------------- #
# Expression returns a value
"Ibrahim" # is an expression, returns "Ibrahim"

# Statement is an operation on a value
name = "Ibrahim" # is an operation: 'assignment to a variable'
print(name) 

# A program is formed by a series of statements.
# This is a program:
name = input("Please enter your name: ")
print(f"Hell0 {name}")


# ---------------------------------- Comments ---------------------------------- #
# This is a comment line.
name = "Ibrahim" # This is an inline comment. 
'''
This is a comment
written in
more than just one line
'''

# --------------------------------- Data Types --------------------------------- #
name = "Ibrahim"
lucky_number = 8
pi = 3.14

type(name) # -> str (string)
type(lucky_number) # -> int (integer)
type(pi) # -> float (floating number)

print(type(name) == str) # -> True
print(isinstance(lucky_number, float)) # -> False

lucky_number = float(lucky_number) # Converting to float
print(lucky_number) # -> 8.0
print(isinstance(lucky_number, float)) # True

# Casting
age = "42"
age = int(age)
print(isinstance(age, int)) # True

text = "ibrahim"
text = int(text) # ValueError: invalid literal for int() with base 10: 'ibrahim'

# Other data types
complex # for complex numbers
bool # for booleans (True or False)
list # for lists
tuple # for tuples
range # for ranges
dict # for dictionaries
set # for sets