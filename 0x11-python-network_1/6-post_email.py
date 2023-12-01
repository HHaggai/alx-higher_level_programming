#!/usr/bin/python3
"""This is a script that:
- takes in URL,
- sends request to URL and disp val
- of X-Request-Id var found in header of response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
