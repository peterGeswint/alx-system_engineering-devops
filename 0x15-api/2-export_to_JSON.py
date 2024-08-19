#!/usr/bin/python3

"""
Module Documentation:
This module exports the TODO list data of a specified employee to a JSON file.

The script accepts an employee ID as a command-line argument,
fetches the user's TODO list data,
and writes this data to a JSON file named after the employee ID.
The JSON file contains a single
record with the employee ID as the key and a list of tasks as the value.
Each task is represented
as a dictionary with the following fields:
- "task": The title of the task.
- "completed": A boolean indicating whether the task is completed.
- "username": The username of the employee.

Usage:
    ./2-export_to_JSON.py <employee_id>

Arguments:
    employee_id (int):
    The ID of the employee whose TODO list data is to be fetched.

Example:
    $ python3 2-export_to_JSON.py 2
    Data exported to 2.json
"""


import json
import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """Fetches and writes TODO progress for given employee to a JSON file."""

    # URLs for the REST API endpoints
    user_url = (
            f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    )

    todos_url = (
            f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    )

    # Fetch employee data
    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()
        employee_name = user_data.get('username')
    except requests.RequestException as e:
        print(f'Error fetching user data: {e}')
        return

    # Fetch TODO list data
    try:
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()
    except requests.RequestException as e:
        print(f'Error fetching TODO data: {e}')
        return

    # Prepare data for JSON output
    tasks = [
        {
            "task": todo['title'],
            "completed": todo['completed'],
            "username": employee_name
        }
        for todo in todos_data
    ]
    data = {str(employee_id): tasks}

    # Write to JSON file
    json_filename = f'{employee_id}.json'
    with open(json_filename, mode='w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f'Data exported to {json_filename}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: ./2-export_to_JSON.py <employee_id>')
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print('Error: employee_id must be an integer')
        sys.exit(1)

    fetch_employee_todo_progress(employee_id)
