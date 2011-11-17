#!/usr/bin/python
#
# Problem 50
#
# Which prime, below 1-milliion, can be written as the sum of the
# most consecutive primes?

import unittest
import math

class Test_Problem_50(unittest.TestCase):

	def test_is_prime(self):
		""" Check if we correctly compute primes """
		self.assertFalse(is_prime(1))
		self.assertTrue(is_prime(7))
		self.assertFalse(is_prime(10))

	def test_longest_consecutive_prime_sum(self):
		""" Compute text cases for longest-consecutive-prime sums """
		self.assertEqual(41, compute_consecutive_prime_sum_below(100))
		self.assertEqual(953, compute_consecutive_prime_sum_below(1000))

def is_prime(n):
	""" Determine if n is prime """
	if n <= 1: return False

	divisor = 2
	while divisor <= math.sqrt(n):
		if not n % divisor:
			return False
		divisor += 1

	return True

def compute_consecutive_prime_sum_below(upper_limit):
	""" Compute prime below upper_limit which is sum of 
	longest consecutive sequence of primes """
	
	# Obtain list of primes from list of numbers below upper limit
	primes = filter(is_prime, range(upper_limit))

	# Compute prime which is sum of most primes in allowed range	
	max_length = 0
	prime_result = 0
	low = 0
	while low < len(primes):
		# Only compute if possible to exceed current longest sequence
		high = low + max_length + 1
		while high < len(primes) and sum(primes[low:high]) < upper_limit:
			# Update if sum is a prime
			if sum(primes[low:high]) in primes:
				max_length = high - low
				prime_result = sum(primes[low:high])
			high += 1
		low += 1
		
	return prime_result

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_50)
	unittest.TextTestRunner(verbosity=2).run(suite)

	print "Prime sum of most consecutive primes below 1 million", \
			compute_consecutive_prime_sum_below(1000000)
