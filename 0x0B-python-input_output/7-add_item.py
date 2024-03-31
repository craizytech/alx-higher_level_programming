#!/usr/bin/python3
"""This module converts a python object to a json rep and stores it."""
import json
import sys
from os.path import exists


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'

if exists(filename):
    old_list = load_from_json_file(filename)
else:
    old_list = []

# Extract the new items from the commandline arguments
new_list = old_list + sys.argv[1:]

# save the combined lists to the JSON file
save_to_json_file(new_list, filename)
