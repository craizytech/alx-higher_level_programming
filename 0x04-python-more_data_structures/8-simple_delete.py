#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """This function deletes a key in a dictionary."""
    if a_dictionary:
        if key in list(a_dictionary.keys()):
            del a_dictionary[key]
        return a_dictionary
