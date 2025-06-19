# =======================================
# PYTHON INTERPRETER & EXECUTION
# =======================================
# - An interpreted language; no compilation step needed.
# - The interpreter executes code top-to-bottom, line by line.
# - Run scripts from terminal: `python your_script_name.py`
# - Use the interactive shell (REPL) for quick experiments: `python` or `ipython`


# =======================================
# 2. SYNTAX FUNDAMENTALS
# =======================================
# - Whitespace is significant; indentation defines code blocks (e.g., loops, functions)
# - Convention: Use 4 spaces or 1 tab for each level of indentation.
# - Comments start with `#` for single lines.
# - Docstrings (multi-line comments) use `""" Triple quotes """` for documenting modules, functions, and classes.
# - Statements are typically one per line and do not require a terminator like a semicolon.


# =======================================
# 3. VARIABLES & NAMING CONVENTIONS
# =======================================
# - Variables are dynamically typed (type is inferred at runtime)
# - Assign values using the equals sign `=`
# - Naming style (PEP8): `snake_case` for variables and functions (e.g., `my_variable`)
# - `PascalCase` for classes (e.g. `MyClass`)
# - Constants are written in `ALL_CAPS` (e.g., `PI=3.14`)


# =======================================
# 4. VIRTUAL ENVIRONMENTS
# =======================================
# - Isolated environments to manage project-specific dependencies.
# - Avoids conflicts between projects requiring different package versions.
# - Create: `python -m venv my_env_name`
# - Activate (macOS/Linux): `source/my_env_name/bin_activate`
# - Activate (Windows): `my_env_name\Scripts\activate`
# - Deactivate: `deactivate`


# =======================================
# 5. PACKAGE MANAGEMENT WITH PIP
# =======================================
# - `pip` is Python's standard package installer
# - Install packages: `pip install package_name`
# - Install specific versions: `pip install package_name==1.0.4`
# - List installed packages: `pip list`
# - Save dependencies to a file: `pip freeze > requirements.txt`
# - Install from a file: `pip install -r requirements.txt`


# =======================================
# 6. "HELLO, WORLD!" PROGRAM
# =======================================
# - The `print()` function outputs text to the console.
# - It's a fundamental function for displaying results and debugging.

print("Hello, World! Welcome to Python for Data Science.")


# --- End of File
