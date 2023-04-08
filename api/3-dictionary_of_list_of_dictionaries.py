#!/usr/bin/python3
"""Script that exports all information of an API to a JSON file"""
import json
import requests

if __name__ == '__main__':
    API_URL = 'https://jsonplaceholder.typicode.com'

    user_request = requests.get('{}/users'.format(
            API_URL))
    user_response = user_request.json()

    new_dict = {}
    for user in user_response:
        request = requests.get('{}/users/{}/todos'.format(
            API_URL, user['id']))

        response = request.json()

        new_dict[user['id']] = []
        for task in response:
            task_dict = {
                "username": user['username'],
                "task": task["title"],
                "completed": task["completed"]
            }
            new_dict[user['id']].append(task_dict)

    with open('todo_all_employees.json', 'w') as file:
        json.dump(new_dict, file)
