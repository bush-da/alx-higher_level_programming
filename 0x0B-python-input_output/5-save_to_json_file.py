#!/usr/bin/python3
""" Defines function that writes an Object to a text file """
import json


def save_to_json_file(my_obj, filename):
    """ writes an object to a text file using JSON representation """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
