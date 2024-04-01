#!/usr/bin/python3
"""This is a pascal module."""


def pascal_triangle(n):
    """This method is used to represent the pascals triangle.

    Args:
        n (int): the number of lists to return
    Returns:
        a list of lists containing the pascals integers
    """
    res = [[1]]
    for i in range(n-1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append[temp[j] + temp[j + 1])
        res.append(row)
    return res
