#!/usr/bin/python3
"""
using the https://jsonplaceholder.typicode.com/ API with the requests module,
saves a todo_all_employees.json with specific content of the requests maded
"""


import json as js
import os
import requests
from sys import argv


if __name__ == "__main__":

    def lazy(n, dictio):
        """
        automatize the task in one single function
        """
        todos = requests.get("https://jsonplaceholder.typicode.com/\
todos?userId={}".format(n))
        user = requests.get("https://jsonplaceholder.typicode.com/users/{}\
".format(n))
        todos = todos.json()
        user = user.json()
        if len(user) == 0 or len(todos) == 0:
            return None

        key = "{}".format(n)
        if dictio is None:
            bigDict = {key: []}
        else:
            bigDict = dictio
            bigDict["{}".format(n)] = []

        if not os.path.exists("todo_all_employees.json"):
            for info in todos:
                littleDict = {}
                littleDict["username"] = user.get('username')
                littleDict["task"] = info.get('title')
                littleDict["completed"] = info.get('completed')
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
    with open("todo_all_employees.json", 'a') as f:
        js.dump(FinalDict, f)
