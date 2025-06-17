"""
Key Concepts:
- List creation and operations
- Slicing and copying behaviour
- List comprehensions (transform/filter)
- Nested comprehensions
- Memory considerations
"""

# ====================
# 1. List Basics
# ====================
# Ordered, mutable collections
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]  # Can hold different types

# Creation alternatives
from_range = list(range(5))  # [0, 1, 2, 3, 4]
from_string = list("data")  # ['d', 'a', 't', 'a']


# ====================
# 2. List Operations
# ====================
# Concatenation
combined = numbers + [6, 7]  # [1, 2, 3, 4, 5, 6, 7]

# Repetition
repeated = [0] * 3  # [0, 0, 0]

# Membership
print(3 in numbers)  # True

# Length
print(len(numbers))  # 5


# ====================
# 3. Indexing/Slicing
# ====================
print(numbers[0])  # 1 (first element)
print(numbers[-1])  # 5 (last element)
print(numbers[1:4])  # [2, 3, 4] (slice)
print(numbers[::2])  # [1, 3, 5] (step)

# Slicing for copying
numbers_copy = numbers[:]  # Shallow copy


# ====================
# 4. List Methods
# ====================
# Adding elements
numbers.append(6)  # [1, 2, 3, 4, 5, 6]
numbers.insert(0, 0)  # [0, 1, 2, 3, 4, 5, 6]

# Removing elements
popped = numbers.pop()  # Returns 6, numbers is now [0, 1, 2, 3, 4, 5]
numbers.remove(0)  # [1, 2, 3, 4, 5]

# Sorting
numbers.sort(reverse=True)  # [5, 4, 3, 2, 1]


# ====================
# 5. List Comprehensions
# ====================
# Basic comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Nested Comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# ====================
# 6. Advanced Patterns
# ====================
# Conditional expressions
categorized = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print(categorized)  # ['Even', 'Odd', 'Even', 'Odd', 'Even']


# ====================
# 7. Memory Considerations
# ====================
# Shallow vs deep copy
original = [[1, 2], [3, 4]]
shallow_copy = original[:]  # Copies only outer list
deep_copy = [row[:] for row in original]  # Copies inner lists too

# Size comparison
import sys

print(sys.getsizeof([0] * 100))  # Memory size in bytes


# ====================
# 8. DS Applications
# ====================
# Feature transformation
data = [10, 20, 30, 40, 50]
normalized = [(x - min(data)) / (max(data) - min(data)) for x in data]
print(normalized)  # [0.0, 0.25, 0.5, 0.75, 1.0]

# Filtering outliers
values = [12, 15, 19, 21, 100, 18, 17]
clean = [x for x in values if 15 <= x <= 20]  # [15, 19, 18, 17]

# Matrix operations
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
sum_matrix = [
    [a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(matrix_a, matrix_b)
]
# [[6, 8], [10, 12]]
