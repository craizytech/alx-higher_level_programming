#!/usr/bin/python3
"""Checks if an object is in a class."""


def is_kind_of_class(obj, a_class):
    """returns True if an object is a class, False otherwise.

    Args:
        obj (object): object
        a_class: a class of an object

    Returns:
        Boolean
    """
    return isinstance(obj, a_class)

