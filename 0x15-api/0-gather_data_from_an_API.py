#!/usr/bin/python3

""" Python script that, uses a  REST API, for a given employee ID, returns information about his/her TODO list progress.
"""
import requests
import sys

def get_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch TODO list for the user
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()

    # Calculate number of completed tasks
    completed_tasks = [task for task in todo_data if task['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todo_data)

    # Display information
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)
