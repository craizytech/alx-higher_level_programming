#!/usr/bin/python3
"""This is the new version of multiplying matrix using numpy"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This method takes 2 matrixes and multiplies them using numpy

    Args:
        m_a (list): The first matrix
        m_b (list): The second matrix

    Return: The new matrix
    """

    return (np.matmul(m_a, m_b))
