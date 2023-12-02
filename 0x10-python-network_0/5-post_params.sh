#!/bin/bash
# sends a POST req and set email and subject
curl -s -X POST -H "email: test@gmail.com" "subject: I will always be here for PLD" "$1"
