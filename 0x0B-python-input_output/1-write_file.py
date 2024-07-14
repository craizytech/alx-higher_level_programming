#!/usr/bin/python3
"""This module writes to a file"""


def write_file(filename="", text=""):
    """
    This method writes to a file.
    Args:
        filename: name of the file to be written on
        text: the contents to write to the file
    """
    with open(filename, "w", encoding="utf-8") as file:
        num = file.write(text)

    return num
