#!/usr/bin/python
#
# Problem 2
# By considering the terms in the Fibonacci sequence whose values do not 
# exceed four million, find the sum of the even-valued terms. 

import unittest

class Test_Problem_2(unittest.TestCase):

	def setUp(self):
		pass

	def test_sum_of_even_valued_less_than_100_fibonacci(self):
		self.assertEqual(44, compute_even_valued_fibonacci_sum_under_n(100))

def compute_even_valued_fibonacci_sum_under_n(n):
	n_previous = 1
	n_current = 2
	total = 0
	while n_current <= n:
		if n_current % 2 == 0:		
			total += n_current
		n_current += n_previous
		n_previous = n_current - n_previous
	return total

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_2)
	unittest.TextTestRunner(verbosity=2).run(suite)

	print "4 Million:", compute_even_valued_fibonacci_sum_under_n(4000000)	
