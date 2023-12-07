#!/usr/bin/python3
import urllib.request


req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
with urllib.request.urlopen(req) as response:
    res = response.read()

print(
    f"Body response:\n\t- type: {type(res)}\n\t-\
 content: {res}\n\t- utf8 content: {res.decode('utf-8')}"
)
