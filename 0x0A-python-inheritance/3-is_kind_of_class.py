#!/usr/bin/python3
""" Defines a function that return True if object is an instance
of, or if the object is an instance of a class that inherited from
otherwise returns False
"""


def is_kind_of_class(obj, a_class):
    """ checks for instance or not """
    return (isinstance(obj, a_class))
