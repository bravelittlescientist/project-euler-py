#!/usr/bin/python
#
# IntegerArraysReader
#
# Basic auxiliary file to read large quantities of space-separated
# integers from a file. 

def read_integer_arrays_from_file(filename):
	""" Reads numbers from file, returns multi-dimensional array """
	result = []
	f = open(filename)
	for line in f:
		result.append(map(int, line.strip('\n').split()))
	f.close()
	return result
