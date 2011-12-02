#!/usr/bin/python
#
# Problem 92
#
# A number chain is created by continuously adding the square of the digits 
# in a number to form a new number until it has been seen before.
#
# For example,
#
# 44 > 32 > 13 > 10 > 1 > 1
# 85 > 89 > 145 > 42 > 20 > 4 > 16 > 37 > 58 > 89
#
# How many starting numbers below ten million will arrive at 89?

# Initialize 89 tracker
arrive_89 = 0
tracker = {}

# All values below 10,000,000
for value in range(1, 10000000):

	# Update n until we reach 1 or 89
	n = value
	while n != 89 and n != 1:

		# If n has been seen before, skip forward
		if n in tracker:
			n = tracker[n]
		# Otherwise compute sum of digit squares
		else:
			n = sum([int(x)**2 for x in list(str(n))])

	# Update counter and tracking table
	if n == 89:
		arrive_89 += 1
		tracker[value] = 89
	else:
		tracker[value] = 1

print "Starting numbers arriving at 89:",arrive_89
