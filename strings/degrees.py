#!/usr/bin/env python3
def to_celsius(x):
	return (x-32)*5/9
for x in range(0,101,10): #range goes from 1 to 101 each 10 numbers
	print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x))) #{:>3} aligns characters to the left
