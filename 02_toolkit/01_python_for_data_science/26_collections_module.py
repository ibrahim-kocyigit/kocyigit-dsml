from collections import Counter, defaultdict, deque, namedtuple, ChainMap
import numpy as np

# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. `Counter`: For Frequency Analysis
# 2. `defaultdict`: For Grouping Data
# 3. `deque`: For Sliding Windows & Data Streams
# 4. `namedtuple`: For Lightweight Data Records
# 5. `ChainMap`: For Managing Configurations


# =======================================
# 1. `Counter`: FOR FREQUENCY ANALYSIS
# =======================================
# - A dict subclass for counting hashable objects.
# - In data science, this is the go-to tool for frequency analysis,
#   especially in Natural Language Processing (NLP).

print("--- Counter for NLP Word Frequency ---")
# Sample text data after tokenization (splitting into words)
document = [
    "machine",
    "learning",
    "is",
    "a",
    "subset",
    "of",
    "artificial",
    "intelligence",
    "and",
    "machine",
    "learning",
    "models",
    "use",
    "data",
]

# Use Counter to get the frequency of each word
word_counts = Counter(document)
print(f"Word Counts: {word_counts}")

# The `.most_common(n)` method is invaluable for finding top keywords
print(f"The 2 most common words are: {word_counts.most_common(2)}")
print("-" * 30)


# =======================================
# 2. `defaultdict`: FOR GROUPING DATA
# =======================================
# - A dict subclass that provides a default value for a key that does not exist.
# - In data science, this is perfect for grouping data points by a specific category.

print("--- defaultdict for Grouping Log Data ---")
# Sample log data: list of (user_id, action) tuples
log_data = [
    ("user1", "login"),
    ("user2", "view_page"),
    ("user1", "logout"),
    ("user3", "login"),
    ("user2", "add_to_cart"),
    ("user1", "login"),
]

# Group all actions for each user
user_actions = defaultdict(list)
for user, action in log_data:
    user_actions[user].append(action)

# Convert to a regular dict for clean printing
print("Actions grouped by user:\n", dict(user_actions))
print("-" * 30)


# =======================================
# 3. `deque`: FOR SLIDING WINDOWS & DATA STREAMS
# =======================================
# - A list-like container with fast appends and pops from both ends.
# - Its `maxlen` argument is perfect for keeping a "sliding window" of the
#   most recent items from a data stream (e.g., sensor readings, stock prices).

print("--- deque for a Sliding Window of Sensor Data ---")
# A deque that only ever holds the last 5 readings.
last_5_readings = deque(maxlen=5)

# Simulate a stream of sensor data
data_stream = [10.1, 10.2, 10.3, 10.2, 10.4, 10.5, 10.6, 10.7]

for reading in data_stream:
    last_5_readings.append(reading)
    # Calculate the moving average of the current window
    current_avg = np.mean(last_5_readings)
    print(
        f"New reading: {reading} | Current Window: {list(last_5_readings)} | Moving Avg: {current_avg:.2f}"
    )

print("-" * 30)


# =======================================
# 4. `namedtuple`: FOR LIGHTWEIGHT DATA RECORDS
# =======================================
# - Creates tuple subclasses with named fields.
# - In data science, this is great for creating simple, immutable objects to
#   represent a single record or row of data, without the overhead of a full class.

print("--- namedtuple for Structured Data Records ---")
# Define a 'DataRecord' type
DataRecord = namedtuple("DataRecord", ["sample_id", "feature1", "feature2", "label"])

# Create a list of records, perhaps from a CSV file
data_records = [
    DataRecord(1, 0.5, 0.2, "A"),
    DataRecord(2, 0.6, 0.3, "B"),
    DataRecord(3, 0.4, 0.1, "A"),
]

# Access data using clear, self-documenting field names
record_2 = data_records[1]
print(f"Record 2: {record_2}")
print(f"Feature 1 of Record 2: {record_2.feature1}")
print("-" * 30)


# =======================================
# 5. `ChainMap`: FOR MANAGING CONFIGURATIONS
# =======================================
# - Groups multiple dictionaries into a single, viewable mapping.
# - Perfect for managing machine learning experiment configurations, where you have
#   default settings that can be overridden by specific experiment settings.

print("--- ChainMap for ML Experiment Configs ---")
default_config = {"learning_rate": 0.01, "optimizer": "adam", "epochs": 20}
experiment_config = {"learning_rate": 0.005, "batch_size": 64}

# Create a ChainMap. It searches `experiment_config` first, then `default_config`.
combined_config = ChainMap(experiment_config, default_config)

print(
    f"Learning Rate: {combined_config['learning_rate']}"
)  # Found in experiment_config
print(f"Optimizer: {combined_config['optimizer']}")  # Found in default_config
print(f"Batch Size: {combined_config['batch_size']}")  # Found in experiment_config
print(f"Epochs: {combined_config['epochs']}")  # Found in default_config

# --- End of File ---
