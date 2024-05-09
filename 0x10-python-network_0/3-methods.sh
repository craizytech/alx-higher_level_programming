#!/bin/bash
# This script returns the request methods that a server can accept
curl -sIX "$1" | grep -i Allow | awk '{ print $2 }'
