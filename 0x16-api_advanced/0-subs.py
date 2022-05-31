#!/usr/bin/python3
"""module which contains a function to bring information of Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and
    returns the number of subscribers
    """
    response = requests.get('https://reddit.com/r/{}/about.json\
'.format(subreddit), headers = {'User-agent': 'botardo'})
    return response.json().get('data').get('subscribers\
') if response.status_code != 404 else 0
