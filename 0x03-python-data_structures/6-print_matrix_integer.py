#!/usr/bin/python3

def print_matrix_integer(matrix=[]):
    if len(matrix) == 0:
        print("")
    for i in matrix:
        for j in i:
            if j == i[-1]:
                print("{}".format(j), end="")
            else:
                print("{}".format(j), end=" ")
        print("")
