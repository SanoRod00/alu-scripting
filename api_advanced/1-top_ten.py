#!/usr/bin/python3
"""Print the titles of the first 10 hot posts for a subreddit."""
import requests


def top_ten(subreddit):
    """Query Reddit API and print titles of first 10 hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(
            url,
            headers=headers,
            params={"limit": 10},
            allow_redirects=False,
            timeout=10,
        )
    except requests.RequestException:
        print(None)
        return

    if response is None or response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])
    for post in posts:
        title = post.get("data", {}).get("title")
        if title:
            print(title)
