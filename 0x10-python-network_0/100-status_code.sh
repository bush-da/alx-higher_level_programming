#!/bin/bash
# script that sends a request to a URL passed as an argument
curl -s -w "%{http_code}" "$1"
