#!/usr/bin/python3
"""Exports as json the tasks of a certain user"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    emp_id = argv[1]

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/", params={"id": emp_id}).json()
    tasks = requests.get(url + "todos/", params={"userId": emp_id}).json()

    username = user[0].get("username") if len(user) > 0 else None
    task_list = [{"task": task.get('title'),
                  "completed": task.get('completed'),
                  "username": username} for task in tasks]

    with open("{}.json".format(emp_id), "w", newline="") as jsonfile:
        json.dump({emp_id: task_list}, jsonfile)
