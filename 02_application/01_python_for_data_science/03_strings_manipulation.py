"""
Key Concepts:
- String indexing/slicing (text processing)
- Common string methods (data cleaning)
- Formatting (report generation)
- Regular expressions (pattern matching)
- Encoding issues (handling real-world data)
"""

# ====================
# 1. String Basics
# ====================
text = "Data Science"

# Indexing (zero-based)
print(text[0])  # 'D' (first character)
print(text[-1])  # 'e' (last character)

# Slicing [start:end:step]
print(text[0:4])  # 'Data' (positions 0-3)
print(text[5:])  # 'Science' (from index 5 to end)
print(text[::2])  # 'Dt cec' (every 2nd character)


# ====================
# 2. Common Methods
# ====================
# Case conversion (standardization)
print("lower():", text.lower())  # 'data science'
print("upper():", text.upper())  # 'DATA SCIENCE'
print("title():", "data science".title())  # 'Data Science'

# Stripping (cleaning whitespace)
dirty_text = "  data science \t\n"
print("strip():", dirty_text.strip())  # 'data science'

# Splitting/Joining (common in CSV processing)
csv_line = "age,income,education"
fields = csv_line.split(",")
print("split():", fields)  # ['age', 'income', 'education']
print("join():", "|".join(fields))  # 'age|income|education'

# Replacement (simple cleaning)
print("replace():", text.replace(" ", "_"))  # 'Data_Science'


# ====================
# 3. String Formatting
# ====================
# f-strings (Python 3.6+ preferred)
name = "Alice"
score = 95.52
print(f"{name} scored {score:.1f}%")  # 'Alice scored 95.5%'

# .format() method (backwards compatibility)
print("{} scored {:.1f}%".format(name, score))


# ====================
# 5. Regular Expressions
# ====================
import re

# Searching (pattern extraction)
text = "Contact: email@example.com, phone: 123-456-7890"
email_match = re.search(r"\b[\w.-]+@[\w.-]+\.\w+\b", text)  # Check Regex for more info
print("Email found:", email_match.group()) if email_match else None

# Substitution (pattern replacement)
anonymized = re.sub(r"\d{3}-\d{3}-\d{4}", "[PHONE]", text)
print("Anonymized:", anonymized)


# ====================
# 6. Encoding Handling
# ====================
# Critical when working with external data
messy_text = " café "
encoded = messy_text.encode("utf-8")
decoded = encoded.decode("utf-8")
print("Encoded/decoded:", decoded.strip())


# ====================
# 7. DS/NLP Examples
# ====================
# Text cleaning pipeline
def clean_text(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    return text


sample = "  This is a SAMPLE text!  "
print("\nCleaned text:", clean_text(sample))  # 'this is a sample text'

# Tokenization (simplified)
tokens = clean_text(sample).split()
print("Tokens:", tokens)  # ['this', 'is', 'a', 'sample', 'text']


# ====================
# 8. Performance Tips
# ====================
# String concatenation (avoid + in loops)
words = ["data"] * 1000
# Good:
joined = " ".join(words)
# Bad:
# result = ""
# for w in words: result += w  # Creates new objects each time
