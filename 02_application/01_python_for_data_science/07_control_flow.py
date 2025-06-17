"""
Key Concepts:
- Conditional execution (data validation)
- Looping patterns (data iteration)
- Comprehension optimizations
- Loop control statements
- Structural pattern matching (Python 3.10+)
"""


# ====================
# 1. CONDITIONAL LOGIC
# ====================
# Basic if/elif/else (data validation)
def validate_temperature(temp):
    if temp < -20:
        return "Invalid (too cold)"
    elif temp > 50:
        return "Invalid (too hot)"
    else:
        return "Valid"


# Ternary operator (compact conditions)
value = 42
classification = "High" if value > 30 else "Low"

# Truthiness (important for data checks)
data = []
if not data:
    print("Warning: Empty dataset")  # Prints


# ====================
# 2. LOOPING PATTERNS
# ====================
# Basic for loop (data iteration)
numbers = [10, 20, 30, 40]
for num in numbers:
    if num > 25:
        print(num * 2)  # 60, 80

# enumerate() (track indices)
for idx, value in enumerate(["a", "b", "c"], start=1):
    print(f"Index {idx}: {value}")

# zip() (parallel iteration)
features = ["age", "income"]
values = [30, 5000]
for feature, value in zip(features, values):
    print(f"{feature}: {value}")


# ====================
# 3. LOOP OPTIMIZATIONS
# ====================
# Precompute values outside loop
threshold = calculate_threshold()  # Expensive operation
for item in large_dataset:
    if item > threshold:
        process(item)

# Use built-ins where possible
total = sum(x for x in range(1000))  # Faster than manual loop


# ====================
# 4. LOOP CONTROL
# ====================
# break/continue (data filtering)
usernames = ["alice", "", "bob", None, "carol", "admin"]

for name in usernames:
    if not name:  # Skip empty/None names
        continue
    print(f"Processing: {name}")
    if name == "admin":  # Stop if admin is found
        print("Admin found, stopping.")
        break

# else clause (loop completion)
for item in items:
    if item == target:
        break
else:
    print("Target not found")  # Executes if no break


# ====================
# 5. COMPREHENSIONS
# ====================

# List comprehension (transformation)
squared = [x**2 for x in range(10)]  # [0, 1, 4, 9...]

# Dict comprehension (feature engineering)
features = {f"col_{i}": i * 2 for i in range(5)}  # {'col_0':0, 'col_1':2...}

# Conditional comprehension
evens = [x for x in range(100) if x % 2 == 0]


# ====================
# 6. STRUCTURAL MATCHING
# ====================
# Python 3.10+ (data pattern matching)
def process_data(response):
    match response:
        case {"status": 200, "data": data}:
            return clean_data(data)
        case {"status": 404}:
            return "Not found"
        case {"status": _}:  # For any other case
            return "Unknown error"


# ====================
# 7. DS APPLICATIONS
# ====================
# 1) Data pipeline
for batch in data_loader:
    if not preprocess(batch):
        continue  # Skip bad batches
    results = []
    for sample in batch:
        if sample["quality"] < 0.7:
            results.append(None)
        else:
            results.append(transform(sample))
    yield results

# 2) Early stopping
for epoch in range(max_epochs):
    loss = train_model()
    if loss < stopping_threshold:
        print(f"Early stop at epoch {epoch}")
        break

# 3) Dictionary processing
config = {"lr": 0.01, "batch_size": 32, "optimizer": "adam"}
required_keys = {"lr", "batch_size"}
if not required_keys.issubset(config):
    missing = required_keys - config.keys()
    raise ValueError(f"Missing configs: {missing}")


# ====================
# 8. PERFORMANCE TIPS
# ====================
"""
Optimization Guidelines:
1. Use vectorized operations when possible
2. Minimize work inside loops
3. Prefer comprehensions over manual loops
4. Use built-in functions (map, filter, zip)
5. Consider generator expressions for large data
"""

# Generator example (memory efficient)
large_data = (x**2 for x in range(1000000))  # Doesn't create full list
print(sum(large_data))  # Processes one item at a time

print("\nControl flow patterns ready for data pipelines!")
