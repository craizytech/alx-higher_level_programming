#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Function computes the square values of all integers in the matrix."""
    new_matrix = []
    for elem in matrix:
        new_elem = []
        for num in elem:
            num = num ** 2
            new_elem.append(num)
        new_matrix.append(new_elem)

    return new_matrix
