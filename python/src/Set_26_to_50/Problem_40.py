#!/usr/bin/python
#
# Problem 40
# An irrational decimal fraction is created by concatenating the 
# positive integers:
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value 
# of the following expression.
# d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000

import unittest

class Test_Problem_40(unittest.TestCase):

	def test_nth_digit_of_fractional_part(self):
		""" Check that nth digits are correctly calculated """
		counter = 1
		for digit in generate_digits(20):
			if counter == 1 or counter == 10 or counter == 12:
				self.assertEqual(1, digit)
		
			counter += 1

	def test_computes_max_nth_digit_by_multiples_of_10(self):
		""" Ensure that generator knows when to stop """
		self.assertEqual(1, products_of_multiple_of_ten_nth_digits(100000))

def generate_digits(maximum):
	""" Generates digit of irrational decimal fraction """ 
	yield 0

def products_of_multiple_of_ten_nth_digits(maximum):
	""" Computes product of d1, d10 ... dmaximum via multiples of 10

	Assuming nth maximum is some 1 x 10^x """
	return 0

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_40)
	unittest.TextTestRunner(verbosity=2).run(suite)
