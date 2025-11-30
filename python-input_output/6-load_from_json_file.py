#!/usr/bin/python3
"""
This module defines a function to load an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.
    
    Args:
        filename (str): The name of the file from which the JSON data will be loaded.
    
    Returns:
        object: The Python object created from the JSON data.
    
    This function opens the file in read mode, reads the JSON data, and converts
    it into a corresponding Python object.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
