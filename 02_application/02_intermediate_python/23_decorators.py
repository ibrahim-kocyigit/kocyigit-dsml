import time
import functools  # Needed for functools.wraps

# =======================================
# 1. WHAT ARE DECORATORS?
# =======================================
# - A decorator is a function that takes another function as input,
#   adds some functionality to it (by "wrapping" it), and returns the modified function.
# - It allows you to extend the behavior of functions without permanently modifying their code.
# - Decorators are a practical application of Higher-Order Functions and Closures.
# - The syntax for using them is `@decorator_name`.


# =======================================
# 2. THE ANATOMY OF A DECORATOR
# =======================================
# - A decorator is a callable that returns a callable.
# - Let's build one from scratch to understand the pattern.


def logger_decorator(original_function):
    """A decorator that logs when a function is called."""

    # A decorator returns a new function, usually called a "wrapper".
    # This wrapper function is a closure; it has access to `original_function`.
    def wrapper(*args, **kwargs):
        # `*args` and `**kwargs` allow our wrapper to accept any arguments,
        # making it compatible with any function.

        print(f"--- Calling function: '{original_function.__name__}' ---")

        # Call the original function, passing along the arguments.
        result = original_function(*args, **kwargs)

        print(f"--- Function '{original_function.__name__}' finished. ---")

        # Return the result of the original function call.
        return result

    # The decorator returns the wrapper function.
    return wrapper


# =======================================
# 3. APPLYING DECORATORS
# =======================================


# --- Method 1: The Manual Way ---
def say_hello(name):
    print(f"Hello, {name}!")


# We are manually "decorating" our function by passing it to the decorator.
# The `decorated_say_hello` variable now holds the `wrapper` function.
decorated_say_hello = logger_decorator(say_hello)
decorated_say_hello("Alice")
print("-" * 30)


# --- Method 2: The Pythonic Way with `@` Syntactic Sugar ---
# The `@` symbol is just a cleaner, more readable way to do the exact same thing as above.
# `@logger_decorator` is equivalent to `say_goodbye = logger_decorator(say_goodbye)`


@logger_decorator
def say_goodbye(name):
    print(f"Goodbye, {name}!")


say_goodbye("Bob")
print("-" * 30)


# =======================================
# 4. PRESERVING METADATA WITH `functools.wraps`
# =======================================
# - Problem: Decorators replace the original function with a wrapper. This can hide
#   the original function's name, docstring, and other metadata.
# - Solution: Use `@functools.wraps` inside your decorator.


def timer_decorator(original_function):
    """A decorator to measure the execution time of a function."""

    @functools.wraps(original_function)  # This is the key!
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = original_function(*args, **kwargs)
        end_time = time.perf_counter()
        print(
            f"Function '{original_function.__name__}' took {end_time - start_time:.4f} seconds."
        )
        return result

    return wrapper


@timer_decorator
def process_data(size):
    """A sample function that simulates some work."""
    print(f"Processing {size} data points...")
    time.sleep(size)  # Simulate work by sleeping
    return "Done"


# Check the function's metadata
print(
    f"Function name: {process_data.__name__}"
)  # Without @wraps, this would be 'wrapper'
print(f"Docstring: {process_data.__doc__}")  # Without @wraps, this would be None

# Call the decorated function
process_data(1)
print("-" * 30)


# =======================================
# 5. DECORATORS WITH ARGUMENTS
# =======================================
# - To create a decorator that accepts its own arguments, you need an extra layer of nesting.
# - It's a function that takes arguments and *returns a decorator*.


def repeat(num_times):
    """A decorator factory. Returns a decorator that repeats a function call."""

    def decorator_repeat(original_function):
        @functools.wraps(original_function)
        def wrapper(*args, **kwargs):
            total_result = None
            for _ in range(num_times):
                total_result = original_function(*args, **kwargs)
            return total_result

        return wrapper

    return decorator_repeat


# The `@` syntax now calls `repeat(3)`, which returns the actual decorator.
@repeat(num_times=3)
def greet(name):
    """Greets a person."""
    print(f"Hello again, {name}!")


greet("Charlie")
