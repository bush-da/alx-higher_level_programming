#!/usr/bin/python3
"""Define a function that sum given two arguments"""


def add_integer(a, b=98):

    """ Return the sum of a and b

    Floats are typecasted to integer

    Raises:
          TypeError: if one of the arguemnts is not integer or float
    Args:
        a(int): first parameter
        b(int): second parameter default value 98
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
