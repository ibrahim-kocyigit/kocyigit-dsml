import pandas as pd
import os

# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. Introduction and Setup
# 2. Column Selection
# 3. Label-Based Selection with `.loc`


# =======================================
# 1. INTRODUCTION AND SETUP
# =======================================
# - Selecting subsets of data is a fundamental part of data analysis.
# - Pandas provides powerful and flexible tools for this, primarily:
#   - `[]` for basic column selection.
#   - `.loc` for selecting by labels.
#   - `.loc` for selecting by integer position.

# --- Load the sample dataset we created in the previous lesson ---
DATA_FOLDER = "pandas_data"
file_path = os.path.join(DATA_FOLDER, "sample_sales_data.csv")

try:
    # We'll use OrderID as the index to better demonstrate label-based selection
    df = pd.read_csv(file_path, index_col="OrderID")
    print("--- Sample Sales DataFrame (OrderID as index) ---")
    print(df)
except FileNotFoundError:
    print(f"Error: The data file was not found at '{file_path}'")
    print("Please run '04_reading_and_writing_data.py' first to create it.")
    df = pd.DataFrame()  # Create an empty df to avoid further errors

print("-" * 30)


# =======================================
# 2. COLUMN SELECTION
# =======================================
# - As seen before, you can easily select one or more columns.
print("--- Column Selection ---")
# --- Selecting a single column (returns a Series) ---
products = df["Product"]
print("Selecting the 'Product' column (returns a Series):\n", products)

# --- Selecting multiple columns (returns a DataFrame) ---
# Pass a list of column names.
price_and_qty = df[["Product", "Price", "Quantity"]]
print("\nSelecting 'Product', 'Price', and 'Quantity' columns:\n", price_and_qty)
print("-" * 30)


# =======================================
# 3. LABEL-BASED SELECTION WITH `.loc`
# =======================================
# - `.loc` is the primary method for selecting data by its *row and column labels*.
# - It is inclusive of the end label when slicing.
