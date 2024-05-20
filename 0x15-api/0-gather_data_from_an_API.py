#!/usr/bin/python3
"""
Gather data from REST API and display employee TODO loist progress
"""


import requests
import sys

def fetch_employee_data(employee_id):
    """
    fetch employee data including name and todo list progress.
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = f"{base_url}users/{employee_id}"
    todos_url = f"{base_url}todos?userId={employee_id}"

    #getemployee information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        return None, None

    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Get employee todos
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        return employee_name, None

    todos_data = todos_response.json()

    return employee_name, todos_data

def display_todo_progress(employee_name, todos_data):
    """
    Display the TODO list progress of the employee.
    """
    if not employee_name or todos_data is None:
        print("Invalid employee ID or no data found")
        return

    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")

    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_name, todos_data = fetch_employee_data(employee_id)
    display_todo_progress(employee_name, todos_data)
