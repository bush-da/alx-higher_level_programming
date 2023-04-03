#!/usr/bin/python3
""" represent rectangle """


class Rectangle:

    """ Class represent rectangle """

    def __init__(self, width, height):
        """ initialize width and height of rectangle"""

        self.__width = width
        self.__height = height

    """getter/setter for width of the rectangle"""
    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """getter/setter for height of the rectangle"""
    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
