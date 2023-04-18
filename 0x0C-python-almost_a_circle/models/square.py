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
        return (self.height)

    @size.setter
    def size(self, value):
        self.height = value
        self.width = value

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.size)
