# =======================================
# 1. LIST BASICS
# =======================================
# - A list is a mutable, ordered sequence of items.
# - "Mutable" means the list can be changed after it is created.
# - "Ordered" means items maintain a stable position (index).
# - Created with square brackets `[]`.
# - Can contain duplicate values and mixed data types.

# An empty list
empty_list = []

# A list of integers
numbers = [1, 2, 3, 4, 5]

# A list with mixed data types
mixed_list = [1, "hello", 3.14, True, [10, 20]]


# =======================================
# 2. ACCESSING ELEMENTS (INDEXING & SLICING)
# =======================================
# - Use an integer index to get a single element (starts at 0).
# - Use slicing `[start:stop:step]` to get a sub-list.

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter"]
print(f"First planet: {planets[0]}")  # Mercury
print(f"Third planet: {planets[2]}")  # Earth
print(f"Last planet: {planets[-1]}")  # Jupiter

# Slicing
# Gets items from index 1 up to (but not including) index 4
inner_planets = planets[1:4]
print(f"Inner planets: {inner_planets}")  # ['Venus', 'Earth', 'Mars']


# =======================================
# 3. MODIFYING LISTS
# =======================================
# - Lists are mutable, so you can change their content directly.

data_points = [10, 20, 35, 40, 50]
print(f"Original data: {data_points}")

# Change a single element
data_points[2] = 30
print(f"After changing index 2: {data_points}")

# Change a range of elements
data_points[3:5] = [45, 55, 65]
print(f"After changing a slice: {data_points}")


# =======================================
# 4. ADDING AND REMOVING ELEMENTS
# =======================================
# - Common methods for adding/removing items from a list.

# --- Adding ---
# - `.append(item)`: Adds an item to the very end of the list.
# - `.insert(index, item)`: Adds an item at a specific position.
# - `.extend(iterable)`: Appends all items from another list (or any iterable).
tasks = ["wash dishes", "do laundry"]
tasks.append("buy groceries")  # ['wash dishes', 'do laundry', 'buy groceries']
tasks.insert(
    1, "pay bills"
)  # ['wash dishes', 'pay bills', 'do laundry', 'buy groceries']
tasks.extend(["call mom", "walk dog"])  # Appends two new items

# --- Removing ---
# - `.remove(value)`: Removes the first matching value (raises ValueError if not found).
# - `.pop(index)`: Removes and returns the item at an index (or the last item if blank).
# - `del list[index]`: Keyword to remove an item by index.
tasks.remove("pay bills")
last_task = tasks.pop()  # Removes and returns 'walk dog'
del tasks[0]  # Deletes 'wash dishes'
print(f"Remaining tasks: {tasks}")


# =======================================
# 5. OTHER USEFUL LIST METHODS
# =======================================
# --- Sorting and Reversing ---
# - `.sort()`: Sorts the list in-place (modifies the original).
# - `.reverse()`: Reverses the list in-place.
# - `sorted(list)`: A built-in function that returns a NEW sorted list.
numbers = [5, 1, 4, 2, 3]
print(f"\nOriginal numbers: {numbers}")

sorted_numbers = sorted(numbers)  # Returns a new sorted list
print(f"Sorted (new list): {sorted_numbers}")
print(f"Original is unchanged: {numbers}")

numbers.sort(reverse=True)  # Sorts the original list in descending order
print(f"Sorted in-place (desc): {numbers}")

# --- Searching and Counting ---
# - `.index(value)`: Returns the index of the first occurrence of a value.
# - `.count(value)`: Counts how many times a value appears.
letters = ["a", "b", "c", "a", "d", "a"]
print(f"Index of 'c': {letters.index('c')}")
print(f"Count of 'a': {letters.count('a')}")


# =======================================
# 6. COPYING LISTS (THE RIGHT WAY)
# =======================================
# - Simple assignment (`new = old`) creates a reference, NOT a copy.
# - Modifying the new list will also modify the original.
# - To create an independent copy, use `.copy()` or a full slice `[:]`.

original_list = [1, 2, 3]

# INCORRECT: This is just a reference
bad_copy = original_list
bad_copy[0] = 99
print(f"Bad copy result: {original_list}")  # Original is changed!

# CORRECT: Create a true, independent copy
correct_copy = original_list.copy()
# Alternative: correct_copy = original_list[:]
correct_copy[0] = 100
print(f"Correct copy: {correct_copy}")
print(
    f"Original is safe: {original_list}"
)  # Note: original is back to [99, 2, 3] due to the bad copy
