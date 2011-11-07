#!/usr/bin/python
#
# Problem 28
#
# Starting with the number 1 and moving to the right in a clockwise direction 
# a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
# formed in the same way?
import unittest

class Test_Problem_28(unittest.TestCase):

	def test_compute_sum_of_dimension_5_spiral(self):
		self.assertEqual(101, get_spiral_diagonal_sum(5))

	def test_compute_sum_of_dimension_3_spiral(self):
		self.assertEqual(25, get_spiral_diagonal_sum(3))

	def test_compute_sum_of_dimension_7_spiral(self):
		self.assertEqual(261, get_spiral_diagonal_sum(7))

def get_spiral_diagonal_sum(dimension):
	"""
	Update total using a formula for exponential growth around the spiral
	Each time, the total is append with 4 times the "top-right" of the next
	inner spiral, equivalent to (2*power - 1)^2.
	Then it is appended with 10 times 2 to the current power.

	In this way we I can compute the spiral without saving it to a list.
	"""
	# Initialize with sum for center of spiral
	total = 1
	level = 1
	while level*2 + 1 <= dimension:
		# Sum total with 4 of end of last spiral as base
		total += 4*pow(2*level - 1, 2)
		
		# Sum total with 20 of the level counter, 
		# like moving around spiral
		total += 10*(2*level)
		
		# Update level counter
		level += 1

	return total

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_28)
	unittest.TextTestRunner(verbosity=2).run(suite)

	target = 1001
	print "1001 x 1001 Spiral Diagonal Sum:",get_spiral_diagonal_sum(target)
