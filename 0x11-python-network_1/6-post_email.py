#!/usr/bin/python3
import requests
import sys

"""takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response."""

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = requests.post(url, data={'email': email})
    print(data.text)

