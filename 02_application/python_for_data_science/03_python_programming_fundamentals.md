# Python Programming Fundamentals

* [1. Control Flow](#1-control-flow)
* [2. Functions](#2-functions)
* [3. Classes and Objects](#3-classes-and-objects)
* [4. Comparison Operators](#4-comparison-operators)
* [5. Logical Operators](#5-logical-operators)
* [6. Built-in Functions](#6-built-in-functions)

## 1. Control Flow

**1. If Statement**  
Executes code block `if` the condition is `True`.
```python
if temperature > 30: 
    print("It's a hot day!") 
```

**2. If-Else Statement**  
Executes the first code block if the condition is `True`, otherwise the second block.
```python
if age >= 18:
    print("You're an adult.")
else:
    print("You're not an adult yet.")
```

**3. If-Elif-Else**  
Executes the first code block if condition1 is `True`, otherwise checks condition2, and so on. If no condition is `True`, the else block is executed.
```python
score = 85  # Example score
if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B.")
else:
    print("You need to work harder.")
```

**4. For Loop**  
A `for` loop repeatedly executes a block of code for a specified number of iterations or over a sequence of elements (list, range, string, etc.).
```python
for num in range(1, 10): 
    print(num) 

fruits = ["apple", "banana", "orange", "grape", "kiwi"] 
for fruit in fruits:
    print(fruit)
```

**5. While Loop**  
A `while` loop repeatedly executes a block of code as long as a specified condition remains `True`.
```python
count = 0 
while count < 5: 
    print(count) 
    count += 1
```

**6. Loop Controls**  
* `break`: Exits the loop prematurely.
* `continue`: Skips the rest of the current iteration and moves to the next iteration.
```python
for num in range(1, 6):
    if num == 3:
        break
    print(num)

for num in range(1, 6):
    if num == 3:
        continue
    print(num)
```

**7. Try-Except Block**  
Tries to execute the code in the try block. If an exception of the specified type occurs, the code in the except block is executed.
```python
try: 
    num = int(input("Enter a number: ")) 
except ValueError: 
    print("Invalid input. Please enter a valid number.")
```

**8. Try-Except with Else Block**  
Code in the `else` block is executed if no exception occurs in the try block.
```python
try: 
    num = int(input("Enter a number: ")) 
except ValueError: 
    print("Invalid input. Please enter a valid number") 
else: 
    print("You entered:", num)
```

**9. Try-Except with Finally Block**  
Code in the `finally` block always executes, regardless of whether an exception occurred.
```python
try: 
    file = open("data.txt", "r") 
    data = file.read() 
except FileNotFoundError: 
    print("File not found.") 
finally: 
    file.close()
```

## 2. Functions

**1. Define Function**  
A `function` is a reusable block of code that performs a specific task or set of tasks when called.
```python
def greet(name): 
    print("Hello,", name)
```

**2. Function Call**  
A function call is the act of executing the code within the function using the provided arguments.
```python
greet("Alice")
```

**3. Return Statement**  
`return` is a keyword used to send a value back from a function to its caller.
```python
def add(a, b): 
    return a + b 
result = add(3, 5)
```

## 3. Classes and Objects

**1. Class Definition**  
Defines a blueprint for creating objects and defining their attributes and behaviors.
```python
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age
```

**2. Object Creation**
Creates an instance of a class (object) using the class constructor.
```python
person1 = Person("Alice", 25)
```

## 4. Comparison Operators

**1. Equal (==)**  
Checks if two values are equal.
```python
5 == 5 # True
age = 25 
age == 30 # False
```

**2. Not Equal (!=)**  
Checks if two values are not equal.
```python
a = 10 
b = 20 
a!= b # True
count = 0 
count!= 0 # False
```

**3. Greater Than (>)**  
Checks if the value of variable1 is greater than variable2.
```python
9 > 6 # True
age = 20 
max_age = 25 
age > max_age # False
```

**4. Greater Than or Equal To (>=)**  
Checks if the value of variable1 is greater than or equal to variable2.
```python
5 >= 5 and 9 >= 5 # True
quantity = 105 
minimum = 100 
quantity >= minimum # True
```

**5. Less Than (<)**  
Checks if the value of variable1 is less than variable2.
```python
4 < 6 # True
score = 60 
passing_score = 65 
score < passing_score # True
```

**6. Less Than or Equal To (<=)**  
Checks if the value of variable1 is less than or equal to variable2.
```python
5 <= 5 and 3 <= 5 # True
size = 38 
max_size = 40 
size <= max_size # True
```

## 5. Logical Operators

**1. AND**  
Returns `True` if both statement1 and statement2 are `True`. Otherwise, returns `False`.
```python
marks = 90
attendance_percentage = 87

if marks >= 80 and attendance_percentage >= 85:
    print("qualify for honors")
else:
    print("Not qualified for honors")
```

**2. OR**  
Returns `True` if either statement1 or statement2 (or both) are `True`. Otherwise, returns `False`.
```python
grade = 12 
grade == 11 or grade == 12 # True
```

**3. NOT**  
Returns `True` if variable is `False`, and vice versa.
```python
isLocked = False!isLocked # True
```

## 6. Built-in Functions

Python offers a variety of built-in functions to perform common tasks. Here are a few examples:

* **`print()`:** Displays output to the console.
```python
print("Hello, world!")
```

* **`len()`:** Returns the length of a sequence (e.g., string, list, tuple).
```python
my_list =
print(len(my_list))  # Output: 3
```

* **`type()`:** Returns the data type of a variable.
```python
x = 10
print(type(x))  # Output: <class 'int'>
```

* **`range()`:** Generates a sequence of numbers.
```python
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4
```

* **`input()`:** Accepts user input from the console.
```python
name = input("Enter your name: ")
print("Hello,", name)
```