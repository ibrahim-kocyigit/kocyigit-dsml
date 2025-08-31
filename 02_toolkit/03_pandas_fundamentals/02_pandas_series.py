import pandas as pd
import numpy as np

# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. What is a Pandas Series?
# 2. Creating a Series
# 3. Series Attributes and Methods


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


# --- With a Costom Index ---
# The index should have the same number of elements as the data.
s_custom_index = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print("\nSeries with a custom index:\n", s_custom_index)


# --- From a Dictionary ---
# The dictionary keys are automatically used as the index
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
print(f"Data Type: {s_from_dict.dtype}")
print(f"Size: {s_from_dict.size}")
print(f"Shape: {s_from_dict.shape}")
