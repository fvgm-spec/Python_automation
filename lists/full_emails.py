#!/usr/bin/env python3

def full_emails(people):
	result = []
	for email,name in people:
	  result.append("{} <{}>".format(name, email))
	return result
	
print(full_emails([("felixmlb@gmail.com", "Felix Gutierrez"), ("joymerhoney@gmail.com", "Joymer Gutierrez")]))  
