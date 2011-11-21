#!/usr/bin/python
#
# Problem 30
#
# Find sum of all the numbers that can be written as the sum of
# fifth powers of their digits

import unittest

class Test_Problem_30(unittest.TestCase):

	def test_sum_of_numbers_written_as_4th_powers_of_digits(self):
		""" 19316 is the sum of all numbers written as 4th powers of digits """
		self.assertEqual(19316, compute_sum_of_nth_power_numbers(4))

	def test_only_three_numbers_can_be_written_as_sum_of_4th_powers(self):
		""" Only 1634, 8208, and 9474 can be written as sums of 5th powers """
		self.assertEqual(3, len(get_sum_of_nth_power_numbers(4)))

def get_sum_of_nth_power_numbers(n):
	""" Returns list of numbers written as nth sum of their digits """
	computed = []
	for i in range(2, n*(9**n)):
		digits = map(int, list(str(i)))
		if i == sum(map(lambda x: x**n, digits)):
			computed.append(i)

	return computed
	
def compute_sum_of_nth_power_numbers(n):
	""" Computes sum of numbers written as nth sum of their digits """
	return sum(get_sum_of_nth_power_numbers(n))

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_30)
	unittest.TextTestRunner(verbosity=2).run(suite)

	print "5th Powers:",compute_sum_of_nth_power_numbers(5)
