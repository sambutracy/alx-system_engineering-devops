#!/usr/bin/python3
"""
Gather data from a REST API and export employee TODO list progress to JSON.
"""

import json
import requests
import sys


def fetch_employee_data(employee_id):
    """
    Fetch employee data including name and todo list progress.
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = f"{base_url}users/{employee_id}"
    todos_url = f"{base_url}todos?userId={employee_id}"

    # Get employee information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        return None, None

    user_data = user_response.json()
    employee_name = user_data.get('username')

    # Get employee's todos
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        return employee_name, None

    todos_data = todos_response.json()

    return employee_name, todos_data


def export_to_json(employee_id, employee_name, todos_data):
    """
    Export the TODO list progress of the employee to a JSON file.
    """
    if not employee_name or todos_data is None:
        print("Invalid employee ID or no data found.")
        return

    tasks_list = []
    for task in todos_data:
        tasks_list.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name
        })

    data = {str(employee_id): tasks_list}

    filename = f"{employee_id}.json"
    with open(filename, mode='w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_name, todos_data = fetch_employee_data(employee_id)
    export_to_json(employee_id, employee_name, todos_data)
