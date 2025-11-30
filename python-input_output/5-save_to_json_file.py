#!/usr/bin/python3
import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.
    
    Args:
        my_obj (object): The object to be serialized.
        filename (str): The name of the file to write the JSON string to.
    
    This function opens the file in write mode, serializes the object `my_obj`
    to a JSON formatted string, and writes it to the specified file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
