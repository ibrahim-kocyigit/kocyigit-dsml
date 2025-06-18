import pandas as pd
import numpy as np

# =======================================
# 1. WHAT IS A PANDAS DATAFRAME?
# =======================================
# - A DataFrame is the primary data structure in Pandas.
# - It is a 2-dimensional, size-mutable, tabular data structure with labeled
#   axes (rows and columns).
# - Analogies: A spreadsheet, an SQL table, or a dictionary of Series objects.
# - It is composed of three main parts: the data, the index, and the columns.


# =======================================
# 2. CREATING A DATAFRAME
# =======================================
print("--- Creating a DataFrame ---")

# --- From a Dictionary of Lists (most common) ---
# The dictionary keys become column names. All lists must be the same length.
data_dict = {
    "City": ["Söke", "İzmir", "İstanbul", "Ankara"],
    "Population": [123_301, 4_479_525, 15_655_924, 5_803_482],
    "Region": ["Aegean", "Aegean", "Marmara", "Anatolia"],
}
df_from_dict = pd.DataFrame(data_dict)
print("DataFrame from a dictionary of lists:\n", df_from_dict)


# --- From a 2D NumPy Array ---
# You must provide the column and index labels separately.
data_np = np.random.randint(80, 100, size=(4, 3))  # 4x3 array of random scores
df_from_np = pd.DataFrame(
    data_np,
    index=["Alice", "Bob", "Charlie", "David"],
    columns=["Math", "Science", "History"],
)
print("\nDataFrame from a NumPy array:\n", df_from_np)
print("-" * 30)


# =======================================
# 3. ESSENTIAL DATAFRAME ATTRIBUTES
# =======================================
print("--- Essential Attributes ---")
print("Using the DataFrame created from the dictionary:")

# .index: The labels for the rows
print(f"\nIndex: {df_from_dict.index}")

# .columns: The labels for the columns
print(f"Columns: {df_from_dict.columns}")

# .dtypes: The data type of each column
print(f"\nData types of each column (dtypes):\n{df_from_dict.dtypes}")

# .shape: A tuple of (number of rows, number of columns)
print(f"\nShape: {df_from_dict.shape}")

# .values: The data as a 2D NumPy array
print(f"\nValues (as a NumPy array):\n{df_from_dict.values}")
print("-" * 30)


# =======================================
# 4. INSPECTING DATA (ESSENTIAL METHODS)
# =======================================
print("--- Inspecting Data ---")
print("Using the DataFrame created from the NumPy array:")

# .head(n): Returns the first `n` rows (default is 5).
print("\nFirst 2 rows with .head(2):\n", df_from_np.head(2))

# .tail(n): Returns the last `n` rows.
print("\nLast 2 rows with .tail(2):\n", df_from_np.tail(2))

# .info(): Provides a concise summary of the DataFrame.
# This is often the first method you call after loading data.
print("\nConcise summary with .info():")
df_from_np.info()

# .describe(): Generates descriptive statistics for numerical columns.
print("\nStatistical summary with .describe():\n", df_from_np.describe())
print("-" * 30)


# =======================================
# 5. BASIC COLUMN OPERATIONS
# =======================================
print("--- Basic Column Operations ---")
print("Original DataFrame:\n", df_from_dict)

# --- Selecting a Single Column (returns a Series) ---
# Bracket notation is preferred as it's more robust.
city_series = df_from_dict["City"]
print("\nSelecting the 'City' column:\n", city_series)
print(f"Type of the selection: {type(city_series)}")

# --- Selecting Multiple Columns (returns a DataFrame) ---
# Pass a list of column names.
subset_df = df_from_dict[["City", "Region"]]
print("\nSelecting the 'City' and 'Region' columns:\n", subset_df)

# --- Adding a New Column ---
# Add a new column by simple assignment.
df_from_dict["Is_Metropolitan"] = df_from_dict["Population"] > 1_000_000
print("\nDataFrame with new 'Is_Metropolitan' column:\n", df_from_dict)

# --- Deleting a Column ---
# Use the `del` keyword for in-place deletion.
del df_from_dict["Region"]
print("\nDataFrame after deleting 'Region' column:\n", df_from_dict)
