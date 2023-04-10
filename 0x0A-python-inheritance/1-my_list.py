#!/usr/bin/python3
""" Defines a class """


class MyList(list):
    """ inherits from class list and add custom method """

    def print_sorted(self):
        """ prints the list in sorted """
        print(sorted(self))
