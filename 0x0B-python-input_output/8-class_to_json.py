#!/usr/bin/python3
""" Defines function that returns the dict description for json serialization"""


def class_to_json(obj):
    """ Returns the dictionary description """
    return obj.__dict__
