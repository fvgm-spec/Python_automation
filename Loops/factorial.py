#!/usr/bin/env python3

# File: factorial.py
# Simple example program to calculate the factorial of a number that is imputed by the user

# returns the factorial of  the argument "n"
def factorial(n):
    result = 1
    for i in range(n):
        result = result * (i + 1)
    return result

print(factorial(5))

#n = input("Enter any non negative integer to take the factorial of: ")
