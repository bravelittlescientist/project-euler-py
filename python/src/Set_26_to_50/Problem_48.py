#!/usr/bin/python
#
# Problem 48
#
# Find the last ten digits of the series 1^1 + 2^2 + 3^3 + ... + 1000^1000

import unittest

class Test_Problem_48(unittest.TestCase):

	def test_compute_sum_of_series(self):
		self.assertEqual(10405071317, compute_sum_of_n_n_series(10))

	def test_retrieve_last_10_digits_of_sum(self):
		self.assertEqual("0405071317", last_ten_digits_of_series_sum(10))

def compute_sum_of_n_n_series(n):
	""" Computes sum of 1**1 + 2**2 ...n**n series """
	return sum(map(lambda x: x**x, range(1, n+1)))

def last_ten_digits_of_series_sum(n):
	""" Returns last 10 digits of sum of 1**1 + 2**2 + 3**3 ... n**n """
	n_to_string = str(compute_sum_of_n_n_series(n))

	return n_to_string[-10:]

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_48)
	unittest.TextTestRunner(verbosity=2).run(suite)

	print "Last 10 digits of 1^1 + 2^2 + ... + 1000^1000:",\
		last_ten_digits_of_series_sum(1000)
