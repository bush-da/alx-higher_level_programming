#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response
(decoded in utf-8)."""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print(f"Error code: {e.code}")
