# =======================================
# 1. ERRORS AND EXCEPTIONS
# =======================================
# - Syntax Errors: Errors in your code's structure (e.g., typos, wrong indentation) that prevent the program from even starting.
# - Exceptions: Errors that occur during the execution of the program. If unhandled, they will stop the program.
# - Examples: `ZeroDivisionError`, `ValueError`, `FileNotFoundError`, `TypeError`.
# - We use "exception handling" to manage these runtime errors gracefully.


# =======================================
# 2. THE `try...except` BLOCK
# =======================================
# - The fundamental tool for handling exceptions.
# - `try`: The code that might cause an exception goes here.
# - `except`: If an exception occurs in the `try` block, this block is executed.

print("--- Basic try...except ---")
try:
    # This code is "tried".
    numerator = 10
    denominator = 0
    result = numerator / denominator  # This will cause a ZeroDivisionError
    print("This line will not be reached.")
except:
    # This block runs because an error occurred.
    print("An error occurred! Cannot divide by zero.")

print("Program continues after the try...except block.")
print("-" * 30)


# =======================================
# 3. HANDLING SPECIFIC EXCEPTIONS
# =======================================
# - It's best practice to catch specific exceptions instead of using a bare `except:`.
# - This prevents you from accidentally hiding bugs you didn't anticipate.
# - You can have multiple `except` blocks to handle different types of errors.

print("--- Handling specific exceptions ---")
try:
    user_input = input("Enter a number: ")
    number = int(user_input)  # This can cause a ValueError
    result = 20 / number  # This can cause a ZeroDivisionError
    print(f"20 divided by your number is: {result}")

except ValueError:
    # This block only runs if the user enters something that is not a valid integer.
    print("Invalid input! Please enter a whole number.")
except ZeroDivisionError:
    # This block only runs if the user enters 0.
    print("You can't divide by zero!")
except Exception as e:
    # A general catch-all for any other unexpected errors.
    # It's good practice to log the actual error for debugging.
    print(f"An unexpected error occurred: {e}")


# =======================================
# 4. THE `else` BLOCK
# =======================================
# - An optional block that runs ONLY IF no exceptions were raised in the `try` block.
# - Useful for code that should only execute if the `try` part was successful.

print("\n--- Using the 'else' block ---")
try:
    user_number = int(input("Enter a number to divide 100 by: "))
    result = 100 / user_number
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
else:
    # This code only runs if the `try` block completed without any errors.
    print(f"Success! The result is {result}.")


# =======================================
# 5. THE `finally` BLOCK
# =======================================
# - An optional block that ALWAYS runs, no matter what.
# - It executes whether an exception occurred or not.
# - Perfect for cleanup actions like closing a file or a network connection.

print("\n--- Using the 'finally' block ---")
f = None  # Initialize file variable
try:
    f = open("some_file.txt", "r")  # This will likely cause a FileNotFoundError
    print("File opened successfully.")
except FileNotFoundError as e:
    print(f"Error: {e}")
finally:
    # This block will always execute.
    if f:
        f.close()
        print("File has been closed.")
    else:
        print("Cleanup finished, but no file was opened.")

print("-" * 30)


# =======================================
# 6. RAISING YOUR OWN EXCEPTIONS
# =======================================
# - You can deliberately trigger an exception using the `raise` keyword.
# - This is useful for enforcing rules in your own functions (input validation).


def set_age(age):
    """Sets a user's age, raising an error if the age is invalid."""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer.")
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age has been set to {age}.")


try:
    set_age(25)
    set_age(-5)  # This will trigger the ValueError
except (ValueError, TypeError) as e:
    print(f"Could not set age. Reason: {e}")
