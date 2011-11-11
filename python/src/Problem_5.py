#!/usr/bin/python
# 
# Problem 5 
#
# What is the smallest positive number that is evenly divisible by 
# all of the numbers from 1 to 20?

import unittest
import math

class Test_Problem_5(unittest.TestCase):
	def test_2520_smallest_result_for_1_to_10(self):
		self.assertEqual(2520, compute_smallest_divisible_multiple(1,10))

	def test_60_smallest_result_for_1_to_5(self):
		self.assertEqual(60, compute_smallest_divisible_multiple(1,5))

def is_prime(n):
	""" Check if prime """
	factor = 2
	while factor <= math.sqrt(n):  
		if not n % factor:
			return False
		factor += 1

	return True

def divide_if_possible(n, div):
	""" Divide n by div, if divisible """
	if not n % div:
		return n / div
	return n

def compute_smallest_divisible_multiple(start, stop):
	""" Determine minimum number divisable by numbers in range """
	# Initialize array of elements to divide
	to_divide = range(1,stop + 1)
	
	# Initialize smallest number
	smallest_multiple = 1

	# Eliminate prime factors of array members
	for i in range(len(to_divide)):  
		# Check if candidate is prime
		if is_prime(to_divide[i]):

			# Multiple smallest multiple
			smallest_multiple *= to_divide[i]
		
			# Try to divide each number
			factor = to_divide[i]	
			to_divide = map(lambda x: divide_if_possible(x, factor), to_divide)		
	# Found!
	return smallest_multiple

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_5)
	unittest.TextTestRunner(verbosity=2).run(suite)

	print "Target:", compute_smallest_divisible_multiple(1,20)
