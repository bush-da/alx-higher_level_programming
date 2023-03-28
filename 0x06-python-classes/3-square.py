#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Represent a Square"""
    def __init__(self, size=0):

        """Initialize a new Square

        Args:
            size: the size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """class method that find the area of square

        Returns:
               the area of square
        """
        return (self.__size * self.__size)
