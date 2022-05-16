#!/usr/bin/python3
"""
using the https://jsonplaceholder.typicode.com/ API with the requests module,
saves a <USERID>.csv with specific content of the requests maded
"""
import requests
from sys import argv
import csv
import os

todos = requests.get(f'https://jsonplaceholder.typicode.com/\
todos?userId={argv[1]}')
user = requests.get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
todos = todos.json()
user = user.json()

completedList = [f"{argv[1]}", f"{user.get('username')}", "", ""]

if not os.path.exists(f"{user.get('id')}.csv"):
    for info in todos:
        completedList[2] = info.get('completed')
        completedList[3] = info.get('title')
        with open(f"{user.get('id')}.csv", 'a') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerow(completedList)
