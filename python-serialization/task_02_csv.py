#!/usr/bin/python3
"""Convert CSV data to JSON format"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to JSON and writes to data.json

    Args:
        csv_filename (str): CSV file to read

    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        # Read CSV file
        with open(csv_filename, mode=r, encoding=utf-8) as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        # Write JSON file
        with open("data.json", mode=w, encoding=utf-8) as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        # CSV file does not exist
        return False
    except Exception:
        # Any other exceptions (malformed CSV, permission errors, etc.)
        return False
