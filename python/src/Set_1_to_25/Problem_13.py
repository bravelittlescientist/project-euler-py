#!/usr/bin/python
#
# Problem 13
#
# Determine first 10 digits of sum of 100 50-digit numbers

# Initialize sum
total = 0

# Add each number in data file to total
f = open('data/data_13.txt')
for numline in f:
	total += int(numline.strip())
f.close()

print "First 10 digits of sum",str(total)[:10]
