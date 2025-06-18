# 24_type_hints.py

# =======================================
# 1. WHAT ARE TYPE HINTS?
# =======================================
# - A way to formally indicate the expected type of variables, function parameters, and return values.
# - IMPORTANT: Python is still a dynamically typed language. These hints are NOT enforced
#   at runtime by the interpreter. They are for developers and static analysis tools.
# - Benefits:
#   1. Improved Readability: Makes code self-documenting.
#   2. Bug Prevention: Tools like `mypy` can catch type errors before execution.
#   3. Better IDE Support: Enables enhanced autocompletion and error highlighting.


# =======================================
# 2. BASIC TYPE HINTING SYNTAX
# =======================================

# --- Variable Hinting ---
# Syntax: `variable_name: type = value`
name: str = "Alice"
age: int = 30
is_active: bool = True
height: float = 1.75


# --- Function and Return Value Hinting ---
# Syntax: `def func(param: type, ...) -> return_type:`
def greet(user_name: str) -> str:
    """Greets a user, with type hints for the parameter and return value."""
    return f"Hello, {user_name}!"


greeting_message = greet(name)
print(greeting_message)
# Calling greet(123) would still RUN, but a type checker like `mypy` would flag it as an error.
print("-" * 30)


# =======================================
# 3. HINTING COMPLEX TYPES (from `typing` module)
# =======================================
# - For complex types like lists or dictionaries with specific contents, we use the `typing` module.
# - Note: Since Python 3.9+, you can use built-in types like `list` and `dict` directly.
#   We will use the modern syntax here.

# --- Hinting for Lists, Sets, and Tuples ---
# A list of integers
scores: list[int] = [90, 85, 92, 78]

# A set of strings
unique_tags: set[str] = {"python", "data", "science"}

# A tuple with a fixed structure of item types
user_record: tuple[int, str, bool] = (101, "Bob", True)


# --- Hinting for Dictionaries ---
# A dictionary with string keys and integer values
id_to_score: dict[str, int] = {"user1": 100, "user2": 85}

print("--- A function with complex type hints ---")


def process_scores(score_map: dict[str, int]) -> float:
    """Calculates the average score from a dictionary."""
    if not score_map:
        return 0.0
    return sum(score_map.values()) / len(score_map)


average_score = process_scores(id_to_score)
print(f"The average score is: {average_score}")
print("-" * 30)


# =======================================
# 4. HINTING OPTIONAL VALUES AND UNION TYPES
# =======================================
# - Used when a value could be of a specific type OR `None`.


# --- `| None` (modern syntax, Python 3.10+) ---
# This is the new, preferred way to denote an optional type.
def find_user(user_id: int) -> str | None:
    """Finds a user by ID, returning their name or None if not found."""
    if user_id in (1, 2, 3):
        return f"User_{user_id}"
    else:
        return None


# --- `from typing import Optional` (older syntax) ---
# `Optional[str]` is exactly the same as `str | None`. You will see this in older codebases.
from typing import Optional


def find_user_legacy(user_id: int) -> Optional[str]:
    # ... same logic as above ...
    pass


user = find_user(2)
if user:
    print(f"Found user: {user.upper()}")  # Type checker knows `user` is a string here
else:
    print("User not found.")

print("-" * 30)


# =======================================
# 5. TYPE ALIASES AND CALLABLES
# =======================================
# - Type Alias: A custom name for a complex type hint to improve readability.
# - Callable: A hint for something that can be called, like a function.

from typing import Callable

# --- Create a Type Alias ---
# This makes other type hints much cleaner.
Vector = list[float]
Matrix = list[Vector]


def scale_vector(scalar: float, vector: Vector) -> Vector:
    """Scales a vector by a scalar value."""
    return [scalar * item for item in vector]


# --- Hinting a Function (Callable) ---
# A callable that takes two floats and returns a float
Operation = Callable[[float, float], float]


def apply_operation(a: float, b: float, op: Operation) -> float:
    """Applies a given operation to two numbers."""
    return op(a, b)


def add(x: float, y: float) -> float:
    return x + y


def multiply(x: float, y: float) -> float:
    return x * y


result_add = apply_operation(10, 20, add)
result_mult = apply_operation(10, 20, multiply)
print(f"Result of add operation: {result_add}")
print(f"Result of multiply operation: {result_mult}")
print("-" * 30)


# =======================================
# 6. USING A STATIC TYPE CHECKER (`mypy`)
# =======================================
# - To actually check your types, you use a tool like `mypy`.
# - Installation: `pip install mypy`
# - Usage: `mypy your_script_name.py`


def calculate_length(text: str) -> int:
    return len(text)


# This line is correct
calculate_length("hello")

# This line has a type error. `mypy` will catch it!
# calculate_length(123)

print("Run `mypy 24_type_hints.py` in your terminal to check this file.")
print("Mypy will report an error on the commented-out line above.")


# --- End of File ---
