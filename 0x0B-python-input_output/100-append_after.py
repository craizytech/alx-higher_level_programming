#!/usr/bin/python3
"""Append module"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function inserts a line of text to a file after each line
    containing a specific string

    Args:
        filename: Name of the file to be written
        search_string: this is the string that we insert new string after
        new_string: this is the new string to be inserted
    """
    with open(filename, "r+", encoding="utf-8") as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        modified_lines.append(line)
        if search_string in line:
            modified_lines.append(new_string)

    with open(filename, "w") as file:
        file.writelines(modified_lines)

