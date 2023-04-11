#!/usr/bin/python3
""" define function that read text file """


def read_file(filename=""):
    """ reads a text file from filename """
    with open(filename, 'r') as f:
        print(f.read(), end="")
