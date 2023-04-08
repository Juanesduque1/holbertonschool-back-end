#!/usr/bin/python3
"""Script that exports specific information to a JSON file"""
import json
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage error")
        sys.exit(1)

    API_URL = 'https://jsonplaceholder.typicode.com'
    id = sys.argv[1]
    request = requests.get('{}/users/{}/todos'.format(
        API_URL, id), params={"_expand": "user"})

    response = request.json()
    if len(response) == 0:
        print("RequestError: 404")
        sys.exit(1)

    new_dict = {id: []}
    for info in response:
        aux = {}
        aux.update(
            {"task": info['title'], "completed": info['completed'],
             "username": info['user']['username']})
        new_dict[id].append(aux)

        with open(f'{id}.json', 'w') as file:
            json.dump(new_dict, file)
