#!/usr/bin/python
#
# Problem 9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, 
# for which a^2 + b^2 = c^2. There exists exactly one pythagoreon triplet
# for which a + b + c = 1000. Find the product abc.

def brute_force():
	for a in range(1,1000):
		for b in range(1,1000):
			for c in range(1,1000):
				if a**2 + b**2 == c**2 and a + b + c == 1000:
					return a*b*c
				
print "Result:",brute_force()
