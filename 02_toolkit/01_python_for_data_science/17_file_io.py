import os  # The `os` module is essential for interacting with the operating system.

# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. Setting Up The Environment
# 2. The `with open(...)` Statement
# 3.


# =======================================
# 1. SETTING UP THE ENVIRONMENT
# =======================================
# - To keep our project clean, we'll create a dedicated folder for our files.
# - `os.makedirs(path, exist_ok=True)` creates a directory, and doesn't raise an error if it doesn't exist.
# - `os.path.join()` creates a file path that works on any OS.

FOLDER_NAME = "files_for_17_file_io"
os.makedirs(FOLDER_NAME, exist_ok=True)

# - Define file paths using our new folder
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
# =======================================æ
# - Mode 'w' (write):
