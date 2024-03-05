#!/bin/bash
# make a specific request and get a respond message from the server
curl -s -X PUT -H "Accept: */*" -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me -L
