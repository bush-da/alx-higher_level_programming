#!/bin/bash

# Take in URL as argument
url=$1

# Send request to URL and store response in variable
response=$(curl -s $url | wc -c)

# Display size of response body in bytes
echo $response
