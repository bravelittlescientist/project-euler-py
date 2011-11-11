#!/usr/bin/python
#
# Problem 6
#
# Find the difference between the sum of the squares of the first one hundred 
# natural numbers and the square of the sum.

import unittest

class Test_Problem_6(unittest.TestCase):

	def test_compute_difference_sum_of_squares_and_square_of_sum(self):
		self.assertEqual(2640, diff_sum_squares_square_sum(10))

def diff_sum_squares_square_sum(n):
	"""
	Find difference betweem sum of squares and square of sums of
	first n natural numbers.
	"""
	sum_of_squares = sum(map(lambda x: x*x, range(1,n+1)))
	square_of_sum = sum(range(1,n+1))**2
	return square_of_sum - sum_of_squares

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_6)
	unittest.TextTestRunner(verbosity=2).run(suite)

	print "Result:", diff_sum_squares_square_sum(100)
