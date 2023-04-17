#!/usr/bin/python3
""" Define class that is base to of all other class """


class Base:
    """ Represent the base model

    Attributes:
          __nb_objects (int): The number of instantiated Bases"""

    __nb_objects = 0
    def __init__(self, id=None):
        """ initialize the base class
        Args:
            id (int): id of the base class created
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
