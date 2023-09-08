#!/usr/bin/python3
# 2-matrix_divided.py
"""Defynes a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elmnts of a matrix.

    Args:
        matrix (list): A list of lists of intgrs or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numrs.
        TypeError: If the matrix contains rows of diffrnt sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Retrns:
        A new matrix reprsnting the reslt of the divisn.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "intgrs/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a num")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
