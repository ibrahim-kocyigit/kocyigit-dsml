# 26_collections_module.py

from collections import Counter, defaultdict, deque, namedtuple, ChainMap

# =======================================
# 1. `Counter`: DICTIONARY FOR COUNTING
# =======================================
# - A dict subclass for counting hashable objects.
# - It's one of the most useful tools for data analysis and counting tasks.
# - Keys are the items being counted, and values are their counts.

# --- Counting characters in a string ---
char_counts = Counter("hello world")
print(f"--- Counter ---")
print(f"Character counts: {char_counts}")

# --- Counting words in a list ---
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_counts = Counter(words)
print(f"Word counts: {word_counts}")

# --- The `.most_common(n)` method is incredibly useful ---
# It returns a list of the n most common items and their counts.
print(f"The 2 most common words are: {word_counts.most_common(2)}")
print(f"The count for 'orange' is: {word_counts['orange']}")
# Accessing a missing key returns 0 instead of raising an error.
print(f"The count for 'grape' is: {word_counts['grape']}")
print("-" * 30)


# =======================================
# 2. `defaultdict`: DICT WITH DEFAULT VALUES
# =======================================
# - A dict subclass that calls a "factory function" to supply a default
#   value for a key that does not exist.
# - This eliminates the need to manually check if a key is in the dictionary.

# --- The "Old Way" of grouping items ---
pairs = [("a", 1), ("b", 2), ("a", 3), ("c", 4), ("b", 5)]
grouped_old = {}
for key, value in pairs:
    if key not in grouped_old:
        grouped_old[key] = []
    grouped_old[key].append(value)

# --- The clean `defaultdict` way ---
# We provide `list` as the factory. When a key is first accessed,
# it will automatically be created with an empty list as its value.
grouped_new = defaultdict(list)
for key, value in pairs:
    grouped_new[key].append(value)

print(f"--- defaultdict ---")
print(f"Grouped items (the clean way): {dict(grouped_new)}") # Convert to dict for clean printing

# Another example: using `int` as the factory defaults new keys to 0.
int_dict = defaultdict(int)
int_dict["a"] += 1
print(f"defaultdict(int): {dict(int_dict)}")
print("-" * 30)


# =======================================
# 3. `deque`: DOUBLE-ENDED QUEUE
# =======================================
# - A list-like container with fast appends and pops from BOTH ends.
# - Pronounced "deck".
# - While list appends/pops from the end are fast, doing so from the
#   beginning is slow. `deque` is fast for both.
# - Useful for implementing queues (FIFO) and stacks (LIFO).

d = deque([3, 4, 5])
print(f"--- deque ---")
print(f"Initial deque: {d}")

# --- Appending and popping from the right (like a list) ---
d.append(6)       # Add to the right
d.pop()           # Remove from the right

# --- The special `deque` methods for the left side ---
d.appendleft(2)   # Add to the left
print(f"After appendleft(2): {d}")

d.popleft()       # Remove from the left
print(f"After popleft(): {d}")

# `deque` can also be created with a max length
last_five_items = deque(maxlen=5)
for i in range(10):
    last_five_items.append(i)
    print(list(last_five_items), end=" -> ")
print(f"\nFinal deque (last 5 items): {last_five_items}")
print("-" * 30)


# =======================================
# 4. `namedtuple`: TUPLE WITH NAMED FIELDS
# =======================================
# - A factory function for creating tuple subclasses with named fields.
# - Makes code more readable by allowing access to elements by name instead of just index.
# - Lightweight and memory-efficient, like a regular tuple.

# Define a "Point" named tuple type
Point = namedtuple('Point', ['x', 'y', 'z'])

# Create an instance
p1 = Point(10, 20, 30)

print(f"--- namedtuple ---")
print(f"Our Point object: {p1}")

# Access elements by name (more readable)
print(f"The x-coordinate is: {p1.x}")

# Still accessible by index (like a regular tuple)
print(f"The y-coordinate is: {p1[1]}")
print("-" * 30)


# =======================================
# 5. `ChainMap`: A CHAIN OF DICTIONARIES
# =======================================
# - Groups multiple dictionaries into a single, viewable mapping.
# - Lookups search through the underlying mappings sequentially until a key is found.
# - Writes, updates, and deletions operate ONLY on the first mapping in the chain.
# - Useful for managing layered contexts (e.g., default settings overridden by user settings).

default_config = {'theme': 'dark', 'font_size': 12, 'show_sidebar': True}
user_config = {'font_size': 14, 'language': 'Python'}

# Create a ChainMap
combined_config = ChainMap(user_config, default_config)

print(f"--- ChainMap ---")
# Lookups check `user_config` first, then `default_config`
print(f"Theme: {combined_config['theme']}")             # From default_config
print(f"Font Size: {combined_config['font_size']}")     # From user_config (overrides default)
print(f"Language: {combined_config['language']}")       # From user_config

# Modifying the ChainMap affects ONLY the first dictionary in the chain
combined_config['language'] = 'JavaScript'
print(f"Modified user_config: {user_config}")

# --- End of File ---