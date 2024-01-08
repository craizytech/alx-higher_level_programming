#!/usr/bin/python3
def element_at(my_list, idx):
    """Function that returns element at index."""
    if idx < 0 or idx > len(my_list) - 1:
        return
    return my_list[idx]
