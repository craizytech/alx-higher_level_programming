#!/usr/bin/python3
"""This module appends to a file"""


def append_write(filename="", text=""):
    """
    This method appends text to the end of a file

    Args:
        filename: the name of the file
        text: the text to write to the file (append)
    """
    with open(filename, "a", encoding="utf-8") as file:
        num = file.write(text)
    return num
