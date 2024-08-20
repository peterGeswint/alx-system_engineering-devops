#!/usr/bin/python3
"""
This module provides a recursive function to query the Reddit API and
return a list of titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): The list of titles accumulated over recursive calls.
        after (str): The `after` parameter for pagination.

    Returns:
        list: A list containing the titles of all hot articles, or None if the
        subreddit is invalid or has no hot articles.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(

            url, headers=headers, params=params, allow_redirects=False

        )
        if response.status_code == 200:
            data = response.json().get('data', {})
            children = data.get('children', [])
            for child in children:
                hot_list.append(child['data']['title'])
            after = data.get('after')
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
