#!/usr/bin/python
#
# Problem 36
#
# Find the sum of all numbers, less than 1 million, which are
# palindromic in base 10 and base 2

import unittest

class Test_Problem_36(unittest.TestCase):
	
	def test_is_palindromic(self):
		""" Test if a string is palindromic """
		self.assertFalse(is_palindromic("1010"))
		self.assertTrue(is_palindromic("101"))
		self.assertTrue(is_palindromic("1001"))
		self.assertTrue(is_palindromic("58785"))
		self.assertTrue(is_palindromic("978879"))

	def test_to_binary_form(self):
		self.assertEqual("100", to_binary_form(4))
		self.assertEqual("1010", to_binary_form(10))

def is_palindromic(value):
	""" Determine if a string is palindromic """	
	first_half = value[:len(value)/2]
	if not len(value) % 2:
		second_half = value[len(value)/2:]
	else:
		second_half = value[(len(value)/2)+1:]
	
	return first_half == second_half[::-1]

def to_binary_form(n):
	""" Converts number to binary, strips 0b at front """
	return bin(n).split("0b")[1]

def compute_sum_of_palindromics():
	""" Compute sum of palindromic numbers, < 1 mil, in base 10 and 2 """
	# Filter out non-palindromic numbers
	base_10_palindromic = filter(is_palindromic, (map(str,range(1000000))))

	# Increment sum if value is also palindromic in Base 2
	sum = 0
	for value in base_10_palindromic:
		if is_palindromic(to_binary_form(int(value))):
			sum += int(value)
	
	return sum

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_36)
	unittest.TextTestRunner(verbosity = 2).run(suite)

	print "Sum of Base 10, Base 2 palindromic numbers < 1 million:",\
			compute_sum_of_palindromics()
