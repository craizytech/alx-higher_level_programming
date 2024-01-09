#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the biggest integer of a list."""
    num = my_list[0]
    for x in my_list:
        if x > num:
            num = x
    return num
