#!/usr/bin/env python3

import csv
def read_employees(csv_file_location):
    with open('employees.csv') as employee_file:
        employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
        employee_list = []
        for data in employee_file:
            employee_list.append(data)
    return employee_list

employee_list = read_employees('/home/superunk/employees.csv')
print(employee_list)
