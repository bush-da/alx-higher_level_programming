#!/usr/bin/python3
""" script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""

import requests
import sys

if __name__ == "__main__":
    if (len(sys.argv) == 2):
        q = {"q": sys.argv[1]}
    else:
        q = {"q": ""}
    url = "http://0.0.0.0:5000/search_user"
    req = requests.post(url, data=q)
    try:
        res = req.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
