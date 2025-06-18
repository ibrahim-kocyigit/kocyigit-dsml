# =======================================
# 1. WHAT IS A CLOSURE?
# =======================================
# - A closure is a function object that "remembers" values from the enclosing scope,
#   even after the outer function has completed execution.
# - Analogy: It's a function with a "backpack". The function carries this backpack of
#   enclosed variables with it wherever it goes.
# - We saw this pattern when creating "function factories" in the higher-order functions lesson.
#   Closures are the principle that makes them work.

# --- The 3 Criteria for a Closure ---
# 1. There must be a nested function (a function inside another function).
# 2. The nested function must refer to a variable defined in the enclosing (outer) function.
# 3. The enclosing function must return the nested function itself.


# =======================================
# 2. A SIMPLE CLOSURE EXAMPLE
# =======================================
# - Let's create a function that makes custom greeters.


def create_greeter(greeting):
    """
    The outer, enclosing function. `greeting` is its local variable.
    """

    def greeter(name):
        """
        The nested function. It refers to `greeting` from the outer scope.
        """
        # `greeting` is a "free variable" here because it's not defined locally.
        print(f"{greeting}, {name}!")

    # 3. Return the nested function
    return greeter


# --- Create instances of our closure ---
# When create_greeter("Hello") is called, the `greeter` function is created.
# It "closes over" the `greeting` variable, which has the value "Hello".
say_hello = create_greeter("Hello")

# Do the same for "Hi"
say_hi = create_greeter("Hi")

# `create_greeter` has finished executing, but the returned functions
# `say_hello` and `say_hi` STILL remember their respective `greeting` values.
print("--- Calling the closure functions ---")
say_hello("Alice")  # Output: Hello, Alice!
say_hi("Bob")  # Output: Hi, Bob!

# We can inspect the closure to prove it's holding onto the variable.
# This is for demonstration; you rarely do this in practice.
print(f"\n`say_hello` remembers: '{say_hello.__closure__[0].cell_contents}'")
print("-" * 30)


# =======================================
# 3. THE `nonlocal` KEYWORD
# =======================================
# - If you only *read* a variable from the outer scope, it works fine.
# - If you try to *reassign* it, Python creates a new local variable by default.
# - The `nonlocal` keyword tells a function that you want to work with a variable
#   from an enclosing scope, not create a new local one.


def make_counter():
    """A factory for creating counter functions."""
    count = 0  # This variable will be enclosed.

    def counter():
        # Without `nonlocal`, the next line would cause an UnboundLocalError
        # because Python would assume `count` is a new local variable.
        nonlocal count
        count += 1
        return count

    return counter


# Create a new counter instance
counter1 = make_counter()
print("--- Using a stateful closure with `nonlocal` ---")
print(f"Counter 1, 1st call: {counter1()}")  # 1
print(f"Counter 1, 2nd call: {counter1()}")  # 2
print(f"Counter 1, 3rd call: {counter1()}")  # 3

# Each counter has its own independent state (its own `count` variable).
counter2 = make_counter()
print(f"\nCounter 2, 1st call: {counter2()}")  # 1
print("-" * 30)


# =======================================
# 4. PRACTICAL USE CASES FOR CLOSURES
# =======================================
# 1. Data Hiding & Encapsulation:
#    The enclosed variables (like `count` above) are "private".
#    They can only be modified by the inner function, not from outside.
#    This avoids using a full class for simple stateful objects.

# 2. Function Factories:
#    As seen with `create_greeter` and `make_counter`.

# 3. Decorators:
#    Closures are the fundamental building block for decorators,
#    which allow us to add functionality to existing functions dynamically.
#    This will be the topic of our next lesson.

print("Why are closures useful?")
print("1. Data Hiding: The `count` variable is protected.")
print("2. Function Factories: We can create specialized functions like `say_hello`.")
print("3. Decorators: They are the foundation for our next topic!")

# --- End of File ---
