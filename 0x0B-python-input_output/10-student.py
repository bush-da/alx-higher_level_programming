#!/usr/bin/python3
""" Defines module that create class student and retrive a dictionary
representation of a Student instance"""


class Student:
    """ class that contain firstname lastname and there age"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrives a dictionary representation of a Student instance

        Args:
            attr(list): list of string
        """
        if attrs != None:
            return list(attrs)
        return self.__dict__
