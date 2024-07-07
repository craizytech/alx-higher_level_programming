#!/usr/bin/python3
"""This module contains the function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """This method takes a matrix and divides each element by div
    Args:
        matrix (list): list of lists containing the numbers
        div (int or float): Number divides the matrix
    Returns: The divided matrix
    """
    if not isinstance(matrix, list):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    " of integers/floats"
                    )

        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(
                        "matrix must be a matrix (list of lists) of"
                        " integers/floats")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        new_row = [round(num / div, 2) for num in row]
        new_matrix.append(new_row)

    return new_matrix
