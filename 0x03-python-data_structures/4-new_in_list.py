#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or len(my_list) < idx:
        return my_list

    my_copy = my_list[:]
    my_copy[idx] = element
    return my_copy
