#!/usr/bin/python
#
# Problem 52
#
# Find smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, 
# contain the same digits.

import unittest

class Test_Problem_52(unittest.TestCase):

	def test_has_same_digits_identifies_same_digits(self):
		self.assertTrue(has_same_digits(12345, 32451))
		self.assertFalse(has_same_digits(21, 22))
		self.assertTrue(has_same_digits(25,25))

def has_same_digits(n1, n2):
	""" Check if two input values contain same digits """
	n1_list_form = list(str(n1))
	n2_list_form = list(str(n2))
	
	n2_list_form.sort()
	n1_list_form.sort()
	
	return n1_list_form == n2_list_form

def find_smallest_scramblable_x():
	""" 
	Finds smallest positive x such that 2x, 3x, 4x, 5x, and 6x
	contain same digits
	"""
	x = 9
	all_multiples = False
	while not all_multiples:
		x += 1
		if has_same_digits(2*x, 6*x) and has_same_digits(3*x, 5*x) and has_same_digits(2*x, 4*x):
			all_multiples = True

	return x

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_52)
	unittest.TextTestRunner(verbosity=2).run(suite)

	print "Result:",find_smallest_scramblable_x()
