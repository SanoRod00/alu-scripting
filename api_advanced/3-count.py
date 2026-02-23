#!/usr/bin/python3
"""Count given keywords in hot article titles for a subreddit."""
from reddit_oauth import oauth_get


def count_words(subreddit, word_list, after=None, word_count=None):
    """Print word frequencies sorted by count desc, then alphabetically."""
    if word_count is None:
        word_count = {}
        for word in word_list:
            word_count[word.lower()] = 0

    if not word_count:
        return

    params = {"limit": 100}
    if after:
        params["after"] = after

    response = oauth_get("/r/{}/hot.json".format(subreddit), params=params)
    if response is None or response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "")
        for token in title.split():
            lowered = token.lower()
            if lowered in word_count:
                word_count[lowered] += 1

    next_after = data.get("after")
    if next_after:
        return count_words(subreddit, word_list, next_after, word_count)

    sorted_counts = sorted(
        word_count.items(),
        key=lambda item: (-item[1], item[0]),
    )
    for word, total in sorted_counts:
        if total > 0:
            print("{}: {}".format(word, total))
