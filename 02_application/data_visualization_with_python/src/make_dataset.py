import pandas as pd
import os

current_dir = os.getcwd()
file_path = os.path.join(current_dir, "data", "external", "Canada.xlsx")

try:
    df = pd.read_excel(
        file_path,
        sheet_name="Canada by Citizenship",
        skiprows=range(20),
        skipfooter=2,
    )
    print("Data read successfully.")
except FileNotFoundError:
    print(
        "Error: 'your_file.xlsx' not found. Make sure the file exists and the path is correct."
    )
except ValueError as e:
    print(f"ValueError: {e}. Check the sheet name and skiprows arguments.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
