#!/usr/bin/python3
def weight_average(my_list=[]):
    high = sum([(x * y) for x, y in my_list])
    low = sum([x[1] for x in my_list])
    average = high / low
    return average
