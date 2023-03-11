#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list) - 1
    for i in range(i, -1, -1):
        print("{:d}".format(my_list[i]))
