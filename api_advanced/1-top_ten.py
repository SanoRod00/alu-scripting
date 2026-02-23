#!/usr/bin/python3
"""Query Reddit API and print the first 10 hot post titles."""

import requests


def _hot_response(subreddit):
    """Return a 200-response object for subreddit hot posts, or None."""
    headers = {"User-Agent": "linux:api_advanced:v1.0 (by /u/reddit_api_bot)"}
    endpoints = [
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        "https://old.reddit.com/r/{}/hot.json".format(subreddit),
        "https://api.reddit.com/r/{}/hot".format(subreddit),
    ]

    for url in endpoints:
        try:
            response = requests.get(
                url,
                headers=headers,
                params={"limit": 10},
                allow_redirects=False,
            )
        except requests.RequestException:
            continue

        if response.status_code == 200:
            return response

        if response.status_code in (301, 302, 303, 307, 308, 404):
            return None

    return None


def top_ten(subreddit):
    """Print titles of first 10 hot posts for a subreddit, else None."""
    response = _hot_response(subreddit)
    if response is None:
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
