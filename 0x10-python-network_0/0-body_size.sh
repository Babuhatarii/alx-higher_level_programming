#!/bin/bash
#send a GET request to the url specified print the size of response body to stdout
curl -sI "$1" | grep -i "Content-Length" | cut -d ":" -f 2
