#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
curl -sd "X-School-User-Id: 98" "$1"
