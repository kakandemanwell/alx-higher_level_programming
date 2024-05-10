#!/bin/bash
# sends a request to a URL with CURL and displays the content-size of the response body.
curl -s "$1" | wc -c
