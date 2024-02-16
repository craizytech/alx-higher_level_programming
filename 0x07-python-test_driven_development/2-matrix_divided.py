#!/usr/bin/python3
"""This module contains the method that divides a matrix by a divisor."""


def matrix_divided(matrix, div):
    """The method divides a matrix with div.

    Args:
        matrix (list): This is a list of lists containing (int, float) elements
        div (int): the number to divide the matrix with

    Returns:
        list : the new matrix after the division operation
    """
    if type(div) in [float, int]:
        if div == 0:
             raise TypeError("division by zero")
    else:
         raise TypeError("div must be a number")

    if isinstance(matrix, list):
        check_list(matrix)
        new_matrix = []
        for i in matrix:
            if isinstance(i, list):
                new_row = []
                for j in i:
                    if type(j) in [float, int]:
                            new_row.append(round(j / div, 2))
                    else:
                         raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                new_matrix.append(new_row)
            else:
                 raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
         raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return new_matrix


def check_list(l):
    """This method checks wether the lists are of the same length
      
    Args:
        l (list): The list containing the elements
    """
    if isinstance(l[0], list):
        first_element_length = len(l[0])
    else:
         raise TypeError("matrix must be a matrix (list of lists) of integers/floats")         
    for i in l:
         if len(i) != first_element_length:
              raise TypeError("Each row of the matrix must have the same size")
     
