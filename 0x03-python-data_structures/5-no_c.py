#!/usr/bin/python3
def no_c(my_string):
    """Removes all the characters c and C from a string"""
    new_str = []
    for char in my_string:
        if char == 'c' or char == 'C':
            continue
        new_str.append(char)
    new_str = "".join(new_str)
    return new_str
