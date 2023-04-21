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

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file
        Args:
            list_objs(list): a list of instance who inherits of Base class
        """
        with open(f"{cls.__name__}.json", "w") as jn:
            if list_objs is None:
                jn.write("[]")
            else:
                dicts = [i.to_dictionary() for i in list_objs]
                jn.write(Base.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string
        Args:
            json_string: a string representing a list of dictionaries
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
