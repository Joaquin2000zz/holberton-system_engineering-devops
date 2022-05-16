#!/usr/bin/python3
"""
using the https://jsonplaceholder.typicode.com/ API with the requests module
"""
import requests
from sys import argv
todos = requests.get(f'https://jsonplaceholder.typicode.com/\
todos?userId={argv[1]}')
user = requests.get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
todos = todos.json()
user = user.json()
totalTasks = 0
completed = 0
completedList = []
for info in todos:
    totalTasks += 1
    if info.get('completed') is True:
        completed += 1
        completedList.append(info.get('title'))
print(f"Employee {user.get('name')} is done with tasks({completed}/\
{totalTasks}):")
for line in completedList:
    print(f"\t{line}")
