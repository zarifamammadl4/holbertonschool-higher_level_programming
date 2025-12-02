#!/usr/bin/python3
"""
Fetches posts from JSONPlaceholder and processes them.
"""

import requests
import csv


def fetch_and_print_posts():
    """Fetch all posts and print their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print("Status Code:", response.status_code)
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch all posts and save them into a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        structured_data = [
            {"id": post.get("id"), "title": post.get("title"), "body": post.get("body")}
            for post in posts
        ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(structured_data)
