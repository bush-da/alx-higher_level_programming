#!/usr/bin/python3
""" Defines a module that adds all arguments to a python list
and save them to a file """
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []
    args = len(sys.argv)
    for i in range(1, args):
        my_list.append(sys.argv[i])
    save_to_json_file(my_list, filename)
