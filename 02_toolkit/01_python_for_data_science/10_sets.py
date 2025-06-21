# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. Set Basics
# 2. Adding & Removing Elements
# 3. Set Operations
# 4. Membership & Iteration
# 5. Common Use Case: Removing Duplicates
# 6. Frozenset: The Immutable Set


# =======================================
# 1. SET BASICS
# =======================================
# - A set is a mutable, unordered collection of UNIQUE, immutable items.
# - "Unordered" means items have no index or stable position.
# - "Unique" means duplicate elements are automatically removed.
# - Created with curly braces `{}` or `set()` function.
# - To create an EMPTY set, you MUST use `set()`, as `{}` creates an empty dictionary.

# --- Creation ---
# From a list with duplicates
numbers_list = [1, 2, 2, 3, 4, 3, 5]
unique_numbers = set(numbers_list)
print(f"Set from list: {unique_numbers}")  # {1, 2, 3, 4, 5}

# Direct creation
tags = {"python", "data", "science", "python"}
print(f"Tags set: {tags}")  # {'data', 'python', 'science'}

# Creating an empty set
empty_set = set()
print(f"Is empty_set a set? {isinstance(empty_set, set)}")


# =======================================
# 2. ADDING AND REMOVING ELEMENTS
# =======================================
# - Methods for modifying a set's contents.

permissions = {"read", "write"}
print(f"\nOriginal permissions: {permissions}")

# --- Adding ---
# - `.add(element)`: Adds a single element
permissions.add("execute")
print(f"After adding 'execute': {permissions}")

# - `.update(iterable)`: Adds all elements from another set, list, etc.
permissions.update(["admin", "guest", "read"])  # 'read' is a duplicate, so it's ignored
print(f"After update: {permissions}")

# --- Removing ---
# - `.remove(element)`: Removes an element. Raises KeyError if not found.
permissions.remove("guest")

# - `.discard(element)`: Safer removal. Does nothing if element is not found.
permissions.discard("sudo")  # 'sudo' is not in the set, no error is raised.
print(f"After removing: {permissions}")


# =======================================
# 3. SET OPERATIONS (THEIR SUPERPOWER)
# =======================================
# - Used to compare and combine sets, based on mathematical set theory.

developers = {"Alice", "Bob", "Charlie", "David"}
testers = {"Charlie", "David", "Eve", "Frank"}
print(f"\nDevelopers: {developers}")
print(f"Testers: {testers}")

# --- Union (`|`) ---
# - All unique members from both sets
all_staff = developers.union(testers)
# Alternative: all_staff = developers | testers
print(f"\nUnion (all staff): {all_staff}")

# --- Intersection (`&`) ---
# - Members who are in BOTH sets.
overlap = developers & testers
# Alternative: overlap = developers.intersection(testers)
print(f"Intersection (both dev & tester): {overlap}")

# --- Difference (`-`) ---
# - Members in the first set but NOT in the second.
devs_only = developers.difference(testers)
# Alternative: devs_only = developers - testers
print(f"Difference (only developers): {devs_only}")

# --- Symmetric Difference (`^`) ---
# - Members in either set, but not in both
non_overlapping_roles = developers ^ testers
# Alternative: non_overlapping_roles = developers.symmetric_difference(testers)
print(f"Symmetric Difference (exclusive roles): {non_overlapping_roles}")


# =======================================
# 4. MEMBERSHIP AND ITERATION
# =======================================
# - Checking for an item's existence is very fast in sets.
# - You can loop through a set, but the order is not guaranteed.

print("\n---Membership & Iteration ---")
print(f"Is Alice a developer? {'Alice' in developers}")

print("All testers:")
for person in testers:
    print(f" - {person}")


# =======================================
# 5. COMMON USE CASE: REMOVING DUPLICATES
# =======================================
# - The fastest way to get unique items from a list.

data_with_duplicates = [10, 20, 5, 10, 15, 20, 10, 5]
unique_data = list(set(data_with_duplicates))
print(f"\nOriginal data: {data_with_duplicates}")
print(f"Data with duplicates removed: {unique_data}")


# =======================================
# 6. FROZENSET: THE IMMUTABLE SET
# =======================================
# - The immutable version of a set. Once created, it cannot be changed.
# - Because it's immutable, it can be used as a dictionary key or as an element in another set.

immutable_set = frozenset(["read", "write"])
# immutable_set.add("execute") # This would raise an AttributeError

# Using a frozenset as a dictionary key
permission_sets = {
    immutable_set: "Standard User",
    frozenset(["read", "write", "execute"]): "Power User",
}
print(f"\nRole for {immutable_set}: {permission_sets[immutable_set]}")


# --- End of File ---
