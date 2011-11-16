#!/usr/bin/python
#
# Problem 53
# 
# Combinatorics
# How many, not necessarily distinct, values of nCr, for 1 <= n <= 100,
# are greater than 1 million?

import unittest

class Test_Problem_53(unittest.TestCase):

	def test_compute_combinatoric_correctly(self):
		""" Computes correct combinator of n, r """
		self.assertEqual(10, compute_combinatoric(5,3))
		self.assertEqual(1144066, compute_combinatoric(23,10))

	def test_compute_permutation(self):
		""" Compute n! """
		self.assertEqual(1, permute(0))
		self.assertEqual(120, permute(5))

def permute(n):
	""" Returns n! recursively """
	if n == 0:
		return 1
	return n*permute(n - 1)

def compute_combinatoric(n, r):
	""" Compute nCr for inputs n,r """
	# r must be <= n
	if r > n:
		return 0

	# nCr = n! / (r!(n-r)!)
	return permute(n) / (permute(r) * permute(n-r))

def count_values_nCr_exceeding_1_million():
	""" 1 <= n <= 100, count nCr > 1 million """
	# Count > 1 million, can have repeats
	counter = 0
	
	for n in range(1, 101):
		for r in range(1, n + 1):
			if compute_combinatoric(n, r) > 1000000:
				counter += 1

	return counter

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_53)
	unittest.TextTestRunner(verbosity=2).run(suite)

	print "Result:", count_values_nCr_exceeding_1_million()
