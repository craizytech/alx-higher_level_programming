#!/usr/bin/python3
"""This module is used for file I/O."""


def append_write(filename="", text=""):
    """ This file appends a string to the end of the file.

    Args:
        filename (str): the name of the file name
        text (str): the string to be appended to the end of the file
    Returns:
        the number of characters written
    """
    with open(filename, 'a', encoding="UTF-8") as f:
        num = f.write(text)
    return num
