#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ret_list = []
    for i in my_list:
        if i % 2 == 0:
            ret_list.append(True)
        else:
            ret_list.append(False)

    return ret_list
