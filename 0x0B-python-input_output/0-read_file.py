#!/usr/bin/python3
"""This module reads a test file and prints it out to stdout"""


def read_file(filename=""):
    """Read the contents of the file and print it to the stdout
    Args:
        filename: the filename of the file to be read
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
