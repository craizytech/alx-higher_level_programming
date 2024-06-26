#!/usr/bin/python3
"""This module checks if an object is a subclass of a class."""


def inherits_from(obj, a_class):
    """This method retuns true if an object is in a class.

    Args:
        obj (object): object
        a_class (class): class

    Returns:
        boolean
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
