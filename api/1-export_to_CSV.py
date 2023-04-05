#!/usr/bin/python3
"""
Script to export data in the CSV format.
"""

import requests
import sys
import csv

BASE_URL = 'https://jsonplaceholder.typicode.com'

employee_id = int(sys.argv[1])

response = requests.get(f'{BASE_URL}/todos?userId={employee_id}')

todos = response.json()

response = requests.get(f'{BASE_URL}/users/{employee_id}')
employee_name = response.json()['username']

csv_file_name = f'{employee_id}.csv'

with open(csv_file_name, mode='w', newline='') as csv_file:
    # Create CSV writer
    writer = csv.writer(csv_file, delimiter=',')

    writer.writerow(['USER_ID', 'USERNAME',
                     'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

    for todo in todos:
        writer.writerow([employee_id, employee_name,
                         todo['completed'], todo['title']])

    print(f'{csv_file_name} has been created successfully.')
