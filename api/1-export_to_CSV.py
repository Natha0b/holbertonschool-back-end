#!/usr/bin/python3
"""Script to export data in the CSV format."""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    emp_id = argv[1]

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/", params={"id": emp_id}).json()
    tasks = requests.get(url + "todos/", params={"userId": emp_id}).json()

    username = user[0].get("username") if len(user) > 0 else None
    rows = [[emp_id, username, task.get('completed'), task.get('title')]
            for task in tasks]

    with open("{}.csv".format(emp_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        writer.writerows(rows)
