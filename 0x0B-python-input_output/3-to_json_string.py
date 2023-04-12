#!/usr/bin/python3
""" Defines function that retuns the JSON representation """
import json

def to_json_string(my_obj):
    """ return JSON representation """
    return (json.dumps(my_obj))
