# ------------------------------ Lambda Functions ------------------------------ #
# Lambda functions, aka anonymous functions have no name and only one expression
# as their body (expression, so it must return a value)
lambda num: num * 2
lambda a, b: a * b

# It doesn't make much sense to assign a lambda function to a variable and call.
# Instead, we use them within built-in functions such as .map(), filter(), and .reduce()


# ------------------------ .map(), .filter(), .reduce() ------------------------ #
numbers = [1, 2, 3, 4, 5]


def multipy_by_two(number):
    return number * 2


# The map() function is used to apply a given function to every item of an iterable, such as a list or tuple, and returns a map object (which is an iterator).
doubles_1 = map(multipy_by_two, numbers)
print(list(doubles_1))  # -> [2, 4, 6, 8, 10]

doubles_2 = map(lambda num: num * 2, numbers)
print(list(doubles_2))  # -> [2, 4, 6, 8, 10]

# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
even_numbers = filter(lambda num: num % 2 == 0, numbers)
print(list(even_numbers))  # -> [2, 4]

# The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along. This function is defined in "functools" module.
from functools import reduce

expenses = [("Dinner", 80), ("Car Repair", 120)]
total = reduce(lambda a, b: a + b[1], expenses, 0)
print(total)  # Output: 200
