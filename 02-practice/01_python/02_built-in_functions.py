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


# Invoke the built-in help system
help(type)  # Prints info about the type object


# Return True if the object argument is an instance of an object.
isinstance(1, int)  # -> True
isinstance(1, str)  # -> False


# Return an iterator that applies function to every item of iterable. The type of element stored to the map object will be identical to the type returned from the function.
def double(x):
    return x * 2


nums = [1, 2, 3, 4, 5]
list(map(double, nums))  # [2, 4, 6, 8, 10]

original_dict = {"a": 2, "b": 3}
dict(map(lambda item: (item[0], item[1] * 2), original_dict.items()))


# Return the largest or smallest item in an iterable.
nums = [1, 2, 3, 4, 5]
max(nums)  # -> 5
min(nums)  # -> 1


# Return number rounded to ndigits precision after the decimal point.
round(1.45)  # -> 1
round(1.5)  # -> 2
round(1.65)  # -> 2
round(1.45, ndigits=1)  # 1.4
round(2 / 3, ndigits=3)  # 0.667


# Return a new sorted list from the items in iterable.
sorted([1, 2, 3, 7, 4])  # [1, 2, 3, 4, 7]


# Sums start and the items of an iterable from left to right and returns the total.
sum([2, 4, 6])  # -> 12
