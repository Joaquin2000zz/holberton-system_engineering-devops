#!/usr/bin/python3
"""module which contains a function to bring information of Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and
    returns the number of subscribers
    """
    response = requests.get('https://reddit.com/r/{}/about.jsoni\
'.format(subreddit), headers = {'User-agent': 'botardo'})
    return response.json().get('data').get('subscribers\
') if response.json().get('data').get('subscribers') is not None else 0
