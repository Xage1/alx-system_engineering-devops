#!/usr/bin/python3


"""
 Python script to export data in the CSV format.
"""
import requests
import csv
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

    # Prepare data for CSV
    csv_data = []
    for task in todo_data:
        task_completed_status = str(task['completed'])
        task_title = task['title']
        csv_data.append([user_id, username, task_completed_status, task_title])

    # Export to CSV file
    csv_file_name = f"{user_id}.csv"
    with open(csv_file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(csv_data)

    print(f"Data exported to {csv_file_name}")

if __name__ == "__main__":
    # Check if the correct number and type of command-line arguments are provided
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    # Convert the provided argument to an integer (employee ID)
    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)
