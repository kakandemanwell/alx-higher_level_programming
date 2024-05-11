#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
and displays the body of the response
"""
import urllib
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        response = response.read()
        print("Body Response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode('utf-8')))
