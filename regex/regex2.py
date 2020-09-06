#!/usr/bin/env python3

import re
def repeating_letter_a(text):
  result = re.search(r"[aA].*[aA]", text) #matches lowercase and uppercase letters
  return result != None

print(repeating_letter_a("banana")) # True
#print(repeating_letter_a("pineapple")) # False
#print(repeating_letter_a("Animal Kingdom")) # True
#print(repeating_letter_a("A is for apple")) # True
