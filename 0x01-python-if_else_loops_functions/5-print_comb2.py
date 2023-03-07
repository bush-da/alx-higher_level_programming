#!/usr/bin/python3
for i in range(10):
    for x in range(10):
        if i == 9 and x == 9:
            print("{}{}".format(i, x))
            break;
        print("{}{}, ".format(i, x), end="")
