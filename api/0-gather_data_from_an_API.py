#!/usr/bin/python3
'''given employee ID, returns information about his/her.'''


if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    EMPLOYEE_ID = sys.argv[1]

    # Make API request to get employee's TODO list
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}")
    tasks_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={EMPLOYEE_ID}")

    if user_response.status_code != 200 or tasks_response.status_code != 200:
        print("Failed to get TODO list for employee", EMPLOYEE_ID)
        sys.exit(1)

    user = user_response.json()
    tasks = tasks_response.json()

    # Count completed tasks
    completed_tasks = [task for task in tasks if task['completed']]
    NUMBER_OF_DONE_TASKS = len(completed_tasks)

    # Count total tasks
    TOTAL_NUMBER_OF_TASKS = len(tasks)

    # Get employee name
    EMPLOYEE_NAME = user['name']

    # Print progress report
    print(f"Employee {EMPLOYEE_NAME} is done with tasks ({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

    # Print completed tasks
    for task in completed_tasks:
        print(f"\t{task['title']}")