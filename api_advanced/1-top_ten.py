#!/usr/bin/python3
"""Print the titles of the first 10 hot posts for a subreddit."""
from reddit_oauth import oauth_get


def top_ten(subreddit):
    """Query Reddit API and print titles of first 10 hot posts."""
    response = oauth_get("/r/{}/hot.json".format(subreddit), params={"limit": 10})
    if response is None or response.status_code != 200:
        print(None)
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])
    for post in posts:
        title = post.get("data", {}).get("title")
        if title is not None:
            print(title)
