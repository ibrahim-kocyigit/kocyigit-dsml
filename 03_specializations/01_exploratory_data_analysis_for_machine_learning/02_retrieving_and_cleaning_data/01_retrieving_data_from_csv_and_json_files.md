# Retrieving Data from CSV and JSON Files

## Reading CSV Files

- **CSV (Comma Separated Values):**  
  - Rows of data separated by commas.
  - Common format for tabular data.

- **Basic Pandas Usage:**
    ```python
    import pandas as pd

    file_path = 'data/iris_data.csv'
    data = pd.read_csv(file_path)
    print(data.iloc[:5])  # Show first 5 rows
    ```

- **Useful `read_csv` Arguments:**
  - `sep`: Specify a different separator (e.g., `sep='\t'` for tab-separated files).
  - `delim_whitespace=True`: Use any whitespace as a delimiter.
  - `header`: Choose which row to use as column names.
  - `names`: Provide a list of column names.
  - `na_values`: Specify values to treat as missing/NA (e.g., `na_values=['NA', 99]`).

## Reading JSON Files

- **JSON (JavaScript Object Notation):**
  - Standard for data storage and exchange (especially in NoSQL databases and APIs).
  - Structure is similar to Python dictionaries (key-value pairs).

- **Basic Pandas Usage:**
    ```python
    import pandas as pd

    file_path = 'data/example.json'
    data = pd.read_json(file_path)
    ```

- **Useful `read_json` Arguments:**
  - `orient`: Specifies the expected JSON string format (`'split'`, `'records'`, `'index'`, `'columns'`, `'values'`).
  - If you have trouble reading a JSON file, check the documentation and try different `orient` options.

- **Writing JSON Files:**
    ```python
    data.to_json('output.json')
    ```

## Summary

- Pandas makes it easy to read and write both CSV and JSON files with flexible options for handling different formats and missing values.
- Understanding these basics is essential for working with real-world data in machine learning projects.

---

**Next:** [Retrieving Data from Databases, APIs, and the Cloud](./02_retrieving_data_from_databases_apis_and_the_cloud.md)