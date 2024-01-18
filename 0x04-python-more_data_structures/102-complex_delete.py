#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Deletes keys with specific value in a dictionary."""
    for k in a_dictionary:
        if a_dictionary[k] == value:
            del a_dictionary[k]
    return a_dictionary
