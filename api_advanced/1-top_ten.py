#!/usr/bin/python3
"""Print the titles of the first 10 hot posts for a subreddit."""
import requests


def top_ten(subreddit):
    """Query Reddit API and print titles of first 10 hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])
    for post in posts:
        title = post.get("data", {}).get("title")
        if title:
            print(title)
