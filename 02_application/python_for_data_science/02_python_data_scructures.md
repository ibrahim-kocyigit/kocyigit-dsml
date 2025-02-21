# Python Data Structures

* [1. Lists](#1-lists)
* [2. Tuples](#2-tuples)
* [3. Dictionaries](#3-dictionaries)
* [4. Sets](#4-sets)


## 1. Lists

**1. Creating a List**  
A list is a built-in data type that represents an ordered and mutable collection of elements. Lists are enclosed in square brackets `` and elements are separated by commas.
```python
fruits = ["apple", "banana", "orange", "mango"] 
```

**2. Add an element to the end**  
The `append()` method is used to add an element to the end of a list.
```python
fruits = ["apple", "banana", "orange"] 
fruits.append("mango") 
print(fruits) # ['apple', 'banana', 'orange', 'mango']
```

**3. Create a shallow copy**  
The `copy()` method is used to create a shallow copy of a list.
```python
new_list = my_list.copy() 
print(new_list) #
```

**4. Count occurrences of an element**  
The `count()` method is used to count the number of occurrences of a specific element in a list in Python.
```python
count = my_list.count(2) 
print(count) # 4
```

**5. Remove an element by index**  
The `del` statement is used to remove an element from list. `del` statement removes the element at the specified index.
```python
del my_list # Removes the element at index 2 
print(my_list) #
```

**6. Add multiple elements**  
The `extend()` method is used to add multiple elements to a list. It takes an iterable (such as another list, tuple, or string) and appends each element of the iterable to the original list.
```python
fruits = ["apple", "banana", "orange"] 
more_fruits = ["mango", "grape"] 
fruits.extend(more_fruits) 
print(fruits) # ['apple', 'banana', 'orange', 'mango', 'grape']
```

**7. Access elements by index**  
Indexing in a list allows you to access individual elements by their position. In Python, indexing starts from 0 for the first element and goes up to `length_of_list - 1`.
```python
print(my_list)  # 10 (accessing the first element) 
print(my_list[-1]) # 50 (accessing the last element using negative indexing)
```

**8. Insert an element at a specific index**  
The `insert()` method is used to insert an element at a specified index.
```python
my_list.insert(2, 6)  
print(my_list) #
```

**9. Modify an element**  
You can use indexing to modify or assign new values to specific elements in the list.
```python
my_list = 25 # Modifying the second element 
print(my_list) #
```

**10. Remove and return an element by index**  
`pop()` method is another way to remove an element from a list in Python. It removes and returns the element at the specified index. If you don't provide an index to the `pop()` method, it will remove and return the last element of the list by default.
```python
removed_element = my_list.pop(2) # Removes and returns the element at index 2 
print(removed_element) # 30 
print(my_list) # 

removed_element = my_list.pop() # Removes and returns the last element 
print(removed_element) # 50
print(my_list) #
```

**11. Remove an element by value**  
To remove an element from a list by its value, use the `remove()` method. The `remove()` method removes the first occurrence of the specified value.
```python
my_list.remove(30) # Removes the element 30 
print(my_list) #
```

**12. Reverse the list**  
The `reverse()` method is used to reverse the order of elements in a list.
```python
my_list.reverse() 
print(my_list) #
```

**13. Slicing**  
You can use slicing to access a range of elements from a list.
```python
print(my_list[1:4])  # (elements from index 1 to 3)
print(my_list[:3])  # (elements from the beginning up to index 2) 
print(my_list[2:])  # (elements from index 2 to the end) 
print(my_list[::2]) # (every second element)
```

**14. Sort the list**  
The `sort()` method is used to sort the elements of a list in ascending order. If you want to sort the list in descending order, you can pass the `reverse=True` argument to the `sort()` method.
```python
my_list.sort() 
print(my_list) # 

my_list.sort(reverse=True) 
print(my_list) #
```

## 2. Tuples

**1. Count occurrences of an element**  
The `count()` method for a tuple is used to count how many times a specified element appears in the tuple.
```python
fruits = ("apple", "banana", "apple", "orange")
print(fruits.count("apple")) # 2
```

**2. Find the index of an element**  
The `index()` method in a tuple is used to find the first occurrence of a specified value and returns its position (index). If the value is not found, it raises a ValueError.
```python
fruits = ("apple", "banana", "orange")
print(fruits.index("banana")) # 1
```

**3. Calculate the sum of elements**  
The `sum()` function in Python can be used to calculate the sum of all elements in a tuple, provided that the elements are numeric (integers or floats).
```python
numbers = (10, 20, 5, 30)
print(sum(numbers)) # 65
```

**4. Find the smallest and largest elements**  
Find the smallest (`min()`) or largest (`max()`) element in a tuple.
```python
numbers = (10, 20, 5, 30)
print(min(numbers)) # 5
print(max(numbers)) # 30
```

**5. Get the length**  
Get the number of elements in the tuple using `len()`.
```python
fruits = ("apple", "banana", "orange")
print(len(fruits)) # 3
```

## 3. Dictionaries

**1. Creating a Dictionary**  
A dictionary is a built-in data type that represents a collection of key-value pairs. Dictionaries are enclosed in curly braces `{}`.
```python
dict_name = {} # Creates an empty dictionary
person = { "name": "John",  "age": 30, "city": "New York"}
```

**2. Accessing Values**  
You can access the values in a dictionary using their corresponding keys.
```python
name = person["name"] # "John"
age = person["age"] # 30
```

**3. Add or Modify**  
Inserts a new key-value pair into the dictionary. If the key already exists, the value will be updated; otherwise, a new entry is created.
```python
person["Country"] = "USA" # A new entry will be created.
person["city"] = "Chicago"  # Update the existing value for the same key
```

**4. Delete a key-value pair**  
Removes the specified key-value pair from the dictionary. Raises a `KeyError` if the key does not exist.
```python
del person["Country"]
```

**5. Update with another dictionary**  
The `update()` method merges the provided dictionary into the existing dictionary, adding or updating key-value pairs.
```python
person.update({"Profession": "Doctor"})
```

**6. Clear the dictionary**  
The `clear()` method empties the dictionary, removing all key-value pairs within it. After this operation, the dictionary is still accessible and can be used further.
```python
grades = {"math": 90, "science": 85}
grades.clear()
```

**7. Check for key existence**  
You can check for the existence of a key in a dictionary using the `in` keyword.
```python
if "name" in person:
    print("Name exists in the dictionary.")
```

**8. Create a copy**  
Creates a shallow copy of the dictionary. The new dictionary contains the same key-value pairs as the original, but they remain distinct objects in memory.
```python
new_person = person.copy()
new_person = dict(person) # another way to create a copy of dictionary
```

**9. Retrieve keys**  
Retrieves all keys from the dictionary and converts them into a list. Useful for iterating or processing keys using list methods.
```python
person_keys = list(person.keys()) # ['name', 'age', 'city', 'Profession']
```

**10. Retrieve values**  
Extracts all values from the dictionary and converts them into a list. This list can be used for further processing or analysis.
```python
person_values = list(person.values()) # ['John', 30, 'Chicago', 'Doctor']
```

**11. Retrieve key-value pairs**  
Retrieves all key-value pairs as tuples and converts them into a list of tuples. Each tuple consists of a key and its corresponding value.
```python
info = list(person.items()) # [('name', 'John'), ('age', 30), ('city', 'Chicago'), ('Profession', 'Doctor')]
```

## 4. Sets

**1. Defining Sets**  
A set is an unordered collection of unique elements. Sets are enclosed in curly braces `{}`. They are useful for storing distinct values and performing set operations.
```python
empty_set = set() # Creating an Empty Set
fruits = {"apple", "banana", "orange"}
```

**2. Add an element**  
Elements can be added to a set using the `add()` method. Duplicates are automatically removed, as sets only store unique values.
```python
fruits.add("mango") # {'apple', 'banana', 'orange', 'mango'}
```

**3. Clear the set**  
The `clear()` method removes all elements from the set, resulting in an empty set. It updates the set in-place.
```python
fruits.clear() # set()
```

**4. Create a copy**  
The `copy()` method creates a shallow copy of the set. Any modifications to the copy won't affect the original set.
```python
new_fruits = fruits.copy()
```

**5. Discard an element**  
Use the `discard()` method to remove a specific element from the set. Ignores if the element is not found.
```python
fruits = {"apple", "banana", "orange"}
fruits.discard("apple") # {'banana', 'orange'}
```

**6. Check if it is a subset**  
The `issubset()` method checks if the current set is a subset of another set. It returns True if all elements of the current set are present in the other set, otherwise False.
```python
fruits = {"apple", "banana"}
colors = {"apple", "banana", "red", "green"}
is_subset = fruits.issubset(colors) # True
```

**7. Check if it is a superset**  
The `issuperset()` method checks if the current set is a superset of another set. It returns True if all elements of the other set are present in the current set, otherwise False.
```python
fruits = {"apple", "banana"}
colors = {"apple", "banana", "red", "green"}
is_superset = colors.issuperset(fruits) # True
```

**8. Remove and return an arbitrary element**  
The `pop()` method removes and returns an arbitrary element from the set. It raises a `KeyError` if the set is empty. Use this method to remove elements when the order doesn't matter.
```python
fruits = {"apple", "banana", "orange"}
removed_fruit = fruits.pop() # removes and returns an arbitrary element
```

**9. Remove a specific element**  
Use the `remove()` method to remove a specific element from the set. Raises a `KeyError` if the element is not found.
```python
fruits = {"apple", "banana", "orange"}
fruits.remove("banana") # {'apple', 'orange'}
```

**10. Set Operations**  
Perform various operations on sets: `union`, `intersection`, `difference`, `symmetric difference`.
```python
fruits = {"apple", "banana"}
colors = {"red", "apple"}
combined = fruits.union(colors) # {'apple', 'banana', 'red'}
common = fruits.intersection(colors) # {'apple'}
unique_to_fruits = fruits.difference(colors) # {'banana'}
sym_diff = fruits.symmetric_difference(colors) # {'banana', 'red'}
```

**11. Update with another iterable**  
The `update()` method adds elements from another iterable into the set. It maintains the uniqueness of elements.
```python
fruits = {"apple", "banana"}
fruits.update(["kiwi", "grape"]) # {'apple', 'banana', 'kiwi', 'grape'}
```
