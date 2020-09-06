#! /usr/bin/env python3

def create_python_script(filename): #identifies the method create_python_script taht accept filename variable as the parameter
  comments = "# Start of a new Python program" #defines a string variable comments that holds string values
  with open("filename","w+") as file: #uses an open method taht open file in w+ mode
    file.write(comments) #uses write method that inputs the value in the file
    file.close() #closes the fie
  import os #import package os for the file
  filesize = os.path.getsize(filename) #defines a variable filesize that uses the getsize method to calculate its size
  return(filesize) #return filesize value

#print(create_python_script("program.py")) 
#uses the print method that call create_python_script and print its return value
