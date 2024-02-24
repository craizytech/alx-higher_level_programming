#!/usr/bin/python3
"""This module writes a string to a text file."""


def write_file(filename="", text=""):
    """This module writes a string to a text file.

    Args:
        filename (string): The name of the file
        text (string): the text string of arguments

    Returns:
        The number of characters written
    """

    with open(filename, mode='w', encoding="utf-8") as text_file:
        num = text_file.write(text)

    return num
