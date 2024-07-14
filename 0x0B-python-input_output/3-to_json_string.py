#!/usr/bin/python3
"""This module serializes a string"""
import json


def to_json_string(my_obj):
    """
    This method serializes a string object to json

    Args:
        my_obj: the object to be serialized to json

    Returns: the jsonn representation of the object
    """
    return json.dumps(my_obj)
