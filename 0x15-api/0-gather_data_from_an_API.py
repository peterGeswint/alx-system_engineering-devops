#!/usr/bin/python3

"""
0-gather_data_from_an_API.py

This script fetches the TODO list progress for a given employee ID from
the JSONPlaceholder API and prints the progress in a formatted way. It
displays the employee's name, the number of completed tasks, and the
total number of tasks. Additionally, it lists the titles of the completed
tasks.

Usage:
    ./0-gather_data_from_an_API.py <employee_id>

Arguments:
    <employee_id> - An integer representing the ID of the employee.

The output format is as follows:
    Employee EMPLOYEE_NAME is done with
    tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    [TAB] TASK_TITLE

Where:
    - EMPLOYEE_NAME: The name of the employee.
    - NUMBER_OF_DONE_TASKS: Number of completed tasks.
    - TOTAL_NUMBER_OF_TASKS: Total number of tasks.
    - TASK_TITLE: The title of each completed task,
    indented with a tab and a space.

Example:
    $ python3 0-gather_data_from_an_API.py 2
    Employee Ervin Howell is done with tasks(8/20):
         distinctio vitae autem nihil ut molestias quo
         voluptas quo tenetur perspiciatis explicabo natus
         ...
"""


import sys
import requests


def fetch_employee_todo_progress(employee_id):
    """Fetches and prints the TODO list progress for a given employee ID"""

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
        employee_name = user_data.get('name')
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

    # Calculate TODO list progress
    total_tasks = len(todos_data)
    done_tasks = [

            todo['title'] for todo in todos_data if todo['completed']

    ]

    # Print results
    print(
        f'Employee {employee_name} is done with tasks({len(done_tasks)}/'
        f'{total_tasks}): '
    )
    for task in done_tasks:
        print(f'    {task}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: ./0-gather_data_from_an_API.py <employee_id>')
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print('Error: employee_id must be an integer')
        sys.exit(1)

    fetch_employee_todo_progress(employee_id)
