#!/usr/bin/python3
"""This module reads a file."""


def read_line(filename=""):
    """This method reads a text file and displays the output.

    Args:
        filename (string): the name of the file to be printed
    
    Returns:
        the contents of the file
    """

    with open(filename, mode='r', encoding="utf-8") as text_file:
        print(text_file.read())
