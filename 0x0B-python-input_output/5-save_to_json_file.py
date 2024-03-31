#!/usr/bin/python3
"""This module is for seriliazation."""
import json


def save_to_json_file(my_obj, filename):
    """This method converts a py object to json and stores this in a file.

    Args:
        my_obj (python object): This is a python object
        filename: name of the file the json is written on
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, filename)
