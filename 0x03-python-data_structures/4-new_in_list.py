#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position."""
    if idx < 0 or len(my_list) - 1:
        return my_list[:]
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
