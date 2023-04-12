#!/usr/bin/python3
""" Defines function that returns an Python object represent by JSON string """
import json


def from_json_string(my_str):
    """ returns python object """

    return (json.loads(my_str))
