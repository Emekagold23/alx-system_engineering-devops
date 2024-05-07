#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    user_agent = {"User-Agent": "my_reddit_bot/1.0"}
    parameters = {"limit": 10}

    response = requests.get(url, headers=user_agent, params=parameters)
    try:
        data = response.json()
        host_posts = data.get('data').get('children')

        for i in hot_posts:
            print(i.get('data').get('title'))
    except Exception:
        print("None")
