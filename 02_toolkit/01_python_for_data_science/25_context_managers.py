# 25_context_managers.py

import time
from contextlib import contextmanager
import os

# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. What is a Context Manager?
# 2. Creating a Context Manager (Class-Based)
# 3. Creating a Context Manager (Function-Based)
# 4. Practical Use Cases


# =======================================
# 1. WHAT IS A CONTEXT MANAGER?
# =======================================
# - An object that defines a temporary context for a block of code.
# - It handles the setup of resources before the block is entered and the teardown
#   (cleanup) of those resources after the block is exited.
# - The `with` statement is the mechanism used to work with context managers.
# - Key Benefit: Guarantees that cleanup logic is ALWAYS executed, preventing resource leaks.
#
# - Familiar Example: `with open(...)` is the most common context manager.
#   It ensures the file is automatically closed when you are done with it.


# =======================================
# 2. CREATING A CONTEXT MANAGER (CLASS-BASED)
# =======================================
# - To create a context manager as a class, it must implement two special methods:
#   - `__enter__(self)`: The setup method. Called when entering the `with` block.
#     The value it returns is assigned to the variable after `as`.
#   - `__exit__(self, exc_type, exc_value, traceback)`: The teardown method.
#     Called when exiting the block. If an exception occurred, the details are passed
#     to these parameters; otherwise, they are all `None`.


class Timer:
    """A class-based context manager to measure execution time."""

    def __enter__(self):
        print("Timer started...")
        self.start_time = time.perf_counter()
        # This return value is optional. Here we return the object itself.
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.perf_counter()
        elapsed_time = self.end_time - self.start_time
        print(f"Elapsed time: {elapsed_time:.4f} seconds.")
        print("Timer finished.")
        # If we return False (or None), any exceptions will be re-raised.
        # If we returned True, it would suppress the exception.
        return False


print("--- Using a class-based context manager ---")
with Timer() as t:
    # The `t` variable holds the return value of __enter__
    print("Executing a block of code...")
    time.sleep(1)

print("-" * 30)


# =======================================
# 3. CREATING A CONTEXT MANAGER (FUNCTION-BASED)
# =======================================
# - A much simpler, more "Pythonic" way using a decorator from the `contextlib` module.
# - `@contextmanager`: Decorates a generator function.
# - The function must `yield` exactly once.
#   - Code before the `yield` is the `__enter__` logic.
#   - The value that is `yield`ed becomes the `as` variable's value.
#   - Code after the `yield` is the `__exit__` logic.
#   - Using a `try...finally` block is the best practice to ensure cleanup happens.


@contextmanager
def simple_timer():
    """A generator-based context manager for timing."""
    start = 0.0  # Initialize before the try block
    try:
        print("Simple timer started...")
        start = time.perf_counter()
        # The generator pauses here. The code inside the `with` block runs.
        yield
    finally:
        # This code is guaranteed to run when the block exits.
        end = time.perf_counter()
        print(f"Simple timer finished. Elapsed: {end - start:.4f} seconds.")


print("--- Using the function-based context manager ---")
with simple_timer():
    print("Executing another block of code...")
    time.sleep(1.5)

print("-" * 30)


# =======================================
# 4. PRACTICAL USE CASES
# =======================================

# 1. File and Network Connections: Guarantees `close()` is called.
# 2. Database Sessions: Ensures a transaction is committed or rolled back and the connection is closed.
# 3. Threading Locks: Guarantees a lock is acquired and, crucially, released.
# 4. Temporarily changing state, like the current directory.


@contextmanager
def change_dir(destination):
    """Temporarily change the current working directory."""
    cwd = None  # Initialize before the try block
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        print(f"Changed directory to: {os.getcwd()}")
        yield
    finally:
        if cwd:  # Only change back if we successfully got the original directory
            os.chdir(cwd)
            print(f"Reverted directory back to: {os.getcwd()}")


# Example of using the change_dir context manager
# with change_dir("some_other_folder"):
#     # All code here runs inside "some_other_folder"
#     print("Listing contents of new directory...")
# # After the block, we are automatically back where we started.


# --- End of File ---
