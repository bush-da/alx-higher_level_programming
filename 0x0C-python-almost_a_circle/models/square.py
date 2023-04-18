#!/usr/bin/python3
""" Defines square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ defines a class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initilize the Square instance when created

        Args:
            size(int): size of the square
            x(int): x coordinate of square
            y(int): y coordinate of square
            id(int): identity of square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get/set size for square"""
        return (self.width)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """ update square with args and kwargs attribute

        Args:
            id(int): identity of square
            size(int): the size of square
            x(int): x coordinate of square
            y(int): y coordinate of square
        """
        if args and len(args) != 0:
            d = 0
            for arg in args:
                if d == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif (d == 1):
                    self.size = arg
                elif (d == 2):
                    self.x = arg
                elif (d == 3):
                    self.y = arg
                d += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.size)
