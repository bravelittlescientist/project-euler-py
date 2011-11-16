#!/usr/bin/python
#
# Problem 7
# 
# What is the 10001st prime number?

import unittest
import math

class Test_Problem_7(unittest.TestCase):
	
	def test_6th_prime_is_13(self):
		self.assertEqual(13, find_nth_prime(6))

def find_nth_prime(n):
	"""
	A prime only has two positive integer divisors: 1 and itself.
	Find the nth prime by checking each number to make sure it is not
	divisible by any previously found primes.
	"""
	# Track sum of primes including 2, the first prime
	primes = []
	prime_it = 2

	while len(primes) < n:
		# Check all divisors in primes list up to square root of prime
		ind = 0
		divisors = 0
		while ind < len(primes) and primes[ind] <= math.sqrt(prime_it) and divisors == 0:
			if prime_it % primes[ind] == 0:
				divisors = 1
			ind += 1

		# If no divisors were found, then this number is prime
		if not divisors:
			primes.append(prime_it)		
		
		prime_it += 1

	# The last found prime is the nth one
	return primes[-1]

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_7)
	unittest.TextTestRunner(verbosity=2).run(suite)

	target = 10001
	print "The 10001th prime number is", find_nth_prime(target)
