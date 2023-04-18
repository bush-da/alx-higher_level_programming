#!/usr/bin/python3
""" Define class that is base to of all other class """


class Base:
    """ Represent the base model

    Attributes:
          __nb_objects (int): The number of created object
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize the base class objects

        Args:
            id (int): identity of the each created object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
