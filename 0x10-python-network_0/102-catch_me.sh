#!/bin/bash
# makes request to 0.0.0.0:5000/catch_me the causes the server to respond
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
