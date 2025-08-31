import pandas as pd
import os

# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. Introduction to Pandas I/O
# 2. Step 1: Creating Our Sample Dataset
# 3. Step 2: Reading Data From a CSV File
# 4. A Note on Other File Formats


# =======================================
# 1. INTRODUCTION TO PANDAS I/O
# =======================================
# - A huge part of data analysis involves reading data from external sources
#   (like CSV, Excel files) and writing results back to them.
# - Pandas provides a powerful and easy-to-use set of I/O (Input/Output) tools.
# - We will focus on CSV (Comma-Separated Values) files, the most common format.
# - Our Strategy: This script will first CREATE a sample CSV file, and then
#   we will learn how to read it back into a DataFrame.


# =======================================
# 2. STEP 1: CREATING OUR SAMPLE DATASET
# =======================================
# - To make our tutorial self-contained, we will programmatically create our own data.

# --- First, create a dedicated folder for our data files ---
DATA_FOLDER = "pandas_data"
os.makedirs(DATA_FOLDER, exist_ok=True)
file_path = os.path.join(DATA_FOLDER, "sample_sales_data.csv")


# --- Second, define the data as a dictionary ---
sales_data = {
    "OrderID": [101, 102, 103, 104, 105, 106],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Mouse", "Webcam"],
    "Category": [
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Accessories",
        "Accessories",
    ],
    "Price": [1200.00, 25.50, 75.00, 300.00, 27.00, 50.00],
    "Quantity": [1, 2, 1, 2, 3, 1],
    "OrderDate": [
        "2025-01-15",
        "2025-01-15",
        "2025-01-16",
        "2025-01-17",
        "2025-01-18",
        "2025-01-18",
    ],
}
df_to_save = pd.DataFrame(sales_data)


# --- Third, write the DataFrame to a CSV file using `.to_csv()` ---
# - `index=False` is crucial. It prevents Pandas from writing the DataFrame's
#   index (0, 1, 2...) as a column in the CSV file. This is usually what you want.
try:
    df_to_save.to_csv(file_path, index=False)
    print(f"--- Data Creation ---")
    print(f"Successfully created and saved sample data to '{file_path}'")
except Exception as e:
    print(f"Error saving file: {e}")

print("\nOriginal DataFrame that was saved:\n", df_to_save)
print("-" * 30)


# =======================================
# 3. STEP 2: READING DATA FROM A CSV FILE
# =======================================
# - `pd.read_csv()` is the primary function for reading data from CSV files.
# - It's powerful and has many optional parameters to handle different file formats.

print("--- Reading Data from CSV ---")

try:
    # --- Basic Read ---
    df_loaded = pd.read_csv(file_path)

    print("Successfully loaded data from CSV. First 5 rows:\n")
    # Use .head() to inspect the first few rows of the loaded DataFrame
    print(df_loaded.head())

    # --- Reading with Parameters ---
    # `index_col` can set a specific column as the DataFrame index.
    # `parse_dates` can be given a list of columns to automatically convert to datetime objects.
    print("\n--- Reading data again with more parameters ---")
    df_loaded_adv = pd.read_csv(
        file_path, index_col="OrderID", parse_dates=["OrderDate"]
    )
    print("Loaded data with 'OrderID' as index and 'OrderDate' as datetime object:\n")
    print(df_loaded_adv.head())

    # Use .info() to see the effect of `parse_dates`
    print("\nDataFrame info after parsing dates:")
    df_loaded_adv.info()
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print("-" * 30)


# =======================================
# 4. A NOTE ON OTHER FILE FORMATS
# =======================================
# - Pandas can handle many other formats with similar `read_*` and `to_*` functions.
# - Excel: `pd.read_excel()`, `df.to_excel()` (may require `pip install openpyxl`)
# - JSON: `pd.read_json()`, `df.to_json()`
# - SQL: `pd.read_sql()`, `df.to_sql()` (requires a database connection library like SQLAlchemy)


# --- End of File ---
