#!/usr/bin/python3
"""
Fetch Data from a site using api and save to csv file
"""
import json
from requests import get
import sys


if __name__ == '__main__':
    employee = get("https://jsonplaceholder.typicode.com/users")
    if employee.ok:
        employee_data = employee.json()
        outer_dict_format = dict()
        with open("todo_all_employees.json", "w",
                  encoding="utf-8") as file:
            for employee in employee_data:
                list_format = []
                todo = get(
                    "https://jsonplaceholder.typicode.com/users/{}/todos".
                    format(employee.get('id')))
                if todo.ok:
                    for task in todo.json():
                        data = {"task": task.get("title"),
                                "completed": task.get("completed"),
                                "username": employee.get("username")
                                }
                        list_format.append(data)
                outer_dict_format[employee.get("id")] = list_format
            json.dump(outer_dict_format, file)
