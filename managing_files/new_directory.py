#! /usr/bin/env python3

import os

def new_directory(directory, filename):
    # Before creating a new directory, check to see if it already exists
    if not os.path.exists(directory):
        os.mkdir(directory)
    filepath = os.path.join(directory, filename)
    with open(filepath,'w') as file:
        pass
    # Return the list of files in the new directory
    return os.listdir(directory)

print(new_directory("PythonPrograms", "script.py"))
