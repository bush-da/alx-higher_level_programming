#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    keys = [x for x in a_dictionary]
    max_key = keys[0]
    max_val = a_dictionary[max_key]
    for i in keys:
        if a_dictionary[i] > max_val:
            max_key = i
            max_val = a_dictionary[max_key]

    return max_key
