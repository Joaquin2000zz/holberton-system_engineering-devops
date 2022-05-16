#!/usr/bin/python3
"""
using the https://jsonplaceholder.typicode.com/ API with the requests module,
saves a <USERID>.json with specific content of the requests maded
"""
import requests
from sys import argv
import json as js
import os

todos = requests.get(f'https://jsonplaceholder.typicode.com/\
todos?userId={argv[1]}')
user = requests.get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
todos = todos.json()
user = user.json()

key = f"{argv[1]}"
bigDict = {key: []}

if not os.path.exists(f"{user.get('id')}.json"):
    for info in todos:
        littleDict = {}
        littleDict["task"] = info.get('title')
        littleDict["completed"] = info.get('completed')
        littleDict["username"] = user.get('username')
        bigDict[key].append(littleDict)
    with open(f"{user.get('id')}.json", 'a') as f:
        js.dump(bigDict, f)
