#!/usr/bin/python3
"""Query Reddit API and print titles of the first 10 hot posts."""

import requests


def top_ten(subreddit):
    """Print titles of the first 10 hot posts for subreddit, else None."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "ALX-API-Advanced"}

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
        )
    except requests.RequestException:
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json().get("data", {}).get("children", [])
    except ValueError:
        print(None)
        return

    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
