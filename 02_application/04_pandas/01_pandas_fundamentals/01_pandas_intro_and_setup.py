# =======================================
# 1. WHAT IS PANDAS?
# =======================================
# - Pandas is an open-source Python library for data manipulation and analysis.
# - Its name is derived from "Panel Data," an econometrics term for multidimensional data sets.
# - It is built on top of NumPy, meaning it leverages NumPy's performance and
#   efficiency for numerical operations.
# - It is the single most important tool for practical, real-world data analysis in Python.


# =======================================
# 2. INSTALLATION AND IMPORT CONVENTION
# =======================================
# - To install Pandas, run this command in your terminal:
#   `pip install pandas`
#   (It's also included by default in distributions like Anaconda).
#
# - The universal community convention for importing Pandas is:
import pandas as pd

# - Since Pandas is built on NumPy, it's standard practice to import NumPy as well.
import numpy as np


# =======================================
# 3. WHY USE PANDAS?
# =======================================
# - Pandas excels at handling tabular data (data organized in rows and columns).
# - Key Features:
#   1. DataFrame Object: A powerful, flexible 2D data structure for handling
#      and manipulating table-like data.
#   2. Data I/O: Tools for easily reading and writing data from various formats
#      (CSV, Excel, SQL databases, JSON, etc.).
#   3. Data Cleaning: Robust features for handling missing data, filtering,
#      and transforming datasets.
#   4. Analysis & Aggregation: Powerful methods for grouping, aggregating, and
#      exploring data.
#   5. Time Series: Specialized functionality for working with time-series data.


# =======================================
# 4. PANDAS' CORE DATA STRUCTURES
# =======================================
# - We will cover these in detail in the next lessons, but here is a brief introduction.

# --- The `Series` ---
# - A one-dimensional, labeled array capable of holding any data type.
# - Think of it as a single column in a spreadsheet or a dictionary with an ordered index.
s = pd.Series([1, 3, 5, np.nan, 6, 8])

print("--- A Pandas Series ---")
print(s)
print(f"Type of object: {type(s)}")
print("-" * 30)


# --- The `DataFrame` ---
# - A two-dimensional, labeled data structure with columns of potentially different types.
# - This is the primary Pandas data structure. Think of it as a spreadsheet or an SQL table.
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
}
df = pd.DataFrame(data)

print("--- A Pandas DataFrame ---")
print(df)
print(f"Type of object: {type(df)}")
print("-" * 30)


# =======================================
# 5. CONFIGURING PANDAS DISPLAY OPTIONS
# =======================================
# - Pandas has options to customize how DataFrames are displayed, which is very
#   useful in interactive environments like Jupyter notebooks.

# pd.set_option('display.max_rows', 100) # Show up to 100 rows
# pd.set_option('display.max_columns', 20) # Show up to 20 columns
# pd.set_option('display.width', 1000) # Set the width of the display in characters

print("Pandas display options can be configured with `pd.set_option()`.")
print("This is useful for exploring large datasets.")
