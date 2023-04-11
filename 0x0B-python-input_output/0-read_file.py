#!/usr/bin/python3
import sys
""" define function that read text file """


def read_file(filename=""):
    """ reads a text file from filename """
    with open(filename, 'r') as f:
        x = f.read()
        sys.stdout.write(x)
