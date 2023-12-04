#!/usr/bin/python3
""" peak find algorithm """


def find_peak(list_of_integers):
    """ checks for peak iterating through the list and return if
    current number if greater than from both side """
    if list_of_integer == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    if size == 2:
        return max(list_of_integers)
    mid = len(list_of_integers)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
