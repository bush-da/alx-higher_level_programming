#!/usr/bin/python3
import sys
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

    def my_print(self):
        """print the square with the character #"""
        for i in range(self.__size):
            for j in range(self.__size):
                sys.stdout.write('#')
            print("")
        if self.__size == 0:
            print("")
