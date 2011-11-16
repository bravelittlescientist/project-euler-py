#!/usr/bin/python
#
# Problem 4
# 
# A palindromic number reads the same both ways. Find the largest 
# palindrome made from the product of two 3-digit numbers.

import unittest

class Test_Problem_4(unittest.TestCase):

	def test_largest_palindrome_from_product_of_2_digit(self):
		""" 9009 is largest palindrome product of two 2-digit numbers """
		self.assertEqual(9009, largest_palindrome_product_of_n_digit_numbers(2))

	def test_palindromic_and_non_palindromic_numbers(self):
		""" is_number_palindromic correctly determines palindromes """
		self.assertTrue(is_number_palindrome(91919))
		self.assertTrue(is_number_palindrome(9229))
		self.assertFalse(is_number_palindrome(91191))

	def test_target(self):
		""" Largest palindrome made from the product of two 3-digit numbers """
		result = largest_palindrome_product_of_n_digit_numbers(3)
		self.assertIsNotNone(result)
		print "Result:", result

def is_number_palindrome(number):
	""" Determine if number is a palindrome by converting to string """
	is_palindrome = str(number)

	# Even-length number
	if not len(is_palindrome) % 2:
		return is_palindrome[0:len(is_palindrome)/2] == \
			is_palindrome[len(is_palindrome)/2::][::-1]
	# Odd-length number
	else:
		return is_palindrome[0:len(is_palindrome)/2] == \
			is_palindrome[len(is_palindrome)/2 + 1::][::-1]

def largest_palindrome_product_of_n_digit_numbers(n):
	"""
	Multiple all n-digit numbers by each other once to
	check for palindromes, updating largest if found
	"""
	# Initialize largest_product and upper multiplier bound
	largest_product = 0
	upper_bound = pow(10,n)

	# Check each possible multiple for largest product
	for smaller in range(pow(10, n-1), upper_bound):
		for larger in range(smaller, upper_bound):
			if is_number_palindrome(smaller*larger):
				largest_product = max(largest_product,smaller*larger)
		
	return largest_product

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_4)
	unittest.TextTestRunner(verbosity=2).run(suite)
