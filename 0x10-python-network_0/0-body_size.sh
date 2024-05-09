#!/usr/bin/env bash
# This script takes in a url,sends a request to that url and displays the 
# size of the body in its response
# curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
curl -s "$1" | wc -c
