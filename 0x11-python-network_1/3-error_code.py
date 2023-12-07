#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response
(decoded in utf-8)."""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys

try:
    url = sys.argv[1]
    req = Request(url)
    with urlopen(req) as response:
        print(response.read().decode('utf-8'))
except HTTPError as e:
    print('Error code: ', e.code)
