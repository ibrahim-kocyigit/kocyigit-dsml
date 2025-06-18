# =======================================
# 1. THE `enumerate()` FUNCTION
# =======================================
# - Solves a common problem: needing both the index and the value of an item during a loop.
# - It adds a counter to an iterable and returns it as an enumerate object.
# - Each item it yields is a tuple of (index, value).
# - Syntax: `enumerate(iterable, start=0)`

# --- The "Old Way" (manual counter) ---
planets = ["Mercury", "Venus", "Earth", "Mars"]
i = 0
print("--- Looping the old way ---")
for planet in planets:
    print(f"Index {i}: {planet}")
    i += 1

# --- The "Pythonic Way" with `enumerate()` ---
print("\n--- Looping with enumerate ---")
for index, planet in enumerate(planets):
    print(f"Index {index}: {planet}")


# --- Changing the start index ---
# Use the `start` argument to begin counting from a different number (e.g., 1).
print("\n--- Enumerate starting from 1 ---")
for rank, planet in enumerate(planets, start=1):
    print(f"Rank {rank}: {planet}")

print("-" * 30)


# =======================================
# 2. THE `zip()` FUNCTION
# =======================================
# - Used to iterate over two or more iterables in parallel.
# - It creates an iterator that aggregates elements from each of the iterables.
# - Each item it yields is a tuple containing one element from each list.
# - Important: `zip` stops as soon as the SHORTEST iterable is exhausted.

students = ["Alice", "Bob", "Charlie", "David"]
grades = [85, 92, 78]
courses = ("Math", "Science", "History", "Art")

# --- Zipping multiple lists together ---
print("--- Zipping students and grades ---")
zipped_data = zip(students, grades)
# We convert the zip object to a list to see its contents
print(f"Zipped object as a list: {list(zipped_data)}")

# Zipping is best used directly in a for loop
print("\n--- Looping with zip ---")
for student, grade, course in zip(students, grades, courses):
    # The loop stops after Charlie, because the `grades` list has only 3 items.
    # David is ignored.
    print(f"{student} scored {grade} in {course}.")

print("-" * 30)


# =======================================
# 3. UNZIPPING WITH `zip(*)`
# =======================================
# - The `zip` function can also be used to "unzip" a sequence.
# - This is a common idiom using the asterisk `*` operator (splat operator).
# - It effectively transposes a list of tuples.

data_pairs = [("x1", 10), ("x2", 20), ("x3", 30)]
print(f"Original data pairs: {data_pairs}")

# Unzip the pairs into separate sequences
labels, values = zip(*data_pairs)

# The result is two tuples
print(f"Unzipped labels: {labels}")
print(f"Unzipped values: {values}")
print("-" * 30)


# =======================================
# 4. COMBINING `zip` AND `enumerate`
# =======================================
# - You can combine these functions to handle more complex looping scenarios cleanly.

# Goal: Print the rank, student, and grade.
student_names = ["Eve", "Frank", "Grace"]
student_scores = [95, 88, 100]

print("--- Combining enumerate and zip ---")
# First, zip the two lists together
zipped_students = zip(student_names, student_scores)

# Then, enumerate the result of the zip
for rank, (name, score) in enumerate(zipped_students, start=1):
    # Note: We unpack the tuple from zip `(name, score)` directly in the loop signature.
    print(f"Rank {rank}: {name} scored {score}.")

# --- End of File ---
