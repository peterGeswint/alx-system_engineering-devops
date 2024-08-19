#!/usr/bin/python3

"""
1-export_to_CSV.py

This script fetches the TODO list progress for a given employee ID from
the JSONPlaceholder API and exports the data to a CSV file. Each record
in the CSV file contains the employee ID, username, task completion status,
and task title.

Usage:
    ./1-export_to_CSV.py <employee_id>

Arguments:
    <employee_id> - An integer representing the ID of the employee.

The resulting CSV file is named <employee_id>.csv.
"""
import csv
import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """Fetches and writes TODO list progress for an employee to a CSV file."""

    # URLs for the REST API endpoints
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
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

    # Write to CSV file
    csv_filename = f'{employee_id}.csv'
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            writer.writerow([
                employee_id,
                employee_name,
                todo['completed'],
                todo['title']
            ])

    print(f'Data exported to {csv_filename}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: ./1-export_to_CSV.py <employee_id>')
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print('Error: employee_id must be an integer')
        sys.exit(1)

    fetch_employee_todo_progress(employee_id)
