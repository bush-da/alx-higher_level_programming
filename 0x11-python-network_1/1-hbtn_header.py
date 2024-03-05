#!/usr/bin/python3
""" displays the value of the X-Request-Id variable found in the header of the response. """
import sys
from urllib.request import urlopen, Request


if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)
    with urlopen(req) as res:
        val = res.getheader("X-Request-Id")
        print(val)
