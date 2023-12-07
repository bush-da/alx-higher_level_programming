#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
import requests

if __name__ == "__main__":
    req = requests.get("https://alx-intranet.hbtn.io/status")
    print(
        f"Body response:\n\t- type: \
    {type(req.text)}\n\t- content: {req.text}"
    )
