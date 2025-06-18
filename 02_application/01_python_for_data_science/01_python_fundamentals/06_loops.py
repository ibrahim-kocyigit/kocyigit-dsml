# =======================================
# 1. THE `for` LOOP
# =======================================
# - Used for iterating over a sequence (e.g., list, tuple, dictionary, set, or string).
# - Executes a block of code once for each item in the sequence.

# --- Looping through a list ---
fruits = ["apple", "banana", "cherry"]
print("--- Looping through a list ---")
for fruit in fruits:
    print(f"Current fruit: {fruit}")

# --- Looping through a string ---
print("\n--- Looping through a string ---")
for letter in "Python":
    print(f"Current letter: {letter}", end=" ")  # `end=" "` prints on the same line
print("\n")

# =======================================
# 2. THE `range()` FUNCTION
# =======================================
# - A common companion to `for` loops for executing a block a specific number of times.
# - Generates a sequence of numbers.
# - `range(stop)`: From 0 up to (but not including) `stop`.
# - `range(start, stop)`: From `start` up to `stop`.
# - `range(start, stop, step)`: From `start` up to `stop`, incrementing by `step`.

print("--- Using range(5) ---")
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

print("\n--- Using range(2, 6) ---")
for i in range(2, 6):
    print(i)  # Prints 2, 3, 4, 5

print("\n--- Using range(0, 10, 2) ---")
for i in range(0, 10, 2):
    print(i)  # Prints 0, 2, 4, 6, 8


# =======================================
# 3. THE `while` LOOP
# =======================================
# - Executes a block of code as long as a specified condition is True.
# - Requires a way for the condition to become False to avoid an infinite loop.
# - Often involves a counter that is initialized before the loop and updated inside it.

print("\n--- A simple while loop ---")
count = 0
while count < 5:
    print(f"While loop count is: {count}")
    count += 1  # Crucial step to prevent an infinite loop


# =======================================
# 4. LOOP CONTROL STATEMENTS
# =======================================

# --- `break` ---
# - Terminates the current loop prematurely.
# - Execution continues at the first statement after the loop block.
print("\n--- Loop with break ---")
for i in range(10):
    if i == 5:
        print("Breaking the loop at 5")
        break
    print(i)

# --- `continue` ---
# - Skips the rest of the code inside the loop for the current iteration only.
# - The loop proceeds with the next iteration.
print("\n--- Loop with continue ---")
for i in range(5):
    if i == 2:
        print("Skipping iteration 2")
        continue
    print(f"Processing iteration {i}")


# =======================================
# 5. THE `else` CLAUSE IN LOOPS
# =======================================
# - A less common but useful feature.
# - The `else` block executes ONLY if the loop completes its entire sequence
#   without being terminated by a `break` statement.

print("\n--- Loop with else (no break) ---")
for i in range(3):
    print(f"Looping: {i}")
else:
    # This will run because the loop finished normally.
    print("The loop completed without a break.")

print("\n--- Loop with else (with break) ---")
for i in range(5):
    if i == 2:
        print("Breaking the loop")
        break
    print(f"Looping: {i}")
else:
    # This will NOT run because the loop was broken.
    print("This else block will not be executed.")


# =======================================
# 6. ITERATING OVER DICTIONARIES
# =======================================
# - You can loop through a dictionary's keys, values, or key-value pairs.

user_profile = {"name": "Eve", "role": "developer", "id": 101}
print("\n--- Iterating over dictionary items ---")

# --- .keys() (default behavior) ---
# for key in user_profile:

# --- .items() for key-value pairs (most common) ---
for key, value in user_profile.items():
    print(f"Key: {key}, Value: {value}")

# --- .values() for values only ---
# for value in user_profile.values():

# --- End of File ---
