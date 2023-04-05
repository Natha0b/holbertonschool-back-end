#!/usr/bin/python3
"""given employee ID, returns information about his/her"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python employee_todo.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = sys.argv[1]

    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = response.json()

    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todos_data = response.json()

    num_completed_tasks = sum(1 for todo in todos_data if todo["completed"])
    total_num_tasks = len(todos_data)

    print(f"Employee {employee_data['name']} is done with tasks ({num_completed_tasks}/{total_num_tasks}):")
    for todo in todos_data:
        if todo["completed"]:
            print(f"\t {todo['title']}")
