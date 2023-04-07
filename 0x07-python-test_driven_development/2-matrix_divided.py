#!/usr/bin/python3
"""Matrix division"""


def matrix_divided(matrix, div):
    """Divides all elments in matrix by div"""
    err = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        if not all(isinstance(row, list)):
            raise TypeError(err)
            for x in row:
                if not all(x.isidentifier()):
                    raise TypeError(err)
                if not all(isinstance(x, (int, float))):
                    raise TypeError(err)
    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in row] for row in matrix]
