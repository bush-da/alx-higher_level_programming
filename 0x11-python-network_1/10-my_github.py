#!/usr/bin/python3
""" script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    usr = sys.argv[1]
    pas = sys.argv[2]
    auth = HTTPBasicAuth(usr, pas)
    req = requests.get("https://api.github.com/user", auth=auth)
    print(req.json().get("id"))
