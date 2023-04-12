#!/usr/bin/python3
""" Defines a module that adds all arguments to a python list
and save them to a file """
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
check = './add_item.json'
if os.path.isfile(check):
    my_list = load_from_json_file(filename)
    args = len(sys.argv)
    for i in range(1, args):
        my_list.append(sys.argv[i])
    save_to_json_file(my_list, filename)
else:
    with open(filename, 'a') as what:
        what.write('[]')
