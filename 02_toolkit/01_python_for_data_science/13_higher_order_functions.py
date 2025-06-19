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
    # We call it inside this function.
    formatted_greeting = formatting_function(f"Hello, {name}")
    print(formatted_greeting)


# Pass the `shout` function as an argument
greet("Alice", shout)

# Pass the `whisper` function as an argument
greet("Bob", whisper)

print("-" * 30)


# =======================================
# 3. BUILT-IN HIGHER-ORDER FUNCTIONS
# =======================================
# - We've already used these with lambdas, but they can take any function.


# --- `map(function, iterable)` ---
# - Applies a function to every item in an iterable.
def get_length(word):
    """Returns the length of a word."""
    return len(word)


words = ["python", "is", "awesome"]
word_lengths = map(get_length, words)
print(f"Lengths of words (using map): {list(word_lengths)}")


# --- `filter(function, iterable)` ---
# - Filters an iterable, returning only items where the function returns True.
def is_long_word(word):
    """Checks if a word has more than 5 letters."""
    return len(word) > 5


long_words = filter(is_long_word, words)
print(f"Long words (using filter): {list(long_words)}")


# --- `functools.reduce(function, iterable)` ---
# - From the `functools` module.
# - Cumulatively applies a function to items in a sequence to reduce it to a single value.
from functools import reduce


def multiply(x, y):
    """Multiplies two numbers."""
    return x * y


numbers = [1, 2, 3, 4, 5]
# reduce(multiply, numbers) works like this:
# 1. multiply(1, 2) -> 2
# 2. multiply(2, 3) -> 6
# 3. multiply(6, 4) -> 24
# 4. multiply(24, 5) -> 120
product = reduce(multiply, numbers)
print(f"Product of numbers (using reduce): {product}")
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

    return multiplier  # We return the `multiplier` function itself, not the result of calling it.


# --- Using the function factory ---
# Create a function that doubles a number
double = create_multiplier(2)
# Create a function that triples a number
triple = create_multiplier(3)

# Now `double` and `triple` are actual functions we can call
print(f"Double of 10: {double(10)}")
print(f"Triple of 10: {triple(10)}")
print(f"The type of `double` is: {type(double)}")  # <class 'function'>

# This concept is closely related to "closures," which we'll cover later.

# --- End of File ---
