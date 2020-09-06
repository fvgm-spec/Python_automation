#!/usr/bin/env python3

import re
def transform_comments(line_of_code):
  result = re.sub(r'\#+\s\b', r'// ', line_of_code) #match the hash symbol (#) more than one time followed
  return result                                     #by blank space and the start of a word. Then is repla-
                                                    #ced by double slash (//)
print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"

