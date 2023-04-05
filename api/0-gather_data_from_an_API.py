#!/usr/bin/python3
'''Script that given employee ID, returns information'''

if __name__ == '__main__':
    import requests
    import sys

    '''API endpoint URL'''
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    '''Get employee ID from command line argument'''
    employee_id = int(sys.argv[1])

    response = requests.get(f'{BASE_URL}/todos?userId={employee_id}')

    '''Extract JSON data from response'''
    todos = response.json()

    num_completed_tasks = sum(todo['completed'] for todo in todos)
    total_num_tasks = len(todos)

    response = requests.get(f'{BASE_URL}/users/{employee_id}')
    employee_name = response.json()['name']

    '''Print employee TODO list progress'''
    print(f'Employee {employee_name} is done with\
        tasks({num_completed_tasks}/{total_num_tasks}):')

    '''Print title of completed tasks'''
    for todo in todos:
        if todo['completed']:
            print(f'\t {todo["title"]}')
