import json
import requests

# Define the base URL for the JSONPlaceholder API
base_url = 'https://jsonplaceholder.typicode.com/'

# Fetch all users
users_response = requests.get(base_url + 'users')
users = users_response.json()

# Fetch all tasks
todos_response = requests.get(base_url + 'todos')
todos = todos_response.json()

# Initialize a dictionary to hold the tasks for each user
tasks_by_user = {}

# Organize the tasks by user ID
for user in users:
    user_id = user['id']
    username = user['username']
    tasks_by_user[user_id] = []
    for todo in todos:
        if todo['userId'] == user_id:
            task_info = {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            }
            tasks_by_user[user_id].append(task_info)

# Export the tasks by user dictionary to a JSON file
with open('todo_all_employees.json', 'w') as json_file:
    json.dump(tasks_by_user, json_file, indent=4)

print("Data has been exported to todo_all_employees.json")
