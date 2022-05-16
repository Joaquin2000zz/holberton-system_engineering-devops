#!/usr/bin/python3
"""
using the https://jsonplaceholder.typicode.com/ API with the requests module,
saves a todo_all_employees.json with specific content of the requests maded
"""
import requests
from sys import argv
import json as js
import os


def lazy(n, dictio):
    """
    automatize the task in one single function
    """
    todos = requests.get(f'https://jsonplaceholder.typicode.com/\
todos?userId={n}')
    user = requests.get(f'https://jsonplaceholder.typicode.com/users/{n}')
    todos = todos.json()
    user = user.json()
    if len(user) == 0 or len(todos) == 0:
        return None

    key = f"{n}"
    if dictio is None:
        bigDict = {key: []}
    else:
        bigDict = dictio
        bigDict[f"{n}"] = []

    if not os.path.exists(f"todo_all_employees.json"):
        for info in todos:
            littleDict = {}
            littleDict["task"] = info.get('title')
            littleDict["completed"] = info.get('completed')
            littleDict["username"] = user.get('username')
            bigDict[key].append(littleDict)
    return bigDict


flag = False
for i in range(10):
    if flag is False:
        flag = True
        check = lazy(i + 1, None)
        if check is not None:
            FinalDict = check
    else:
        check = lazy(i + 1, FinalDict)
        if check is not None:
            FinalDict = check
with open(f"todo_all_employees.json", 'a') as f:
    js.dump(FinalDict, f)
