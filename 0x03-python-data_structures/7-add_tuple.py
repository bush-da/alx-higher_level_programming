#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    tmp_list = [0, 0]
    tmp_list2 = [0, 0]

    if len(tuple_a) >= 2:
        tmp_list[0] = tuple_a[0]
        tmp_list[1] = tuple_a[1]

    elif len(tuple_a) == 1:
        tmp_list[0] = tuple_a[0]

    if len(tuple_b) >= 2:
        tmp_list2[0] = tuple_b[0]
        tmp_list2[1] = tuple_b[1]

    elif len(tuple_b) == 1:
        tmp_list2[0] = tuple_b[0]

    for i in range(2):
        tmp_list[i] += tmp_list2[i]

    tmp_list = tuple(tmp_list)
    return tmp_list
