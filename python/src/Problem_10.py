#!/usr/bin/python
#
# Problem 10
# 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 + 17
# Find the sum of all the primes below two million

import unittest
from sets import Set

class Test_Problem_10(unittest.TestCase):

	def test_sum_of_primes_below_10_is_17(self):
		self.assertEqual(17, sum_of_primes_below(10))

	def test_multiples_generator_yields_multiples(self):
		multiples = list(multiples_of_k(2,10))
		self.assertEqual([2,4,6,8] , multiples)

def multiples_of_k(k, n):
	"""
	Generator yields multiples of k in range(k,n)
	"""
	val = k
	while val < n:
		yield val
		val += k

def sum_of_primes_below(n):
	"""
	Algorithm: Sieve of Eratosthenes, efficient for generating
	ranges of prime numbers
	"""
	# Track sum of primes including 2, the first prime
	total = 2
	number_tracker = Set(list(multiples_of_k(2,n)))
	
	# Iterator
	p = 2

	# Prime sieve adds all multiples of current prime to number set
	# then searches for next largest number not in number set, which is
	# the next prime
	while p < n:
		# Update sum of primes and extend set of visited numbers
		if p not in number_tracker:
			total += p
			number_tracker.update(list(multiples_of_k(p,n)))
		# Increment p until next prime is found
		p += 1

	return total

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_10)
	unittest.TextTestRunner(verbosity=2).run(suite)

	target = 2000000
	print "Sum of primes below",target,"=",sum_of_primes_below(target)
