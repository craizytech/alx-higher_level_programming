#!/usr/bin/python3
"""This module checks for object Identity"""

def is_same_class(obj, a_class):
    """
    This method checks if obj is an instance of a_class
    Args:
        obj (object): This is the object to be checked
        a_class(class): 
    """
    if isinstance(obj, a_class):
        return type(obj) is a_class