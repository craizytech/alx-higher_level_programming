#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Function that prints a matrix of integers."""
    for elem in matrix:
        for num in elem:
            print("{:d}".format(num), end=" ")
        print()
