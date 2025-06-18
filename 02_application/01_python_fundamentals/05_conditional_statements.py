# =======================================
# 1. THE `if` STATEMENT
# =======================================
# - The most basic decision-making statement.
# - Executes a block of code only if its condition evaluates to True.
# - The code block must be indented (typically 4 spaces).

temperature = 35

if temperature > 30:
    # This block runs because the condition is True
    print("It's a hot day!")
    print("Remember to stay hydrated.")


# =======================================
# 2. THE `else` STATEMENT
# =======================================
# - Provides an alternative block of code to run if the `if` condition is False.
# - Catches anything that the `if` statement doesn't.

age = 17

if age >= 18:
    print("You are eligible to vote.")
else:
    # This block runs because the condition (age >= 18) is False
    print("You are not eligible to vote yet.")


# =======================================
# 3. THE `elif` (ELSE IF) STATEMENT
# =======================================
# - Allows you to check multiple, mutually exclusive conditions.
# - Python checks `elif` conditions in order, only if the preceding `if`/`elif`s were False.
# - An `if` block can have zero or more `elif` blocks.

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    # This block runs. The `if` was False, but this `elif` is True.
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"

print(f"Your grade is: {grade}")


# =======================================
# 4. NESTED `if` STATEMENTS
# =======================================
# - An `if` statement can be placed inside another `if`, `elif`, or `else` block.
# - Useful for checking secondary conditions.
# - Can lead to complex code; use with care.

is_registered = True
user_age = 25

if is_registered:
    print("Welcome, registered user.")
    # Nested if statement
    if user_age >= 18:
        print("You have access to all content.")
    else:
        print("You have access to limited content due to your age.")
else:
    print("Please register to continue.")


# =======================================
# 5. TERNARY OPERATOR (CONDITIONAL EXPRESSIONS)
# =======================================
# - A concise, one-line shorthand for a simple if-else statement.
# - Syntax: `value_if_true if condition else value_if_false`
# - Primarily used for assigning a value to a variable based on a condition.

user_role = "admin"

# Long form using if-else
# if user_role == "admin":
#     can_access = True
# else:
#     can_access = False

# Short form using ternary operator
can_access = True if user_role == "admin" else False
print(f"Can access system: {can_access}")


# =======================================
# 6. TRUTHINESS AND FALSINESS
# =======================================
# - In a boolean context, Python considers more than just True/False.
# - "Falsy" values: `False`, `None`, numeric zero (0, 0.0), and empty collections ("", [], (), {}).
# - "Truthy" values: Everything else (non-empty collections, non-zero numbers, etc.).
# - Allows writing more concise checks, e.g., `if my_list:` instead of `if len(my_list) > 0:`.

my_list = []
my_name = "Alice"

# This checks if the list is not empty
if my_list:
    print("List is not empty.")
else:
    print("List is empty.")  # This will be printed

# This checks if the string is not empty
if my_name:
    print(f"Name is: {my_name}")  # This will be printed
else:
    print("Name is not provided.")
