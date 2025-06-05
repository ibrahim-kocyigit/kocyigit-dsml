# ----------------------------------- Basics ----------------------------------- #
# Sets are like dictionaries without keys.

names_1 = {"Ibrahim", "Aykut"}
names_2 = {"Ibrahim"}
names_3 = {"John"}

intersect = names_1 & names_2
print(intersect)  # -> {'Ibrahim'}

mod = names_1 | names_3
print(mod)  # -> {'Ibrahim', 'Aykut', 'John'}

difference = names_1 - names_2
print(difference)  # -> {'Aykut'}

is_superset = names_1 > names_2
print(is_superset)  # -> True

is_subset = names_2 < names_1
print(is_subset)  # -> True

# Sets cannot have two of the same item:
names_3 = {"John", "John"}
print(names_3)  # -> {'John'}
