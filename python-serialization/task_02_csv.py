#!/usr/bin/python3
"""Convert CSV data to JSON"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format and save as data.json

    Args:
        csv_filename (str): Path to the input CSV file

    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        # Read CSV file into a list of dictionaries
        with open(csv_filename, mode=r, encoding=utf-8) as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        # Serialize list of dictionaries to JSON
        with open(data.json, mode=w, encoding=utf-8) as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except (FileNotFoundError, IOError, csv.Error, json.JSONDecodeError):
        return False
