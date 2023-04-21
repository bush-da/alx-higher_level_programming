#!/usr/bin/python3
""" Define class that is base to of all other class """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ retuns the JSON string representations
        Args:
            list_dictionaries(list): A list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
