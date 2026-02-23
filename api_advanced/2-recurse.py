#!/usr/bin/python3
"""Recursively query Reddit API and return hot post titles."""
import requests


def recurse(subreddit, hot_list=[]):
    """Return a list of hot post titles for a subreddit."""
    titles = list(hot_list)
    headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    def _fetch(after=None):
        params = {"limit": 100}
        if after:
            params["after"] = after

        try:
            response = requests.get(
                url, headers=headers, params=params, allow_redirects=False
            )
        except requests.RequestException:
            return []

        if response.status_code != 200:
            return []

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
