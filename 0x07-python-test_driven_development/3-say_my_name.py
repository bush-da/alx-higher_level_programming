#!/usr/bin/python3
""" define function that full name"""


def say_my_name(first_name, last_name=""):
    """ print a text My name is with arguements passed

    Args:
        first_name(str): first name
        last_name(str): last name
    """

    if first_name == "":
        raise TypeError("first_name must be a string")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
