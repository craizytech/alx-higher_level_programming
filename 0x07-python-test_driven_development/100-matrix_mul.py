#!/usr/bin/python3
"""This module defines matrix multiplication"""


def matrix_mul(m_a, m_b):
    """
    This function takes two matrices multiplies them together and returns
    a resulting matrix.
    Args:
        m_a (list): this is the first matrix
        m_b (list): this is the second matrix
    Return (list): The resulting matrix after m_a * m_b
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")

        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

        for _ in row:
            if not isinstance(_, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

        for _ in row:
            if not isinstance(_, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m = len(m_a)         # Number of rows in the first matrix
    n = len(m_a[0])      # Nuber of columns in m_a (no of rows in m_b)
    p = len(m_b[0])      # Number of columns in B

    # Initialize matrix C with zeros of size m * p
    C = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m):
        for j in range(p):
            sum = 0
            for k in range(n):
                sum += m_a[i][k] * m_b[k][j]
            C[i][j] = sum

    return C
