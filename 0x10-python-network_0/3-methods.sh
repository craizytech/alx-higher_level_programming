#!/bin/bash
# This script returns the request methods that a server can accept
curl -sI "$1" | grep "Allow" | awk '{ print $2 }'
