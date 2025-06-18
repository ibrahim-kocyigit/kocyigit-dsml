import pandas as pd
import numpy as np

# =======================================
# 1. WHAT IS A PANDAS SERIES?
# =======================================
# - A Series is the fundamental 1-D data structure in Pandas.
# - It's like a single column in a spreadsheet or a NumPy array with an explicit index.
# - A Series consists of two main components:
#   1. The data (values), which is a NumPy array.
#   2. The index, which labels the data.


# =======================================
# 2. CREATING A SERIES
# =======================================
print("--- Creating a Series ---")

# --- From a Python List ---
# Pandas creates a default integer index automatically.
s_from_list = pd.Series([10, 20, 30, 40])
print("Series from a list:\n", s_from_list)


# --- With a Custom Index ---
# The index should have the same number of elements as the data.
s_custom_index = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print("\nSeries with a custom index:\n", s_custom_index)


# --- From a Dictionary ---
# The dictionary keys are automatically used as the index.
data_dict = {"New York": 8.4, "Los Angeles": 3.9, "Chicago": 2.7}
s_from_dict = pd.Series(data_dict)
print("\nSeries from a dictionary (population in millions):\n", s_from_dict)
print("-" * 30)


# =======================================
# 3. SERIES ATTRIBUTES AND METHODS
# =======================================
print("--- Series Attributes ---")
print(f"Data values (as a NumPy array): {s_from_dict.values}")
print(f"Index object: {s_from_dict.index}")
print(f"Data type: {s_from_dict.dtype}")
print(f"Size: {s_from_dict.size}")
print(f"Shape: {s_from_dict.shape}")

# You can also name a Series
s_from_dict.name = "City Populations"
print("\nNamed Series:\n", s_from_dict)

# The .describe() method gives a quick statistical summary
print("\nStatistical summary with .describe():\n", s_from_dict.describe())
print("-" * 30)


# =======================================
# 4. INDEXING AND SELECTION
# =======================================
print("--- Indexing and Selection ---")
print("Original Series:\n", s_from_dict)

# --- Selection by Label ---
# Use the index label. `.loc` is the explicit and preferred way.
print(f"\nPopulation of Chicago: {s_from_dict['Chicago']}")
print(f"Using .loc['Chicago']: {s_from_dict.loc['Chicago']}")

# --- Selection by Position ---
# Use the integer position. `.iloc` is the explicit and preferred way.
print(f"\nFirst element using .iloc[0]: {s_from_dict.iloc[0]}")

# --- Slicing ---
# Slicing with labels is INCLUSIVE of the end label.
print(
    "\nSlicing with labels ('New York':'Chicago'):\n",
    s_from_dict.loc["New York":"Chicago"],
)

# Slicing with integer positions is EXCLUSIVE of the end position.
print("\nSlicing with positions (0:2):\n", s_from_dict.iloc[0:2])

# --- Conditional Selection (Boolean Indexing) ---
# Get cities with population > 3 million
print("\nCities with population > 3M:\n", s_from_dict[s_from_dict > 3])
print("-" * 30)


# =======================================
# 5. VECTORIZED OPERATIONS & INDEX ALIGNMENT
# =======================================
# - Because Series are built on NumPy, they support fast, vectorized operations.
# - A key feature of Pandas is its automatic index alignment.

# --- Vectorized Operations ---
print("--- Vectorization & Alignment ---")
print("Original populations:\n", s_from_dict)
print("\nPopulations doubled:\n", s_from_dict * 2)


# --- Index Alignment ---
# When you perform an operation between two Series, Pandas aligns the data
# based on the index labels.
s1 = pd.Series([1, 2, 3], index=["a", "b", "c"])
s2 = pd.Series([10, 20, 30], index=["b", "c", "d"])

print("\nSeries s1:\n", s1)
print("Series s2:\n", s2)

# The result contains the sum for matching labels ('b', 'c')
# and `NaN` (Not a Number) for labels that don't exist in both ('a', 'd').
s_sum = s1 + s2
print("\nSum of s1 and s2 (with alignment):\n", s_sum)
