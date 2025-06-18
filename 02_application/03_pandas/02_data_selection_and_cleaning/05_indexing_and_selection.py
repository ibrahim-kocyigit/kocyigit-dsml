import pandas as pd
import os

# =======================================
# 1. INTRODUCTION AND SETUP
# =======================================
# - Selecting subsets of data is a fundamental part of data analysis.
# - Pandas provides powerful and flexible tools for this, primarily:
#   - `[]` for basic column selection.
#   - `.loc` for selecting by labels.
#   - `.iloc` for selecting by integer position.

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
if not df.empty:
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
if not df.empty:
    print("--- Label-Based Selection with .loc ---")

    # --- Selecting a single row by its index label ---
    row_102 = df.loc[102]
    print("Selecting row with index label 102 (returns a Series):\n", row_102)

    # --- Slicing rows by label ---
    # Note: Slicing with .loc is INCLUSIVE of the start and end labels.
    rows_102_to_104 = df.loc[102:104]
    print("\nSlicing rows from 102 to 104 (inclusive):\n", rows_102_to_104)

    # --- Selecting rows and columns simultaneously ---
    # Get the 'Price' for OrderID 105
    price_105 = df.loc[105, "Price"]
    print(f"\nPrice for order 105: {price_105}")

    # Get 'Product' and 'Quantity' for orders 101 and 106
    subset = df.loc[[101, 106], ["Product", "Quantity"]]
    print("\nProduct and Quantity for orders 101 and 106:\n", subset)
    print("-" * 30)


# =======================================
# 4. POSITION-BASED SELECTION WITH `.iloc`
# =======================================
# - `.iloc` is the primary method for selecting data by its *integer position*.
# - It works just like indexing lists or NumPy arrays.
# - It is exclusive of the end position when slicing.
if not df.empty:
    print("--- Position-Based Selection with .iloc ---")

    # --- Selecting a single row by its integer position ---
    # Get the second row (position 1)
    row_pos_1 = df.iloc[1]
    print("Selecting row at position 1 (returns a Series):\n", row_pos_1)

    # --- Slicing rows by position ---
    # Note: Slicing with .iloc is EXCLUSIVE of the end position (like standard Python).
    rows_pos_1_to_4 = df.iloc[1:4]  # Gets rows at positions 1, 2, 3
    print("\nSlicing rows from position 1 to 4 (exclusive):\n", rows_pos_1_to_4)

    # --- Selecting rows and columns simultaneously ---
    # Get the element at row 3, column 1
    element_3_1 = df.iloc[3, 1]
    print(f"\nElement at position (3, 1) ('Category' for Order 104): '{element_3_1}'")

    # Get a slice of rows and a slice of columns
    # First two rows (pos 0, 1) and first three columns (pos 0, 1, 2)
    subset_iloc = df.iloc[0:2, 0:3]
    print("\nSlice of first 2 rows and first 3 columns:\n", subset_iloc)
    print("-" * 30)


# =======================================
# 5. SUMMARY: `.loc` vs `.iloc`
# =======================================
# - Use `.loc` for L-abels: Selecting based on the index names and column names.
# - Use `.iloc` for I-nteger LOC-ations: Selecting based on numerical positions.
# - AVOIDING AMBIGUITY: Being explicit with .loc and .iloc is best practice and
#   helps you avoid common errors, especially the `SettingWithCopyWarning`.
