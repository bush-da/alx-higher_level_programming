#!/usr/bin/python3
""" Define class that is base to of all other class """
import json
import csv


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

    @classmethod
    def create(cls, **dictionary):
        """ return a instance with all attributes already set
        Args:
            dictionary(kwargs): can be thought of as a double pointer
            to a dictionary
        """
        if (cls.__name__ == "Rectangle"):
            r1 = cls(1, 1)
        else:
            r1 = cls(1)
        r1.update(**dictionary)
        return r1

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """

        try:
            with open(f"{cls.__name__}.json", "r") as jsonfile:
                lists_of_dict = Base.from_json_string(jsonfile.read())
                return [cls.create(**f) for f in lists_of_dict]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes CSV file"""
        with open(f"{cls.__name__}.csv", "w") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    csv_writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes CSV file"""
        try:
            with open(f"{cls.__name__}.csv", "r") as csv_file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_of_dicts = csv.DictReader(csv_file, fieldnames=fieldnames)
                list_of_dicts = [dict([key, int(value)]
                                 for key, value in d.items())
                                 for d in list_of_dicts]
                return [cls.create(**d) for d in list_of_dicts]
        except FileNotFoundError:
            return []
