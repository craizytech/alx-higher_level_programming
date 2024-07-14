#!/usr/bin/python3
"""Load, add, save"""
import json
import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

old_list = None
if os.path.exists(filename):
    old_list = load_from_json_file(filename)

argv_list = sys.argv[1:]

if old_list is None:
    save_to_json_file(argv_list, filename)
else:
    final_list = old_list + argv_list
    save_to_json_file(final_list, filename)
