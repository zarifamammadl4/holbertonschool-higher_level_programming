#!/usr/bin/python3
"""
This script adds all command line arguments to a Python list, 
and saves them to a JSON file.
"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Try to load the current content of the file, if it exists
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Add command line arguments to the list (excluding the script name)
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
