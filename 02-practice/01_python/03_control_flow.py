# -------------------- Comparison Operators -------------------- #

"""
==	Equal to
!=	Not equal to
<	Less than
>	Greater Than
<=	Less than or Equal to
>=	Greater than or Equal to
"""

print("Hello" == "hello")  # -> False
print(42 == 42.0)  # -> True
print(42 == "42")  # -> False


# --------------------- Boolean Operators --------------------- #

print(True and True)  # -> True
print(True and False)  # -> False
print(False and True)  # -> False
print(False and False)  # -> False

print(True or True)  # -> True
print(True or False)  # -> True
print(False or True)  # -> True
print(False or False)  # -> False

print(not True)  # -> False
print(not False)  # -> True


# --------------------- Mixing Operators ---------------------- #
print((4 < 5) and (5 < 6))  # -> True
print(2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2)  # -> True
print((5 > 4 or 3 < 4) and 5 > 5)  # -> False


# ----------------------- If Statements ----------------------- #

age = 17

if age >= 18:
    print("You can drive and vote.")
elif age >= 16:
    print("You can drive, but you can't vote.")
else:
    print("You can neither drive nor vote.")


# ---------------- Ternary Conditional Operator ---------------- #

age = 17
print("kid" if age < 18 else "adult")  # -> kid
print("kid" if age < 13 else "teen" if age < 18 else "adult")  # -> teen


# ------------------- Switch-Case Statement -------------------- #

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


# ------------------- while Loop Statements ------------------- #

spam = 0
while spam < 5:
    print("Hello world!")
    spam += 1
