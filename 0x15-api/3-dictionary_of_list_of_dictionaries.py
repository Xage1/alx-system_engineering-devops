#!/usr/bin/python3
"""
Script to export data in JSON format for all tasks from all employees.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    api_url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(api_url + 'users').json()
    all_tasks = {}

    for user in users:
        user_id = str(user.get('id'))
        username = user.get('username')
        tasks = requests.get(api_url + f'todos?userId={user_id}').json()

        user_tasks = []
        for task in tasks:
            task_data = {
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed'),
            }
            user_tasks.append(task_data)

        all_tasks[user_id] = user_tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file)
