#!/usr/bin/python3
"""
function that queries the 'Reddit API' and returns the number of subscribers
"""
from reddit_oauth import oauth_get


def number_of_subscribers(subreddit):
    """
    number of subscribers
    """
    response = oauth_get("/r/{}/about.json".format(subreddit))
    if response is None or response.status_code != 200:
        return 0
    data = response.json()
    return data.get("data", {}).get("subscribers", 0)
