#!/usr/bin/python3
"""
Sends a POST request with a letter and handles JSON responses.
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    response = requests.post(url, data={"q": q})

    try:
        json_data = response.json()
    except ValueError:
        print("Not a valid JSON")
        sys.exit()

    if not json_data:
        print("No result")
    else:
        print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
