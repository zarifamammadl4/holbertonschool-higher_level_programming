#!/usr/bin/python3
"""
Displays the GitHub user id using Basic Authentication.
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]  # personal access token

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, token))

    try:
        json_data = response.json()
        print(json_data.get("id"))
    except ValueError:
        print("None")
