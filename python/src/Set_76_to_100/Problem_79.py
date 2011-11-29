#!/usr/bin/python
#
# Problem 79 - Keylogger
#
# A common security method used for online banking is to ask the user for 
# three random characters from a passcode. For example, if the passcode was 
# 531278, they may ask for the 2nd, 3rd, and 5th characters; 
# the expected reply would be: 317.
#
# The text file, data/keylog.txt, contains fifty successful login attempts.
#
# Given that the three characters are always asked for in order, analyse 
# the file so as to determine the shortest possible secret passcode 
# of unknown length.

# Initialize ordered list of digits
ordering = {}
passcode = []

# Open file, read log
f = open('data/keylog.txt')
for line in f:
	# Get combo
	combo = map(int, list(line.strip()))
		
	# First value is either very first, or doesn't have an assigned parent
	if combo[0] not in ordering:
		ordering[combo[0]] = -1

	# Second value is either right after the first value, or there is another
	# value or a few in between
	if combo[1] not in ordering:
		ordering[combo[1]] = combo[0]
	# Current parent of combo[1] is before combo[0]
	elif ordering[combo[1]] != combo[0] and \
			ordering[combo[0]] == ordering[combo[1]]:
		ordering[combo[1]] = combo[0]
			

	# Third value is either right after the second value, or there is another
	# value or a few in between
	if combo[2] not in ordering:
		ordering[combo[2]] = combo[1]
	# current parent of combo[2] is before combo[1]
	elif ordering[combo[2]] != combo[1] and \
			ordering[combo[2]] == ordering[combo[1]]:
		ordering[combo[2]] = combo[1]

f.close()

for key in ordering:
	print key,"after",ordering[key]

# Fixme: Need to make this print out pretty
