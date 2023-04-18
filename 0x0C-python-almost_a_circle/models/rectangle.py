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
        Raises:
              TypeError: if width or height is not int
              ValueError: if width or height <= 0
              TypeError: if x or y is not int
              ValueError: if x or y < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get/set for width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get/set for height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def area(self):
        """ returns the area of the rectangle"""
        return (self.width * self.height)

    @property
    def x(self):
        """get/set for x in rectangle"""
        return (self.__x)

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get/set for y in rectangle"""
        return (self.__y)

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def display(self):
        """ display rectanlge using # by the height and width
        of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        for i in range(self.y):
            print("")
        for i in range(self.__height):
            for d in range(self.x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            if (i != self.__height - 1):
                print("")
        print("")
        return ("")

    def update(self, *args, **kwargs):
        """Update the Rectangle by using *args to assign to each attribute

        Args:
            id(int): identity of rectangle
            width(int): width of the rectangle
            height(int): height of the rectangle
            x(int): x coordinate of the rectangle
            y(int): y coordinate of the rectangle
        """
        if args and len(args) != 0:
            d = 0
            for arg in args:
                if d == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif (d == 1):
                    self.width = arg
                elif (d == 2):
                    self.height = arg
                elif (d == 3):
                    self.x = arg
                elif (d == 4):
                    self.y = arg
                d += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}

    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.x,
                                                                 self.y,
                                                                 self.width,
                                                                 self.height)
