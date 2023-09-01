#!/bin/bash
# script that sends a JSON POST request to a URL passed as the first argument
curl -s -H "content-Type: application/json" -d "$(cat "$2")" "$1"
