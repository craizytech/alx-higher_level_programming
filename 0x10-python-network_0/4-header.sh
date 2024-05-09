#!/bin/bash
# This script sends a GET request with an additional header variable
curl -H "X-School-User-Id: 98" "$1"
