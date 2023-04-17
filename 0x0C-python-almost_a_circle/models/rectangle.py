#!/usr/bin/python3
""" Defines a rectangle class. """
from models.base import Base


class Rectangle(Base):
    """ defines a class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initilize the rectanlge instance when created

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
            x(int): x coordinate of rectangle
            y(int): y coordinate of rectangle
            id(int): identity of rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter/setter for width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise TypeError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter/setter for height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise TypeError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter/setter for x in rectangle"""
        return (self.__x)

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise TypeError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter/setter for y in rectangle"""
        return (self.__y)

    @x.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise TypeError("y must be >= 0")
        self.__y = value
