#!/usr/bin/python
#
# Problem 34
#
# Find the sum of all numbers which are equal to the sum of the
# factorial of their digits.
# 
# Note: as 1! = 1 and 2! = 2 are not sums, they are not included.

import unittest

class Test_Problem_34(unittest.TestCase):

	def test_sum_of_digit_factorials(self):
		""" Test correct computation of sum of factorials """
		factorials = compute_all_factorials()
		self.assertEqual(145, sum_of_digit_factorials(145, factorials))

def sum_of_digit_factorials(n, factorial):
	""" Test whether sum of factorials of digits of n equals n """
	digits = [int(x) for x in list(str(n))]
	return sum([factorial[d] for d in digits])

def compute_all_factorials():
	""" Returns a dictionary with all digit factorials computed """
	
	# Compute all factorials
	factorial = {}
	perm = 1
	for i in range(1,10):
		perm = perm * i;
		factorial[i] = perm
	factorial[0] = 1

	return factorial

def sum_of_digit_factorial_sums():
	""" Compute sum of all numbers equal to sum of factorial of digits """
	# Track total sum of n where sum of factorials of digits = n	
	factorial_sum = 0

	# 999...99 has the largest possible factorial sum. At point when 
	# that number exceeds the sum of its factorial then we stop
	digit_increase = 10

	# 1! and 2! are not sums, so not included
	current = 3

	# Precomputed factorials
	factorial = compute_all_factorials()

	while True:

		# Check power stop condition
		if current == digit_increase:
			# Check if previous all 9's number exceeds its factorial sum
			if current - 1 > sum_of_digit_factorials(current - 1, factorial):
				return factorial_sum
			else: 
				# Set stop-check to next length number
				digit_increase *= 10

		# Continue to check factorial number sums
		if current == sum_of_digit_factorials(current, factorial):
			factorial_sum += current	

		# Increment current
		current += 1

	return factorial_sum

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_34)
	unittest.TextTestRunner(verbosity=2).run(suite)

	print "Sum of factorial sums:", sum_of_digit_factorial_sums()
