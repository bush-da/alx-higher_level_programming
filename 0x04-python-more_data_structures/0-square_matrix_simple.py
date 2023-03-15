#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    x = []
    for i in range(len(matrix)):
        x.append([])
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            y = matrix[i][j] ** 2
            x[i].append(y)
    return x
