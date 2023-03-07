#!/usr/bin/python3
flag = 0
for i in range(122, 96, -1):
    if flag == 0:
        print("{}".format(chr(i)), end="")
        flag = 1
    elif flag == 1:
        i = i - 32
        print("{}".format(chr(i)), end="")
        i = i + 32
        flag = 0
