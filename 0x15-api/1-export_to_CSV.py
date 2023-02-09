#!/usr/bin/python3
"""
Fetch Data from a site using api and save to csv file
"""
import csv
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
        # Design the output
        with open("{}.csv".format(sys.argv[1]), "w", encoding="utf-8") as file:
            writer = csv.writer(file, quotechar="'")
            for todo in todos_list:
                writer.writerow([
                    "\"{}\"".format(employee_data.get("id")),
                    "\"{}\"".format(employee_data.get("username")),
                    "\"{}\"".format(todo.get("completed")),
                    "\"{}\"".format(todo.get("title")),
                ]
                )
