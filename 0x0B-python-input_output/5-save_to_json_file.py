#!/usr/bin/python3
"""This module writes an Object to a text file using a JSON rep"""


import json


def save_to_json_file(my_obj, filename):
    """This method writes an Object to a textfile, using json.
    
    Args:
        my_obj (py object): python object
        filename (str): the name of th file
    """

    with open(filename, mode='w', encoding="utf-8") as object_file:
        json.dump(my_obj, object_file)
