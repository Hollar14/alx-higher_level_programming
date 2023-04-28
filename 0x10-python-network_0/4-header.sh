#!/bin/bash
# takes a URL and displays all HTTP methhods accepted
curl -sI "$1" | grep -i "Allow" | awk -F ": " '{ print $2 }'
