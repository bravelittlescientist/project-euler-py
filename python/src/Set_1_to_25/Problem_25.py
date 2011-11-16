#!/usr/bin/python
# 
# Problem 25
#
# Find the first term in the Fibonacci sequence to 
# contain 1000 digits.

import unittest

class Test_Problem_25(unittest.TestCase):

	def test_first_fibonacci_with_2_digits(self):
		""" """
		self.assertEqual(7, first_term_in_fibonacci_sequence_with_n_digits(2))
	
	def test_first_fibonacci_with_3_digits(self):
		""" """
		self.assertEqual(12, first_term_in_fibonacci_sequence_with_n_digits(3))

def first_term_in_fibonacci_sequence_with_n_digits(n_digits):
	"""
	Computes fibonacci numbers, tracking term count until number
	exceeds 10^(n-1) digits. 
	"""
	# Initializations
	term = 2
	previous = 1
	current = 1
	
	# Compute fibonacci numbers until current exceeds 10^(n-1)
	while current < pow(10, n_digits - 1):
		# Update fibonacci numbers		
		current += previous
		previous = current - previous

		# Increment term count
		term += 1

	return term

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_25)
	unittest.TextTestRunner(verbosity=2).run(suite)

	target = 1000
	print "First Fibonacci to contain 1000 digits:", \
		first_term_in_fibonacci_sequence_with_n_digits(target)
