#!/usr/bin/python
#
# Problem 63
#
# The 5-digit number, 16807=7^5, is also a fifth power. 
# Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
# How many n-digit positive ingeters exist which are also an nth power

# Initialize nth_power counter
counter = 0

# 10^2 is 100 so essentially the range of bases is limited to 1 to 9
for base in range(1, 10):
	# Power is length of n
	power = 1

	while len(str(base**power)) == power:
		# Update counter
		counter += 1

		# Increment power
		power += 1

print "n-digit nth-powers:", counter
