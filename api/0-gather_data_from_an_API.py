#!/usr/bin/python3
"""given employee ID, returns information about his/her"""

import requests
import sys


if __name__ == "__main__":

    BASE_URL = 'https://jsonplaceholder.typicode.com'

    employee_id = int(sys.argv[1])

    response = requests.get(f'{BASE_URL}/todos?userId={employee_id}')
    todos = response.json()

    num_completed_tasks = sum(todo['completed'] for todo in todos)
    total_num_tasks = len(todos)

    try:
        response = requests.get(f'{BASE_URL}/users/{employee_id}')
        employee_name = response.json()['name']
    except requests.exceptions.RequestException:
        employee_name = 'Unknown'

    print(f'Employee {employee_name} is done with tasks(\
          {num_completed_tasks}/{total_num_tasks}):')

    for todo in todos:
        if todo['completed']:
            print(f'\t {todo["title"]}')
