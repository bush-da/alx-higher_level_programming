#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    if (len(sys.argv) == 1):
        print("{} arguments.".format(len(sys.argv) - 1), end="\n")
    else:
        print("{} arguments:".format(len(sys.argv) - 1), end="\n")
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]), end="\n")
