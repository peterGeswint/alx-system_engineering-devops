#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and return the number
of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for the given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "my-app/0.0.1"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
        else:
            return 0
    except requests.RequestException as e:
        return 0
