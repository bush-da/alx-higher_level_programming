#!/usr/bin/python3
""" Define a function that return True or False """


def inherits_from(obj, a_class):
    """ Function to check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
    obj: An object to check.
    a_class: A class to check if the object is an instance of.

    Returns:
    True if the object is an instance of a class that inherited (directly
    or indirectly) from the specified class; False otherwise.
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
