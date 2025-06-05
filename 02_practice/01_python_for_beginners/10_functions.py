# ----------------------------------- Basics ----------------------------------- #
# A function is a block of organized code that is used to perform a single task. They provide better modularity for your application and reuse-ability.
def hello():
    print("Hello!")


hello()  # -> Hello!


# Function Arguments:
def say_hello(name):
    print(f"Hello {name}!")


say_hello("Ibrahim")  # -> Hello Ibrahim!
say_hello(name="Aykut")  # -> Hello Aykut!


# Return Values:
def add(number_1, number_2):
    return number_1 + number_2


total = add(2, 3)
print(total)  # -> 5


# --------------------------- Local and Global Scope --------------------------- #
# Code in the global scope cannot use any local variables. However, a local scope can access global variables.
# Code in a function’s local scope cannot use variables in any other local scope.
# You can use the same name for different variables if they are in different scopes. That is, there can be a local variable named spam and a global variable also named spam.
global_variable = "I am available everywhere"


def some_function():
    print(global_variable)  # because is global
    local_variable = "Only available within this function"


print(local_variable)  # raises NameError

# If you need to modify a global variable from within a function, use the global statement:


def spam():
    global eggs
    eggs = "spam"


eggs = "global"
spam()
print(eggs)  # -> spam


# ------------------------------ Nested Functions ------------------------------ #
# Functions nested in another function is only visible inside that function. They are used to create utilities that are useful for only the main function
def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(" ")
    for word in words:
        say(word)


talk("I am going.")
"""
I
am
going.
"""


# If we want to access a variable declared inside the outer function from the inner function, we have to use the keyword nonlocal
def count():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        print(count)

    increment()


count()  # -> 1

# ----------------------------------- Closure ---------------------------------- #
# A closure allows a function to remember and access variables from its lexical scope, even when the function is executed outside that scope.


def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count

    return increment


increment = counter()

print(increment())  # -> 1
print(increment())  # -> 2
print(increment())  # -> 3

# ------------------------------ Lambda Functions ------------------------------ #
# Lambda functions are useful when combined with other functions such as map, filter, and reduce. Check 13_map_filter_reduce.py for more information
