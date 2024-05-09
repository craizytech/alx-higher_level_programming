#!/bin/bash
# This script sends a GET request with an additional header variable
curl -sH "X-School-User-Id: 98" "$1"
