#!/usr/bin/python3
"""This module reads a file."""


def read_file(filename=""):
    """This method reads a file and prints output.

    Args:
        filename (str): this is the name of the file to be opened.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        """with creates a runtime context used for opening and closing files"""
        print(f.read(), end="")
