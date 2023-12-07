#!/usr/bin/python3
# displays X-Request-Id variable found in the header of the response.
import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as res:
    print(res.info()['X-Request-Id'])
