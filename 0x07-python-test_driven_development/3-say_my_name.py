#!/usr/bin/python3
"""This module prints a persons full names"""


def say_my_name(first_name, last_name=""):
    """
    This function prints the persons full name.

    Args:
        first_name (str): This is the persons first name
        last_name (str): This is a persons last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
