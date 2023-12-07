#!/usr/bin/python3
"""  sends a POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter."""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": ""}
    if (len(sys.argv) == 2):
        payload["q"] = sys.argv[1]
    req = requests.post(url, data=payload)
    try:
        response = req.json()
        if (response == {}):
            print("No result")
        else:
            print(f"[{response.get('id')}] {response.get('name')}")
    except ValueError:
        print("Not a valid json")
