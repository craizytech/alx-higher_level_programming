#!/usr/bin/python3
"""This module appends a file."""


def append_write(filename="", text=""):
    """This function appends a string to the end of a text file.

    Args:
        filename (string): the filename of the string
        text (string): the string to append to the end of the file

    Returns:
        the number of characters appended to the file
    """

    with open(filename, mode='a', encoding="utf-8") as text_file:
        num = text_file.write(text)
    
    return num
