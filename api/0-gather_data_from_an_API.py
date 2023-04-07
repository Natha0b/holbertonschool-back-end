#!/usr/bin/python3
'''given employee ID, returns information about his/her.'''


if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    # Make API request to get employee's TODO list
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    tasks_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

    if user_response.status_code != 200 or tasks_response.status_code != 200:
        print("Failed to get TODO list for employee", employee_id)
        sys.exit(1)

    user = user_response.json()
    tasks = tasks_response.json()

    # Count completed tasks
    completed_tasks = [task for task in tasks if task['completed']]
    num_completed_tasks = len(completed_tasks)

    # Count total tasks
    num_total_tasks = len(tasks)

    # Get employee name
    employee_name = user['name']

    # Print progress report
    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{num_total_tasks}):")

    # Print completed tasks
    for task in completed_tasks:
        print(f"\t{task['title']}")