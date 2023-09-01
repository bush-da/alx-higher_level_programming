#!/usr/bin/python3
"""peak-finding algorithm."""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    size = len(list_of_integers)
    if size == 0:
        return None
    elif size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    left = 0
    right = size - 1

    while left <= right:
        mid = (left + right) // 2
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1])\
           and (mid == size - 1 or
                list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            right = mid - 1
        else:
            left = mid + 1
