# ----------------------------------- Basics ----------------------------------- #
# Dictionaries hold key-value pairs

# Create an empty dictionary
empty_dict = {}

# Create a dictionary with initial key-value pairs
dog = {"name": "Roger", "age": 8}

print(dog)  # -> {'name': 'Roger', 'age': 8}
type(dog)  # -> dict

# Copy a dictionary
dog_copy = dog.copy()

# Change a value
dog["name"] = "Syd"
print(dog["name"])  # -> "Syd"

# Add a new key-value pair
dog["color"] = "black"
print(dog)  # -> {'name': 'Syd', 'age': 8, 'color': 'black'}

# Remove a key-value pair
print(dog.pop("color"))  # -> "black" (Because .pop also returns the value it deleted)
print(dog)  # -> {'name': 'Syd', 'age': 8}

print(dog.popitem())  # -> ('age', 8) (removes and returns the last key-value pair)
print(dog)  # -> {'name': 'Syd'}

dog["best_friend"] = "rabbit"
del dog["best_friend"]  # Deletes the key-value pair without returning it
print(dog)  # -> {'name': 'Syd'}


# ------------------------------ Retrieve Values ------------------------------- #
# Retrieve values based on keys
print(dog["name"])  # -> "Syd"
print(dog.get("name"))  # -> "Syd"
print(dog.get("color", "brown"))  # If cannot find dog["color"], it returns "brown"
dog["color"]  # KeyError! (Statement above didn't add a new key-value pair)

print(dog.get("name", "Alex"))  # -> "Syd" (Because it already exists)

dog["age"] = 8

# Retrieve all values
print(dog.values())  # -> dict_values(['Syd', 8])
print(list(dog.values()))  # -> ['Syd', 8]

# Retrieve all keys
print(dog.keys())  # -> dict_keys(['name', 'age'])
print(list(dog.keys()))  # -> ['name', 'age']

# Retrieve all items
print(dog.items())  # -> dict_items([('name', 'Syd'), ('age', 8)])
print(list(dog.items()))  # -> [('name', 'Syd'), ('age', 8)]

# Check if a key or a value exists
print("name" in dog)  # -> True
print("Syd" in dog.values())  # True
