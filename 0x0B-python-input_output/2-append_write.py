#!/usr/bin/python3
""" Defines function that writes a string to a text file """


def append_write(filename="", text=""):
    """ writes a string text to a filename """
    with open(filename, 'a') as f:
        f.write(text)
        return (len(text))
