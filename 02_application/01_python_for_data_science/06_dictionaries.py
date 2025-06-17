"""
Key Concepts:
- Dictionary creation and operations
- Dictionary comprehensions
- Specialized dictionary variants
- Hashability and key requirements
- Performance characteristics
"""

# ====================
# 1. DICTIONARY BASICS
# ====================
# Key-value pair collections
empty_dict = {}
person = {"name": "Alice", "age": 30, "city": "New York"}

# Creation alternatives
from_pairs = dict([("a", 1), ("b", 2)])  # {'a': 1, 'b': 2}
from_keys = dict.fromkeys(["a", "b"], 0)  # {'a': 0, 'b': 0}


# ====================
# 2. CORE OPERATIONS
# ====================
# Access
print(person["name"])  # Alice
print(person.get("country", "USA"))  # USA (default if missing)

# Modification
person["age"] = 31  # Update
person["country"] = "USA"  # Add new
del person["city"]  # Remove

# Membership
print("name" in person)  # True

# Iteration
print("Keys:", list(person.keys()))  # Keys: ['name', 'age', 'country']
print("Values:", list(person.values()))  # Values: ['Alice', 31, 'USA']
print(
    "Items:", list(person.items())
)  # Items: [('name', 'Alice'), ('age', 31), ('country', 'USA')]


# ====================
# 3. DICT COMPREHENSIONS
# ====================
# Transformations
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Conditional
even_squares = {
    x: x**2 for x in range(10) if x % 2 == 0
}  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Key transformation
data = {"a": 1, "b": 2}
flipped = {v: k for k, v in data.items()}  # {1: 'a', 2: 'b'}


# ====================
# 4. SPECIALIZED DICTS
# ====================
from collections import defaultdict, Counter, OrderedDict

# Default values
word_counts = defaultdict(int)  # Missing keys return 0
for word in ["a", "b", "a"]:
    word_counts[word] += 1  # defaultdict(int, {'a': 2, 'b': 1})

word_counts.get("a")  # 2
word_counts["b"]  # 1

# Frequenct counting
colors = ["red", "blue", "red", "green"]
color_counts = Counter(colors)
print(color_counts)  # Counter({'red': 2, 'blue': 1, 'green': 1})
color_counts.get("red")  # 2

# Ordered insertion
ordered = OrderedDict([("a", 1), ("b", 3), ("c", 2)])


# ====================
# 5. MERGING DICTIONARIES
# ====================
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Python 3.9+
merged = dict1 | dict2  # {'a': 1, 'b': 3, 'c': 4}


# ====================
# 6. HASHABILITY
# ====================
"""
Valid keys must be hashable (immutable):
- Strings, numbers, tuples
- NOT lists, dicts, sets
"""
valid_key = ("USA", "NY")  # Tuple as key
# invalid_key = ["USA", "NY"]   # TypeError


# ====================
# 7. DS APPLICATIONS
# ====================
# 1) Feature Storage
sample = {"temperature": 28.5, "humidity": 0.65, "pressure": 1012, "label": "normal"}

# 2) One-hot encoding
categories = ["red", "blue", "green"]
one_hot = {cat: 1 if cat == "blue" else 0 for cat in categories}

# 3) Grouping data
from collections import defaultdict

data = [("A", 10), ("B", 20), ("A", 30)]
grouped = defaultdict(list)
for key, value in data:
    grouped[key].append(value)  # {'A': [10, 30], 'B': [20]})

# 4) Configuration storage
config = {"learning_rate": 0.01, "batch_size": 32, "epochs": 100, "optimizer": "adam"}

# 5) Efficient lookups
# Convert list to dict for 0(1) lookups
items_list = ["a", "b", "c"]
items_dict = {k: True for k in items_list}
print("Fast lookup:", "b" in items_dict)  # True


# ====================
# 8. PERFORMANCE NOTES
# ====================
"""
Dictionary Characteristics:
- Average 0(1) for lookup, insert, delete
- Memory overhead higher than lists
- Preserves insertion order (Python 3.7+)
"""

# Memory comparison
import sys

print(f"Dict size: {sys.getsizeof({'a': 1})} bytes")
print(f"List size: {sys.getsizeof([1])} bytes")
# Dict size higher
