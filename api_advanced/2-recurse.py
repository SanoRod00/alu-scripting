#!/usr/bin/python3
"""Recursively query Reddit API and return hot post titles."""
from reddit_oauth import oauth_get


def recurse(subreddit, hot_list=[]):
    """Return a list of hot post titles for a subreddit."""
    titles = list(hot_list)
    def _fetch(after=None):
        params = {"limit": 100}
        if after:
            params["after"] = after

        response = oauth_get("/r/{}/hot.json".format(subreddit), params=params)
        if response is None or response.status_code != 200:
            return None

        data = response.json().get("data", {})
        posts = data.get("children", [])

        for post in posts:
            title = post.get("data", {}).get("title")
            if title is not None:
                titles.append(title)

        next_after = data.get("after")
        if next_after is None:
            return titles
        return _fetch(next_after)

    return _fetch()
