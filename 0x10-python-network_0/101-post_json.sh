#!/bin/bash
# send JSON POST request to URL passed as first argument and displays the response
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
