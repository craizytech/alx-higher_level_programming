#!/usr/bin/python3
"""This module checks if an object is in a class"""


def is_same_class(obj, a_class):
    """This method checks if obj is an instance of a a_class.

    Args:
        obj (object): object
        a_class (class): class

    Returns (boolean): True or false
    """
    return type(obj) is a_class
