import pandas as pd

# =======================================
# 1. INTRODUCTION AND SETUP
# =======================================
# - Data often comes from multiple sources and needs to be combined.
# - Pandas provides three primary ways to combine DataFrames:
#   1. `pd.concat()`: Stacking/appending DataFrames.
#   2. `pd.merge()`: SQL-style joins on common columns.
#   3. `.join()`: A convenient method for index-based joins.

# --- Setup: Create sample DataFrames for our examples ---
# Employee data
staff_df = pd.DataFrame(
    {
        "employee_id": ["E1", "E2", "E3", "E4"],
        "name": ["Alice", "Bob", "Charlie", "David"],
        "department_id": ["D1", "D2", "D1", "D3"],
    }
)

# Department data
dept_df = pd.DataFrame(
    {
        "department_id": ["D1", "D2", "D4"],
        "department_name": ["Sales", "Engineering", "Marketing"],
    }
)

# Salary data
salary_df = pd.DataFrame(
    {"employee_id": ["E1", "E2", "E3", "E4"], "salary": [70000, 80000, 65000, 90000]}
)

print("--- Sample DataFrames ---")
print("Staff DataFrame:\n", staff_df)
print("\nDepartment DataFrame:\n", dept_df)
print("\nSalary DataFrame:\n", salary_df)
print("-" * 30)


# =======================================
# 2. CONCATENATING DATAFRAMES (`pd.concat`)
# =======================================
# - Concatenation "stacks" DataFrames on top of each other (axis=0)
#   or side-by-side (axis=1). It's primarily for combining data with the same structure.

print("--- Concatenating DataFrames ---")
# --- Vertical Concatenation (axis=0) ---
new_staff_df = pd.DataFrame(
    {"employee_id": ["E5"], "name": ["Eve"], "department_id": ["D2"]}
)
all_staff = pd.concat([staff_df, new_staff_df], ignore_index=True)
# `ignore_index=True` creates a new, clean index for the combined DataFrame.
print("Vertically concatenated staff data:\n", all_staff)
print("-" * 30)


# =======================================
# 3. MERGING DATAFRAMES (`pd.merge`)
# =======================================
# - `pd.merge()` is the primary tool for combining DataFrames based on the
#   values in common columns, like a JOIN in SQL.

print("--- Merging DataFrames (SQL-style Joins) ---")

# --- Inner Join (Default) ---
# - Keeps only the rows where the key ('department_id') exists in BOTH DataFrames.
# - Notice 'David' (D3) and 'Marketing' (D4) are dropped.
inner_join = pd.merge(staff_df, dept_df, on="department_id", how="inner")
print("Inner Join:\n", inner_join)


# --- Outer Join ---
# - Keeps ALL rows from both DataFrames, filling with `NaN` where data is missing.
# - Notice 'David' and 'Marketing' are now included.
outer_join = pd.merge(staff_df, dept_df, on="department_id", how="outer")
print("\nOuter Join:\n", outer_join)


# --- Left Join ---
# - Keeps ALL rows from the LEFT DataFrame (`staff_df`) and only matching rows from the right.
# - 'David' is kept, but his department_name is NaN. 'Marketing' is dropped.
left_join = pd.merge(staff_df, dept_df, on="department_id", how="left")
print("\nLeft Join:\n", left_join)


# --- Right Join ---
# - Keeps ALL rows from the RIGHT DataFrame (`dept_df`) and only matching rows from the left.
# - 'Marketing' is kept. 'David' is dropped.
right_join = pd.merge(staff_df, dept_df, on="department_id", how="right")
print("\nRight Join:\n", right_join)
print("-" * 30)


# =======================================
# 4. JOINING DATAFRAMES (`.join`)
# =======================================
# - `.join()` is a convenient method for merging that works on the DataFrames' indices.
# - It performs a left join by default.
# - It's a quick alternative to `merge` when the join key is the index.

print("--- Joining DataFrames on Index ---")
# Let's set the index to the column we want to join on
staff_indexed = staff_df.set_index("employee_id")
salary_indexed = salary_df.set_index("employee_id")

print("Staff DataFrame (indexed):\n", staff_indexed)
print("\nSalary DataFrame (indexed):\n", salary_indexed)

# Join the two DataFrames on their common index
staff_with_salary = staff_indexed.join(salary_indexed)
print("\nJoined staff and salary data:\n", staff_with_salary)

# Note: `pd.merge` can also join on indices using `left_index=True` and `right_index=True`.
# `merge` is the more powerful and flexible function overall.
