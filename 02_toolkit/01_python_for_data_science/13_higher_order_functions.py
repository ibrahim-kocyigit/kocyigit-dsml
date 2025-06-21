# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. What is a Higher-Order Function?
# 2. Example: Taking a Function as an Argument
# 3. Built-in Higher-Order Functions
# 4. Example: Returning a Function


# =======================================
# 1. WHAT IS A HIGHER-ORDER FUNCTION?
# =======================================
# - A function that operates on other functions.
# - It does at least one of the following:
#   1. Takes one or more functions as an argument.
#   2. Returns a function as its result.
# - This is possible because in Python, functions are "first-class citizens,"
#   meaning they can be passed around and used just like any other object (e.g., int, str, list).


# =======================================
# 2. EXAMPLE: TAKING A FUNCTION AS AN ARGUMENT
# =======================================
# - We can create our own higher-order functions to make our code more flexible.


def shout(text):
    """Converts text to uppercase with an exclamation mark."""
    return text.upper() + "!"


def whisper(text):
    """Converts text to lowercase with ellipses."""
    return text.lower() + "..."


def greet(name, formatting_function):
    """Greets a person using a provided formatting function."""
    # `formatting_function` is a function passed as an argument.
    # We call it inside this function
    formatted_greeting = formatting_function(f"Hello, {name}")
    print(formatted_greeting)


# Passing the `shout` function as an argument
greet("Alice", shout)  # HELLO, ALICE!

# Passing the `whisper` function as an argument
greet("Bob", whisper)  # hello, bob...

print("-" * 30)


# =======================================
# 3. BUILT-IN HIGHER-ORDER FUNCTIONS
# =======================================
# - `map()`, `filter()`, and `reduce()` are classic examples of built-in higher-order functions.


# --- `.map(function, iterable)` ---
# - Applies a function to every item in an iterable and returns a map object (an iterator).
print("--- Using map() ---")
words = ["python", "is", "awesome"]


# Example with a named `def` function
def get_length(word):
    """Returns the length of a word."""
    return len(word)


word_lengths_def = map(get_length, words)
print(f"Word lengths (using `def`): {list(word_lengths_def)}")

# Example with a `lambda` function
# For simple, one-off functions, a lambda is more concise.
word_lengths_lambda = map(lambda word: len(word), words)
print(f"Word lengths (using `lambda`): {list(word_lengths_lambda)}")


# --- `.filter(function, iterable)` ---
# - Filters an iterable, returning only items for which the function returns True.
print("\n--- Using filter() ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Example with a named `def` function
def is_even(num):
    """Checks if a number is even."""
    return num % 2 == 0


even_numbers_def = filter(is_even, numbers)
print(f"Even numbers (using `def`): {list(even_numbers_def)}")

# Example with a `lambda` function
even_numbers_lambda = filter(lambda num: num % 2 == 0, numbers)
print(f"Even numbers (using `lambda`): {list(even_numbers_lambda)}")


# --- `functools.reduce(function, iterable)` ---
# - Cumulatively applies a function of two arguments to the items in a sequence
#   to reduce it to a single value.
print("\n--- Using reduce() ---")
from functools import reduce


# Example with a named `def` function
def multiply(x, y):
    """Multiplies two numbers."""
    return x * y


product_def = reduce(multiply, [1, 2, 3, 4, 5])
# reduce(multiply, [1,2,3,4,5]) works like: multiply(multiply(multiply(multiply(1,2),3),4),5)
print(f"Product of numbers (using `def`): {product_def}")

# Example with a `lambda` function
product_lambda = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(f"Product of numbers (using `lambda`): {product_lambda}")

print("-" * 30)


# =======================================
# 4. EXAMPLE: RETURNING A FUNCTION
# =======================================
# - A function that creates and returns another function is called a "function factory."
# - This allows us to create specialized, configured functions on the fly.


def create_multiplier(factor):
    """
    This is a function factory. It creates and returns a new function
    that will multiply any number by the given `factor`.
    """

    def multiplier(number):
        """This is the function that gets returned."""
        return number * factor

    return multiplier  # We return the function itself, not the result of calling it.


# --- Using the function factory ---
double = create_multiplier(2)
triple = create_multiplier(3)

print("--- Using a Function Factory ---")
print(f"Double of 10: {double(10)}")
print(f"Triple of 10: {triple(10)}")
print(f"The type of `double` is: {type(double)}")  # <class 'function'>


# --- End of File ---
