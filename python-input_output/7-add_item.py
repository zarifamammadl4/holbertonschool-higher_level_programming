#!/usr/bin/python3
"""
This script adds all command line arguments to a Python list,
and saves them to a JSON file named add_item.json.
It uses the functions save_to_json_file and load_from_json_file
to handle the JSON file.
"""

import sys
import importlib.util
import os

# Import save_to_json_file
spec = importlib.util.spec_from_file_location(
    "save_to_json_file",
    os.path.join(os.path.dirname(__file__), "5-save_to_json_file.py")
)
save_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(save_module)
save_to_json_file = save_module.save_to_json_file

# Import load_from_json_file
spec = importlib.util.spec_from_file_location(
    "load_from_json_file",
    os.path.join(os.path.dirname(__file__), "6-load_from_json_file.py")
)
load_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(load_module)
load_from_json_file = load_module.load_from_json_file

filename = "add_item.json"

# Load existing list if file exists, otherwise start with empty list
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Add all command line arguments (except script name)
items.extend(sys.argv[1:])

# Save updated list back to file
save_to_json_file(items, filename)
