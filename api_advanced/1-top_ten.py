#!/usr/bin/python3
"""Print the titles of the first 10 hot posts for a subreddit."""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "python:api_advanced:v1.0 (by /u/reddit_user)"}

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=10,
        )
    except requests.RequestException:
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get("data", {}).get("children", [])
    for post in posts:
        title = post.get("data", {}).get("title")
        if title is not None:
            print(title)
