#!/bin/bash
# takes a URL, sends it request and displays the body-size of the response
curl -sI "$1" | awk '/Content-Length/{print $2}'
