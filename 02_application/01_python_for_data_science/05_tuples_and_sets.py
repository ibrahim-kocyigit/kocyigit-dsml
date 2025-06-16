"""
Key Concepts:
- Tuples: Immutable sequences (fixed data records)
- Sets: Unordered unique collections (deduplication)
- Frozen sets: Immutable sets
- Hashability requirements
- Performance characteristics
"""

# ====================
# 1. TUPLES BASICS
# ====================
# Immutable sequences (fixed-size records)
coordinates = (40.7128, -74.0060)  # Latitude/Longitude pair
single_element = (42,)  # Comma required for single-element tuples

# Creation alternatives
from_range = tuple(range(5))  # (0, 1, 2, 3, 4)
from_list = tuple([1, 2, 3])  # (1, 2, 3)


# ====================
# 2. TUPLE OPERATIONS
# ====================
# Packing/unpacking (common in data returns)
min_max = (10, 90)  # Packing
low, high = min_max  # Unpacking

# Extended unpacking
values = (1, 2, 3, 4, 5)
first, *midle, last = values  # first=1, middle=[2,3,4], last=5

# Named tuples (self-documenting)
from collections import namedtuple

DataPoint = namedtuple("DataPoint", ["x", "y"])
pt = DataPoint(10.5, 20.3)
print(f"Point at ({pt.x}, {pt.y})")  # Field access # -> Point at (10.5, 20.3)


# ====================
# 3. TUPLE VS LIST
# ====================
"""
When to use tuples:
- Fixed data records (CSV rows, database records)
- Dictionary keys (requires hashable)
- Function arguments/returns
- When immutability is desired
"""

# Memory comparison
import sys

data = [1, 2, 3]
print(f"List size: {sys.getsizeof(data)} bytes")  # Typically larger
print(f"Tuple size: {sys.getsizeof(tuple(data))} bytes")  # More compact


# ====================
# 4. SETS BASICS
# ====================
# Unordered unique collections
unique_numbers = {1, 2, 3, 2, 1}  # {1, 2, 3}
empty_set = set()  # {} creates empty dict!

# Creation alternatives
from_list = set([1, 2, 2, 3])  # {1, 2, 3}
from_string = set("hello")  # {'h', 'e', 'l', 'o'}


# ====================
# 5. SET OPERATIONS
# ====================
a = {1, 2, 3}
b = {2, 3, 4}

print("Union:", a | b)  # {1, 2, 3, 4}
print("Intersection:", a & b)  # {2, 3}
print("Difference:", a - b)  # {1}
print("Symmetric Diff:", a ^ b)  # {1, 4}

# Membership testing (O(1) complexity)
print(2 in a)  # True

# Set comprehensions
squares = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}


# ====================
# 6. FROZENSETS
# ====================
# Immutable sets (hashable)
fs = frozenset([1, 2, 3])
# fs.add(4) → AttributeError


# ====================
# 7. DS APPLICATIONS
# ====================
# 1) Deduplication
duplicates = [
    1,
    2,
    2,
    3,
    4,
    4,
    4,
]
unique = list(set(duplicates))  # [1, 2, 3, 4]

# 2) Feature intersection
user_features = {"age", "location", "income"}
model_features = {"age", "income", "education"}
common = user_features & model_features  # {'age', 'income'}

# 3) Efficient filtering
valid_ids = {1001, 1005, 1010}  # Stored as set for O(1) lookups
input_id = 1005
print("Valid ID:", input_id in valid_ids)  # Fast even for millions

# 4) Distinct value counting
text = "the quick brown fox jumps over the lazy dog"
unique_chars = len(set(text.lower()))  # 27 (spaces included)

# 5) Data record tuples
patient_record = ("P1002", "Maria", "Chen", 35, "F", True)


# ====================
# 8. PERFORMANCE NOTES
# ====================
"""
Set vs List membership:
- Set: O(1) average case
- List: O(n) worst case

When working with >100 elements where membership testing is frequent,
sets provide dramatic performance improvements.
"""
