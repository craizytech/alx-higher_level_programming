#!/usr/bin/python3
"""This module adds all arguments to a Python list and serializes it."""


import json
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file= __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'

if os.path.exists(filename):
    existing_data = load_from_json_file(filename)
else:
    existing_data = []

args = sys.argv[1:]
existing_data.extend(args)

save_to_json_file(existing_data, filename)
