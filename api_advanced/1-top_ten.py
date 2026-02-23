#!/usr/bin/python3
"""Query Reddit API and print titles of the first 10 hot posts."""

import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts for a subreddit, else None."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(
            url,
            headers=headers,
            params={"limit": 10},
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
        title = post.get("data", {}).get("title")
        if isinstance(title, str):
            print(title)
