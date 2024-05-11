#!/usr/bin/python3
import requests
import sys

"""takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter."""

if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        req = req.json()
        if req == {}:
            print('No result')
        else:
            print('[{}] {}'.format(req.get('id'), req.get('name')))
    except ValueError:
        print('Not a valid JSON')
