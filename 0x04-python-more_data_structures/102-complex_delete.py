#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """This function deletes keys with a specific value in a dictionary."""
    if a_dictionary:
        for key in a_dictionary.copy():
            if a_dictionary[key] == value:
                del a_dictionary[key]
    return a_dictionary
