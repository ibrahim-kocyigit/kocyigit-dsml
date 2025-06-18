import os  # The `os` module is essential for interacting with the operating system.

# =======================================
# 1. SETTING UP THE ENVIRONMENT
# =======================================
# - To keep our project clean, we'll create a dedicated folder for our files.
# - `os.makedirs(path, exist_ok=True)` creates a directory, and doesn't raise an error if it already exists.
# - `os.path.join()` creates a file path that works on any OS (Windows, macOS, Linux).

FOLDER_NAME = "files_for_17_file_io"
os.makedirs(FOLDER_NAME, exist_ok=True)

# Define file paths using our new folder
file_path_write = os.path.join(FOLDER_NAME, "my_first_file.txt")
file_path_append = os.path.join(FOLDER_NAME, "log_file.txt")


# =======================================
# 2. THE `with open(...)` STATEMENT
# =======================================
# - This is the modern and recommended way to work with files.
# - It automatically handles closing the file, even if errors occur.
# - This prevents resource leaks and is much safer than manually calling `f.close()`.
# - Syntax: `with open(file_path, mode) as file_variable:`


# =======================================
# 3. WRITING TO FILES
# =======================================
# - Mode 'w' (write): Creates a new file or OVERWRITES an existing file.
# - Mode 'a' (append): Creates a new file or adds content to the END of an existing file.

# --- Writing with mode 'w' ---
print(f"--- Writing to '{file_path_write}' (mode 'w') ---")
try:
    with open(file_path_write, "w") as f:
        f.write("Hello, World!\n")
        f.write("This is the first line written from Python.\n")
        lines_to_write = ["Line 3\n", "Line 4\n"]
        f.writelines(lines_to_write)  # Writes a list of strings
    print("Successfully wrote to the file.")
except IOError as e:
    print(f"Error writing to file: {e}")


# --- Appending with mode 'a' ---
print(f"\n--- Appending to '{file_path_append}' (mode 'a') ---")
try:
    with open(file_path_append, "a") as f:
        # Get current time for a log entry
        from datetime import datetime

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"LOG: System started at {timestamp}\n")
    print("Successfully appended to the log file.")
except IOError as e:
    print(f"Error appending to file: {e}")


# =======================================
# 4. READING FROM FILES
# =======================================
# - Mode 'r' (read): The default mode. Raises a `FileNotFoundError` if the file doesn't exist.

print(f"\n--- Reading from '{file_path_write}' (mode 'r') ---")
try:
    with open(file_path_write, "r") as f:
        # --- Method 1: Iterating line by line (most memory-efficient for large files) ---
        print("Reading line by line:")
        # Move back to the start of the file for the next read method
        f.seek(0)
        for line in f:
            print(
                f"  - {line.strip()}"
            )  # .strip() removes leading/trailing whitespace, including '\n'

        # --- Method 2: .read() - reads the entire file into one string ---
        print("\nReading with .read():")
        f.seek(0)  # Go back to the start of the file
        full_content = f.read()
        print(full_content)

        # --- Method 3: .readlines() - reads all lines into a list of strings ---
        print("Reading with .readlines():")
        f.seek(0)
        all_lines = f.readlines()
        print(all_lines)

except FileNotFoundError:
    print(f"Error: The file '{file_path_write}' was not found.")
except IOError as e:
    print(f"Error reading file: {e}")


# =======================================
# 5. MANAGING FILES WITH `os`
# =======================================
# - The `os` module can be used to check for existence, delete files, etc.

# --- Checking for existence ---
print(f"\n--- File management ---")
if os.path.exists(file_path_write):
    print(f"'{file_path_write}' exists.")
else:
    print(f"'{file_path_write}' does not exist.")

# --- Deleting a file (safely) ---
# It's good practice to check if a file exists before trying to delete it.
# if os.path.exists(file_path_write):
#     try:
#         os.remove(file_path_write)
#         print(f"Successfully deleted '{file_path_write}'.")
#     except OSError as e:
#         print(f"Error deleting file: {e}")

# --- End of File ---
