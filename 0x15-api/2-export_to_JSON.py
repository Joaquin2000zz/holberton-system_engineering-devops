#!/usr/bin/python3
"""
using the https://jsonplaceholder.typicode.com/ API with the requests module,
saves a <USERID>.json with specific content of the requests maded
"""


import json as js
import os
import requests
from sys import argv


if __name__ == "__main__":

    todos = requests.get("https://jsonplaceholder.typicode.com/\
todos?userId={}".format(argv[1]))
    user = requests.get("https://jsonplaceholder.typicode.com/users/\
{}".format(argv[1]))
    todos = todos.json()
    user = user.json()

    key = "{}".format(argv[1])
    bigDict = {key: []}

    if not os.path.exists("{}.json".format(user.get('id'))):
        for info in todos:
            littleDict = {}
            littleDict["task"] = info.get('title')
            littleDict["completed"] = info.get('completed')
            littleDict["username"] = user.get('username')
            bigDict[key].append(littleDict)
        with open("{}.json".format(user.get('id')), 'a+') as f:
            js.dump(bigDict, f)
