#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        print("Invalid subreddit")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    user_agent = {"User-Agent": "my_reddit_bot/1.0"}
    parameters = {"limit": 10}

    try:
        response = requests.get(url, headers=user_agent, params=parameters)
        response.raise_for_status()  # Raise exception for non-200 status codes
        data = response.json()
        hot_posts = data.get('data', {}).get('children', [])

        if not hot_posts:
            print("No posts found")
            return

        for post in hot_posts:
            print(post.get('data', {}).get('title'))
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
