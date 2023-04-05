#!/usr/bin/python3
"""
Script to export data in the CSV format.
"""

if __name__ == "__main__":

    import requests
    import sys
    import csv

    # API endpoint URL
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    # Get employee ID from command line argument
    employee_id = int(sys.argv[1])

    # Send GET request to API endpoint for employee's todos
    response = requests.get(f'{BASE_URL}/todos?userId={employee_id}')

    # Extract JSON data from response
    todos = response.json()

    # Get employee name from API endpoint
    response = requests.get(f'{BASE_URL}/users/{employee_id}')
    employee_name = response.json()['username']

    # Define CSV file name
    csv_file_name = f'{employee_id}.csv'

    # Open CSV file for writing
    with open(csv_file_name, mode='w', newline='') as csv_file:
        # Create CSV writer
        writer = csv.writer(csv_file, delimiter=',')

        # Write CSV header row
        writer.writerow(['USER_ID', 'USERNAME',
                        'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

        # Write CSV data rows
        for todo in todos:
            writer.writerow([employee_id, employee_name,
                            todo['completed'], todo['title']])

        print(f'{csv_file_name} has been created successfully.')
