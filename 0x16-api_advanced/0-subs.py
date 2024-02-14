Certainly! Here's a slightly modified version with some improvements:

python

#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    try:
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        headers = {"User-Agent": "ahmedhatem"}

        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        if response.status_code == 200:
            return response.json().get("data", {}).get("subscribers", 0)
        else:
            print(f"Unexpected response code: {response.status_code}")
            return 0
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0
