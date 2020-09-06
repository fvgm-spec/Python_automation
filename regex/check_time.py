#!/usr/bin/env python3

import re
def check_time(text):
  pattern = r"\b((1[0-2]|1?[1-9]):([0-5][0-9])( ?([AaPp][Mm])))"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
