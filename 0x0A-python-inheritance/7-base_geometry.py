#!/usr/bin/python3
""" defines a class """


class BaseGeometry():
    """ class BaseGeometry defines methods"""
    def area(self):
        """ method that raises exception when it is called """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ function validate integer

        Args:
            name: takes name as input
            value: takes value greater than 0 and integer

        Return:
              TypeError: if value is not integer
              ValueError: if value is lessthan or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
