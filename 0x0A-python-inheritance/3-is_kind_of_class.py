#!/usr/bin/python3
"""
This module checks wether an object is an instance of, or if the object
is an instance of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    This is method checks if obj is an instance of a class
    Args:
        obj (object): an object to be checked
        a_class (class): This is the class the object is checked against
    Returns (boolean): True if obj is an instance of a_class False otherwise
    """
    return isinstance(obj, a_class)
