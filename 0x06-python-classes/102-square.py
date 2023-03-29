#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Represent a Square"""
    def __init__(self, size=0):

        """Initialize a new Square

        Args:
            size: the size of square
        """
        self.__size = size

    def area(self):
        """class method that find the area of square

        Returns:
               the area of square
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __eq__(self, other):
        """define equal comparison b/n instance area of square"""
        return (self.area() == other.area())

    def __nq__(self, other):
        """define not equal comparison to area of square"""
        return (self.area() != other.area())

    def __lt__(self, other):
        """define comparison lessthan to area of square"""
        return (self.area() < other.area())

    def __le__(self, other):
        """define comparison lessthan or equal to area of square"""
        return (self.area() <= other.area())

    def __gt__(self, other):
        """define greate than comparison to area of square"""
        return (self.area() > other.area())

    def __ge__(self, other):
        """define greater than or equal comparsion to a square"""
        return (self.area() >= other.area())
