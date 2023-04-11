#!/usr/bin/python3
""" Defines function that writes a string to a text file """


def write_file(filename="", text=""):
    """ writes a string text to a filename """
    with open(filename, 'w') as f:
        f.write(text)
        return (f.tell())
