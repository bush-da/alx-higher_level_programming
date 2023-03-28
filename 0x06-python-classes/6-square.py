#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Represent a Square"""
    def __init__(self, size=0, position=(0, 0)):

        """Initialize a new Square

        Args:
            size: the size of square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (len(value) != 2 or not isinstance(value, tuple)
            or not all(isinstance(i, int) for i in value)
            or not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """print the square with the character #"""

        for i in range(self.__position[1]):
            print("")

        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
