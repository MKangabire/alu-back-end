#!/usr/bin/python3

import requests

""" we are extracting the todos of the employees by their IDs"""

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(f"{base_url}/users/{employee_id}")
    use_data = user_response.json()
    employee_name = user_data['name']

    todos_response = requess.get(f"{base_url}/todos?userId={employee-id}")
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    print(f"{emplotee_name}\'s completed tasks:")

    for todo in todos_data:
        if todo['completed']:
            print(f"\t{todo['title]}")

if __name__ == "__main__":
    employee_id = int(input("Enter your employee ID: "))
    get_employee_todo_progress(employee_id)
