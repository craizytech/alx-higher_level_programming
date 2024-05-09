#!/bin/bash
# This script returns the value of the content-length header
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
