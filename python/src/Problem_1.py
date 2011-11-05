#!/usr/bin/python
#
# Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import unittest

class Test_Problem_1(unittest.TestCase):

	def setUp(self):
		pass

	def test_sum_of_3_or_5_multiples_under_10_is_23(self):
		self.assertEqual(23, calculate_sum_of_natural_mults_under_n(10))

def calculate_sum_of_natural_mults_under_n(number):
	""" Calculate sum of multiples of 3 or 5 under input number """
	total = 0
	for i in range(number):
		if i % 5 == 0 or i % 3 == 0:
			total += i
	return total
	
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_1)
	unittest.TextTestRunner(verbosity=2).run(suite)

	print "n = 1000:",calculate_sum_of_natural_mults_under_n(1000)
