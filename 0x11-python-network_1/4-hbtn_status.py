#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8)."""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        try:
            print(response.read().decode('utf-8'))
        except urllib.error.URLError as e:
            print("Error code: {}".format(e.code))
