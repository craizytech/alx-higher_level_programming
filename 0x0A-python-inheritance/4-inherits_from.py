#!/usr/bin/python3
"""This module checks if an object is a subclass of a class"""


def inherits_from(obj, a_class):
    """
    This function returns True if an object is an instance/subclass of a_class

    Args:
        obj (object): object is an instance/subclass of a class
        a_class: This is the class the object is tested against

    Return: (boolean) True if obj is an instance of a_class False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
