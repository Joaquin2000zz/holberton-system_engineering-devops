#!/usr/bin/python3
"""
using the https://jsonplaceholder.typicode.com/ API with the requests module,
saves a <USERID>.csv with specific content of the requests maded
"""


import csv
import os
import requests
from sys import argv


todos = requests.get("https://jsonplaceholder.typicode.com/\
todos?userId={}".format(argv[1]))
user = requests.get("https://jsonplaceholder.typicode.com/users/{}\
".format(argv[1]))
todos = todos.json()
user = user.json()

completedList = ["{}".format(argv[1]), "{}".format(user.get('username\
')), "", ""]

if not os.path.exists("{}.csv".format(user.get('id'))):
    for info in todos:
        completedList[2] = info.get('completed')
        completedList[3] = info.get('title')
        with open("{}.csv".format(user.get('id')), 'a') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerow(completedList)
