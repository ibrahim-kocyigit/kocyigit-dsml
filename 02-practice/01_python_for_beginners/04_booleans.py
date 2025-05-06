done = True
postponed = False

# Most commonly use in control flows
if done:
    print("Yes")
else:
    print("No")

# Numbers are always True, except for number zero
print("True") if 1 else print("False")  # -> "True"
print("True") if 0 else print("False")  # -> "False"
print("True") if 3.14 else print("False")  # -> "True"
print("True") if -1 else print("False")  # -> "True"

# Strings, lists, sets, tuples, dictionaries are always True, unless empty
print("True") if "" else print("False")  # -> "False"
print("True") if "a" else print("False")  # -> "True"
print("True") if [1] else print("False")  # -> "True"
print("True") if [] else print("False")  # -> "False"

# `any` and `all` functions
written_exam_passed = True
oral_exam_passed = False

can_take_new_lesson = any([written_exam_passed, oral_exam_passed])  # -> True
can_graduate = all([written_exam_passed, oral_exam_passed])  # -> False
