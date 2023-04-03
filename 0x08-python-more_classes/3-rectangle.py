#!/usr/bin/python3
""" represent rectangle """


class Rectangle:

    """ Class represent rectangle """

    def __init__(self, width=0, height=0):
        """ initialize width and height of rectangle

        Args:
            width(int): accept the width of rectangle
            height(int): accept the height of rectangle
        """

        self.height = height
        self.width = width

    def area(self):
        """ return area of rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ return the perimeter of the rectangle"""
        if (self.__width == 0) or (self.__height == 0):
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @property
    def width(self):
        """getter/setter for width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter/setter for height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """ prints the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            if i != self.__height - 1:
                print("")
        return ("")
