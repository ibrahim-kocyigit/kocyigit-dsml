# =======================================
# TABLE OF CONTENTS
# =======================================

#
#
# 4. Membership & Iteration
# 5. Common Use Case: Removing Duplicates
# 6. Frozenset: The Immutable Set


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
