#!/usr/bin/python3
"""This is a search and update module."""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file after each line containing a 
    specific string.

    Args:
        filename (str): the name of the file to be opened
        search_string (str): the key string we are inserting after
        new_string (str): this is the string to be inserted
    """
    with open(filename
