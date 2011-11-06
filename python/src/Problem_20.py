#!/usr/bin/python
#
# Problem 20
#
# Find the sum of the digits in the number 100!

import unittest

class Test_Problem_20(unittest.TestCase):

	def test_sum_of_10_perm_digits_is_27(self):
		""" Ensure the permutation sum-finding method computes 10! """
		self.assertEqual(27, find_sum_of_permutation_digits(10))

	def test_sum_of_digits_in_string_123_is_6(self):
		""" Correctly compute sum of numbers in a string """
		self.assertEqual(6, compute_sum_of_string_digits("123"))

def compute_sum_of_string_digits(text_num):
	"""
	Given a number in the form of a string, computes sum of
	its digits. 
	"""
	total = 0
	for c in text_num:
		total += int(c)
	return total	

def find_sum_of_permutation_digits(n):
	"""
	Performs a permutation by updating a string of numbers with each
	product, of which the sum can then be computed.
	"""
	permutation_result = "1"
	while n > 1:
		permutation_result = str(int(permutation_result) * n)
		n -= 1

	return compute_sum_of_string_digits(permutation_result)

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_20)
	unittest.TextTestRunner(verbosity=2).run(suite)
	
	print "Target: sum of digits of 100! =", find_sum_of_permutation_digits(100)
