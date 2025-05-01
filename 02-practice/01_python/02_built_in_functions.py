# Return the absolute value of a number
abs(-2.5)  # -> 2.5


# Return True if all elements of the iterable are true (or if the iterable is empty).
all([1, 2, 3])  # -> True
all(["a" == "b", "c" == "c"])  # -> False
all([])  # -> True


# Return True if any element of the iterable is true. If the iterable is empty, return False.
any([1, 2, 3])  # -> True
any(["a" == "b", "c" == "c"])  # -> True
any([])  # -> False


# Return a Boolean value, True or False.
bool()  # -> False
bool("")  # -> False
bool("a")  # -> True
print(bool("a") + bool(0))  # -> 1 (1 + 0 = 1)


# Return an enumarate object. Usually used in a for loop to get the index
for i, item in enumerate([1, 2, 3, 4, 5]):
    print(f"Item {item} is at index {i}")
"""
Output:
Item 1 is at index 0
Item 2 is at index 1
Item 3 is at index 2
Item 4 is at index 3
Item 5 is at index 4
"""


# Filter a sequence (e.g., a list, a tuple, etc.) by applying a certain condition to each element in the sequence.
def is_even(num):
    return num % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # -> [2, 4, 6]
