#!/usr/bin/python3
"""
Fetches user and todo data from 'jsonplaceholder.typicode.com' and
saves it in a JSON file.
"""

import json
import requests


def fetch_data():
    """Fetch data from the API endpoints."""
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")

    users = users_response.json()
    todos = todos_response.json()

    return users, todos


def format_data(users, todos):
    """Format the fetched data into the required JSON structure."""
    data = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = [
            {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            } for todo in todos if todo['userId'] == user_id
        ]
        data[user_id] = user_tasks

    return data


def save_to_file(data):
    """Save the formatted data to a JSON file."""
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    users, todos = fetch_data()
    formatted_data = format_data(users, todos)
    save_to_file(formatted_data)
