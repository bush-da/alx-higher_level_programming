#!/usr/bin/python3
for i in range(100):
    if i <= 9:
        print("{}{}".format(0,i), end=", ")
    else:
        if i == 99:
            print("{}".format(i))
        else:
            print("{}".format(i), end=", ")
