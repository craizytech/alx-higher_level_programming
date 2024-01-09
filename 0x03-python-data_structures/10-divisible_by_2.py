#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Finds all multiples of 2."""
    list = []
    for x in my_list:
        if x % 2 == 0:
            list.append(True)
        elif x % 2 != 0:
            list.append(False)
    return list
