# =======================================
# 1. STRING BASICS & IMMUTABILITY
# =======================================
# - Strings are immutable sequences of Unicode characters.
# - "Immutable" means a string's content cannot be changed after creation.
# - Operations that "change" a string actually create a new one.
# - Defined with single '', double "", or triple """ quotes.

original_string = "Python"
# original_string[0] = "J" # This would cause a TypeError


# =======================================
# 2. INDEXING AND SLICING
# =======================================
# - Access individual characters with square brackets `[]`.
# - Indexing: First character is at index 0, last is at -1.
# - Slicing: `[start:stop:step]` extracts a portion of the string.
# - The `stop` index is exclusive (not included in the result).

text = "Data Science"
print(f"First character: {text[0]}")  # 'D'
print(f"Last character: {text[-1]}")  # 'e'
print(f"Slice (0-4): {text[0:4]}")  # 'Data'
print(f"Slice (from 5): {text[5:]}")  # 'Science'
print(f"Slice (every 2nd char): {text[::2]}")  # 'Dt cec'
print(f"Reversed string: {text[::-1]}")  # 'ecneicS ataD'


# =======================================
# 3. CONCATENATION & REPETITION
# =======================================
# - `+` operator: Combines two strings.
# - `*` operator: Repeats a string multiple times.

str1 = "Hello"
str2 = "World"
greeting = str1 + ", " + str2  # "Hello, World"
separator = "-" * 20  # "--------------------"


# =======================================
# 4. COMMON STRING METHODS
# =======================================

# --- Case Conversion ---
# - `.upper()`: Converts to uppercase.
# - `.lower()`: Converts to lowercase.
# - `.capitalize()`: First character to upper, rest to lower.
# - `.title()`: First character of each word to upper.
mixed_case = "pyTHon is FUN"
print(mixed_case.upper())  # "PYTHON IS FUN"
print(mixed_case.lower())  # "python is fun"
print(mixed_case.capitalize())  # "Python is fun"
print(mixed_case.title())  # "Python Is Fun"

# --- Whitespace Removal ---
# - `.strip()`: Removes leading/trailing whitespace.
# - `.lstrip()`: Removes leading whitespace.
# - `.rstrip()`: Removes trailing whitespace.
padded_string = "   some text   "
print(f"'{padded_string.strip()}'")

# --- Find & Replace ---
# - `.find()`: Returns the first index of a substring (-1 if not found).
# - `.replace()`: Replaces occurrences of a substring with another.
sentence = "the quick brown fox jumps over the lazy dog"
print(sentence.find("fox"))  # 16
print(sentence.replace("fox", "cat"))  # Returns a new string

# --- Checking Content (return True/False) ---
# - `.startswith()`: Checks if the string begins with a substring.
# - `.endswith()`: Checks if the string ends with a substring.
# - `.isdigit()`: Checks if all characters are digits.
# - `.isalpha()`: Checks if all characters are alphabetic.
filename = "document.pdf"
print(filename.startswith("doc"))  # True
print(filename.endswith(".txt"))  # False


# =======================================
# 5. SPLITTING AND JOINING
# =======================================
# - `.split()`: Breaks a string into a list of substrings.
# - `.join()`: Joins elements of an iterable (like a list) into a single string.

# --- Splitting ---
csv_data = "John,Doe,45,Engineer"
user_data_list = csv_data.split(",")  # ['John', 'Doe', '45', 'Engineer']

# --- Joining ---
words_to_join = ["Python", "is", "awesome"]
joined_sentence = " ".join(words_to_join)  # "Python is awesome"


# =======================================
# 6. STRING FORMATTING
# =======================================
# - The modern, preferred way to embed expressions inside string literals.

# --- f-Strings (Formatted String Literals) - Recommended ---
name = "Bob"
age = 42
print(f"{name} is {age} years old.")
# Can include expressions directly
print(f"Next year, {name} will be {age + 1}.")

# --- `.format()` method ---
print("{} is {} years old.".format(name, age))


# =======================================
# 7. STRING LENGTH AND MEMBERSHIP
# =======================================
# - `len()`: Global function to get the number of characters.
# - `in` / `not in`: Operators to check if a substring exists.

my_string = "Machine Learning"
print(f"Length of string: {len(my_string)}")  # 16
print("Machine" in my_string)  # True
print("Java" not in my_string)  # True

# --- End of File ---
