#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Function computes the square values of all integers in the matrix."""
    squared_list = []
    for elem in matrix:
        for num in elem:
            num = num ** 2
            squared_list.append(num)
    return squared_list
