#!/bin/bash
# script that takes in a URL, sends a request and displays the size
echo $(curl -s $1 | wc -c)
