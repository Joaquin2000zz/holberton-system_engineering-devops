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

    def lazy():
        """
        automatize the task in one single function
        """
        users = requests.get("https://jsonplaceholder.typicode.com/use\
rs").json()
        userids = {}
        for user in users:
            userids["{}".format(user.get('id'))] = user.get('username')
        bigDict = {}
        if not os.path.exists("todo_all_employees.json"):
            for userid, username in userids.items():
                bigDict["{}".format(userid)] = []
                todos = requests.get("https://jsonplaceholder.typicode.com/\
todos?userId={}".format(userid)).json()
                for info in todos:
                    littleDict = {}
                    littleDict["username"] = username
                    littleDict["task"] = info.get('title')
                    littleDict["completed"] = info.get('completed')
                    bigDict["{}".format(userid)].append(littleDict)
        return bigDict

    check = lazy()
    if check is not None:
        FinalDict = check
    with open("todo_all_employees.json", 'a+') as f:
        js.dump(FinalDict, f)
