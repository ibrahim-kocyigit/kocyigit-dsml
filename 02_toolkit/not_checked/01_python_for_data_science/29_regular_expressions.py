# 29_regular_expressions.py

import re

# =======================================
# 1. WHAT ARE REGULAR EXPRESSIONS?
# =======================================
# - A "regex" is a special sequence of characters that defines a search pattern.
# - It's used for advanced finding, matching, and manipulation of strings.
# - Python's built-in `re` module is the standard library for working with regex.
# - Pro Tip: Always use raw strings `r"..."` for regex patterns to prevent
#   backslashes from being misinterpreted by Python.


# =======================================
# 2. CORE `re` MODULE FUNCTIONS
# =======================================
# - `re.search(pattern, string)`: Finds the *first* match of a pattern anywhere in the string.
#   Returns a special "match object" if successful, otherwise `None`.
# - `re.findall(pattern, string)`: Finds *all* non-overlapping matches and returns them as a list of strings.
# - `re.sub(pattern, replacement, string)`: Replaces all occurrences of the pattern with a replacement.
# - `re.match(pattern, string)`: Similar to `search`, but only matches at the *beginning* of the string.

text = "The quick brown fox jumps over the lazy dog. The fox is very quick."

print("--- Core Functions ---")
# --- `re.search()` ---
# Let's search for the word "fox"
match = re.search(r"fox", text)
if match:
    print(f"`search` found a match: '{match.group(0)}' at index {match.start()}")
else:
    print("`search` found no match.")

# --- `re.findall()` ---
# Let's find all instances of "The" or "the"
# `re.IGNORECASE` is a flag to make the pattern case-insensitive.
all_thes = re.findall(r"the", text, re.IGNORECASE)
print(f"`findall` found: {all_thes}")

# --- `re.sub()` ---
# Let's replace "fox" with "cat"
substituted_text = re.sub(r"fox", "cat", text)
print(f"`sub` result: {substituted_text}")
print("-" * 30)


# =======================================
# 3. COMMON REGEX PATTERNS (METACHARACTERS)
# =======================================
# - The power of regex comes from special characters (metacharacters).
#   \d : Digit (0-9)              |  \D : Not a Digit
#   \w : Word character (a-zA-Z0-9_) |  \W : Not a Word character
#   \s : Whitespace (space, tab, \n) |  \S : Not Whitespace
#   .  : Any character except newline
#   ^  : Start of the string       |  $  : End of the string
#   [] : Character set (e.g., [aeiou] matches any vowel)
#   |  : OR operator (e.g., `cat|dog` matches "cat" or "dog")
#
# - Quantifiers (how many times to match):
#   * : 0 or more times
#   +  : 1 or more times
#   ?  : 0 or 1 time (optional)
#   {n}: Exactly n times
#   {n,}: n or more times
#   {n,m}: Between n and m times


# =======================================
# 4. PRACTICAL EXAMPLES
# =======================================
print("--- Practical Examples ---")
log_entry = "INFO:2025-06-18 User 'admin' logged in from IP 192.168.1.101"

# --- Example 1: Extracting an IP Address using `search` ---
# Pattern: \d{1,3} matches 1 to 3 digits. We repeat this four times, separated by literal dots.
# The parentheses `()` create a "capture group".
ip_pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
ip_match = re.search(ip_pattern, log_entry)
if ip_match:
    # .group(0) or .group() gives the full match.
    # .group(1) gives the first captured group.
    print(f"Found IP Address: {ip_match.group(1)}")


# --- Example 2: Finding all numbers in a string using `findall` ---
text_with_numbers = "Order 123 for user 456 costs 78.90 dollars."
numbers = re.findall(r"\d+\.?\d*", text_with_numbers) # `\.?` makes the decimal optional
print(f"Found numbers: {numbers}")


# --- Example 3: Validating an email address ---
# This is a simplified pattern for demonstration. Real-world email regex is very complex.
email_pattern = r"^\w+@\w+\.\w+$"
email1 = "test@example.com"
email2 = "not-an-email"
if re.match(email_pattern, email1):
    print(f"'{email1}' is a valid email format.")
if not re.match(email_pattern, email2):
    print(f"'{email2}' is NOT a valid email format.")


# --- Example 4: Compiling a pattern for reuse ---
# If you use a pattern many times, compile it for better performance.
phone_pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
text_with_phones = "Call support at 800-555-1234 or sales at 900-555-5678."
found_phones = phone_pattern.findall(text_with_phones)
print(f"Found phone numbers: {found_phones}")

redacted_text = phone_pattern.sub("[REDACTED]", text_with_phones)
print(f"Redacted text: {redacted_text}")

# --- End of File ---