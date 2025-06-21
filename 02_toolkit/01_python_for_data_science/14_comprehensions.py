# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. What are Comprehensions?
# 2. List Comprehensions
# 3. Dictionary Comprehensions
# 4. Set Comprehensions
# 5. Conditional Expressions (if/else) in Comprehensions
# 6. A Note on Generator Expressions


# =======================================
# 1. WHAT ARE COMPREHENSIONS?
# =======================================
# - A concise, "Pythonic" way to create a new sequence (list, dict, set) from an existing one.
# - They combine a `for` loop, and optionally an `if` condition, into a single line.
# - Often more readable and performant than an equivalent `for` loop.


# =======================================
# 2. LIST COMPREHENSIONS (MOST COMMON)
# =======================================
# - Syntax: `[expression for item in iterable]`
# - Syntax with filter: `[expression for item in iterable if condition]`

# --- Example 1: Basic List Comprehension ---
# Goal: Create a list of the squares of numbers from 0 to 9.

# Using a standard `for` loop
squares_loop = []
for i in range(10):
    squares_loop.append(i * i)

# Using a list comprehension
squares_comp = [i * i for i in range(10)]
print(f"Squares (from loop):         {squares_loop}")
print(f"Squares (from comprehension):  {squares_comp}")
print("-" * 30)

# --- Example 2: List Comprehension with a Condition ---
# Goal: Create a list of even numbers from an existing list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using a for loop with an if statement
evens_loop = []
for num in numbers:
    if num % 2 == 0:
        evens_loop.append(num)

# Using a list comprehension with an `if` filter
evens_comp = [num for num in numbers if num % 2 == 0]

print(f"Even numbers (from loop):        {evens_loop}")
print(f"Even numbers (from comprehension): {evens_comp}")
print("-" * 30)


# =======================================
# 3. DICTIONARY COMPREHENSIONS
# =======================================
# - Similar to list comprehensions but create dictionaries
# - Syntax: `{key_expression: value_expression for item in iterable}`

# --- Example 1: Create a dictionary of numbers and their squares ---
squared_dict = {x: x**2 for x in range(5)}
# Result: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(f"Squared dictionary: {squared_dict}")

# --- Example 2: Create a dictionary from two lists ---
keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]

profile_dict = {keys[i]: values[i] for i in range(len(keys))}
# Result: {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(f"Profile dictionary: {profile_dict}")
print("-" * 30)

# - Note: A better way to create a dictionary from two lists is to use the `zip()` function
#   which will be covered in the next file.

# =======================================
# 4. SET COMPREHENSIONS
# =======================================
# - Similar to list comprehensions but create sets, automatically handling uniqueness.
# - Syntax: `{expression for item in iterable}`

# Goal: Get the unique first letters from a list of words.
words = ["apple", "banana", "apricot", "blueberry", "cherry"]

unique_first_letters = {word[0] for word in words}
# Result: {'a', 'c', 'b'} (order may vary)
print(f"Unique first letters: {unique_first_letters}")
print("-" * 30)


# =======================================
# 5. CONDITIONAL EXPRESSIONS (if-else) IN COMPREHENSIONS
# =======================================
# - You can use a ternary `if-else` on the expression part of the comprehension.
# - This TRANSFORMS items differently based on a condition, unlike the `if` filter which REMOVES items.
# - Syntax: `[value_if_true if condition else value_if_false for item in iterable]`

# Goal: Create a list of y-hats based on the results of a sigmoid function
sigmoid_results = [0.2, 0.3, 0.7, 0.4, 0.4, 0.9, 0.8, 0.1]
is_spam = [1 if result > 0.5 else 0 for result in sigmoid_results]
print(f"Predictions for is_spam: {is_spam}")
print("-" * 30)


# =======================================
# 6. A NOTE ON GENERATOR EXPRESSIONS
# =======================================
# - Syntax: `(expression for item in iterable)` (uses parentheses)
# - Looks like a list comprehension but does NOT build the full list in memory.
# - It creates a "generator" object, which yields items one by one on demand.
# - Extremely memory-efficient for very large sequences.

# Create a generator object for squares of numbers up to 1 billion.
# A list comprehension would crash your computer, but a generator is fine.
large_squares_gen = (x * x for x in range(1_000_000_000))

# The generator hasn't calculated anything yet. It just knows how to.
print(large_squares_gen)  # <generator object <genexpr> at 0x111a30ee0>

# You can iterate over it, and it will produce values as needed.
# For example, let's get the first 5 values.
print("First 5 values from the generator:")
for i in range(5):
    print(next(large_squares_gen))


# --- End of File ---
