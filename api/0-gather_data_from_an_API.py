#!/usr/bin/python3
"""Prints tasks completed of a certain user"""

import requests
from sys import argv


if __name__ == "__main__":
    emp_id = argv[1]

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/", params={"id": emp_id}).json()
    tasks = requests.get(url + "todos/", params={"userId": emp_id}).json()

    name = user[0].get("name") if len(user) > 0 else None
    tasks_d = [task.get('title') for task in tasks
               if task.get('completed') is True]
    tasks_t, tasks_c = len(tasks), len(tasks_d)

    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          tasks_c,
                                                          tasks_t))
    [print("\t {}".format(task)) for task in tasks_d]
