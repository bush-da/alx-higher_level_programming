#!/usr/bin/python3
""" represent rectangle """


class Rectangle:

    """ Class represent rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initialize width and height of rectangle

        Args:
            width(int): accept the width of rectangle
            height(int): accept the height of rectangle
        """

        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
                print("{:s}".format(str(self.print_symbol)), end="")
            if i != self.__height - 1:
                print("")
        return ("")

    def __repr__(self):
        """ returns a string representation of the rectange"""
        new = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return (new)

    def __del__(self):
        """ prints message when instance is deleted"""
        if (Rectangle.number_of_instances != 0):
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
