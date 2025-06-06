delegated = False
postponed = True

# Most commonly used in control flows
if delegated:
    print("Delegated")
elif postponed:
    print("Postponed")
else:
    print("Status unknown")  # -> "Postponed"

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
