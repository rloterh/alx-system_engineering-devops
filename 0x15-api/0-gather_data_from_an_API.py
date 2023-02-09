#!/usr/bin/python3
"""
Fetch Data from a site using api
"""
from requests import get
import sys


if __name__ == '__main__':
    todos = get("https://jsonplaceholder.typicode.com/users/{}/todos".
                format(sys.argv[1]))
    employee = get("https://jsonplaceholder.typicode.com/users/{}".
                   format(sys.argv[1]))

    if todos.ok and employee.ok:
        todos_list = todos.json()
        employee_data = employee.json()
        completed = [complete.get("title") for complete in todos.json()
                     if
                     complete.get('completed')
                     ]
        # Design the output
        print("Employee {} is done with tasks({}/{}):".
              format(employee_data.get("name"),
                     len(completed),
                     len(todos_list)
                     )
              )
        # print titles completed
        for title in completed:
            print("\t {}".format(title))
