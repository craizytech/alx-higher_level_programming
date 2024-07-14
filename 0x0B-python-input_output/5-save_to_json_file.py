#!/usr/bin/python3
"""Save object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes a python object to a file in json format

    Args:
        my_obj: the python object to write to a file
        filename: the name of the file to write the object to
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
