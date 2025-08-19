# 20_oop_inheritance.py

# =======================================
# 1. WHAT IS INHERITANCE?
# =======================================
# - A mechanism that allows a new class to adopt the properties (attributes and methods) of an existing class.
# - The existing class is called the Parent Class, Superclass, or Base Class.
# - The new class is called the Child Class, Subclass, or Derived Class.
# - This establishes an "is-a" relationship (e.g., a Dog "is an" Animal).
# - Key benefit: Code reusability and establishing a logical class hierarchy.


# =======================================
# 2. BASIC INHERITANCE
# =======================================
# - To create a child class, pass the parent class in parentheses in the class definition.

# --- Parent Class ---
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal '{self.name}' created.")

    def eat(self):
        print(f"{self.name} is eating.")

    def speak(self):
        print(f"{self.name} makes a generic sound.")

# --- Child Class ---
# Dog inherits from Animal
class Dog(Animal):
    # For now, the Dog class is empty, but it inherits everything from Animal.
    pass

# Create an instance of the child class
my_dog = Dog("Buddy")

# We can call methods from the parent Animal class on our Dog object
my_dog.eat()
my_dog.speak()
print("-" * 30)


# =======================================
# 3. METHOD OVERRIDING AND `super()`
# =======================================
# - Method Overriding: A child class can provide its own specific implementation
#   of a method that is already defined in its parent class.
# - `super()`: A special function that allows you to call methods from the parent class.
#   This is crucial for extending, not just replacing, parent behavior.

class Cat(Animal):
    def __init__(self, name, breed):
        # Call the parent's __init__ method using super() to handle the `name` attribute.
        # This ensures the parent's setup logic is executed.
        super().__init__(name)
        
        # Add a new attribute specific to the Cat class
        self.breed = breed
        print(f"It's a {self.breed} cat.")

    # Override the speak method to be cat-specific
    def speak(self):
        print(f"{self.name} says 'Meow!'")

    # A new method specific to Cat
    def purr(self):
        print(f"{self.name} is purring...")

my_cat = Cat("Whiskers", "Siamese")
my_cat.eat()      # Inherited from Animal
my_cat.speak()    # Overridden in Cat
my_cat.purr()     # Defined in Cat
print("-" * 30)


# =======================================
# 4. MULTI-LEVEL INHERITANCE
# =======================================
# - When a child class inherits from another child class. This creates a deeper hierarchy.
#   (e.g., Animal -> Dog -> WorkingDog)

# Re-defining Dog with its own overridden method for this example
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says 'Woof!'")

# WorkingDog inherits from Dog, which inherits from Animal
class WorkingDog(Dog):
    def __init__(self, name, job):
        super().__init__(name)
        self.job = job

    def report_for_duty(self):
        print(f"{self.name} the {self.job} is ready to work!")

police_dog = WorkingDog("Rex", "K-9 Officer")
police_dog.eat()            # From Animal
police_dog.speak()          # From Dog (the immediate parent)
police_dog.report_for_duty() # From WorkingDog
print("-" * 30)


# =======================================
# 5. MULTIPLE INHERITANCE
# =======================================
# - A class can inherit from more than one parent class.
# - Syntax: `class Child(Parent1, Parent2, ...)`
# - Python searches for methods in the parents from left to right.
# - Note: Can be complex. Use with care.

class Flyer:
    def fly(self):
        print("Spreading wings and taking off!")

class Swimmer:
    def swim(self):
        print("Paddling through the water.")

# Duck inherits from both Flyer and Swimmer
class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack!")

donald = Duck()
donald.quack() # From Duck
donald.fly()   # From Flyer
donald.swim()  # From Swimmer


# --- End of File ---