#!/usr/bin/python3
def weight_average(my_list=[]):
    high = [x[0] * x[1] for x in my_list]
    low = [x[1] for x in my_list]
    return sum(high)/sum(low)
