"""
Key Concepts:
- Lambda syntax and limitations
- Where they shine in data pipelines
- When to prefer over named functions
- Common pitfalls to avoid
- Performance characteristics
"""


# ====================
# 1. LAMBDA SYNTAX
# ====================
# Basic form: lambda arguments: expression
# Key features:
# - Single expression only
# - Implicit return
# - No statements or annotations

# Simple example
square = lambda x: x**2  # Not PEP8-recommended as named object

# Proper use: Inline with higher-order functions
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16]


# ====================
# 2. DATA SCIENCE USES
# ====================
# 1) Quick data transformations
temps = [("NY", 45.2), ("CA", 72.8), ("TX", 88.1)]
f_to_c = list(map(lambda loc_temp: (loc_temp[0], (loc_temp[1] - 32) * 5 / 9), temps))

# 2) DataFrame-style column operations
patients = [
    {"name": "Alice", "age": 32, "bp": (120, 80)},
    {"name": "Bob", "age": 45, "bp": (140, 90)},
]
high_bp = list(filter(lambda p: p["bp"][0] > 130, patients))

# 3) Sorting with custom keys
data = ["patient_10", "patient_2", "patient_1"]
sorted_data = sorted(data, key=lambda x: int(x.split("_")[1]))


# ====================
# 3. COMBINING WITH FUNCTIONAL TOOLS
# ====================
from functools import reduce

# 1) Multi-column aggregation
sales = [("NY", 100), ("CA", 200), ("NY", 150)]
ny_sales = reduce(lambda acc, x: acc + x[1] if x[0] == "NY" else acc, sales, 0)

# 2) Feature engineering pipeline
raw_features = [1.2, 3.4, 5.6, -1.0]
processed = list(
    map(lambda x: x**2 if x > 0 else 0, filter(lambda x: x < 5, raw_features))
)


# ====================
# 4. WHEN TO AVOID LAMBDAS
# ====================
"""
Anti-patterns:
- Complex logic (use def instead)
- Reused functionality (define properly)
- When it harms readability
- Needs type hints/documentation
"""

# Bad: Trying to do too much
result = (lambda x: x**2 + 2 * x + 1 if x > 0 else None)(5)


# Good: Clear named function
def quadratic_positive(x):
    """Calculate x² + 2x + 1 for positive inputs"""
    return x**2 + 2 * x + 1 if x > 0 else None


# ====================
# 5. ADVANCED PATTERNS
# ====================
# 1) Multiple arguments
points = [(1, 2), (3, 4), (5, 6)]
distances = list(map(lambda x, y: (x**2 + y**2) ** 0.5, *zip(*points)))

# 2) Dictionary operations
metrics = {"accuracy": 0.92, "precision": 0.85, "recall": 0.88}
scaled = {
    k: lambda v, f=1.5: v * f for k, v in metrics.items()
}  # Watch out! This doesn't work as expected

# Fixed version:
scaled = {k: (lambda v, f=1.5: v * f)(v) for k, v in metrics.items()}


# ====================
# 6. PERFORMANCE NOTES
# ====================
"""
Lambda Performance:
- Same as regular functions at runtime
- Slight overhead during compilation
- No impact in hot loops
- List comprehensions often faster than map+lambda
"""

# Time-critical alternative
squared_lc = [x**2 for x in range(1000)]  # Faster than map+lambda


# ====================
# 7. REAL DATA PIPELINES
# ====================
# 1) Data cleaning
dirty = [" 12.5 ", "3.14kg", "invalid", " 0.99 "]
clean = list(
    map(float, filter(lambda x: x.replace(".", "").isdigit(), map(str.strip, dirty)))
)

# 2) One-hot encoding
categories = ["red", "blue", "green", "red"]
encoded = list(map(lambda x: 1 if x == "red" else 0, categories))

# 3) Grouping with reduce
from collections import defaultdict

data = [("A", 10), ("B", 20), ("A", 30)]
grouped = reduce(lambda d, x: d[x[0]].append(x[1]) or d, data, defaultdict(list))
