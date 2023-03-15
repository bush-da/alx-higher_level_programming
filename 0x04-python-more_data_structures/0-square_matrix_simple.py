#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    x = [[item[i] ** 2 for i in range(len(matrix))] for item in matrix]

    return x
