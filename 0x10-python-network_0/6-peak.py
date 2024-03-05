#!/usr/bin/python3

def find_peak(list_of_integers):
    """ finds a peak in the list of unsorted integers """

    if not list_of_integers:
        return None

    start = 0
    end = len(list_of_integers) - 1

    while start < end:
        mid = (start + end) // 2
        if (list_of_integers[mid] < list_of_integers[mid + 1]):
            start = mid
        else:
            end = mid
    return list_of_integers[start]
