#!/usr/bin/python3
"""given employee ID, returns information about his/her
"""
if __name__ == "__main__":
    from requests import get
    from sys import argv

    user = get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    url = get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    user = user.json()
    url = url.json()
    done = len([n for n in url if n['completed']])
    not_done = len([m for m in url])
    print("Employee {} is done with tasks({}/{}):".format(user['name'],
                                                          done,
                                                          not_done))
    for task in url:
        if task['completed'] is True:
            print("\t {}".format(task['title']))
