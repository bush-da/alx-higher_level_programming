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
        self.position = position


    @property
    def size(self):
        """Get/set current size"""
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
        """Get/set current positon"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """class method that find the area of square

        Returns:
               the area of square
        """
        return (self.__size * self.__size)


    def my_print(self):
        """print the square with the character #"""
        if self.__size == 0:
            print("")
            return

        for i in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for k in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print("")
