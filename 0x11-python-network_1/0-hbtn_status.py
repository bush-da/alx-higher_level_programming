#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = Request(url)
    with urlopen(req) as res:
        body = res.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
