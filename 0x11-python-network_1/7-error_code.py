#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body of the response."""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        req = requests.get(url)
    except requests.exceptions.RequestException as e:
        if e.response.status_code >= 400:
            print("Error code: {}".format(e.response.status_code))
