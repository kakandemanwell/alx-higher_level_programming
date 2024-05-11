#!/usr/bin/python3
"""
Takes 2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name
"""
import requests
import sys
if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    req = requests.get(url)
    commits = req.json()
    for i in range(10):
        print("{}: {}".format(commits[i].get("sha"),
                              commits[i].get("commit").get("author").get("name")))
