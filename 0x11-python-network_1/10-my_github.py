#!/usr/bin/python3
import requests
import sys

"""takes your GitHub credentials (username and password) and uses the GitHub API to display your id"""

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get('https://api.github.com/user', auth=(username, password))
    print(response.json().get('id'))
