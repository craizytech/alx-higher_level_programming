#!/usr/bin/python3
"""This module creates a json object"""


import json

def to_json_string(string):
    """This method returns the JSON Representation of an object

    Args:
        string (str): string to be converted to json object

    Returns:
        json (object)
    """

    return json.dumps(string)
