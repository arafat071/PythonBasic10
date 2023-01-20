"""
And
OR
NOT
"""

"""
AND: Check whether two conditions are equal. Returns True if they are equal else False
OR: Checks multiple conditions are equal. Returns True if either or not both are equal or False
NOT: Checks single condition. Reverse order. Returns True if the condition is False.
"""


def AND(condition1, condition2):
    if condition1 and condition2:
        return True
    else:
        return False


print(AND(True, False))


def OR(condition1, condition2, condition3):
    if condition1 or condition2:
        return True
    else:
        return False


print(OR(False, True,False))


def NOT(condition):
    if not condition:
        return True
    else:
        return False


print(NOT(True))
