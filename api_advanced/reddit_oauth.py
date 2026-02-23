#!/usr/bin/python3
"""Helpers for Reddit OAuth2 requests."""
import os
import time

import requests


TOKEN_URL = "https://www.reddit.com/api/v1/access_token"
API_BASE_URL = "https://oauth.reddit.com"
PUBLIC_BASE_URL = "https://www.reddit.com"
REQUEST_TIMEOUT = 10

CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")

APP_ID = os.getenv("REDDIT_APP_ID", "api_advanced")
APP_VERSION = os.getenv("REDDIT_APP_VERSION", "1.0.0")
REDDIT_USER = os.getenv("REDDIT_USERNAME", "reddit_user")

USER_AGENT = os.getenv(
    "REDDIT_USER_AGENT",
    "linux:{}:v{} (by /u/{})".format(APP_ID, APP_VERSION, REDDIT_USER),
)

_TOKEN = None
_TOKEN_EXPIRES_AT = 0


def get_access_token():
    """Return an app-only access token, or None if unavailable."""
    global _TOKEN
    global _TOKEN_EXPIRES_AT

    if _TOKEN and time.time() < _TOKEN_EXPIRES_AT - 30:
        return _TOKEN

    if not CLIENT_ID or not CLIENT_SECRET:
        return None

    try:
        response = requests.post(
            TOKEN_URL,
            auth=(CLIENT_ID, CLIENT_SECRET),
            data={"grant_type": "client_credentials"},
            headers={"User-Agent": USER_AGENT},
            timeout=REQUEST_TIMEOUT,
        )
    except requests.RequestException:
        return None

    if response.status_code != 200:
        return None

    payload = response.json()
    token = payload.get("access_token")
    expires_in = payload.get("expires_in", 0)

    if not token:
        return None

    _TOKEN = token
    _TOKEN_EXPIRES_AT = time.time() + int(expires_in)
    return _TOKEN


def oauth_get(path, params=None):
    """GET Reddit data with OAuth when possible, else use public endpoint."""
    token = get_access_token()

    if token:
        headers = {
            "Authorization": "bearer {}".format(token),
            "User-Agent": USER_AGENT,
        }
        try:
            response = requests.get(
                "{}{}".format(API_BASE_URL, path),
                headers=headers,
                params=params,
                allow_redirects=False,
                timeout=REQUEST_TIMEOUT,
            )
            if response.status_code not in (401, 403):
                return response
        except requests.RequestException:
            pass

    try:
        return requests.get(
            "{}{}".format(PUBLIC_BASE_URL, path),
            headers={"User-Agent": USER_AGENT},
            params=params,
            allow_redirects=False,
            timeout=REQUEST_TIMEOUT,
        )
    except requests.RequestException:
        return None
