#!/usr/bin/python3
""" defines function that return True if the object is an instance of class
False if it is not """


def inherits_from(obj, a_class):
    """ check for instance of not """
    return issubclass(type(obj), a_class)
