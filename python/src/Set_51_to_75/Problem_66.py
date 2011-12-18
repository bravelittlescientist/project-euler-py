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
		self.assertEqual(5, optimal_diophantine_minimal_in_x(7))

def minimal_diophantine_solution_in_x(D):
	""" Compute minimal diophantine solution in x, given D """
	# Check if D is a square by rounding sqrt
	if 0.0 == int(D**0.5) % D**0.5:
		return -1

	# We increment x and y until a y is found such that 
	# x^2 - D*y^2 = 1
	x = 1
	y = 1
	while x > 0:
		# Increment y until it is too large to satisfy for D in x
		while x**2 - (D*(y**2)) > 1:
			y += 1

		if x**2 - (D*(y**2)) == 1:
			return x
		else:
			x += 1 

	return 0

def optimal_diophantine_minimal_in_x(upper_limit):
	""" Find D for which largest X is obtianed, for diophantine solutions
	minimal in x
	"""
	return 0

if __name__ == '__main__':
	# Run unit tests
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_66)
	unittest.TextTestRunner(verbosity=2).run(suite)
