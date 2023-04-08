#!/usr/bin/python3
"""Script to export data in the JSON format."""

import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users/").json()
    tasks = requests.get(url + "todos/").json()

    all_todos = {}
    for user in users:
        user_id = user.get("id")
        task_list = [{"task": task.get('title'),
                      "completed": task.get('completed'),
                      "username": user.get("username")}
                     for task in tasks if user_id == task.get("userId")]
        all_todos[user_id] = task_list

    with open("todo_all_employees.json", "w", newline="") as jsonfile:
        json.dump(all_todos, jsonfile)
