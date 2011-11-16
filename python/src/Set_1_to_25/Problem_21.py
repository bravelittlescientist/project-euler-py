#!/usr/bin/python
#
# Problem 21
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
# which divide evenly into n). If d(a) = b and d(b) = a, where a  b, then a and
# b are an amicable pair and each of a and b are called amicable numbers. 
# Evaluate the sum of all the amicable numbers under 10000

import unittest
import math

class Test_Problem_21(unittest.TestCase):

	def test_compute_sum_of_proper_divisors(self):
		""" Compute sums of proper divisors of amicables 220 and 284 """
		self.assertEqual(284, sum_of_proper_divisors(220))
		self.assertEqual(220, sum_of_proper_divisors(284))
		self.assertEqual(1, sum_of_proper_divisors(2))
		self.assertEqual(0, sum_of_proper_divisors(1))

	def test_count_sum_of_amicables(self):
		""" Compute sum of amicable numbers under 10 as 0 """
		self.assertEqual(0, compute_sum_of_amicables_under_n(10))

def sum_of_proper_divisors(n):
	""" Compute sum of all numbers < n which divide equally into n """
	if n == 1: return 0

	total = 1
	i = 2
	while i <= math.sqrt(n):
		if not n % i:
			total += i + n/i
		i += 1
	return total

def compute_sum_of_amicables_under_n(n):
	""" Compute all amicables under n, tracking their sum """
	# Initialization
	divisor_sums = {}
	amicable_sum = 0
	iterator = 2
	
	# Track amicable sums
	while iterator < n:
		iterator_divisors = sum_of_proper_divisors(iterator)
		divisor_sums[iterator] = iterator_divisors
		if iterator_divisors in divisor_sums and \
			iterator == divisor_sums[iterator_divisors] and \
			iterator_divisors != iterator:
		
			amicable_sum += iterator + iterator_divisors

		iterator += 1

	return amicable_sum

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_21)
	unittest.TextTestRunner(verbosity=2).run(suite)

	print "Result:",compute_sum_of_amicables_under_n(10000)
