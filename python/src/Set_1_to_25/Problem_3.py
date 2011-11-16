#!/usr/bin/python
#
# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

import unittest
import math

class Test_Problem_3(unittest.TestCase):

	def setUp(self):
		pass

	def test_largest_prime_factor_of_13195_is_29(self):
		self.assertEqual(29, compute_largest_prime_factor(13195))

def compute_largest_prime_factor(n):
	""" Recursive computation of largest factors, up to square root n """	
	it = 2
	while it < math.sqrt(n):
		if n % it == 0:
			break 
		it += 1

	# w
	if it > math.sqrt(n):
		return n
	else:
		return max(it, compute_largest_prime_factor(n/it))

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_3)
	unittest.TextTestRunner(verbosity=2).run(suite)

	target = 600851475143
	print "Result", compute_largest_prime_factor(target) 
