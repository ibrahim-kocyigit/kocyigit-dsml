# ---------------------- Regular Functions --------------------- #
def say_hello(name):
    print(f"Hello {name}")


say_hello(name="Ibrahim")  # -> Hello Ibrahim


def add(x, y):
    return x + y


# Return multiple values:
def first_second_set_split(list, first_set_length):
    return list[:first_set_length], list[-(len(list) - first_set_length) :]


my_list = [1, 2, 3, 4, 5]
first_set, second_set = first_second_set_split(my_list, 2)
print(first_set, second_set)  # -> [1, 2, 3] [4, 5]


# ---------------------- Lambda Functions ---------------------- #
# Lambda functions are one-time use, single-line functions with any number of arguments but only one expression)

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)
