#!/usr/bin/python3
""" defines a class """


class BaseGeometry():
    """ class contain area method """
    def area(self):
        """ method that raises exception when it is called """
        raise Exception("area() is not implemented")
