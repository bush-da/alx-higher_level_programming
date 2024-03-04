#!/bin/bash
# script that takes in a URL sends a request and count the body size
curl -s "$1" | wc -c
