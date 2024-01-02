#!/usr/bin/python3

"""
Python script to export data in the JSON format.
"""

import requests
import json
import sys

def get_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    user_id = user_data.get('id')
    username = user_data.get('username')

    # Fetch TODO list for the user
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()

    # Prepare data for JSON
    json_data = {str(user_id): [{"task": task['title'], "completed": task['completed'], "username": username} for task in todo_data]}

    # Export to JSON file
    json_file_name = f"{user_id}.json"
    with open(json_file_name, 'w') as json_file:
        json.dump(json_data, json_file)

    print(f"Data exported to {json_file_name}")

if __name__ == "__main__":
    # Check if the correct number and type of command-line arguments are provided
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    # Convert the provided argument to an integer (employee ID)
    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)
