#!/usr/bin/python3
"""
Module that defines a function to load
a Python object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): The file containing the JSON string.

    Returns:
        object: The Python object created from the JSON data.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
