#!/usr/bin/python3
"""Print the titles of the first 10 hot posts for a subreddit."""
import requests


def top_ten(subreddit):
    """Query Reddit API and print titles of first 10 hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:api_advanced.top_ten:v1.0 (by /u/reddit_client)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10,
        )
    except requests.RequestException:
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    if not posts:
        print(None)
        return

    for post in posts:
        print(post.get("data", {}).get("title"))
