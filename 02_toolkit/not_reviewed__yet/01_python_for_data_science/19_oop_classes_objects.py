# 19_oop_classes_objects.py

# =======================================
# 1. INTRODUCTION TO OOP
# =======================================
# - Object-Oriented Programming (OOP) is a way of thinking about and structuring code.
# - It's based on two core concepts:
#   - Class: A blueprint for creating objects. It defines a set of attributes and methods.
#   - Object: An instance of a class. It's a concrete entity created from the blueprint.
#
# - Analogy: A `Car` class is the blueprint. Your specific car (a red Tesla Model 3) is an object.
#   - Attributes: Data associated with an object (e.g., color='red', make='Tesla').
#   - Methods: Functions that belong to an object (e.g., drive(), brake()).


# =======================================
# 2. DEFINING A CLASS AND CREATING OBJECTS
# =======================================
# - Use the `class` keyword. Class names traditionally use PascalCase.
# - Creating an object (instantiation) is done by calling the class name as if it were a function.

class Car:
    # `pass` is a placeholder indicating an empty block.
    pass

# Create two separate instances (objects) of the Car class
car_1 = Car()
car_2 = Car()

print(f"Object 1: {car_1}")
print(f"Object 2: {car_2}")
print(f"Are they the same object? {car_1 == car_2}") # False, they are different instances
print("-" * 30)


# =======================================
# 3. THE `__init__()` METHOD (CONSTRUCTOR)
# =======================================
# - A special method that is automatically called when a new object is created.
# - Its primary job is to initialize the object's attributes.
# - The `self` parameter refers to the specific instance of the class being created.

class Dog:
    # --- Class Attribute ---
    # This attribute is shared by ALL instances of the Dog class.
    species = "Canis familiaris"

    def __init__(self, name, age):
        # --- Instance Attributes ---
        # These attributes are unique to each instance (each dog).
        # We use `self` to attach them to the specific object.
        self.name = name
        self.age = age
        print(f"A new dog named '{self.name}' has been created!")

# Create two Dog objects. The `__init__` method is called for each one.
dog_1 = Dog("Fido", 5)
dog_2 = Dog("Lucy", 3)

# Accessing instance attributes using dot notation
print(f"\n{dog_1.name} is {dog_1.age} years old.")
print(f"{dog_2.name} is {dog_2.age} years old.")

# Accessing the shared class attribute
print(f"{dog_1.name} belongs to the species '{dog_1.species}'.")
print("-" * 30)


# =======================================
# 4. INSTANCE METHODS
# =======================================
# - Functions defined inside a class that perform actions on an object.
# - They must have `self` as their first parameter to access the object's attributes.

class DataProcessor:
    def __init__(self, data_list):
        self.data = data_list

    # An instance method that uses the object's data
    def calculate_average(self):
        """Calculates the average of the object's data list."""
        if not self.data:
            return 0
        return sum(self.data) / len(self.data)

    # Another instance method
    def add_value(self, value):
        """Adds a new value to the data list."""
        self.data.append(value)
        print(f"Added {value}. New data: {self.data}")

# Create an instance of DataProcessor
proc = DataProcessor([10, 20, 30, 40, 50])

# Call its methods
avg = proc.calculate_average()
print(f"Initial data: {proc.data}")
print(f"Average: {avg}")

proc.add_value(60)
new_avg = proc.calculate_average()
print(f"New average: {new_avg}")
print("-" * 30)


# =======================================
# 5. THE `__str__()` METHOD
# =======================================
# - A special method that controls what gets displayed when you `print()` an object.
# - It should return a user-friendly string.
# - If you don't define it, printing an object gives you a default, unhelpful representation.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        # This determines what `print(my_book)` will output
        return f"'{self.title}' by {self.author}"

book_1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams")
book_2 = Book("Dune", "Frank Herbert")

# The __str__ method is called automatically by print()
print("--- My Library ---")
print(f"Book 1: {book_1}")
print(f"Book 2: {book_2}")


# --- End of File ---