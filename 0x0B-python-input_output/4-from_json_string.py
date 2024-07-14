#!/usr/bin/python3
"""From JSON string to Object"""
import json


def from_json_string(my_str):
    """
    This method returns a python object from a json format

    Args:
        my_str: The json representation of the file

    Returns: The python object/data structure
    """
    return json.loads(my_str)
