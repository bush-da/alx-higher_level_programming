#!/bin/bash
# sends JSON POST req and display response
curl -s -H "Content-type: application/json" -d "$(cat "$2")" "$1"
