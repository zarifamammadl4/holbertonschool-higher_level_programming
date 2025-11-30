#!/usr/bin/python3
import json

def load_from_json_file(filename):
    """
    Creates an object from a JSON file.
    
    Args:
        filename (str): The name of the file from which the JSON data will be loaded.
    
    Returns:
        object: The Python object created from the JSON data.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
