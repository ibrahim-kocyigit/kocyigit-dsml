# ----------------------------------- Basics ----------------------------------- #
greeting = "Hello"
name = "Ibrahim"

print(greeting + " " + name)  # -> "Hello Ibrahim"
print(2 * greeting)  # -> "HelloHello"

age = str(42)
print(type(age))  # -> <class 'str'>

# Multi-line strings
print("""
I am
42
years
old.
""")


# --------------------------- Common String Methods ---------------------------- #
# (*) All these methods return new string. Original string's not effected.

my_str = "name@mail.com"

my_str.isalpha()  # check if a string contains only characters # -> False
my_str.isalnum()  # check if a string contains characters or digits # -> False
my_str.isdecimal()  # check if a string contains digits # -> False

my_str.lower()  # get a lowercase version of a string # -> 'name@mail.com'
my_str.islower()  # check if a string is lowercase # -> True
my_str.upper()  # get an uppercase version of a string -> 'NAME@MAIL.COM'
my_str.isupper()  # check if a string is uppercase -> -> False (*)
my_str.title()  # to get a capitalized version of a string -> # -> 'Name@Mail.Com'

my_str.startswith("substring")  # check if a string starts with a specific substring
my_str.endswith("substring")  # check if a string ends with a specific substring

my_str.replace("mail", "yahoo")  # replace a part of a string -> 'name@yahoo.com'
my_str.split("@")  # split on a specific character seperator # -> ['name', 'mail.com']
my_str.strip()  # trim the white space from a string
my_str.join("__")  # append new letters to a string # -> "_name@mail.com_"
my_str.find("ame")  # find the position of a substring -> 1 (the index)

# We can use built-in functions with strings too
len("ibrahim")  # -> 7
print("ibr" in "ibrahim")  # -> True


# ---------------------------- Escaping Characters ----------------------------- #
# Use `\` to tell Python to treat the next character as part of the string
print('Cat\'s name is "Meow"')  # -> "Cat's name is "Meow""
print("\\ is an escaping character!")  # -> "\ is an escaping character!"

# Use `\` to tell Python to format the output in a specific way
print("This is the first line.\nAnd this is the second line.")


# ------------------------ String Characters & Slicing ------------------------- #
name = "Ibrahim"

# `[index]` returns a specific character
name[0]  # -> "I"
name[-1]  # -> "m"

# `[starting_index_inclusive : ending_index_exclusive : step]` returns a substring
name[1:3]  # -> "br" (same as `name[1:3:0]`)
name[1:-2]  # -> "brah" (same as `name[1:-2:0]`)
name[:3]  # -> "Ibr" (Same as `name[0:3]`)
name[3:]  # -> "ahim" (Same as `name[3:0]`)
name[::2]  # -> "Irhm" (same as `name[0:0:0]`)
name[1:5:2]  # -> "ba"
name[::-1]  # -> 'miharbI' ('step = -1' means reverse)
