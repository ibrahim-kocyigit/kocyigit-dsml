# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. Defining & Calling Functions
# 2. Parameters & Arguments
# 3. The `return` Statement
# 4. Default & Keyword Arguments
# 5. Arbitrary Arguments: *args
# 6. Arbitrary Keyword Arguments: **kwargs
# 7. Docstrings (Documentation Strings)


# =======================================
# 1. DEFINING & CALLING FUNCTIONS
# =======================================
# - A function is a named, reusable block of code that performs a specific action.
# - Defined using the `def` keyword.
# - Called using the function's name followed by parentheses `()`.
# - Promotes code organization and reusability (DRY - Don't Repeat Yourself)

# --- Defining a simple function ---
def print_separator():
    """This function prints a line of dashes."""
    print("-" * 30)


# --- Calling the function ---
print("First message.")
print_separator()
print("Second message.")


# =======================================
# 2. PARAMETERS & ARGUMENTS
# =======================================
# - Parameter: The variable name inside the function's definition.
# - Argument: The actual value sent to the function when it's called.


def greet_user(name):  # 'name' is the parameter
    """Greets a user by their name."""
    print(f"Hello, {name}")


greet_user("Ibrahim")  # 'Ibrahim' is the argument
greet_user("Sal")
print_separator()


# =======================================
# 3. THE `return` STATEMENT
# =======================================
# - Used to exit a function and send a value back to the caller.
# - A function that doesn't explicitly return a value implicitly returns `None`.


def add_numbers(a, b):
    """Adds two numbers and returns the result."""
    return a + b


sum_result = add_numbers(5, 7)
print(f"The result of the addition is: {sum_result}")


# --- Returning multiple values (as a tuple) ---
def get_user_info():
    """Returns a user's name and age."""
    name = "Ibrahim"
    age = 42
    return name, age


user_name, user_age = get_user_info()
print(f"User: {user_name}, Age: {user_age}")
print_separator()


# =======================================
# 4. DEFAULT & KEYWORD ARGUMENTS
# =======================================
# - Default Argument: A parameter with a pre-assigned value. Makes the argument optional.
# - Keyword Argument: Passing arguments by explicitly naming the parameter. Improves readability.


# 'message' is a default argument
def send_message(recipient, message="Hello", sender="System"):
    """Sends a message to a recipient."""
    print(f"To: {recipient}, From: {sender} -- Message: {message}")


send_message("David")  # Uses default values for message and sender
# To: David, From: System -- Message: Hello

send_message("Eve", "How are you?")  # Overrides the default message
# To: Eve, From: System -- Message: How are you?

send_message(message="Meeting at 5 PM", recipient="Frank")
# To: Frank, From: System -- Message: Meeting at 5 PM


# =======================================
# 5. ARBITRARY ARGUMENTS: *args
# =======================================
# - Use `*args` to pass a variable number of non-keyword (positional) arguments.
# - The function receives them as a TUPLE.


def calculate_mean(*numbers):  # 'numbers' will be a tuple
    """Calculates the mean of all provided numbers."""
    print(f"Received numbers as a tuple: {numbers}")
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


print(f"Mean of (37, 42, 73, 84): {calculate_mean(37, 42, 73, 84)}")
print_separator()


# =======================================
# 6. ARBITRARY KEYWORD ARGUMENTS: **kwargs
# =======================================
# - Use `**kwargs` to pass a variable number of keyword arguments.
# - The function receives them as a DICTIONARY


def build_profile(**user_data):  # 'user_data' will be a dictionary
    """Builds a user profile from keyword arguments."""
    print(f"Received user data as a dictionary: {user_data}")
    for key, value in user_data.items():
        print(f"- {key.title()}: {value}")


build_profile(name="Ibrahim", age=42, city="Lisbon")
print()  # prints an empty line
build_profile(name="Heidi", occupation="Data Scientist", has_pets=True)
print_separator()


# =======================================
# 7. DOCSTRINGS (DOCUMENTATION STRINGS)
# =======================================
# - A string literal as the first line in a function definition.
# - Enclosed in triple quotes """...""".
# - Standard way to document what a function does, its arguments, and what it returns.
# - Can be accessed using `help(function_name)` or `function_name.__doc__`


def get_circle_area(radius):
    """
    Calculates the area of a circle given its radius.

    Args:
        radius (float or int): The radius of the circle.

    Returns:
        float: The calculated area of the circle.
    """
    pi = 3.14159
    return pi * (radius**2)


# How to see the docstring?
help(get_circle_area)
# Or: print(get_circle_area.__doc__)
# Or: most IDEs show the docstring when you hover over the function name


# --- End of File ---
