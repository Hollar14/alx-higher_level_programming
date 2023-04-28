#!/bin/bash
# takes a a URL, send a POST request and displays the response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
