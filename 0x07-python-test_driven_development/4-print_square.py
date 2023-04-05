#!/usr/bin/python3
""" define function print_square print square"""


def print_square(size):
    """ prints square using sign #

    Args:
        size(int): size of square
    """
    if not isinstance(size, int) or size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
