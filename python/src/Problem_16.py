#!/usr/bin/python
#
# Problem 16
# 
# What is the sum of the digits of the number 2^1000

import unittest

class Test_Problem_16(unittest.TestCase):
	
	def test_sum_of_2_to_15th_digits_is_26(self):
		""" Correctly compute small sample sum of digits """
		self.assertEqual(26, sum_of_digits_2_to_nth_power(15))

def sum_of_digits_2_to_nth_power(n):
	""" Computes sum of digits in string representing 2^n """
	digit_string = str(pow(2,n))
	sum = 0
	for i in digit_string:
		sum += int(i)
	return sum

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_16)
	unittest.TextTestRunner(verbosity=2).run(suite)

	target = 1000
	print "Sum of digits of 2^1000:", \
		sum_of_digits_2_to_nth_power(target)
