#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        x = fct(*args)
        return (x)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
