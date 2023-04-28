#!/bin/bash
# sends a rquest to URL passed as an argument and displays the status code only
curl -sLw "%{http_code}" -o /dev/null "$1"
