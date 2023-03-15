#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    keys = list(a_dictionary.keys())
    first = keys[0]
    max_num = a_dictionary[first]
    key = ""
    for i in keys:
        if a_dictionary[i] >= max_num:
            key = i
            max_num = a_dictionary[i]

    return key
