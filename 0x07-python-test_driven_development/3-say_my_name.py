#!/usr/bin/python3
"""This module contains a function that prints the first_name
and last name
"""


def say_my_name(first_name, last_name=""):
    """This method takes in two arguments and prints them out.
    
    Args:
        first_name (str): The first name to be printed
        last_name (str): The last name to be printed
    """

    if isinstance(first_name, str):
        if isinstance(last_name, str):
            print(f"My name is {first_name} {last_name}")
        else:
            raise TypeError("last_name must be a string")
    else:
        raise TypeError("first_name must be a string")