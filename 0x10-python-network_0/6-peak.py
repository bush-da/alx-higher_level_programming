#!/usr/bin/python3
""" peak find algorithm """

def find_peak(list_of_integers):
    """ checks for peak iterating through the list and return if
    current number if greater than from both side """
    for i in range(1, len(list_of_integers) - 1):
        if list_of_integers[i - 1] <= list_of_integers[i] >= list_of_integers[
            i + 1
        ] and i < len(list_of_integers):
            return list_of_integers[i]
