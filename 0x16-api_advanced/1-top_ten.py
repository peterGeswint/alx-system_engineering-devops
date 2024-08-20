#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and print
the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'my-app/0.0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response is empty or invalid
        if response.status_code != 200 or not response.content.strip():
            print(None)
            return

        data = response.json()
        posts = data.get('data', {}).get('children', [])

        for post in posts:
            print(post.get('data', {}).get('title'))

    except (requests.RequestException, ValueError):
        print(None)
