#!/bin/bash
# send a POST request to passed URL using curl, and displays body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
