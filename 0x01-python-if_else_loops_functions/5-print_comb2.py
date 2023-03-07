#!/usr/bin/python3
endd = ", "
for i in range(100):
    if i <= 9:
        print("{}{}".format(0,i), end=endd)
    else:
        if i == 99:
            endd = "\n"
        print("{}".format(i), end=endd)
