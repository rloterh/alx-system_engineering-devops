#!/usr/bin/python3
"""
Fetch Data from a site using api and save to csv file
"""
import json
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
        outer_dict_format = dict()
        with open("{}.json".format(sys.argv[1]), "w",
                  encoding="utf-8") as file:
            list_format = []
            for task in todos_list:
                data = {"task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": employee_data.get("username")
                        }
                list_format.append(data)
                outer_dict_format[sys.argv[1]] = list_format
            json.dump(outer_dict_format, file)
