#!/bin/bash
# send a request to URL with curl, and displays size of body of the response
curl -s "$1" | wc -c
