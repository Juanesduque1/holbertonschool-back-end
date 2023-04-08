#!/usr/bin/python3
"""Script that exports specific information to a CSV file"""
import csv
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
        print("Error: 404")
        sys.exit(1)

    for info in response:
        new_list = []
        new_list.append(str(id))
        new_list.append(str(info['user']['username']))
        new_list.append(str(info['completed']))
        new_list.append(str(info['title']))

        with open(f'{id}.csv', 'a', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(new_list)
