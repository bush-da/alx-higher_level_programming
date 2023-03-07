#!/usr/bin/python3
endd = ", "
x = 1
for i in range(0, 10, 1):
    for j in range(x, 10, 1):
        if i == 8 and j == 9:
            endd = "\n"
        print("{}{}".format(i, j), end=endd)
    x += 1
