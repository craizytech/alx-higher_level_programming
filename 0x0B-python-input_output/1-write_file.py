#!/usr/bin/python3
"""This module is used to open files and perfom some actions."""


def write_file(filename="", text=""):
    """This method opens the file for writing.

    Args:
        filename (str): This is the name of the file to be opened
        text (str): This is the text to be written to the file
    Returns:
        num (int): The number of characters written to the file
    """
    with open(filename, 'w', encoding="UTF-8") as f:
        num = f.write(text)
    return num
