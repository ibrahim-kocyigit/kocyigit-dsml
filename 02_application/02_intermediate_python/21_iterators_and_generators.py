# =======================================
# 1. THE ITERATION PROTOCOL
# =======================================
# - The foundation of how `for` loops work in Python.
# - Iterable: An object that can be looped over (e.g., list, tuple, string).
#   Technically, any object with an `__iter__()` method.
# - Iterator: An object that represents a stream of data and "remembers" its position.
#   It must have a `__next__()` method.
#
# - How a `for` loop works:
#   1. It calls `iter()` on the iterable to get an iterator.
#   2. On each loop, it calls `next()` on the iterator to get the next item.
#   3. When `next()` raises a `StopIteration` exception, the loop ends.

# --- Manually simulating a `for` loop ---
my_list = [10, 20, 30]
print("--- Manually iterating ---")
# 1. Get an iterator from the iterable list
my_iterator = iter(my_list)
print(f"Iterator object: {my_iterator}")

# 2. Call next() to get items one by one
print(next(my_iterator))  # 10
print(next(my_iterator))  # 20
print(next(my_iterator))  # 30
# print(next(my_iterator))  # This would raise StopIteration
print("-" * 30)


# =======================================
# 2. CUSTOM ITERATORS (THE CLASS-BASED WAY)
# =======================================
# - You can create your own iterators by defining a class with `__iter__` and `__next__` methods.
# - This is powerful but often more verbose than necessary.


class Countdown:
    """A custom iterator to count down from a number."""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        # The __iter__ method must return the iterator object itself.
        return self

    def __next__(self):
        if self.current < 0:
            # Signal that the iteration is complete.
            raise StopIteration
        else:
            # Return the current value and decrement for the next call.
            value = self.current
            self.current -= 1
            return value


print("--- Using a custom iterator class ---")
# Now our Countdown object is iterable
for number in Countdown(5):
    print(number)
print("-" * 30)


# =======================================
# 3. GENERATORS (THE SIMPLE WAY)
# =======================================
# - A much simpler way to create iterators.
# - A generator is a function that uses the `yield` keyword to return values one at a time.
# - When a function contains `yield`, it automatically becomes a generator function.
# - It "pauses" at each `yield`, sends back the value, and waits for the next call.
#   This "state" is automatically saved.


def countdown_generator(start):
    """A generator function that yields numbers counting down."""
    print("(Generator starting...)")
    current = start
    while current >= 0:
        yield current  # Pauses here and sends `current` back to the loop
        current -= 1
    print("(Generator finished.)")


print("--- Using a generator function ---")
# Calling the function returns a generator object (which is an iterator)
countdown_gen_obj = countdown_generator(5)
print(f"Generator object: {countdown_gen_obj}")

# We can iterate over it just like any other iterable
for number in countdown_gen_obj:
    print(number)
print("-" * 30)


# =======================================
# 4. GENERATOR EXPRESSIONS
# =======================================
# - A concise, one-line syntax for creating generators.
# - Looks just like a list comprehension but with parentheses `()` instead of square brackets `[]`.
# - They do not build a full list in memory, making them extremely memory-efficient.

# A list comprehension (builds a full list in memory)
list_comp = [x * x for x in range(10)]

# A generator expression (creates a generator object, values are created on-demand)
gen_exp = (x * x for x in range(10))

print(f"List comprehension: {list_comp}")
print(f"Generator expression object: {gen_exp}")

# You can iterate over the generator expression
print("Values from generator expression:")
for value in gen_exp:
    print(value, end=" ")
print("\n")


# =======================================
# 5. WHY USE GENERATORS?
# =======================================
# - Memory Efficiency: The main advantage. They produce items lazily (one by one)
#   and don't store the entire sequence in memory. Perfect for huge files or infinite sequences.
# - Simplicity: Generator functions are much easier and cleaner to write than custom iterator classes.


def read_large_logfile(filepath):
    """A generator to read a large file line by line without loading it all into memory."""
    with open(filepath, "r") as f:
        for line in f:
            # Imagine processing each line here
            yield line.strip()


# If you had a large log file, you could process it like this:
# for log_entry in read_large_logfile("very_large_log.txt"):
#     if "ERROR" in log_entry:
#         print(log_entry)
