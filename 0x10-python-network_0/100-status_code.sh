#!/bin/bash
#sends a req to URL and display only status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
