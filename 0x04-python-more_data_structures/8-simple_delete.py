#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """This function deletes a key in a dictionary."""
    if a_dictionary:
        for a_key in a_dictionary.copy():
            if a_key == key:
                del a_dictionary[key]
    return a_dictionary
