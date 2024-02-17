#!/usr/bin/python3
"""This module defines a function that indents a string"""

def text_indentation(text):
    """This function takes in a string and indents it based
    on the characters '., ?, :' by adding two lines after each
    of the characters
    
    Args:
        text (str): The string to be indented"""

    if isinstance(text, str):
        text = text.strip()
        new_string = ""
        for i in text:
            if i in ['.', '?', ':']:
                new_string += "\n\n"
            else:
                new_string += i
        new_string = new_string.strip()
        print(new_string)
    else:
        raise TypeError("text must be a string")