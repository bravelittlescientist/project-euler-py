#!/usr/bin/python
#
# Problem 66
#
# Consider quadratic Diophantine equations of the form:
# x^2 -  Dy^2 = 1

# For example, when D=13, the minimal solution in x is 6492 - 13*180^2 = 1.
# It can be assumed that there are no solutions in positive integers when 
# D is square.

# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain 
# the following:
# 3^2 - 2 2^2 = 1
# 2^2 - 3 1^2 = 1
# 9^2 - 5 4^2 = 1
# 5^2 - 6 2^2 = 1
# 8^2 - 7 3^2 = 1
#
# Hence, by considering minimal solutions in x for D <= 7, the largest x 
# is obtained when D=5.

# Find the value of D  1000 in minimal solutions of x for which the largest 
# value of x is obtained.

import unittest
import math

class Test_Problem_66(unittest.TestCase):
	
	def test_minimal_diophantine_solution_in_x(self):
		""" Compute solutions minimal in x """
		self.assertEqual(3, minimal_diophantine_solution_in_x(2))
		self.assertEqual(2, minimal_diophantine_solution_in_x(3))
		self.assertEqual(9, minimal_diophantine_solution_in_x(5))
		self.assertEqual(5, minimal_diophantine_solution_in_x(6))
		self.assertEqual(8, minimal_diophantine_solution_in_x(7))
		self.assertEqual(649, minimal_diophantine_solution_in_x(13))
	
	def test_no_solution_when_D_is_square(self):
		""" No solutions in positive integers when D is square """
		self.assertEqual(-1, minimal_diophantine_solution_in_x(4))

	def test_value_of_D_in_minimal_solutions_of_x_for_largest_x(self):
		""" Considering minimal solutions in x for D <= threshold, find
		D for which largest x is obtained
		"""
		self.assertEqual(5, optimal_diophantine_minimal_in_x(8))

def minimal_diophantine_solution_in_x(D):
	""" Compute minimal diophantine solution in x, given D """
	# Check if D is a square by rounding sqrt
	if 0.0 == int(D**0.5) % D**0.5:
		return -1

	# Dealing only with positive integers, we're not worried about
	# division by 0. y will only satisfy the equation for a given x 
	# if x^2 == Dy^2 + 1, which means that Dy^2 + 1 must have an integer
	# square root. This is much faster than incrementing x, because
	# y will be smaller than x.
	
	# Initialize y at 1
	y = 1
	
	# Only return when square root test passes
	while y > 0:

		# Compute x_squared
		x_squared = D*(y**2) + 1

		# Check if x_squared has an integer square root
		if math.ceil(math.sqrt(x_squared)) == math.sqrt(x_squared):
			return int(math.sqrt(x_squared))
		else:
			y += 1

	return -1

def optimal_diophantine_minimal_in_x(upper_limit):
	""" Find D for which largest X is obtianed, for diophantine solutions
	minimal in x
	"""
	# Initialize D, maximum value of x
	optimal_D = 1
	maximum_x = -1

	# For each 1 <= D <= upper_limit, compute minimal x for D
	# Update maximum_x, optimal_D if satisfied
	for D in range(1, upper_limit):

		# Compute minimal x solution
		x = minimal_diophantine_solution_in_x(D)

		# If x exceeds existing maximum, update maximum and optimal D
		if x > maximum_x:
			maximum_x = x
			optimal_D = D

	return optimal_D

if __name__ == '__main__':
	# Run unit tests
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_66)
	unittest.TextTestRunner(verbosity=2).run(suite)

	print "D <= 1000 in minimal solutions of x -> largest obtained:", \
	optimal_diophantine_minimal_in_x(1001)
