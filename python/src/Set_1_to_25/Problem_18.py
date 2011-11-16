#!/usr/bin/python
#
# Problem 18
#
# Compute maximum total from top to bottom of a triangle.

import unittest
import tools.IntegerArraysReader as reader

class Test_Problem_18(unittest.TestCase):
	
	def test_compute_sum_of_small_triangle(self):
		""" Sample 4-level triangle """
		path = "python/src/data/Problem_18_Test.txt"
		triangle = reader.read_integer_arrays_from_file(path)
		self.assertEqual(23, compute_maximum_value_triangle_path(triangle))

	def test_compute_sum_of_target_triangle(self):
		path = "python/src/data/Problem_18_Target.txt"
		triangle = reader.read_integer_arrays_from_file(path)
		result = compute_maximum_value_triangle_path(triangle)
		print "Bigger triangle maximum path value", result

def navigate_triangle_sum(x,y,triangle):
	"""
	Navigate recursively through triangle until you reach bottom
	"""
	if y < len(triangle):
		return triangle[y][x] + \
			max(navigate_triangle_sum(x, y + 1, triangle), \
				navigate_triangle_sum(x + 1, y + 1, triangle) )
	else:
		return 0

def compute_maximum_value_triangle_path(triangle):
	"""
	Input: Multidimensional list of integers
	"""
	return navigate_triangle_sum(0, 0, triangle) 

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_18)
	unittest.TextTestRunner(verbosity=2).run(suite)
