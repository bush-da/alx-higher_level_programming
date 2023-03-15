#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key = {i for i in a_dictionary if a_dictionary[i] == value}
    for i in key:
        del a_dictionary[i]
    return a_dictionary
