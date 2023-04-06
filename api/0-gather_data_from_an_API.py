#!/usr/bin/python3
'''given employee ID, returns information about his/her.'''

if __name__ == '__main__':
    import requests
    from sys import argv

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(argv[1]))
    tasks = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.
                         format(argv[1]))
    done_list = []
    done_tasks = 0
    total_tasks = 0

    employee_name = user.json()['name']
    for task in tasks.json():
        total_tasks += 1
        if task['completed'] is True:
            done_list.append(task['title'])
            done_tasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(employee_name, done_tasks, total_tasks))
    for task in done_list:
        print("\t {}".format(task))
