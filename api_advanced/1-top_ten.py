#!/usr/bin/python3
"""Print titles of the first 10 hot posts for a subreddit."""

import requests


def top_ten(subreddit):
    """Query Reddit API and print first 10 hot post titles."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
        )
    except requests.RequestException:
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get("data", {}).get("children", [])
    for post in posts[:10]:
        title = post.get("data", {}).get("title")
        if title is not None:
            print(title)
