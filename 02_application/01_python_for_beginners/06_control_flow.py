# ------------------------------- If Statements -------------------------------- #

age = 17

if age >= 18:
    print("You can drive and vote.")
elif age >= 16:
    print("You can drive, but you can't vote.")
else:
    print("You can neither drive nor vote.")


# ------------------------ Ternary Conditional Operator ------------------------ #

age = 17
print("kid" if age < 18 else "adult")  # -> kid
print("kid" if age < 13 else "teen" if age < 18 else "adult")  # -> teen


# --------------------------- Switch-Case Statement ---------------------------- #

today = "Friday"
match today:
    case "Monday":
        print("You can fall apart")
    case "Tuesday" | "Wednesday":
        print("Break my heart")
    case "Thursday":
        print("Doesn't even start")
    case "Friday":
        print("I'm in love.")
    case "Saturday":
        print("Wait!")
    case "Sunday":
        print("Always comes too late.")
    case _:
        print("That's not a day mate.")
# -> I'm in love.


today_responses = [200, 300, 404, 500]
match today_responses:
    case [a]:
        print(f"One response today: {a}")
    case [a, b]:
        print(f"Two responses today: {a} and {b}")
    case [a, b, *rest]:
        print(f"All responses: {a}, {b}, {rest}")
# -> All responses: 200, 300, [404, 500]


response_code = "300"
match response_code:
    case int():
        print("Code is a number")
    case str():
        print("Code is a string")
    case _:
        print("Code is neither a string nor a number")
# -> Code is a string


# --------------------------- while Loop Statements ---------------------------- #

spam = 0
while spam < 5:
    print("Hello world!")
    spam += 1

# `break` exits the while loop immediately
while True:
    name = input("Please enter your name")
    if name == "your name":
        break
print("Thank you!")

# `continue` jumps back to the start of the loop
while True:
    name = input("What's your name? ")
    if name != "ibrahim":
        continue
    password = input("What's your password? (Your favorite number) ")
    if password == "8":  # or if int(password) == 8:
        break
print("Access Granted")


# ---------------------------------- For Loop ---------------------------------- #

pets = ["Dog", "Cat", "Bird"]
for pet in pets:
    print(pet)

# `range` returns a sequence of numbers starting from 0, increments by 1, and stops before a specified number
for i in range(5):
    print(i)
"""
0
1
2
3
4
"""

# arguments can be modified: range(start, stop, step)
for i in range(0, 10, 2):
    print(i)
"""
0
2
4
6
8
"""

for i in range(5, -1, -1):
    print(f"{i} seconds to the clash!")
"""
5 seconds to the clash!
4 seconds to the clash!
3 seconds to the clash!
2 seconds to the clash!
1 seconds to the clash!
0 seconds to the clash!
"""

# `For Else` Statement

for x in range(3):
    print(x)
else:
    print("Finished!")
"""
0
1
2
Finished!
"""
