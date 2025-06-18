import json
import os

# =======================================
# 1. WHAT IS JSON?
# =======================================
# - JSON (JavaScript Object Notation) is a lightweight, text-based data format.
# - It's easy for humans to read and for machines to parse.
# - It is the de-facto standard for APIs and data exchange on the web.
# - The `json` module maps Python objects to JSON objects and vice-versa:
#   - Python `dict`      <-> JSON `object` `{}`
#   - Python `list`, `tuple` <-> JSON `array` `[]`
#   - Python `str`        <-> JSON `string` `""`
#   - Python `int`, `float` <-> JSON `number`
#   - Python `True`/`False` <-> JSON `true`/`false`
#   - Python `None`       <-> JSON `null`


# =======================================
# 2. SERIALIZATION: PYTHON TO JSON
# =======================================
# - Serialization is the process of converting a Python object into a JSON string.
# - `json.dumps()`: "Dump String" - Converts a Python object to a JSON formatted string.
# - `json.dump()`: Converts a Python object and writes it directly to a file.

# --- Step 1: Set up a folder for our JSON files ---
JSON_FOLDER = "json_files"
os.makedirs(JSON_FOLDER, exist_ok=True)
file_path = os.path.join(JSON_FOLDER, "user_profile.json")

# --- A sample Python dictionary ---
user_data = {
    "userId": 101,
    "username": "py_master",
    "isActive": True,
    "courses": ["Python Fundamentals", "Intermediate Python"],
    "last_login": None,
}

# --- Using `json.dumps()` to create a string ---
print("--- `json.dumps()` (Python -> JSON String) ---")
# This is a compact, machine-readable string
json_string_compact = json.dumps(user_data)
print(f"Compact JSON string: {json_string_compact}")

# Use the `indent` parameter for "pretty-printing"
json_string_pretty = json.dumps(user_data, indent=4, sort_keys=True)
print(f"\nPretty JSON string:\n{json_string_pretty}")


# --- Using `json.dump()` to write directly to a file ---
print(f"\n--- `json.dump()` (Python -> JSON File) ---")
try:
    with open(file_path, "w") as f:
        json.dump(user_data, f, indent=4)
    print(f"Successfully wrote data to '{file_path}'")
except IOError as e:
    print(f"Error writing to file: {e}")

print("-" * 30)


# =======================================
# 3. DESERIALIZATION: JSON TO PYTHON
# =======================================
# - Deserialization is the process of parsing a JSON string into a Python object.
# - `json.loads()`: "Load String" - Parses a JSON formatted string.
# - `json.load()`: Parses a JSON formatted stream from a file.

# --- Using `json.loads()` from a string ---
print("--- `json.loads()` (JSON String -> Python) ---")
# Imagine this string came from a web API response
api_response_string = '{"city": "Aydın", "country": "Türkiye", "population": 207554}'
location_data = json.loads(api_response_string)

print(f"Parsed Python dictionary: {location_data}")
print(f"Accessing a value: {location_data['country']}")


# --- Using `json.load()` to read from a file ---
print(f"\n--- `json.load()` (JSON File -> Python) ---")
try:
    with open(file_path, "r") as f:
        loaded_user_data = json.load(f)
    print("Successfully loaded data from file.")
    print(f"Username from file: {loaded_user_data['username']}")
    print(f"Courses: {loaded_user_data['courses']}")
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error reading or parsing file: {e}")

print("-" * 30)


# =======================================
# 4. HANDLING ERRORS
# =======================================
# - If you try to parse text that is not valid JSON, a `json.JSONDecodeError` is raised.

invalid_json = '{"name": "test", "is_valid": True,}'  # Extra comma makes it invalid

print("--- Handling JSON Errors ---")
try:
    json.loads(invalid_json)
except json.JSONDecodeError as e:
    print("Caught an invalid JSON string!")
    print(f"Error details: {e}")

# --- End of File ---
