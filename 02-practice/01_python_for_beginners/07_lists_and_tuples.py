# ----------------------------------- Basics ----------------------------------- #
# Create an empy list
empty_list = []
type(empty_list)  # -> list

# Create a list with existing values
dogs = ["Roger", "Syd"]  # a list of strings
random_values = ["String", 1, True]

# Check if a specific element is in the list
print("Roger" in dogs)  # -> True

# Check the frequency of an element
dogs.count("Dog")  # -> 0
dogs.count("Roger")  # -> 1

# Lists are 0-index as well
print(dogs[0])  # -> "Roger"
print(dogs.index("Syd"))  # -> 1

# Updating an element in the list
dogs[1] = "Beau"
print(dogs)  # -> ['Roger', 'Beau']

# Copying a list
dogs_copy = dogs.copy()


# ---------------------------- Adding New Elements ----------------------------- #
dogs.append("Mika")  # Provide an element to add
print(dogs)  # -> ['Roger', 'Beau', 'Mika']

dogs.extend(["Judah", "Masha"])  # Provide a list to add
dogs += ["Dali"]  # Same as .extend() -- Provide a list!
print(dogs)

items = ["rock", "scissors"]
items.insert(1, "paper")  # inserted element will be index 1
print(items)  # -> ['rock', 'paper', 'scissors']

counting = ["one", "two", "five"]
counting[2:1] = ["three", "four"]  # insert multiple elements
print(counting)  # -> ['one', 'two', 'three', 'four', 'five']


# --------------------------- Subsetting and Slicing --------------------------- #
# Returns a new list.
print(dogs)  # -> ['Roger', 'Beau', 'Mika', 'Judah', 'Masha', 'Dali']
dogs[1:3]  # -> ['Beau', 'Mika']
dogs[1:-2]  # -> ['Beau', 'Mika', 'Judah']
dogs[:3]  # -> ['Roger', 'Beau', 'Mika']
dogs[3:]  # -> ['Judah', 'Masha', 'Dali']
dogs[::2]  # -> ['Roger', 'Mika', 'Masha']
dogs[1:5:2]  # -> ['Beau', 'Judah']
dogs[::-1]  # -> ['Dali', 'Masha', 'Judah', 'Mika', 'Beau', 'Roger']


# ----------------------------- Removing Elements ------------------------------ #
dogs.remove("Roger")
print(dogs)  # -> ['Beau', 'Mika', 'Judah', 'Masha', 'Dali']

last_dog = dogs.pop()  # Removes and returns the last element
print(last_dog)  # -> "Dali"
print(dogs)  # -> ['Beau', 'Mika', 'Judah', 'Masha']


# ------------------------------- Sorting Lists -------------------------------- #
exam_scores = [45, 33, 66, 89, 43, 90, 74]
exam_scores.sort()  # original list updated
print(exam_scores)  # [33, 43, 45, 66, 74, 89, 90]

# If you don't want to update the original:
print(sorted(exam_scores))  # [33, 43, 45, 66, 74, 89, 90]

# Sorting in descending order
exam_scores = [45, 33, 66, 89, 43, 90, 74]
exam_scores.sort(reverse=True)
print(exam_scores)  # -> [90, 89, 74, 66, 45, 43, 33]

# Sorting in alphabetical order
students = ["Jack", "Jill", "Adam", "Eve", "bill"]
students.sort()
print(students)  # -> ['Adam', 'Eve', 'Jack', 'Jill', 'bill'] # Capital letters first!

students = ["Jack", "Jill", "Adam", "Eve", "bill"]
students.sort(key=str.lower)
print(students)  # -> ['Adam', 'bill', 'Eve', 'Jack', 'Jill']


# ----------------------------------- Tuples ----------------------------------- #
# Tuples are like lists, but immutable

names = ("Ibrahim", "Aykut")
type(names)  # -> tuple

print(names)  # -> ('Ibrahim', 'Aykut')

# Any method/built-in function that works with lists without modifying them works with tuples too
print(sorted(names))  # -> ['Aykut', 'Ibrahim']
names.sort()  # Won't work
