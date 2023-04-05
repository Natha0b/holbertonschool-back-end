#!/usr/bin/python3

"""
script that given employee ID, returns information
"""

import requests
import sys

# API endpoint URL
BASE_URL = 'https://jsonplaceholder.typicode.com'

employee_id = int(sys.argv[1])

response = requests.get(f'{BASE_URL}/todos?userId={employee_id}')

todos = response.json()

num_completed_tasks = sum(todo['completed'] for todo in todos)
total_num_tasks = len(todos)

response = requests.get(f'{BASE_URL}/users/{employee_id}')
employee_name = response.json()['name']

print(f'Employee {employee_name} is done with\
      tasks({num_completed_tasks}/{total_num_tasks}):')

for todo in todos:
    if todo['completed']:
        print(f'\t {todo["title"]}')
