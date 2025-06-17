"""
Key Concepts:
- map(): Element-wise transformations
- filter(): Data subset selection
- reduce(): Aggregation operations
- operator module helpers
- performance vs readability tradeoffs
- Real-world data pipeline examples
"""


# ====================
# 1. THE MAP FUNCTION
# ====================
# Transform each element in sequence
# Preferred over loops for simple element-wise operations


def clean_temperature(temp: float) -> float:
    """Apply data cleaning rules to tempreature readings"""
    return round(temp, 1) if -40 <= temp <= 150 else float("nan")


raw_data = [22.345, -41.2, 151.0, 18.999]
cleaned_data = list(map(clean_temperature, raw_data))
# [22.3, nan, nan, 19.0]

# Modern alternative: Generator expression
cleaned_data_gen = (clean_temperature(x) for x in raw_data)


# ====================
# 2. THE FILTER FUNCTION
# ====================
# Select subset of data meeting criteria


def is_valid_reading(temp: float) -> bool:
    """Identify physically plausible temperatures"""
    return -40 <= temp <= 150


valid_temps = list(filter(is_valid_reading, raw_data))
# [22.345, 18.999]

# Combined map+filter pipeline
processed = list(map(clean_temperature, filter(is_valid_reading, raw_data)))
# [22.3, 19.0]


# ====================
# 3. THE REDUCE FUNCTION
# ====================
# Aggregate values to single result
from functools import reduce
from operator import add, mul


# Sum of squares calculation
def sum_of_squares(acc: float, x: float) -> float:
    return acc + x**2


sos = reduce(sum_of_squares, valid_temps, 0)

# Using operator module for common operations
product = reduce(mul, [1, 2, 3, 4])  # 24
total = reduce(add, valid_temps)  # 41.344


# ====================
# 4. OPERATOR MODULE
# ====================
# Pre-built efficient functions for common operations
from operator import itemgetter, attrgetter, methodcaller

# Data sorting patterns
data = [("Alice", 32), ("Bob", 28), ("Charlie", 45)]
sorted_by_age = sorted(data, key=itemgetter(1))
# [('Bob', 28), ('Alice', 32), ('Charlie', 45)]


# ====================
# 5. PERFORMANCE ANALYSIS
# ====================
"""
Functional Tools vs Alternatives:
1. map/filter vs list comprehensions:
   - Similar performance
   - Comprehensions often more readable
   - map/filter better for existing functions

2. reduce vs explicit loops:
   - Reduce can be more concise
   - Loops often clearer for complex logic
   - Built-ins (sum, max, etc.) preferred when available
"""


# ====================
# 6. DATA SCIENCE APPLICATIONS
# ====================
# 1) Feature normalization
def normalize(features: list[float]) -> list[float]:
    """Min-max scaling using functional pipeline"""
    fmin = min(features)
    fmax = max(features)
    return list(map(lambda x: (x - fmin) / (fmax - fmin), features))


# 2) Text processing pipeline
def process_text(texts: list[str]) -> list[str]:
    """Clean and filter text data"""
    processed = map(str.lower, texts)
    processed = map(lambda s: s.strip(), processed)
    processed = filter(lambda s: len(s) > 3, processed)
    return list(processed)


# 3) Efficient aggregation
def weighted_average(values: list[float], weights: list[float]) -> float:
    """Calculate weighted mean using reduce"""
    weighted_sum = reduce(add, map(mul, values, weights))
    return weighted_sum / reduce(add, weights)


# ====================
# 7. WHEN TO USE
# ====================
"""
Best Practices:
- Use map when you have an existing transformation function
- Use filter for simple inclusion/exclusion logic
- Use reduce only for simple, obvious aggregations
- Prefer comprehensions for complex transformations
- Always consider readability over cleverness
"""
