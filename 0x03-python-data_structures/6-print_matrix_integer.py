#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix), 1):
        for n in range(0, len(matrix[i]), 1):
            ln = len(matrix[i])
            k = matrix[i][n]
            print("{:d}".format(k), end="\n" if n == ln - 1 else " ")
