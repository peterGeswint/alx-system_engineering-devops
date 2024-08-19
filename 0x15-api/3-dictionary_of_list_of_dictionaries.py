#!/usr/bin/python3
"""
This script fetches data from a
URL containing to-do tasks for employees,
processes the data, and exports it into a JSON file named
'todo_all_employees.json'.
The JSON format organizes tasks by user ID,
with each entry containing
the username, task title, and completion status.
"""

import json
import requests


def fetch_data(url):
    """Fetch data from the provided URL."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()


def process_data(data):
    """Process the fetched data and return a dictionary organized by ID."""
    user_tasks = {}
    for item in data:
        user_id = str(item.get('userId'))
        username = item.get('username')
        task_title = item.get('title')
        completed = item.get('completed')

        if user_id not in user_tasks:
            user_tasks[user_id] = []

        user_tasks[user_id].append({
            "username": username,
            "task": task_title,
            "completed": completed
        })
    return user_tasks


def save_to_json(data, filename):
    """Save the processed data to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    """Main function to execute the script."""
    url = 'https://jsonplaceholder.typicode.com/todos'
    data = fetch_data(url)
    processed_data = process_data(data)
    save_to_json(processed_data, 'todo_all_employees.json')


if __name__ == "__main__":
    main()
